import face_recognition as fr
import cv2
import numpy as np
import time
from math import ceil, radians, sin
import json
from Perception.FaceRecognition.NumpyEncoder import NumpyEncoder
import dlib

def identify_human_player(reachy, move):
    # Identify the largest face in the picture as human player
    # Returns face encoding of human player

    reachy.turn_on("head")
    try:
        move.do_move_head([0.5, 0, 0])
    except NotImplementedError:
        # Check if modified function for simulation has to be used
        reachy.head.look_at(1, 0, 0, 1, "simul")
    
    image = _take_picture(reachy)

    face_locations = fr.face_locations(image, number_of_times_to_upsample=1)
    box_size = 0
    face_encoding = []
    face_box = []
    for face in face_locations:
        enc = fr.face_encodings(image, known_face_locations=[face], 
                                num_jitters=5, model="large")
        size = (face[2] - face[0]) * (face[1] - face[3])
        if size > box_size:
            box_size = size
            face_encoding = enc
            face_box = face

    # Save largest face as png for debugging and showcase
    cv2.rectangle(
        image, 
        (face_box[3], face_box[0]), 
        (face_box[1], face_box[2]), 
        (255, 0, 0), 
        4
    )

    cv2.imwrite("PythonScripts/Perception/FaceRecognition/Player.png", image)

    print("Face Detected")
    return face_encoding
    
def serialize_player_face(face):
    with open("PythonScripts/Perception/FaceRecognition/face_encoding.json", 
              "w", encoding="utf-8") as file:

        json.dump(
            {"playerFace": face}, 
            file, 
            cls=NumpyEncoder, 
            ensure_ascii=False, 
            indent=4
        )

def deserialize_player_face():
    with open("PythonScripts/Perception/FaceRecognition/face_encoding.json", 
    "r", encoding="utf-8") as file:
        encoding = json.load(file)
    return np.array(encoding["playerFace"])

def look_at_human_player(reachy, move, face_enc):
    print("Looking at Player")
    image = _take_picture(reachy)
    player_face_pos = _compare_faces_for_pos(image, face_enc)
    print(player_face_pos)

    if player_face_pos is not None:
        _center_vision_on_face(reachy, move, image, player_face_pos, face_enc)
    else:
        print("Not in View")
        try:
            move.do_move_head([0.5, 0, 0])
        except NotImplementedError:
            # Check if modified function for simulation has to be used
            reachy.head.look_at(1, 0, 0, 1, "simul")

def _compare_faces_for_pos(image, player_face_enc):
    # Checks where player face is in image

    face_positions = fr.face_locations(image, number_of_times_to_upsample=1)
    smallest_distance = None
    face_box = []

    for face in face_positions:
        unknown_face_enc = fr.face_encodings(
            image, 
            known_face_locations=[face], 
            num_jitters=5, 
            model="large")

        results = fr.face_distance([unknown_face_enc[0]], player_face_enc[0])
        if smallest_distance is None:
            smallest_distance = results
            face_box = face
        elif results < smallest_distance:
            smallest_distance = results
            face_box = face
    
    return face_box

def _take_picture(reachy):
    camera = reachy.right_camera
    image = camera.last_frame
    return image

def _center_vision_on_face(reachy, move, image, face_pos, player_face_enc):
    # Calculate exact Movement of Reachys Neck joint

    print("Moving head to look at Player")
    im_height, im_width, _ = image.shape

    bottom, left, top, right = face_pos
    face_center = [ceil(right + (left - right) / 2), 
                   ceil(bottom + (top - bottom) / 2)]

    # Deviation from top right corner of face bounding box
    x_diff = face_center[0] - im_width/2
    y_diff = face_center[1] - im_height/2

    reachy.turn_on("head")

    x_perc_contr = _calc_center_diff(x_diff, im_width)
    y_perc_contr = _calc_center_diff(y_diff, im_height)

    x_coor = ceil(im_width/2 + im_width*(x_perc_contr * 0.5))
    y_coor = ceil(im_height/2 + im_height*(y_perc_contr * 0.05))

    distance_to_move_horizontally = x_perc_contr * -0.5
    distance_to_move_vertically = y_perc_contr * -0.5

    if distance_to_move_horizontally < 0:
        distance_to_move_horizontally += 0.05
    else:
        distance_to_move_horizontally -= 0.05

    try:
        move.do_move_head([
            1, 
            distance_to_move_horizontally, 
            distance_to_move_vertically
        ])
    except NotImplementedError:
        # Check if modified function for simulation has to be used
        reachy.head.look_at(
            1, 
            distance_to_move_horizontally, 
            distance_to_move_vertically, 
            1, 
            "simul"
        )
    image = _take_picture(reachy)
    cv2.imwrite("PythonScripts/Perception/FaceRecognition/Looking_at_you.png", image)
    reachy.turn_off_smoothly("head")


def _calc_center_diff(p_c_diff, im_dim):
    # Correct differences to face center point according to Reachys Lense
    # im_dim = width or height of image
    # p_c_diff = difference from point p to face center in dimension im_dim

    lense_radius = 10
    lense_degrees = 180
    reachy_degress = 92
    lense_circumference = 10 * 3.14
    
    real_perc_diff = (100 / (im_dim / p_c_diff)) * 0.01
    real_angle_diff = 180 * (real_perc_diff)
    real_p_c_dist = lense_radius * 2 * sin(radians(real_angle_diff/2))
    real_p_c_dist_perc = (100 / (lense_circumference / real_p_c_dist)) * 0.01

    return (lense_degrees / reachy_degress) * real_p_c_dist_perc