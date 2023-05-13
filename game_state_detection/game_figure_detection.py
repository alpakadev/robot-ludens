import cv2
import numpy as np

def game_figure_detection(reachy, game_board_coords):
    camera = reachy.right_camera

    frame = camera.last_frame
    imageFrame = frame.copy()

    # Define the coordinates of game board
    x, y, w, h = game_board_coords[0]

    # Draw the rectangle on the image
    # cv2.rectangle(imageFrame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    red_figure_coords = []
    green_figure_coords = []

    # Crop the image to get only the current rectangle
    roi = imageFrame[y:y+h, x:x+w]

    # Convert the image to HSV color space
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for red color
    lower_red = np.array([0, 70, 50])
    upper_red = np.array([10, 255, 255])
    lower_red1 = np.array([170, 70, 50])
    upper_red1 = np.array([180, 255, 255])

    # Threshold the image to get the red color regions
    red_mask1 = cv2.inRange(hsv, lower_red, upper_red)
    red_mask2 = cv2.inRange(hsv, lower_red1, upper_red1)
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)

    # Find the contours of red regions
    red_contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate over the red contours
    for red_contour in red_contours:
        # Calculate the area of the contour
        area = cv2.contourArea(red_contour)
        # Only draw the rectangle if the area is greater than the threshold
        if area > 100:
            red_rect = cv2.boundingRect(red_contour)
            red_x, red_y, red_w, red_h = red_rect
            red_figure_coords.append((x + red_x, y + red_y, x + red_x + red_w, y + red_y + red_h))
            # cv2.rectangle(roi, (red_x, red_y), (red_x+red_w, red_y+red_h), (0, 0, 255), 2)

    # Define the lower and upper bounds for green color
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([90, 255, 255])

    # Threshold the image to get the green color regions
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    # Find the contours of green regions
    green_contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate over the green contours
    for green_contour in green_contours:
        # Calculate the area of the contour
        area = cv2.contourArea(green_contour)
        if area > 100:
            green_rect = cv2.boundingRect(green_contour)
            green_x, green_y, green_w, green_h = green_rect
            green_figure_coords.append((x + green_x, y + green_y, x + green_x + green_w, y + green_y + green_h))
            # cv2.rectangle(roi, (green_x, green_y), (green_x+green_w, green_y+green_h), (0, 255, 0), 2)

    # Display the image
    cv2.imshow('Frame', imageFrame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

    print("Red figure coords: ", red_figure_coords)
    print("Green figure coords: ", green_figure_coords)
    cv2.destroyAllWindows()
    return red_figure_coords, green_figure_coords