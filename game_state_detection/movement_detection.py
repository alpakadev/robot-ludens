import cv2
import numpy as np
from game_board_detection import game_board_detection

def movement_detection(reachy, game_board_coords):

    camera = reachy.right_camera

    # Initialize previous frame to None
    prev_frame = None

    # Initialize movement to False
    movement = False

    # Define the coordinates of game board
    game_board_coords = game_board_detection(reachy)
    x, y, w, h = game_board_coords[0]

    while True:
        frame = camera.last_frame
        imageFrame = frame.copy()

        if prev_frame is not None:
            # Define region of interest (game_board_coords from game_board_detection)
            roi = frame[y:y+h, x:x+w]
            prev_roi = prev_frame[y:y+h, x:x+w]
            # Perform motion detection on ROI
            if prev_roi is not None:
                # Convert ROI images to grayscale and blur
                gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                gray_prev_roi = cv2.cvtColor(prev_roi, cv2.COLOR_BGR2GRAY)
                gray_roi = cv2.GaussianBlur(gray_roi, (5, 5), sigmaX=0)
                gray_prev_roi = cv2.GaussianBlur(gray_prev_roi, (5, 5), sigmaX=0)

                # Calculate absolute difference between grayscale ROIs
                diff = cv2.absdiff(gray_roi, gray_prev_roi)

                # 4/5 Only take different areas that are different enough (>20 / 255)
                _, thresh = cv2.threshold(diff, 20, 255, cv2.THRESH_BINARY)

                # 4/5 Dilate the image a bit to make differences more seeable; more suitable for contour detection
                kernel = np.ones((5,5),np.uint8)
                thresh = cv2.dilate(thresh, kernel, iterations=1)

                contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, 
                                               cv2.CHAIN_APPROX_SIMPLE)
                movement_pixels = 0
                for contour in contours:
                    if cv2.contourArea(contour) < 500:
                        continue
                    (x, y, w, h) = cv2.boundingRect(contour)
                    # Count the number of movement pixels
                    movement_pixels += cv2.contourArea(contour)

                # Calculate the percentage of changed pixels
                total_pixels = roi.shape[0] * roi.shape[1]
                movement_percentage = (movement_pixels / total_pixels) * 100

                # Set movement flag based on the percentage of changed pixels
                if movement_percentage > 0:
                    movement = True
                else:
                    movement = False

        print(movement)
        # Update previous frame
        prev_frame = frame.copy()

        cv2.imshow('Frame', imageFrame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()