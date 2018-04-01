#Module for the Concordance App

class concordance():
    '''This class contains the properties and methods for creating a concordance with text.'''
    def __init__(self):
        self.state = "new"
        
    def count (self, corpus):
        '''Counts the words in an input string.'''
        if corpus != "":
            #variables
            wordlist = {} #empty dictionary
            punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' #strip out puncutation
            csver = '()\'' #to strip string of tuple to pure CSV
            concordance = ""
            outcord = ""
            
            #clean and split
            for p in punctuation:
                corpus = corpus.replace(p,"")
                words = corpus.split()
                
            # count words in the corpus
            for w in words:
                if w not in wordlist:
                    wordlist[w] = 1
                else:
                    wordlist[w] += 1
            
            return (wordlist)
            
        else:
            return ("Need text in the file.")