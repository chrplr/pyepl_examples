#! /usr/bin/env python
# Time-stamp: <2012-02-26 11:35:34 pallier>

# will display the graphics (*.png) files int the current dir
# waits for a keypress after each image


import glob
from pyepl.locals import *

exp = Experiment()
video = VideoTrack("video")
key = KeyTrack("key")
clk = PresentationClock()

# enable escape
exp.setBreak()

# load all the graphic (png) files in current directory
pictures = []
for f in glob.glob("*.png"):
    pictures.append(Image(f))

video.clear("black")

waitForAnyKey(clk, Text("Press any key to begin"))

for p in pictures:
    video.clear("black")  
    video.showProportional(p, 0.5, 0.5)
    video.updateScreen()
    waitForAnyKey()
    video.clear("black")

video.clear("black")
flashStimulus(Text('Thank you'), duration=2000, clk=clk)
