import dlib
import face_recognition as fr
import cv2
from PIL import Image
import numpy as np
import time
from math import ceil

# Ober Funktion zum erstmaligen erkennen des Gegenspielers
def detect_human_player(reachy):
    # Reachys Kopf in Basis Position bringen
    reachy.turn_on("head")
    reachy.head.look_at(0.5, 0, 0, 1, "simul")
    #move.do_move_head([0.5, 0, 0, 1])
    
    # Bild aufnehmen
    image = take_picture(reachy)
    #hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


    # Zum testen oben auskommentieren und das hier nutzen:
    # image = fr.load_image_file("group-people.jpeg")

    # Alle Gesichter aus dem Bild entnehmen
    face_locations = fr.face_locations(image, number_of_times_to_upsample=1)
    box_size = 0
    face_encoding = []
    for face in face_locations:
        print(face[0])
        enc = fr.face_encodings(image, known_face_locations=[face], num_jitters=10, model="large")
        size = (face[2] - face[0]) * (face[1] - face[3])
        if size > box_size:
            box_size = size
            face_encoding = enc
    print(box_size, largest_face)

    # Größtes Gesicht ermitteln
    cv2.rectangle(image, (face_box[3], face_box[0]), (face_box[1], face_box[2]), (255, 0, 0), 4)
    cv2.imwrite("Player.png", image)
    return face_encoding
    



# Spieler in einem neuen Bild finden und angucken
"""def look_at_human_player(reachy, last_pos):
    image = []
    for i in range(0, 3):
        image = take_picture(reachy)
        player_face_pos = compare_faces_for_pos(image)

        if player_face_pos is not None:
            center_vision_on_face(image, player_face_pos, reachy)
            break
        else:
            if i == 0:
                #Kopf wird nach links gedreht
                #move.move_head([0.5, 0.5, 0])
                reachy.head.look_at(0.5, 0.5, 0, 1, "simul")
                time.sleep(1)
            elif i == 1:
                #Kopf wird nach rechts gedreht 
                #move.move_head([0.5,-0.5, 0])
                reachy.head.look_at(0.5, -0.5, 0, 1, "simul")
                time.sleep(0.5)
                cv2.imshow("ehat", image)
                cv2.waitKey()
            else:
                print("Nothing Found")
                reachy.head.look_at(last_pos[0], last_pos[1], last_pos[2], 1, "simul")
"""

def look_at_human_player(reachy, face_enc):
    image = take_picture(reachy)
    player_face_pos = compare_faces_for_pos(image, face_enc)

    if player_face_pos is not None:
        center_vision_on_face(image, player_face_pos, face_enc, reachy)
    else:
        print("Not in View")
        reachy.head.look_at(0.5, 0, 0, 1, "simul")

def compare_faces_for_pos(image, player_face_enc):
    """player_pic = fr.load_image_file("Player.png")
    player_location = fr.face_locations(player_pic)
    print(len(player_location))
    player_face_enc = fr.face_encodings(player_pic, num_jitters=10, model="large")[0]"""

    face_positions = fr.face_locations(image, number_of_times_to_upsample=1)
    smallest_distance = None
    face_box = []

    for face in face_positions:
        unknown_face_enc = fr.face_encodings(image, known_face_locations=[face], num_jitters=10, model="large")


        print(len(player_face_enc[0]), "\n", len(unknown_face_enc[0]))
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

def center_vision_on_face(image, face_pos, player_face_enc, reachy):
    # Dimensionen das aufgenommenen Bildes speichern
    im_width, im_height, _ = image.shape
    print("w", im_width, "h", im_height)

    bottom, left, top, right = face_pos
    face_center = [ceil(right + (left - right) / 2), ceil(bottom + (top - bottom) / 2)]
    print(face_center)
    cv2.circle(image, (face_center[0], face_center[1]), 5, (255, 0, 0), 3)
    cv2.imwrite("center.png", image)
    # Abweichung der Oberen rechten Ecke von den Mittellinien des Bildes ausrechnen
    percent_x_diff = 100 / (im_width / (face_center[0] - (im_width / 2))) * 0.01
    percent_y_diff = 100 / (im_height / (face_center[1] - (im_height / 2))) * 0.01
    reachy.turn_on("head")

    x_perc = ceil((0 + percent_x_diff * 1) * 100) / 100
    y_perc = ceil((0 + percent_y_diff * 1) * 100) / 100

    x_coor = ceil(im_width / 2 + im_width * x_perc)
    y_coor = ceil(im_height / 2 + im_height * y_perc)
    #cv2.circle(image, (y_coor, x_coor), 5, (255, 0, 0), 3)
    #cv2.imshow("TEst", image)
    #cv2.waitKey()
    last_pos = (0.5, x_perc, y_perc)
    reachy.head.look_at(0.5, 0, 0, 1, "simul")
    reachy.head.look_at(0.5, x_perc, y_perc, 1, "simul")
