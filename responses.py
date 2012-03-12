#! /usr/bin/env python

from pyepl.locals import *

# set up the experiment (parsing command line et al.)
exp = Experiment()

# set up some tracks
video = VideoTrack("video")
keyboard = KeyTrack("keyboard")

# clear the screen
video.clear("black")

# get a presentation clock
clock = PresentationClock()

# set up available keys
possKeys = keyboard.keyChooser('A','B','C','D')

# set up stimulus
stimOnText = Text('AB',color=(.6,.6,.6))
stimGoText = Text('AB',color=(1,1,1))

# set up durations
onDuration = 2000
maxRespDuration = 4000

# show the on stim
stim = video.showProportional(stimOnText,.5,.5)
timeOn = video.updateScreen(clock)

# leave it on for specified duration
clock.delay(onDuration)

# switch it to the go stim and wait for a response
video.replace(stim,stimGoText)
goTime = video.updateScreen(clock)

# collect reponses until num needed or out of time
responses = []
timeLeft = maxRespDuration
while len(responses)<2 and timeLeft > 0:
    button,bc_time = possKeys.waitWithTime(maxDuration=timeLeft,
                                           clock = clock)
    if button:
        # record the response
        responses.append((button,bc_time))
        # update time left
        timeLeft -= bc_time[0] - goTime[0]
    else:
        # out of time
        timeLeft = 0

print ""
print "Reponses: "
for response in responses:
    print "Button: %s (%d ms)" % (response[0].name,response[1][0]-goTime[0])
print "\n"

