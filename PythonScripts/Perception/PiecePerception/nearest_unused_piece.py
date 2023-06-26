import cv2
import numpy as np

def get_nearest_unused_piece(frame, board_corners, available_game_pieces):

    image = frame.copy()

    # List conversion to bring list in correct form for further processing
    converted_list = [[x[0].tolist() for x in sublist] for sublist in board_corners]
    converted_list = converted_list[0]
    reference_image_points = converted_list[1:] + [converted_list[0]]
    reference_real_points = [[0, 0], [36.4, 0], [36.4, 36.6], [0, 36.4]]

    # Convert the reference image points to integer tuples
    reference_image_points = [tuple(point) for point in reference_image_points]

    # Create a mask for the enclosed region
    mask = np.zeros_like(image)

    # Apply the mask to the image
    image = cv2.bitwise_or(image, mask)

    # Define the region of interest (ROI) coordinates
    roi_x_min = 0
    roi_x_max = image.shape[1]
    roi_y_min = 220
    roi_y_max = 560

    # Crop the image to the ROI, to exclude other parts of the image apart from the table
    roi_image = image[roi_y_min:roi_y_max, roi_x_min:roi_x_max]

    lower_green = np.array([0, 100, 0], dtype=np.uint8)
    upper_green = np.array([120, 255, 100], dtype=np.uint8)

    mask = cv2.inRange(roi_image, lower_green, upper_green)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    contours = contours[:available_game_pieces]

    if len(contours) > 0:
        min_distance = float('inf')
        closest_center = None

        for contour in contours:
            # Calculate the center of each contour
            M = cv2.moments(contour)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            # Shift the center coordinates to the full image coordinates
            center = (center[0] + roi_x_min, center[1] + roi_y_min)

            # Calculate Euclidean distance between (0,0) and the current center
            distance = np.linalg.norm(np.array(center) - np.array(reference_image_points[1]))

            if distance < min_distance:
                min_distance = distance
                closest_center = center

        if closest_center is not None:
            # center of contour without correction set to unknown point
            unknown_point = closest_center

            # center of contour without + static correction of x any image coordinates
            # unknown_point = (closest_center[0] + 11, closest_center[1] + 13)

            # Convert the points to numpy arrays
            image_points = np.array(reference_image_points, dtype=np.float32)
            real_points = np.array(reference_real_points, dtype=np.float32)

            # Calculate the homography matrix
            homography, _ = cv2.findHomography(image_points, real_points, cv2.RANSAC)

            # Apply the homography to image points
            transformed_points = cv2.perspectiveTransform(image_points.reshape(-1, 1, 2), homography).reshape(-1, 2)

            # Transform the unknown point
            unknown_point = np.array([unknown_point], dtype=np.float32)
            transformed_unknown_point = cv2.perspectiveTransform(unknown_point.reshape(-1, 1, 2), homography).reshape(-1, 2)

            # Calculate Euclidean distance between (0,0) and the transformed unknown point
            distance = np.linalg.norm(transformed_unknown_point - transformed_points[1])

            # Calculate the distance along the x-axis
            x_distance = transformed_unknown_point[0, 0] - transformed_points[1, 0]

            # Calculate the distance along the y-axis
            y_distance = transformed_unknown_point[0, 1] - transformed_points[1, 1]

            return tuple(float(x_distance), float(y_distance))
        else:
            print("No valid contour center found.")
    else:
        print("No contours outside of the game board found!")