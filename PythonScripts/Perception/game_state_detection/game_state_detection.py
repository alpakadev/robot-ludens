import cv2
import numpy as np
import yaml

config = yaml.safe_load(open("global_config.yml"))

red_figure_coords = []
green_figure_coords = []

game_state = []

# Define the lower and upper bounds for red color
lower_green = np.array(config["color_bounds"]["green_lower"])
upper_green = np.array(config["color_bounds"]["green_upper"])

# Define the lower and upper bounds for red color
lower_red = np.array(config["color_bounds"]["red_lower"])
upper_red = np.array(config["color_bounds"]["red_upper"])

def get_board_state(frame, cases_coords):
    imageFrame = frame.copy()
    hsv = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
    game_state = [[_get_case_value(cases_coords["downR"], hsv), _get_case_value(cases_coords["downMid"], hsv), _get_case_value(cases_coords["downL"], hsv)], 
                  [_get_case_value(cases_coords["midR"], hsv), _get_case_value(cases_coords["midMid"], hsv), _get_case_value(cases_coords["midL"], hsv)], 
                  [_get_case_value(cases_coords["upR"], hsv), _get_case_value(cases_coords["upMid"], hsv), _get_case_value(cases_coords["upL"], hsv)]]
    return game_state

def _get_case_value(case, frame):
    # Example Case: "upL": {"upLeft": {"x": 0, "y": 0}, "upRight": {"x": 0, "y": 0}, "downLeft": {"x": 0, "y": 0}, "downRight": {"x": 0, "y": 0}}
    # Crop the image to get only the current rectangle
    mask = np.zeros(frame.shape[:2], dtype="uint8")

    # Transform case coordinates in array format
    roi = np.array([[case["upLeft"]["x"], case["upLeft"]["y"]], 
                    [case["upRight"]["x"], case["upRight"]["y"]], 
                    [case["downRight"]["x"], case["downRight"]["y"]], 
                    [case["downLeft"]["x"], case["downLeft"]["y"]]])
    
    # Cut everything from image except the area of the case
    cv2.fillPoly(mask, [roi], (255, 255, 255))
    masked = cv2.bitwise_and(frame, frame, mask=mask)
    gray_masked = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)

    # Threshold the image to get the red color regions
    red_mask = cv2.inRange(masked, lower_red, upper_red)

    # Threshold the image to get the green color regions
    green_mask = cv2.inRange(masked, lower_green, upper_green)

    # Calculate the amount of pixels in the square
    total_pixels = cv2.countNonZero(gray_masked)

    # Count red and green pixels within case
    red_count = cv2.countNonZero(red_mask)
    green_count = cv2.countNonZero(green_mask)

    # Calculate percentage of red and green in relation to total pixel count
    red_percent = red_count / total_pixels
    green_percent = green_count / total_pixels

    # Return 1 when piece is red, return -1 when piece is green, return 0 when square is empty
    if red_percent > config["thresholds"]['red'] > green_percent:
            return 1
    elif green_percent > config["thresholds"]['green'] > red_percent:
        return -1
    else:
        return 0