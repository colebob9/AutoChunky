"""
AutoChunky v1.0.0
Written by colebob9
Coded in Python 3
Released under the MIT license
Source code repo: https://github.com/colebob9/AutoChunky
"""
import subprocess

def checkConf():
    print("Reading queue file...")
    print('')
    f = open("queue.txt")
    global queueList
    queueList = f.readlines()
    queueList = [s.rstrip() for s in queueList] # stripping off \n
    f.close()
    print("Currently queued scenes:")
    print(queueList)
    print('')

def render():
    queueNumber = 0
    chunkyPath = "ChunkyLauncher.jar" # please don't keep like this. only windows compatible.
    while True:
        try:
            currentScene = queueList[queueNumber]
            print('')
            print("Now rendering: " + currentScene)
            print('')
            subprocess.call("java -jar %s -render %s" % (chunkyPath, currentScene))
            queueNumber = queueNumber + 1
        except IndexError:
            print('')
            print("All renders done!")
            break

print("AutoChunky v1.0.0")
print("Written by colebob9")
print("Source Code on GitHub.com/colebob9/AutoChunky")
checkConf()
render()
exit
