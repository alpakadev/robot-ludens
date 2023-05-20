import cv2

def capture_video(camera, output_path, width, height):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output = cv2.VideoWriter(output_path, fourcc, 10.0, (width, height))
    return output