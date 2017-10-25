# import speech_recognition as sr
#
# # Record Audio
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)
#     print("stop")
# # Speech recognition using Google Speech Recognition
# try:
#     # for testing purposes, we're just using the default API key
#     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#     # instead of `r.recognize_google(audio)`
#     print("You said: " + r.recognize_google(audio))
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))

# import matplotlib.pyplot as plt
# fig,ax=plt.subplots()
# y1=[]
# for i in range(50):
#     y1.append(i)
#     ax.cla()
#     ax.bar(y1,label='test',height=y1,width=0.3)
#     ax.legend()
#     plt.pause(0.3)
#     print("try")
#
# print("Hello")

import serial
import threading
from time import sleep

usbport = '/dev/cu.usbmodem1431' # change the usb port
ser = serial.Serial(usbport, 9600)
flag = 0

def printData():
    while True:
        print(flag)
        while flag == 1:
            pass
        data = ser.readline()
        data = data.decode("utf-8")
        print(data)

def main():
    threadA = threading.Thread(target=printData).start()
    while True:
        command = input("<<")
        flag = 1
        sleep(0.5)
        data = ser.readline()
        data = data.decode("utf-8")
        print(data)
        flag = 0

if __name__ == '__main__':
    main()
