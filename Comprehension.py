"""
JARVIS mk.1 Comprehension System
Written: July 28 2021 by David Crider

System Description:
    This module contains the Comprehension utilities that JARVIS will use to understand the intention behind statements. In simple terms, this utility deconstructs an input
    statement, produced by a main program.  This statement will be broken down by the word_tokenize NLTK utility, tagged with parts of speech, and compared with a Word2vec
    model until a satisfactory intention is found. The intention is returned to the main program.

Class Variables:
    InputStatement: this variable is the input to the system.
    TaggedStatement: This is the preprocessed statement which will be used by the IntentionFinder
    Testing: This boolean will determine if the system will double check its chosen intention with a user before adding it to the CorpusDicitonary
    CorpusDictionary: This Dictionary contains all statements fed into JARVIS and their intention. It is saved to a JSON when this class is deconstructed, and loaded on initiation. This
                        serves as the comparison point for intention finding.
    W2VModel: This is the model for use by the IntentionFinder
    Intention: The selected intention to match the statement


Functions:
    Preprocessor: This conducts all preprocessing, include sanitization, tokenization, lemmatization and tagging.
    IntentionFinder: This locates the intention of the statement by checking against matches or using the W2VModel.
    CorpDictUpdate: This updates the CorpusDictionary with the new association. If the Testing boolean is true, it will request clarification and provide a list of other intentions ranked by their
                    likelihood

Libraries:
"""
import json
import nltk


def ComprehensionSystem():

    def __init__(self, input, testing, knownIntentions):
        self.InputStatement = input
        self.TaggedStatement = Preprocessor()
        self.Testing = testing
        self.CorpusDictionary = #TODO Load CorpusDictionary
        self.W2VModel = #TODO Load Word2Vec model
        self.Intention

    def __des__(self):
        #TODO create smooth exit process

    def Preprocessor(self):
        #TODO lowercase the input
        self.InputStatement = self.InputStatement.lower()
        #TODO tokenize
        tokenized = nltk.word_tokenize(self.InputStatement)
        #TODO lemmatize
        #TODO tag
        return taggedStatement

    def IntentionFinder(self):
        #TODO check against known intentions
            #If valid, return intention
        #TODO run W2VModel.similarity on intentions
            #select most likely
        return intention

    def CorpDictUpdate(self):
        #TODO append InputStatement to relevant intention section of CorpusDictionary.