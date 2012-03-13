#! /usr/bin/env python
# Time-stamp: <2012-03-13 11:28 christophe@pallier.org>

import csv
from pyepl.locals import *

exp = Experiment(fullscreen=False, 
                 use_opengl=False,
                 use_eeg=False,
                 sync_to_vbl=False)
video = VideoTrack("video")
audio = AudioTrack("audio")
key = KeyTrack("key")
clk = PresentationClock()

# read stimuli files 
stimfile  = open('playlist.csv')
reader = csv.reader(stimfile)
sounds = []
datadir = "audio/"
for row in reader:
    sounds.append(FileAudioClip(datadir + row[0]))  
rownum = len(sounds)

video.clear("black")

# enable escape
exp.setBreak()

# open the instructions file
#instructions = open("instruct.txt")
# show the instructions
#instruct(instructions.read(), clk = clk)

waitForAnyKey(clk, Text("Press any key to begin"))

for trial in range(rownum):

# present pictures and play sound
    video.clear("black")  
    video.showProportional(Text(str(trial+1)), 0.5, 0.5)
    video.updateScreen()

    sound[trial].present(clk=clk)

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
