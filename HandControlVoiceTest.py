import cv2
import serial
import numpy as np
import speech_recognition as sr

ser = serial.Serial('COM3', 9600)

servo_channels = {
    0: 0,  # Canal 0 para o dedo mínimo (mindinho)
    1: 1,  # Canal 1 para o dedo anelar
    2: 2,  # Canal 2 para o dedo médio
    3: 3,  # Canal 3 para o dedo indicador
    4: 4   # Canal 4 para o dedo polegar
}

prev_finger_states = [False, False, False, False, False]

recognizer = sr.Recognizer()

def voice_command():
    with sr.Microphone() as source:
        print("Aguardando comando de voz...")
        audio = recognizer.listen(source, timeout=5)
        try:
            command = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Comando de voz: {command}")
            return command
        except sr.UnknownValueError:
            print("Não foi possível entender o comando de voz.")
        except sr.RequestError:
            print("Não foi possível acessar o serviço de reconhecimento de voz.")
    return None

while True:
    command = voice_command()

    if command:
        if "ligar" in command:
            for channel in servo_channels.values():
                ser.write(f"{channel}:120\n".encode())
        elif "desligar" in command:
            for channel in servo_channels.values():
                ser.write(f"{channel}:0\n".encode())
        elif "dedo mínimo" in command:
            finger_state = not prev_finger_states[0]
            ser.write(f"{servo_channels[0]}:{120 if finger_state else 0}\n".encode())
            prev_finger_states[0] = finger_state

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

ser.close()
cv2.destroyAllWindows()
