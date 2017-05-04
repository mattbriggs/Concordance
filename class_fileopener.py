
class fileopener():
    '''Opens a file and returns the file as a string.'''
    
    def open(self, filepath):
        try:
            f = open(filepath, "r")
            outfile = f.read()
            return outfile
        except:
            return "Unable to open file."
