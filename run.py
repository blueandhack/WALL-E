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

usbport = '/dev/cu.usbmodem1411' # change the usb port
ser = serial.Serial(usbport, 9600)
flag = 0
sem = threading.Semaphore(1)
value_begin = b'b'
value_stop = b'.'
value_right = b'r'
value_left = b'l'

def printData():
    sleep(5)
    while True:
        sem.acquire()
        data = ser.readline()
        data = data.decode("utf-8")
        print(data)
        sem.release()
        sleep(0.5)

def readInput():
    # sem.acquire()
    # command = input("<<")
    # command = command.encode("utf-8")
    # print(command)
    # if(command == 'begin'):
    #     command = value_begin
    # if ser.writable():
    #     ser.write(command)
    # sem.release()
    # sleep(0.5)

    while True:
        command = input("<<")
        sem.acquire()
        command = command.encode("utf-8")
        print(command)
        if(command == b'begin'):
            command = value_begin
        if(command == b'stop'):
            command = value_stop
        if(command == b'left'):
            command = value_left
        if(command == b'right'):
            command = value_right
        print(command)
        if ser.writable():
            print("can write")
            ser.write(command)
        print(command)
        data = ser.readline()
        data = data.decode("utf-8")
        print(data)
        sem.release()

def main():
    threading.Thread(target=printData).start()
    threading.Thread(target=readInput).start()

if __name__ == '__main__':
    main()
