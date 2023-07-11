import cv2
import numpy as np

def estimate_metric_distance(frame, board_corners, centroid_x, centroid_y):
    image = frame.copy()

    reference_image_points = board_corners
    reference_real_points = [[0, 0], [36.4, 0], [36.4, 36.6], [0, 36.4]]

    # Convert the reference image points to integer tuples
    reference_image_points = [tuple(point) for point in reference_image_points]

    # Create a mask for the area outside of the enclosed region
    mask = np.ones_like(image) * 255
    cv2.fillPoly(mask, [np.array(reference_image_points)], (0, 0, 0))
    
    # Apply the mask to the image
    image = cv2.bitwise_or(image, mask)

    # Convert the points to numpy arrays
    image_points = np.array(reference_image_points, dtype=np.float32)
    real_points = np.array(reference_real_points, dtype=np.float32)

    # Calculate the homography matrix
    homography, _ = cv2.findHomography(image_points, real_points, cv2.RANSAC)

    # Apply the homography to image points
    transformed_points = cv2.perspectiveTransform(
        image_points.reshape(-1, 1, 2), homography).reshape(-1, 2)

    # Transform the unknown point for contour
    center = (centroid_x, centroid_y)
    unknown_point = np.array([center], dtype=np.float32)
    transformed_unknown_point = cv2.perspectiveTransform(
        unknown_point.reshape(-1, 1, 2), homography).reshape(-1, 2)

    # Calculate the distance along the x-axis
    x_distance = transformed_unknown_point[0, 0] - transformed_points[3, 0]

    # Calculate the distance along the y-axis
    y_distance = transformed_unknown_point[0, 1] - transformed_points[3, 1]

    # print(f"Distance along the x-axis for contour: {x_distance} cm")
    # print(f"Distance along the y-axis for contour: {y_distance} cm")
    return x_distance, y_distance