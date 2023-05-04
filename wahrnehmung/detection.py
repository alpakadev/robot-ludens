import cv2
import numpy as np
from square import Square
from video import capture_video
from config import parse_config

def get_board_cases(reachy):
    # Use coordinates and thresholds from config.yml
    config = parse_config()

    camera = reachy.right_camera

    width = camera.last_frame.shape[1]
    height = camera.last_frame.shape[0]

    # output = capture_video(camera, 
    #                        'output.mp4', 
    #                        width, 
    #                        height)

    squares = []
    for square_config in config['squares']:
        top_left = square_config['top_left']
        bottom_right = square_config['bottom_right']
        squares.append(Square(top_left[0], 
                              top_left[1], 
                              bottom_right[0], 
                              bottom_right[1], 
                              None))
        
    # game_square = config['game_square']
    # game_square_obj = Square(game_square[0]['top_left'][0],
    #                          game_square[0]['top_left'][1],
    #                          game_square[0]['bottom_right'][0],
    #                          game_square[0]['bottom_right'][1],
    #                          None)

    color_bounds = config['color_bounds']
    thresholds = config['thresholds']

    # Initialize 3x3 matrix which is later handed to movement team
    board_cases = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # Initialize previous frame to None
    prev_frame = None

    # Initialize movement to False
    movement = False

    while True:
        frame = camera.last_frame
        imageFrame = frame.copy()

        rectangles = []
        for idx, square in enumerate(squares):
            color = square.get_color(imageFrame, color_bounds, thresholds)
            if color == 'red':
                square.color = (0, 0, 255)
                board_cases[idx//3][idx%3] = 2
            elif color == 'green':
                square.color = (0, 255, 0)
                board_cases[idx//3][idx%3] = 1
            else:
                square.color = (255, 255, 255)

            rectangles.append(((square.x1, square.y1), 
                               (square.x2, square.y2), 
                               square.color))

        for rect in rectangles:
            cv2.rectangle(imageFrame, 
                          rect[0], 
                          rect[1], 
                          rect[2], 
                          2)

        if prev_frame is not None:
            # Define region of interest
            roi = frame[290:560, 70:355]
            prev_roi = prev_frame[290:560, 70:355]

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
        # prev_frame = frame.copy()

        cv2.imshow('Frame', imageFrame)
        # output.write(imageFrame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # output.release()
    cv2.destroyAllWindows()
    return board_cases