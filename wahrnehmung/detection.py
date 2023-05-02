import cv2
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

    color_bounds = config['color_bounds']
    thresholds = config['thresholds']

    # Initialize 3x3 matrix which is later handed to movement team
    board_cases = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

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

        cv2.imshow('Frame', imageFrame)
        # output.write(imageFrame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # output.release()
    cv2.destroyAllWindows()
    return board_cases