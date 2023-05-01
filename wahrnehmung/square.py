import cv2
import numpy as np

class Square:
    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

    @staticmethod
    def get_color(frame, x1, y1, x2, y2, color_bounds, thresholds):
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = np.zeros(frame.shape[:2], dtype=np.uint8)
        mask[y1:y2, x1:x2] = 255
        masked_frame = cv2.bitwise_and(hsv_frame, hsv_frame, mask=mask)

        red_lower = np.array(color_bounds['red_lower'])
        red_upper = np.array(color_bounds['red_upper'])
        green_lower = np.array(color_bounds['green_lower'])
        green_upper = np.array(color_bounds['green_upper'])

        red_mask = cv2.inRange(masked_frame, red_lower, red_upper)
        green_mask = cv2.inRange(masked_frame, green_lower, green_upper)

        red_count = cv2.countNonZero(red_mask)
        green_count = cv2.countNonZero(green_mask)

        red_threshold = thresholds['red']
        green_threshold = thresholds['green']

        if red_count > red_threshold:
            return 'red'
        elif green_count > green_threshold:
            return 'green'
        else:
            return 'none'
