#from os import listdir
#from os.path import isfile, join
import os
from os.path import splitext




#gets a list of all the files
files = os.listdir("C:/RPA/MOH/files/") 
directory = '''C:/RPA/MOH/files/'''
newfiles = os.listdir("C:/RPA/MOH/files/") 


for file in files:
    if file.startswith('X'):
        if file.find(*"_"):
            newfile=file.split('_'[0])
            #print (newfile[2])
            os.rename(directory + file, directory + newfile[2])
    else:
        print ("no file")
    


#for file in files:
 #   print(file)