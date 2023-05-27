import cv2
import numpy as np
import time

def get_stable_image(reachy, config):
    movement = True
    # Initialize previous frame to None
    prev_frame = None

    while movement == True:
        camera = reachy.right_camera
        frame = camera.last_frame

        if prev_frame is not None:
            # Define region of interest
            roi = frame[290:700, 70:700]
            prev_roi = prev_frame[290:700, 70:700]

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
                    prev_frame = frame.copy()
                    frame = camera.last_frame
                    movement = True
                else:
                    movement = False
        else:
            prev_frame = frame.copy()
            time.sleep(config["time_between_images"])
            frame = camera.last_frame

    return frame