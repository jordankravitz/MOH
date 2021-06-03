#from os import listdir
#from os.path import isfile, join
import os
import rpa as r
import sys
import keyboard

#username and password to log into  Call Manager
un = 'Automation'
pw = 'vgYf9UeX7n23'


#gets a list of all the files
files = os.listdir('C:\\Users\\j.kravitz\\Python\\CUCM\\MOH\\files\\') 
directory = '''C:\\Users\\j.kravitz\\Python\\CUCM\\MOH\\files\\'''


for file in files:
    if file.startswith('X'):
        os.rename(directory + file, directory + "Landover.wav")


newfiles = os.listdir("C:\\Users\\j.kravitz\\Python\\CUCM\\MOH\\files") 

server_ips = ['172.16.1.15', '172.16.1.10', '10.2.121.15']


for file in newfiles:
    for server in server_ips:
        #print("filename "+ file + " ip: "+ server)
        path = directory + file
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
        keyboard.write(path)
        r.wait(5)
        keyboard.press_and_release('tab, tab, enter')
        r.click('Upload File')
        r.wait(6)
        if r.exist('Upload successful'):
            r.close()
        else:
            r.wait(25)
            r.close()

