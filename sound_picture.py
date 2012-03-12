#! /usr/bin/env python

import csv
from pyepl.locals import *

exp = Experiment()
video = VideoTrack("video")
audio = AudioTrack("audio")
key = KeyTrack("key")
clk = PresentationClock()

# read stimuli file 
stimfile  = open('sound_picture.csv')
reader = csv.reader(stimfile)
rownum = 0
picture = []
soundfile = []
for row in reader:
    picture.append(row[0])
    soundfile.append(row[1])  

print picture
print soundfile

video.clear("black")

# enable escape
exp.setBreak()

# open the instructions file
#instructions = open("instruct.txt")
# show the instructions
#instruct(instructions.read(), clk = clk)

waitForAnyKey(clk, Text("Press any key to begin"))

for trial in range(len(picture)):

# present pictures and play sound
    video.clear("black")  
    video.showProportional(Image(picture[trial]), 0.5, 0.5)
    video.updateScreen()

    sound = FileAudioClip(soundfile[trial])  
    sound.present(clk=clk)

    waitForAnyKey()
    video.clear("black")

# Present pictures and record sound
    # video.showProportional(Image(line[2]), 0.5, 0.5)
    # video.updateScreen()

    # (rec,timestamp) = audio.record(5000, line[4], t=clk)

    # waitForAnyKey()
    # video.clear("black")

video.clear("black")
flashStimulus(Text('Thank you'), duration=2000, clk=clk)
