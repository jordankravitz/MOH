#from os import listdir
#from os.path import isfile, join
import os
import rpa as r
import sys
import keyboard
from keyboard import press
import logging

log = '''\\\\automate\\MOH\\log.txt''' 
logging.basicConfig(filename=log, level=logging.DEBUG, format='')


logging.info("Starting Script")

#username and password to log into  Call Manager
un = 'Automation'
pw = 'vgYf9UeX7n23'

#Gets current working directory
#cwd = os.getcwd()

#sets the directory with the MOH files to the correct working directory + files (folder)
#dir_path = cwd + '''\\files'''

#hard coded dir_path for Jenkins server
dir_path = "\\\\automate\\MOH\\files"

#gets a list of all the files
files = os.listdir(dir_path)


#Old renaming of OnHoldWizard filenames - they are now appending _CityName to their files
#for file in files:
#    if file.startswith('X'):
#        os.rename(dir_path + '''\\'''+ file, dir_path + '''\\''' + "Landover.wav")

for file in files:
    if file.startswith('X'):
        if file.find(*"_"):
            newfile=file.split('_'[0])
            #print (newfile[2])
            os.rename(dir_path + file, dir_path + newfile[2])



newfiles = os.listdir(dir_path) 

server_ips = ['172.16.1.15', '172.16.1.10', '10.2.121.15']



for file in newfiles:
    logging.info("Starting 1st for loop")
    for server in server_ips:
        logging.info("Starting 2nd for loop")
        file_path = '''\\\\automate\\MOH\\files\\''' + file
        r.init()
        moh_url = 'https://' + server +'/ccmadmin/mohAudioFileUpload.do?type=mohAudioManagement'
        r.url(moh_url)
        if r.exist('Advanced'):
            r.click('Advanced')
        if r.exist('Proceed to ' + server +' (unsafe)'):
            r.click('Proceed to '+ server + ' (unsafe)')

        
        #Login into CUCM with Username/PW
        r.type('j_username', un) 
        r.type('j_password',pw)
        r.click('cuesLoginButton') 

        logging.info("CLICKING FILE")
        r.click ('FILE')
        r.wait(15)
        logging.info("TYPING PATH")
        keyboard.write(file_path)
        r.wait(4)
        logging.info("path typed - pressing enter to upload")
        keyboard.send('enter')
        logging.info("enter has been pressed")
        r.wait (4)
        r.click('Upload File')
        logging.info("Upload has been clicked")
        if r.exist('Upload successful'):
            r.close()
            logging.info("File Uploaded")
        else:
            r.wait(25)
            r.close()
            logging.info("File Uploaded")

