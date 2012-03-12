from pyepl.locals import *

exp = Experiment()
video = VideoTrack("video")

video.clear("black")

flashStimulus(Text("Hello World!"))
