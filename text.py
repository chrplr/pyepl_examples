#! /usr/bin/env python
# Time-stamp: <2012-02-28 16:25:09 pallier>

from pyepl.locals import *

exp = Experiment()
# press esc + F1 to end experiment if needed
exp.setBreak()

clk = PresentationClock()
vt = VideoTrack("video")
keyboard = KeyTrack("keyboard")

#bc = ButtonChooser(Key("P"))


# reads the stimuli from text file "sentences.txt"
stimuli = [ s.split() for s in open("sentences.txt").readlines() ]

# open the instructions file & show the experiment instructions
instructions = open("instructions.txt")
#instruct(instructions.read(), clk = clk, exitbutton=Key("RETURN"))
instruct(instructions.read(), clk = clk)
vt.clear("black")

def WaitfMRISynchro(clk):
    s = Key("S")
    flashStimulus(Text("Waiting for MRI synchro"), clk=clk)
    s.wait(clk=clk)
    vt.clear("black")

WaitfMRISynchro(clk)

for s in stimuli:
    clk.delay(1500)
    flashStimulus(Text('+'), clk=clk, duration=500)
    clk.delay(500)
    for w in s:
        flashStimulus(Text(w), clk=clk, duration=200)
        clk.delay(100)

