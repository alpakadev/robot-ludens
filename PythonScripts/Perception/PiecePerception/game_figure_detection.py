import cv2
import numpy as np
import yaml

def get_all_pieces_coordinates(frame, game_board_coords):
    imageFrame = frame.copy()
    config = yaml.safe_load(open("global_config.yml"))

    red_figure_centers = []
    green_figure_centers = []

    # Define the lower and upper bounds for red and green color
    lower_green = np.array(config["color_bounds"]["green_lower"])
    upper_green = np.array(config["color_bounds"]["green_upper"])

    lower_red = np.array(config["color_bounds"]["red_lower"])
    upper_red = np.array(config["color_bounds"]["red_upper"])

    # Crop the image to get only the shape of the board
    mask = np.zeros(frame.shape[:2], dtype="uint8")
    roi = np.array(game_board_coords)
    cv2.fillPoly(mask, [roi], (255, 255, 255))
    masked = cv2.bitwise_and(imageFrame, imageFrame, mask=mask)

    # Convert the image to HSV color space
    hsv = cv2.cvtColor(masked, cv2.COLOR_BGR2HSV)

    # Threshold the image to get the red color regions
    red_mask = cv2.inRange(hsv, lower_red, upper_red)

    # Find the contours of red regions
    red_contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate over the red contours
    for red_contour in red_contours:
        # Calculate the area of the contour
        area = cv2.contourArea(red_contour)
        # Only consider the contour if the area is greater than the threshold
        if area > 100:
            # Calculate the centroid of the contour
            M = cv2.moments(red_contour)
            centroid_x = int(M['m10'] / M['m00'])
            centroid_y = int(M['m01'] / M['m00'])
            red_figure_centers.append((centroid_x, centroid_y))

    # Threshold the image to get the green color regions
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    # Find the contours of green regions
    green_contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate over the green contours
    for green_contour in green_contours:
        # Calculate the area of the contour
        area = cv2.contourArea(green_contour)
        if area > 100:
            # Calculate the centroid of the contour
            M = cv2.moments(green_contour)
            centroid_x = int(M['m10'] / M['m00'])
            centroid_y = int(M['m01'] / M['m00'])
            green_figure_centers.append((centroid_x, centroid_y))

    return red_figure_centers, green_figure_centers
