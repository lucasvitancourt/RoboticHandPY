import tkinter as tk
from tkinter import Scale
import serial

ser = serial.Serial('COM3', 9600)

servo_channels = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    11: 11,
    12: 12,
    13: 13,
    14: 14,
    15: 15
}

# Função para atualizar a posição do servo quando o valor do slider é alterado
def update_servo_position(channel):
    position = servo_sliders[channel].get()
    ser.write(f"{channel}:{position}\n".encode())

# Crie a janela da interface gráfica
root = tk.Tk()
root.title("Controle de Servo")

servo_sliders = {}

# Organize os sliders em uma grade
row_num = 0
column_num = 0
for servo_channel in servo_channels.values():
    slider = Scale(root, from_=0, to=180, orient="horizontal", label=f"Servo {servo_channel}")
    slider.set(0)  # Defina o valor inicial no centro (90 graus)
    slider.grid(row=row_num, column=column_num, padx=5, pady=5)
    slider.bind("<Motion>", lambda event, channel=servo_channel: update_servo_position(channel))
    servo_sliders[servo_channel] = slider
    column_num += 1
    if column_num > 3:
        column_num = 0
        row_num += 1

root.mainloop()
