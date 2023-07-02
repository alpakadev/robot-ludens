import dlib
import face_recognition as fr
import cv2
from PIL import Image
import numpy as np
import time
from math import ceil, radians, sin

# Durchsucht ein aufgenommenes Bild auf Gesichter und entnimmt das größte
def detect_human_player(reachy):
    # Reachys Kopf in Basis Position bringen
    reachy.turn_on("head")
    reachy.head.look_at(1, 0, 0, 1, "simul")
    #move.do_move_head([0.5, 0, 0, 1])
    
    image = take_picture(reachy)

    face_locations = fr.face_locations(image, number_of_times_to_upsample=1)
    box_size = 0
    face_encoding = []
    face_box = []
    for face in face_locations:
        enc = fr.face_encodings(image, known_face_locations=[face], num_jitters=10, model="large")
        size = (face[2] - face[0]) * (face[1] - face[3])
        if size > box_size:
            box_size = size
            face_encoding = enc
            face_box = face

    # Größtes Gesicht ermitteln
    cv2.rectangle(image, (face_box[3], face_box[0]), (face_box[1], face_box[2]), (255, 0, 0), 4)
    cv2.imwrite("Player.png", image)
    print("Face Detected")
    return face_encoding
    
# Steuer Funktion um Reachy dazu zubringen den Player anzuschauen
def look_at_human_player(reachy, face_enc):
    print("Looking at Player")
    image = take_picture(reachy)
    player_face_pos = compare_faces_for_pos(image, face_enc)

    if player_face_pos is not None:
        center_vision_on_face(image, player_face_pos, face_enc, reachy)
    else:
        print("Not in View")
        reachy.head.look_at(0.5, 0, 0, 1, "simul")

# überprüft ob sich das Player Gesicht im Bild befindet und wenn ja, dann wo
def compare_faces_for_pos(image, player_face_enc):
    face_positions = fr.face_locations(image, number_of_times_to_upsample=1)
    smallest_distance = None
    face_box = []

    for face in face_positions:
        unknown_face_enc = fr.face_encodings(image, known_face_locations=[face], num_jitters=10, model="large")
        results = fr.face_distance([unknown_face_enc[0]], player_face_enc[0])
        if smallest_distance is None:
            smallest_distance = results
            face_box = face
        elif results < smallest_distance:
            smallest_distance = results
            face_box = face
    
    print(smallest_distance, face_box)
    return face_box

def take_picture(reachy):
    camera = reachy.right_camera
    image = camera.last_frame
    return image

def get_largest_face(face_locations):
    # Die Bounding Box eines Gesichts aussuchen, die die größte Fläche einnimmt
    max = 0
    largest_face = None
    for face in face_locations:
        bottom, left, top, right = face
        size = (top - bottom) * (left - right)
        if size > max:
            max = size
            largest_face = face
    return largest_face

# Berechnet wie sich der Kopf bewegen muss um den Player direkt anzuschauen
def center_vision_on_face(image, face_pos, player_face_enc, reachy):
    print("Moving head to look at Player")
    # Dimensionen das aufgenommenen Bildes speichern
    im_width, im_height, _ = image.shape
    print("w", im_width, "h", im_height)

    bottom, left, top, right = face_pos
    face_center = [ceil(right + (left - right) / 2), ceil(bottom + (top - bottom) / 2)]
    cv2.circle(image, (face_center[0], face_center[1]), 5, (255, 0, 0), 3)
    cv2.imwrite("center.png", image)
    # Abweichung der Oberen rechten Ecke von den Mittellinien des Bildes ausrechnen
    x_diff = face_center[0] - im_width/2
    y_diff = face_center[1] - im_height/2

    reachy.turn_on("head")

    x_perc_contr = calc_center_diff(x_diff, im_width)
    y_perc_contr = calc_center_diff(y_diff, im_height)

    x_coor = ceil(im_width / 2 + im_width * (x_perc_contr * 0.5))
    y_coor = ceil(im_height / 2 + im_height * (y_perc_contr * 0.05))

    cv2.circle(image, (x_coor, y_coor), 5, (0, 255, 0), 3)
    cv2.imwrite("control.png", image)
    reachy.head.look_at(1, -1 * x_perc_contr, -1 * y_perc_contr, 1, "simul")

def calc_center_diff(p_c_diff, im_dim):
    lense_radius = 10
    lense_degrees = 180
    reachy_degress = 92
    lense_circumference = 10 * 3.14
    
    real_perc_diff = (100 / (im_dim / p_c_diff)) * 0.01
    real_angle_diff = 180 * (real_perc_diff)
    real_p_c_distance = lense_radius * 2 * sin(radians(real_angle_diff/2))
    real_p_c_distance_perc = (100 / (lense_circumference / real_p_c_distance)) * 0.01

    return (lense_degrees / reachy_degress) * real_p_c_distance_perc