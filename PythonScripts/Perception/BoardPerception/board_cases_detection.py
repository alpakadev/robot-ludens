def _sort(array, index):
    # Bubblesort for 2D Array in ascending order 
    # index determines wich field of subarray will be used as criterion
    n = len(array)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j][index] > array[j + 1][index]:
                arrayCopy = array.copy()
                swapped = True
                array[j] = arrayCopy[j+1]
                array[j+1] = arrayCopy[j]
        if not swapped:
            return

def _add_between_anchors(corners, config):
    # Calculates two "Midway Points" for each border

    borderlines = {"upperBorder": {
                       "start": corners["upRightCorner"], 
                       "end": corners["upLeftCorner"]}, 
                    "lowerBorder": {
                        "start": corners["downRightCorner"], 
                        "end": corners["downLeftCorner"]}, 
                    "leftBorder": {
                        "start": corners["downLeftCorner"], 
                        "end": corners["upLeftCorner"]}, 
                    "rightBorder": {
                        "start": corners["downRightCorner"], 
                        "end": corners["upRightCorner"]}
                  }

    anchors = corners

    for key, line in borderlines.items():
        firstAnchor = {
            "x": (int((1 - config["line_distance_factors"]["first"]) 
                * line["start"]["x"]) 
                + (config["line_distance_factors"]["first"] 
                * line["end"]["x"])), 
            "y": (int((1 - config["line_distance_factors"]["first"]) 
                * line["start"]["y"]) 
                + (config["line_distance_factors"]["first"] 
                * line["end"]["y"]))
        }
        secondAnchor = {
            "x": (int((1 - config["line_distance_factors"]["second"]) 
                * line["start"]["x"]) 
                + (config["line_distance_factors"]["second"] 
                * line["end"]["x"])), 
            "y": (int((1 - config["line_distance_factors"]["second"]) 
                * line["start"]["y"]) 
                + (config["line_distance_factors"]["second"] 
                * line["end"]["y"]))
        }

        anchors[key + "Between1"] = firstAnchor
        anchors[key + "Between2"] = secondAnchor

    return anchors

def _line_intersection(hLine, vLine):
    # Calculation of intersection points between two "orthogonal" lines

    if vLine[0]["x"] > vLine[1]["x"]:
        temp = vLine[0]
        vLine[0] = vLine[1]
        vLine[1] = temp
    if hLine[0]["x"] > hLine[1]["x"]:
        temp = hLine[0]
        hLine[0] = hLine[1]
        hLine[1] = temp
            
    mVert = (vLine[1]["y"] - vLine[0]["y"]) / (vLine[1]["x"] - vLine[0]["x"])
    mHori = (hLine[1]["y"] - hLine[0]["y"]) / (hLine[1]["x"] - hLine[0]["x"])
    nVert = vLine[0]["y"] - (mVert*vLine[0]["x"])
    nHori = hLine[0]["y"] - (mHori*hLine[0]["x"])
    x = (nVert - nHori) / (mHori - mVert)
    y = mVert*x + nVert

    return {"x": int(x), "y": int(y)}

def _add_line_intersection_anchors(anchors):
    # Adding line intersection to dictionary

    upLeftIntersect = _line_intersection(
        [anchors["rightBorderBetween2"], anchors["leftBorderBetween2"]], 
        [anchors["lowerBorderBetween2"], anchors["upperBorderBetween2"]]
    )
    upRightIntersect = _line_intersection(
        [anchors["rightBorderBetween2"], anchors["leftBorderBetween2"]], 
        [anchors["lowerBorderBetween1"], anchors["upperBorderBetween1"]]
    )
    downLeftIntersect = _line_intersection(
        [anchors["rightBorderBetween1"], anchors["leftBorderBetween1"]], 
        [anchors["lowerBorderBetween2"], anchors["upperBorderBetween2"]]
    )
    downRightIntersect = _line_intersection(
        [anchors["rightBorderBetween1"], anchors["leftBorderBetween1"]], 
        [anchors["lowerBorderBetween1"], anchors["upperBorderBetween1"]]
    )
    anchors.update({
        "upRightIntersect": 
            {"x": upRightIntersect["x"], "y": upRightIntersect["y"]}, 
        "upLeftIntersect": 
            {"x": upLeftIntersect["x"], "y": upLeftIntersect["y"]}, 
        "downRightIntersect": 
            {"x": downRightIntersect["x"], "y": downRightIntersect["y"]}, 
        "downLeftIntersect": 
            {"x": downLeftIntersect["x"], "y": downLeftIntersect["y"]}})

    return anchors

