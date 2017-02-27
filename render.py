"""
AutoChunky v1.0.2
Written by colebob9
Coded in Python 3
Released under the MIT license
Source code repo: https://github.com/colebob9/AutoChunky
"""
import shlex
import subprocess

# Title
print("AutoChunky v1.0.2")
print("Written by colebob9")
print("Source Code on GitHub.com/colebob9/AutoChunky")

# Checking queue file
print("Reading queue file...")
print('')
f = open("queue.txt")
queueList = f.readlines()
queueList = [s.rstrip() for s in queueList] # stripping off \n
f.close()
print("Currently queued scenes:")
print(queueList)
print('')

# Queue and render command
queueNumber = 0
chunkyPath = "ChunkyLauncher.jar"
for r in queueList:
        print('')
        print("Now rendering: " + r)
        print('')
        subprocess.call(shlex.split("java -jar %s -render %s" % (chunkyPath, r)))
        # Uncomment below to see command used.
        #print("java -jar %s -render %s" % (chunkyPath, r))

exit
