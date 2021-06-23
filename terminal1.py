"""
This code is an introductory step towards a JARVIS system. This will use a terminal for interaction, and have both Audio and terminal feedback

"""
import nltk
import pyttsx3
import os
from playsound import playsound
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
import pickle
import io
import speech_recognition as sr
import actionClasses

global actionReferenceList  #This array will contain all of the vocabulary referencing the actions that JARVIS can perform

def testVoice(engine):
    """ RATE"""
    rate = engine.getProperty('rate')  # getting details of current speaking rate
    print("Current voice rate: {0}".format(rate))  # printing current voice rate
    engine.setProperty('rate', 125)  # setting up new voice rate

    """VOLUME"""
    volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    print("Current volume: {0}".format(volume))  # printing current volume level
    engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

    """VOICE"""
    voices = engine.getProperty('voices')  # getting details of current voice
    engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    #engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

#==================================================================================================================================================================
def speak(audioString, engine):
    print(audioString)
    #test(engine)
    engine.say(audioString)
    engine.runAndWait()             #It appears that 'runAndWait' needs to be called after every 'say'

#==================================================================================================================================================================
def listenAndRecognize():
    # obtain audio from the microphone
    r = sr.Recognizer()
    statement = ''
    with sr.Microphone(device_index=1) as source:
        r.adjust_for_ambient_noise(source)
        #print("Say something!")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        statement = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said: " + statement)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    print('returning: "' + statement + '"')
    return statement

#==================================================================================================================================================================
def processText(inputString, engine):

    global actionReferenceList  #the actionReferenceList to determine what actions are required
    actionTag = 'null'
    actionTagList = []

    #These lines load the actionReferenceList from the pickel file
    try:
        with open('actionReferenceList.pickle', 'rb') as f:
            actionReferenceList = pickle.load(f)
    except EOFError:
        actionReferenceList = []
    #these lines dump the action reference into the pickle file if a quit is requested
    if input == 'quit':
        with open('actionReferenceList.pickle', 'wb') as f:
            pickle.dump(actionReferenceList, f)

    taggedInput = pos_tag(word_tokenize(inputString), tagset='universal')

    #this section runs through the tagged input an operates on the VERB s
    for i in range(0, len(taggedInput)):
        #print(taggedInput[i][0] +" "+taggedInput[i][1])
        if taggedInput[i][1] == 'VERB':

            #iterate through action lists
            for j in range (0, len(actionReferenceList)):
                if actionReferenceList[j][0] == taggedInput[i][0]: #checks to see if the action reference is among the list, and if it is sets the tag to it's
                    actionTag = actionReferenceList[j][1]          #corresponding action

                if actionReferenceList[j][0] not in actionTagList: #This creates the actionTagList, which includes all unique action tags from the reference list
                        actionTagList.append(actionReferenceList)
            if actionTag == 'null':
                #request action clarification
                speak("I'm sorry, I don't know what action you want me to perform. Please enter one of the options", engine)
                print("Action options:\n")
                for l in actionTagList:
                    print(l)
                actionLink = input('Type one of the above options: ')

                #add taggedInput[i][1] to that action list
                actionReferenceList.append([taggedInput[i][0], actionLink])
                print(actionReferenceList)

    #print(actionTag)

    #create action instance
    #for now I will structure this as if statements, which I will manually update with new actions.
    if actionTag == "find":
        findAction = actionClasses.fileSearchAction(inputString)
        speak("fileSearchAction instance created", engine)
        foundFilesArray = findAction.actionOperations(findAction.masterPath)
        print(foundFilesArray)
    else:
        speak("Action has no established actionClass", engine)




#==================================================================================================================================================================

#==================================================================================================================================================================
if __name__ == "__main__":
    engine = pyttsx3.init()
    method = input("Please select interaction method (voice or text)>> ")
    if method == 'voice':
        speak('Hello, what can I do for you today?', engine)
        while 1:
            response = listenAndRecognize()
            processText(response, engine)
            if response == 'quit':
                break
    if method == 'text':
        print("Hello, what can I do for you today?")
        while 1:
            response = input(">> ")
            processText(response, engine)
            if response == 'quit':
                break