def _squares(anchors):
    # Naming of points within anchors dictionary 
    # for debugging and readability

    squares = {
        "TOP_LEFT_CORNER": {
            "upLeft": anchors["downRightIntersect"], 
            "upRight": anchors["rightBorderBetween1"], 
            "downLeft": anchors["lowerBorderBetween1"], 
            "downRight": anchors["downRightCorner"]}, 
        "TOP_MIDDLE": {
            "upLeft": anchors["downLeftIntersect"], 
            "upRight": anchors["downRightIntersect"], 
            "downLeft": anchors["lowerBorderBetween2"], 
            "downRight": anchors["lowerBorderBetween1"]}, 
        "TOP_RIGHT_CORNER": {
            "upLeft": anchors["leftBorderBetween1"], 
            "upRight": anchors["downLeftIntersect"], 
            "downLeft": anchors["downLeftCorner"], 
            "downRight": anchors["lowerBorderBetween2"]}, 
        "LEFT_MIDDLE": {
            "upLeft": anchors["upRightIntersect"], 
            "upRight": anchors["rightBorderBetween2"], 
            "downLeft": anchors["downRightIntersect"], 
            "downRight": anchors["rightBorderBetween1"]} , 
        "CENTER": {
            "upLeft": anchors["upLeftIntersect"], 
            "upRight": anchors["upRightIntersect"],
            "downLeft": anchors["downLeftIntersect"], 
            "downRight": anchors["downRightIntersect"]}, 
        "RIGHT_MIDDLE": {
            "upLeft": anchors["leftBorderBetween2"], 
            "upRight": anchors["upLeftIntersect"], 
            "downLeft": anchors["leftBorderBetween1"], 
            "downRight": anchors["downLeftIntersect"]}, 
        "BOTTOM_LEFT_CORNER": {
            "upLeft": anchors["upperBorderBetween1"], 
            "upRight": anchors["upRightCorner"], 
            "downLeft": anchors["upRightIntersect"], 
            "downRight": anchors["rightBorderBetween2"]}, 
        "BOTTOM_MIDDLE": {
            "upLeft": anchors["upperBorderBetween2"], 
            "upRight": anchors["upperBorderBetween1"], 
            "downLeft": anchors["upLeftIntersect"], 
            "downRight": anchors["upRightIntersect"]},
        "BOTTOM_RIGHT_CORNER": {
            "upLeft": anchors["upLeftCorner"], 
            "upRight": anchors["upperBorderBetween2"], 
            "downLeft": anchors["leftBorderBetween2"], 
            "downRight": anchors["upLeftIntersect"]}
    }
    return squares

def calc_board_cases(board_coordinates, config):
    # Returns pixel positions of corners of all squares on the board

    _sort(board_coordinates, 0)
    corner_dict = {
        "upLeftCorner": {"x": 0, "y": 0}, 
        "upRightCorner": {"x": 0, "y": 0}, 
        "downLeftCorner": {"x": 0, "y": 0}, 
        "downRightCorner": {"x": 0, "y": 0}
    }

    if board_coordinates[0][1] < board_coordinates[1][1]:
        corner_dict["downRightCorner"]["x"] = board_coordinates[0][0]
        corner_dict["downRightCorner"]["y"] = board_coordinates[0][1]
        corner_dict["upRightCorner"]["x"] = board_coordinates[1][0]
        corner_dict["upRightCorner"]["y"] = board_coordinates[1][1]
    else:
        corner_dict["downRightCorner"]["x"] = board_coordinates[1][0]
        corner_dict["downRightCorner"]["y"] = board_coordinates[1][1]
        corner_dict["upRightCorner"]["x"] = board_coordinates[0][0]
        corner_dict["upRightCorner"]["y"] = board_coordinates[0][1]
    
    if board_coordinates[2][1] < board_coordinates[3][1]:
        corner_dict["downLeftCorner"]["x"] = board_coordinates[2][0]
        corner_dict["downLeftCorner"]["y"] = board_coordinates[2][1]
        corner_dict["upLeftCorner"]["x"] = board_coordinates[3][0]
        corner_dict["upLeftCorner"]["y"] = board_coordinates[3][1]
    else:
        corner_dict["downLeftCorner"]["x"] = board_coordinates[3][0]
        corner_dict["downLeftCorner"]["y"] = board_coordinates[3][1]
        corner_dict["upLeftCorner"]["x"] = board_coordinates[2][0]
        corner_dict["upLeftCorner"]["y"] = board_coordinates[2][1]
    
    anchors  = _add_between_anchors(corner_dict, config)
    allAnchors = _add_line_intersection_anchors(anchors)
    sqrs = _squares(allAnchors)
    return sqrs