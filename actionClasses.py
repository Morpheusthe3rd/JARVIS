"""In this file I will be writing the classes for the actions JARVIS can perform"""

import os
import nltk
from difflib import SequenceMatcher
import soundex


class actionParent():             #This parent class will include base functions common to all actions

    def __init__(self, commandStatement):
        self.commandStatement = commandStatement

    def actionOperations(self):
        #TODO
        self.actionClarification()

    def actionContext(self):
        #TODO
        self.actionClarification()

    def actionClarification(self):
        #TODO
        #This method is called when there is something unclear in the action, or it is not properly defined.
        print("actionParent.actionClarification is undefined")

class fileSearchAction(actionParent):

    masterPath = "C:\\Users\\dcrid"

    def __init__(self, commandStatement):
        actionParent.__init__(self, commandStatement)
        self.targetFile = ''
        self.discoveredPaths = [0][0]
        self.recursionTracker = 0

    def actionOperations(self, workingPath):
        #print(self.recursionTracker)
        self.recursionTracker += 1
        commandStatement = self.commandStatement

        with os.scandir(workingPath) as dirs:
            for entry in dirs:
                print(entry.name)
                entryName = entry.name
                s1 = entry.name
                s2 = self.commandStatement
                s = soundex.getInstance()
                s1 = s.soundex(entryName)
                s2 = s.soundex(self.commandStatement)
                simmilarityRatio = SequenceMatcher(a=s1, b=s2).ratio()
                print("\"{0}\" and \"{1}\" are {2}% in common".format(entryName, self.commandStatement, simmilarityRatio))

                if simmilarityRatio > 0.45:                                    #This checks if there are more than 75% of the letters shared between the name of the file and the command statement.
                    self.discoveredPaths[0].append(self.appendPath(workingPath, entry.name))   #Appends the discovered path to the discovered paths
                    self.discoveredPaths[1].append(simmilarityRatio)                              #Appends the number of repeated layers.
                else:
                    if os.path.isdir(entry) and entry != 'venv':
                         try:
                            print(workingPath)
                            print("\n" + str(self.discoveredPaths))
                            self.actionOperations(self.appendPath(workingPath, entry.name))
                         except PermissionError as m:
                             print("Permission denied to access: "+self.appendPath(workingPath, entry.name))##

    def actionContext(self):
        #TODO take in commandStatement and return targetFile

        self.actionClarification()

    def actionClarification(self):
        #TODO
        #This method is called when there is something unclear in the action, or it is not properly defined.
        print("fileSearchAction.actionClarification is undefined")

    def appendPath(self, path, newName):      #This function is a simple one, used to append a new section onto the path
        #print("appending: {0} to {1}".format(path, newName))
        newPath = path + "\\" + newName
        #print(newPath)
        return newPath