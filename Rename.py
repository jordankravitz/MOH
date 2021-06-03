#from os import listdir
#from os.path import isfile, join
import os
import rpa as r

#username and password to log into  Call Manager
un = 'Automation'
pw = 'vgYf9UeX7n23'


#gets a list of all the files
files = os.listdir("C:\RPA\MOH") 
directory = '''C:\RPA\MOH\\'''
newfiles = os.listdir("C:\RPA\MOH") 


for file in files:
    if file.startswith('X'):
        os.rename(directory + file, directory + "Landover.wav")
    
    


for file in newfiles:
    print(file)