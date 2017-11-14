# WALL-E

The project's name is WALL-E because it looks like WALL-E robot.

![](https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg)
WALL-E Poster

![](https://i.imgur.com/jWSu0SP.jpg)
My project WALL-E

The project has two parts:

- Code
- 2.5D / 3D Bracket

## Code

I wrote two parts of similar code.

The first part is requirements.

And the second part is like the first part, but I add input  and speech recognition by python that means user can control it by using input or speaking.

There are three python files:

- run.py
- draw.py
- findMic.py

### How to run?

First, install python dependencies

```
python3 -m pip install pyserial
python3 -m pip install SpeechRecognition
python3 -m pip install -U matplotlib
```

Then, run `findMic.py` to find microphone index in `run.py` line 42. Also, you should change line 7 in `run.py`. After, you can decide which input, such as, if you want to use typing, you should uncomment line 71 to 85 and comment line 38 to 66, otherwise, if you want to speaking, you should uncomment line 38 to 66 and comment line 71 to 85.

Then, input `python3 run.py` in your terminal, you can input some commands:

- begin
- stop
- right
- left

When you input `begin`, we should wait it scan around. Then, you can see `result.csv` file in the same directory. Last, input `python3 draw.py` to generate a plot by the csv file.

![](https://i.imgur.com/L4EjPBr.png)


## 2.5D / 3D Bracket

### 2.5D Bracket

It has a stand can hold Arduino board. There has three board can fix the Arduino board and the three boards making the structure firm. Also, it has a little bar can make it stay there.

![Bar](https://i.imgur.com/wWh0VJJ.jpg)
A Little Bar

![Back Side](https://i.imgur.com/3ZbmKEC.jpg)
Back Side

![Right Side](https://i.imgur.com/LuEGLSR.jpg)
Right Side

### 3D Bracket

The 3D Bracket, it has two parts, one is ultrasonic sensor holder, and other one is stand.

![](https://i.imgur.com/LvWvD2j.jpg)
Stand and Holder

![](https://i.imgur.com/GPN6Lue.jpg)
Front Side

![](https://i.imgur.com/d2L7W3f.jpg)
Bottom Side

![](https://i.imgur.com/s5f5YxP.jpg)
Back Side

![](https://i.imgur.com/RU1bFiS.jpg)
Right Side

## Extensions:

1. Using command control ultrasonic sonar.
2. Different visualization by using matplotlib
3. Stronger 2.5D Bracket, it has Arduino board stand.

## References

ISTA 303: Assignment 2, Ultrasonic Sonar with Visualization
[Speech Recognition using Google Speech API](https://pythonspot.com/en/speech-recognition-using-google-speech-api/)
[WALL-E Poster](https://en.wikipedia.org/wiki/WALL-E)


