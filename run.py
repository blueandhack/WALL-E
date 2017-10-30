import speech_recognition as sr
import serial
import threading
import csv
from time import sleep

usbport = '/dev/cu.usbmodem1441' # change the usb port
ser = serial.Serial(usbport, 9600)
flag = 0
sem = threading.Semaphore(1)
value_begin = b'b'
value_stop = b'.'
value_right = b'r'
value_left = b'l'

def printData():
    sleep(4)
    while True:
        sem.acquire()
        while ser.inWaiting():
            data = ser.readline()
            data = data.decode("utf-8")
            data = data.rstrip()
            if(data != 'Initializing...'):
                csv_file = open('result.csv', 'a+', newline='')
                writer = csv.writer(csv_file)
                result = data.split(',')
                # print(result)
                writer.writerow(result)
        sem.release()
        sleep(0.5)

def readInput():
    while True:
        command = b'.'

        ###############################################
        # input("<< Press Enter to Say Something")
        # #
        # # Record Audio
        # r = sr.Recognizer()
        # with sr.Microphone(device_index=8) as source:
        #     print("Say something!")
        #     audio = r.listen(source)
        # # Speech recognition using Google Speech Recognition
        # try:
        #     # for testing purposes, we're just using the default API key
        #     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        #     # instead of `r.recognize_google(audio)`
        #
        #     say = r.recognize_google(audio)
        #     say = say.lower()
        #
        #     if(say.find('begin')!=-1):
        #         command = value_begin
        #     elif(say.find('right')!=-1):
        #         command = value_right
        #     elif(say.find('left')!=-1):
        #         command = value_left
        #     else:
        #         command = value_stop
        #     print("You said: " + say)
        # except sr.UnknownValueError:
        #     print("Google Speech Recognition could not understand audio")
        # except sr.RequestError as e:
        #     print("Could not request results from Google Speech Recognition service; {0}".format(e))
        ###############################################

        # input command
        ##############################################
        command = input("<< ")

        sem.acquire()
        command = command.encode("utf-8")
        # print(command)
        if(command == b'begin'):
            command = value_begin
        elif(command == b'stop'):
            command = value_stop
        elif(command == b'left'):
            command = value_left
        elif(command == b'right'):
            command = value_right
        else:
            command = value_stop
        ###############################################

        if ser.writable():
            ser.write(command)
        sem.release()

def test():
    csv_file = open('result.csv', 'a+', newline='')
    writer = csv.writer(csv_file)
    writer.writerow([3,4])

def main():
    create = open('result.csv', 'w')
    create.close()
    threading.Thread(target=printData).start()
    threading.Thread(target=readInput).start()
    # test()

if __name__ == '__main__':
    main()
