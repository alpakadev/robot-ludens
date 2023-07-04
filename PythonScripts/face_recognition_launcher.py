from Perception.FaceRecognition.FaceRecognition import FaceRecognition
import time
import asyncio
import reachy_sdk
#reachy = reachy_sdk.ReachySDK("192.168.1.94")

reachy = reachy_sdk.ReachySDK("localhost")
face_recognition = FaceRecognition()
face_recognition.identify_human_player(reachy, None)
face_recognition.look_at_human_player(reachy, None)