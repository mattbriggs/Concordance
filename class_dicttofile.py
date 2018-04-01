import csv
 
class dicttofile():
    '''Class saves a dictionary object o a CSV file.'''
    def __init__(self):
        self.state = "new"
    
    def save(self,dictionary,filename):
        '''With a dictionary and a filename, saves the dictionary as a CSV to the filename.'''
        try:
            w = csv.writer(open(filename, "w"))
            for key, val in dictionary.items():
                w.writerow([key, val])
            
        except:
            print ("There was an issue outputing the file.")
            