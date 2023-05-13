import cv2
import numpy as np

def game_board_detection(reachy):
    camera = reachy.right_camera

    while True:
        frame = camera.last_frame
        imageFrame = frame.copy()

        # Convert frame from BGR to HSV color space
        hsv = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

        # Define color range for violet/lila
        lower_violet = np.array([140,50,50])
        upper_violet = np.array([160,255,255])

        # Create a mask that isolates pixels within the color range
        mask = cv2.inRange(hsv, lower_violet, upper_violet)

        # Apply the mask to the original image
        masked_image = cv2.bitwise_and(imageFrame, imageFrame, mask=mask)

        # Convert masked image to grayscale
        gray = cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)

        # Detect corners using goodFeaturesToTrack
        corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)

        # Draw the detected corners on the original image
        # corners = np.int0(corners)
        # for corner in corners:
        #     x, y = corner.ravel()
        #     cv2.circle(imageFrame, (x, y), 3, (0, 0, 255), -1)

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

        # Draw the rectangles around the detected corners
        # for rect in rectangles:
        #     cv2.drawContours(imageFrame, [rect], -1, (0, 255, 0), 2)

        # Sort the rectangles by their area, from largest to smallest
        rectangles = sorted(rectangles, key=lambda x: cv2.contourArea(x), reverse=True)

        # Define game_board as the largest rectangle
        game_board = rectangles[0]

        game_board_coords = []
        x, y, w, h = cv2.boundingRect(game_board)
        game_board_coords.append((x, y, w, h))

        cv2.imshow('Frame', imageFrame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    print("Game board coords:", game_board_coords)
    cv2.destroyAllWindows()
    return game_board_coords
