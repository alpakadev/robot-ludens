import cv2
import numpy as np
import yaml
from .estimate_metric_distance import estimate_metric_distance

def get_all_pieces_coordinates(frame, board_coordinates, 
                               board_cases_coordinates):
    imageFrame = frame.copy()
    config = yaml.safe_load(open("global_config.yml"))

    piece_centers = [0] * 9

    # Define the lower and upper bounds for red and green color
    lower_green = np.array(config["color_bounds"]["green_lower"])
    upper_green = np.array(config["color_bounds"]["green_upper"])

    lower_red = np.array(config["color_bounds"]["red_lower"])
    upper_red = np.array(config["color_bounds"]["red_upper"])

    # Crop the image to get only the shape of the board
    mask = np.zeros(frame.shape[:2], dtype="uint8")
    roi = np.array(board_coordinates)
    cv2.fillPoly(mask, [roi], (255, 255, 255))
    masked = cv2.bitwise_and(imageFrame, imageFrame, mask=mask)

    # Convert the image to HSV color space
    hsv = cv2.cvtColor(masked, cv2.COLOR_BGR2HSV)

    for case_coords in board_cases_coordinates:
        case = board_cases_coordinates[case_coords]

        # Crop the image to the coordinates of the current board case
        case_mask = np.zeros(frame.shape[:2], dtype="uint8")
        case_roi = np.array(
            [case["upLeft"], 
            case["upRight"], 
            case["downRight"], 
            case["downLeft"]]
        )
        cv2.fillPoly(case_mask, [case_roi], (255, 255, 255))
        case_masked = cv2.bitwise_and(hsv, hsv, mask=case_mask)

        # Threshold the image to get the red color regions
        red_mask = cv2.inRange(case_masked, lower_red, upper_red)

        # Find the contours of red regions
        red_contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, 
                                                   cv2.CHAIN_APPROX_SIMPLE)

        # Sort the red contours by area in descending order
        red_contours = sorted(red_contours, key=cv2.contourArea, reverse=True)

        # Proceed only with the largest contour
        if len(red_contours) > 0:
            red_contour = red_contours[0]
            area = cv2.contourArea(red_contour)
            if area > 100:
                # Calculate the centroid of the contour
                M = cv2.moments(red_contour)
                centroid_x = int(M['m10'] / M['m00'])
                centroid_y = int(M['m01'] / M['m00'])
                x_distance, y_distance = estimate_metric_distance(
                    frame, 
                    board_coordinates
                )
                piece_centers[case_coords] = (x_distance, y_distance, "R")

        # Threshold the image to get the green color regions
        green_mask = cv2.inRange(case_masked, lower_green, upper_green)

        # Find the contours of green regions
        green_contours, hierarchy = cv2.findContours(
            green_mask, 
            cv2.RETR_EXTERNAL, 
            cv2.CHAIN_APPROX_SIMPLE
        )

        # Sort the green contours by area in descending order
        green_contours = sorted(green_contours, key=cv2.contourArea, 
                                reverse=True)

        # Proceed only with the largest contour
        if len(green_contours) > 0:
            green_contour = green_contours[0]
            area = cv2.contourArea(green_contour)
            if area > 100:
                # Calculate the centroid of the contour
                M = cv2.moments(green_contour)
                centroid_x = int(M['m10'] / M['m00'])
                centroid_y = int(M['m01'] / M['m00'])
                x_distance, y_distance = estimate_metric_distance(
                    frame, 
                    board_coordinates, 
                    centroid_x, 
                    centroid_y
                )
                piece_centers[case_coords] = (x_distance, y_distance, "G")

    return piece_centers