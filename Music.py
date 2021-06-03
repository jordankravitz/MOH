#from os import listdir
#from os.path import isfile, join
import os
import rpa as r
import sys
import keyboard
#import gitpython - can i have python delete all the MOH files within the "files" folder inside the repo to make upload easier?  


#username and password to log into  Call Manager
un = 'Automation'
pw = 'vgYf9UeX7n23'

#Gets current working directory
cwd = os.getcwd()
#sets the directory with the MOH files to the correct working directory + files (folder)
dir_path = cwd + '''\\files'''

#gets a list of all the files
files = os.listdir(dir_path) 


for file in files:
    if file.startswith('X'):
        os.rename(dir_path + '''\\'''+ file, dir_path + '''\\''' + "Landover.wav")


newfiles = os.listdir(dir_path) 

server_ips = ['172.16.1.15', '172.16.1.10', '10.2.121.15']


for file in newfiles:
    for server in server_ips:
        #print("filename "+ file + " ip: "+ server)
        file_path = dir_path + '''\\''' + file
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


        r.click ('FILE')
        r.wait(4)
        keyboard.write(file_path)
        keyboard.press_and_release('tab, tab, enter')
        r.click('Upload File')
        r.wait(6)
        if r.exist('Upload successful'):
            r.close()
        else:
            r.wait(25)
            r.close()

