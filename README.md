# 🤖 Controle de Mão Robótica com Hand Tracking e Arduino 🤚

Um projeto de controle de mão robótica que utiliza detecção de mão por meio do OpenCV, MediaPipe e Python, permitindo o controle de servos em uma mão robótica conectada a um Arduino. Com este projeto, você pode fazer com que uma mão robótica se mova de acordo com os movimentos da sua própria mão!
Para o projeto do hardware da mão robótica, usei um modelo em 3D e servos SG90, e um arduino UNO.

## ⚙️ Funcionamento: 
(https://img.youtube.com/vi/z33VZ7MibCs/0.jpg)


## ℹ️ Sobre o Projeto

Este projeto combina visão computacional, detecção de mão e controle de hardware para criar uma interface interativa de controle de mão robótica. A detecção da mão é realizada usando a biblioteca MediaPipe, enquanto o controle dos servos na mão robótica é feito por meio de uma conexão serial com um Arduino. Isso permite que você controle os movimentos da mão robótica com gestos da sua própria mão.

## 🚀 Funcionalidades

- Detecção de mão em tempo real com MediaPipe.
- Controle de servos na mão robótica por meio de uma conexão serial com Arduino.
- Interface de usuário que exibe os landmarks da mão e o estado dos dedos em tempo real.
- Personalização dos movimentos e dos canais dos servos.

## 📋 Pré-requisitos

Antes de executar o projeto, certifique-se de ter o seguinte instalado:

- Python 3.x
- OpenCV
- MediaPipe
- NumPy
- Arduino IDE (para carregar o código do Arduino)
- Uma webcam (para a detecção da mão)

## ⚙️ Configuração

1. Instale as bibliotecas Python necessárias:

   ```bash
   pip install opencv-python mediapipe pyserial
