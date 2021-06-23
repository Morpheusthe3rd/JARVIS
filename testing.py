"""This file will contain miscellaneous testing for the JARVIS project"""


"""This section is for testing on the OS library. Here I am figuring out how to check for a certain file anywhere on the system. Currently limited to just my 
user"""
import os
from difflib import SequenceMatcher
import soundex

class pathUtilities():

    def __init__(self, masterPath, targetFile):
        self.masterPath = masterPath
        self.discoveredPaths = []
        self.targetFile = targetFile

    def appendPath(self, path, newName):      #This function is a simple one, used to append a new section onto the path
        newPath = path + "\\" + newName
        return newPath

    def scanEntirePath(self, path):           #This function searches the entire directory under the master path, default to "C:\Users\dcrid"
        with os.scandir(path) as dirs:
            for entry in dirs:
                #print(entry.name)
                if entry.name == self.targetFile:
                    self.discoveredPaths.append(self.appendPath(path, entry.name))
                else:
                    if os.path.isdir(entry):
                         try:
                            self.scanEntirePath(self.appendPath(path, entry.name))
                         except PermissionError as m:
                             print("Permission denied to access: "+self.appendPath(path, entry.name))##

    def scanPathTillFound(self, path):      #TODO This needs implemented, I want to have some way of queueing more common file locations ahead of rarer ones.
        with os.scandir(path) as dirs:
            for entry in dirs:
                #print(entry.name)
                if entry.name == self.targetFile:
                    return self.appendPath(path, entry.name)
                else:
                    if os.path.isdir(entry):
                         try:
                            self.scanEntirePath(self.appendPath(path, entry.name))
                         except PermissionError as m:
                             print("Permission denied to access: "+self.appendPath(path, entry.name))



if __name__ == "__main__":
    #pathUtil = pathUtilities("C:\\Users\\dcrid", "JARVISmk001")

    #pathUtil.scanEntirePath(pathUtil.masterPath)
    s1 = 'JARVISmk001'
    s2 = 'jarvis mark 1'

    print(SequenceMatcher(a=s1, b=s2).ratio())

    s = soundex.getInstance()
    print(s.soundex(s1.lower()))
    print(s.soundex(s2.lower()))

    print(SequenceMatcher(a=s.soundex(s1), b=s.soundex(s2)).ratio())