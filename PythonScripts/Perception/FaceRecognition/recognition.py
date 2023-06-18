import dlib
import face_recognition as fr
import cv2
from PIL import Image
import numpy as np

# Ober Funktion zum erstmaligen erkennen des Gegenspielers
def detect_human_player(reachy, move):
    # TODO: Reachys Kopf in Basis Position bringen
    
    # Bild aufnehmen
    image = take_picture(reachy)

    # Zum testen oben auskommentieren und das hier nutzen:
    # image = fr.load_image_file("group-people.jpeg")

    # Alle Gesichter aus dem Bild entnehmen
    face_locations = fr.face_locations(image)

    # Größtes Gesicht ermitteln
    player_face = get_largest_face(face_locations)

    # Gesicht in einer Datei zwischenspeichern
    top, right, bottom, left = player_face
    image = image[top:bottom, left:right]
    pil_image = Image.fromarray(image)
    pil_image.save("Player.png")


# Spieler in einem neuen Bild finden und angucken
def look_at_human_player(reachy, move):
    image = []
    for i in range(0, 2):
        image = take_picture(reachy)
        # Gespeichertes Gesicht laden
        player_image = fr.load_image_file("Player.png")
        player_face = fr.face_locations(player_image)[0]
        player_face_pos = compare_faces_for_pos(image)

        if player_face_pos is not None:
            break
        else:
            if i == 0:
                # TODO: Werte anpassen, damit Kopf nach links gedreht wird
                move.move_head([0, 0, 0])
            else:
                # TODO: Werte anpassen, damit Kopf nach rechts gedreht wird
                move.move_head([1, 1, 1])
        
    # TODO: Kopf solange drehen, bis das Player Gesicht im horizontalen und vertikalen Zentrum des Bilds ist        
    center_vision_on_face(image, player_face_pos, reachy, move)


def compare_faces_for_pos(image):
    player_pic = fr.load_image_file("Player.png")
    player_enc = fr.face_encodings(player_pic)[0]

    face_positions = fr.face_locations(image)

    for face in face_positions:
        unknown_face_enc = fr.face_encodings(image, known_face_locations=[face])
        results = fr.compare_faces([player_enc], test_enc[0])
        if results[0] == True:
            print("Yay")
            return face
        else:
            print("Nay")
            return None

def take_picture(reachy):
    camera = reachy.right_camera
    image = camer.last_frame
    return image

def get_largest_face(face_locations):
    # Die Bounding Box eines Gesichts aussuchen, die die größte Fläche einnimmt
    max = 0
    largest_face = None
    for face in face_locations:
        top, right, bottom, left = face
        size = (top - bottom) * (left - right)
        if size > max:
            max = size
            largest_face = face
    return largest_face

def center_vision_on_face(image, face_pos, reachy, move):
    # Dimensionen des aufgenommenen Bildes speichern
    im_width, im_height = image.size

    # Obere rechte Ecke der Bounding Box, da wir das rechte Auge als Kamera nutzen
    top_right_corner = face_pos[1]

    # Abweichung der Oberen rechten Ecke von den Mittellinien des Bildes ausrechnen
    percent_x_diff = 100 / (im_width / (face_pos[0] - (im_width / 2))) * 0.01
    percent_y_diff = 100 / (im_height / (face_pos[1] - (im_height / 2))) * 0.01

    # TODO: Kopf Position von Reachy bekommen. Geht das so? Muss getestet werden
    x,y,z,w = reachy.head.forward_kinematics()
    reachy.head.look_at(x*percent_x_diff, y*percent_y_diff, z)