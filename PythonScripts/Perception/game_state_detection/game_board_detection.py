import cv2
import numpy as np
import yaml

def game_board_detection(frame):
    imageFrame = frame.copy()
    config = yaml.safe_load(open("global_config.yml"))

    # Convert frame from BGR to HSV color space
    hsv = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    # Define color range for violet/lila
    lower_violet = np.array(config["color_bounds"]["violet_lower"])
    upper_violet = np.array(config["color_bounds"]["violet_upper"])

    # Create a mask that isolates pixels within the color range
    mask = cv2.inRange(hsv, lower_violet, upper_violet)

    # Apply the mask to the original image
    masked_image = cv2.bitwise_and(imageFrame, imageFrame, mask=mask)

    # Convert masked image to grayscale
    gray = cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)

    # Find contours around the detected corners
    contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Find all rectangles among the contours
    rectangles = []
    for cnt in contours:
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.07 * peri, True)
        if len(approx) == 4:
            area = cv2.contourArea(approx)
            if area > 1000:
                rectangles.append(approx)

    # Sort the rectangles by their area, from largest to smallest
    rectangles = sorted(rectangles, key=lambda x: cv2.contourArea(x), reverse=True)

    # Define game_board as the largest rectangle
    game_board = rectangles[0]
    game_board_coords = []

    # Transform coordinates to flat the game board array: [[[x1, y1]]] => [[x1, y1]]
    for coords in game_board:
        game_board_coords.append([coords[0][0], coords[0][1]])
    
    return game_board_coords
