##Concordance V1.0
#This program will count all of the words in the file
#and export a CSV named "Indexof_<inputfilename>.csv"
#Written in 2016 by Matt Briggs
#

import cmd
import class_fileopener as O
import class_concordance as C
import class_dicttofile as DF

appversion = "Concordance Version 1.0 201610091100\nType \'help\' to get info on using the application.\n"
'''This is the command line interface to the base application.'''

class TagTerminal(cmd.Cmd):
    """Accepts commands via the normal interactive prompt or on the command line."""

    prompt = "> "
        
    def do_index(self, line):
        '''Type the name of a text file and the concordance tool will create a concordance file. Note, on a MAC unless you use the pathname, the application will save the file in your user home directory.'''
        try:
            op = O.fileopener()
            inputtext = op.open(line)
            concord = C.concordance()
            indexedtext = concord.count(inputtext)
            outname = line[0:-4]
            outname = outname + "_concord.csv"
            do = DF.dicttofile()
            do.save(indexedtext,outname)
            print(indexedtext)
            return
        except:
            print("There was an issue.")
            return
            
    def do_concord(self,line):
        '''Paste the text you would like to index into the command prompt.'''
        try:
            concord = C.concordance()
            indexedtext = concord.count(line)
            print(indexedtext)
            return
        except:
            print("There was an issue.")
            return
            
    def do_concordandsave(self,line):
        '''Paste the text you would like to index into the command prompt, and it will save to \'concord.csv\'. On a Mac it will save this file in our user home directory.'''
        try:
            concord = C.concordance()
            indexedtext = concord.count(line)
            outname = "concord.csv"
            do = DF.dicttofile()
            do.save(indexedtext,outname)
            print(indexedtext)
            return
        except:
            print("There was an issue.")
            return

    def do_quit(self, line):
        '''Type quiet to exit the application.'''
        return True

    def do_exit(self, line):
        '''Type exit to exit the application.'''
        return True

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    TagTerminal().cmdloop(appversion)
