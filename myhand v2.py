import cv2
import mediapipe as mp
import serial
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

sample_rate = 2

hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5,
    max_num_hands=1
)

cap = cv2.VideoCapture(0)

ser = serial.Serial('COM3', 9600)

servo_channels = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4
}

prev_finger_states = [False, False, False, False, False]

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results_hands = hands.process(frame_rgb)

    if results_hands.multi_hand_landmarks:
        for hand_landmarks in results_hands.multi_hand_landmarks:
            thumb_threshold = hand_landmarks.landmark[3].y + (hand_landmarks.landmark[4].y - hand_landmarks.landmark[3].y) * 0.7

            finger_states = [hand_landmarks.landmark[4].y > hand_landmarks.landmark[3].y,
                             hand_landmarks.landmark[8].y > hand_landmarks.landmark[7].y,
                             hand_landmarks.landmark[12].y > hand_landmarks.landmark[11].y,
                             hand_landmarks.landmark[16].y > hand_landmarks.landmark[15].y,
                             hand_landmarks.landmark[20].y > thumb_threshold]

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            for i, finger_state in enumerate(finger_states):
                if finger_state != prev_finger_states[i]:
                    if finger_state:
                        ser.write(f"{servo_channels[i]}:120\n".encode())
                    else:
                        ser.write(f"{servo_channels[i]}:0\n".encode())

            prev_finger_states = finger_states

        landmarks_frame = np.zeros_like(frame)
        mp_drawing.draw_landmarks(landmarks_frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        cv2.imshow("Landmarks da Mão", landmarks_frame)

        status_frame = np.zeros((300, 300, 3), np.uint8)
        for i, finger_state in enumerate(finger_states):
            if finger_state:
                cv2.putText(status_frame, f"Dedo {i + 1}: Ativo", (10, 30 * (i + 1)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            else:
                cv2.putText(status_frame, f"Dedo {i + 1}: Inativo", (10, 30 * (i + 1)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow("Status dos Dedos", status_frame)

    else:
        for channel in servo_channels.values():
            ser.write(f"{channel}:0\n".encode())

    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

ser.close()
cap.release()
cv2.destroyAllWindows()
