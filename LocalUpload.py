import os
import rpa as r
import sys
import keyboard
from keyboard import press
import unzip
import zipfile
#import logging



#log = '''\\\\automate\\MOH\\log.txt''' 
#logging.basicConfig(filename=log, level=logging.DEBUG, format='')


#username and password to log into  Call Manager
un = 'Automation'
pw = 'vgYf9UeX7n23'

#Gets current working directory
#cwd = os.getcwd()

#sets the directory with the MOH files to the correct working directory + files (folder)
#dir_path = cwd + '''\\files'''

#hard coded dir_path for Jenkins server
dir_path = 'C:\\Users\\j.kravitz\\Python\\CUCM\\MOH\\files'


#gets a list of all the files
zippyfiles = os.listdir(dir_path)

#Unzip a zip file into specific directory then delete the zip file
for zippyfile in zippyfiles:
    if zippyfile.endswith('.zip'):
        zipname=dir_path + '\\' + zippyfile
        #print (zipname)
        with zipfile.ZipFile(zipname, 'r') as zipitem:
            zipitem.printdir()
            zipitem.extractall(path='C:\\Users\\j.kravitz\\Python\\CUCM\\MOH\\files')
        os.remove(zipname)



files = os.listdir(dir_path)

#Rename all the on hold media files - using only the city name as the file name.  
#using the underscore as the delimiter to choose the correct field
for file in files:
    if file.startswith('X'):
        if file.find(*"_"):
                newfile=file.split('_'[0])
            #print (newfile[2])
        os.rename(dir_path +"/"+ file, dir_path +"/"+ newfile[2])




newfiles = os.listdir(dir_path) 


#server_ips = ['172.16.0.10', '172.16.0.15', '10.1.121.15']
#server_ips = ['10.176.0.10', '10.176.0.15', '10.176.80.10']
server_ips = ['10.176.80.10']


for server in server_ips:
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
    for file in newfiles:
        file_path = 'C:\\Users\\j.kravitz\\Python\\CUCM\\MOH\\files\\' + file
        r.upload('#FILE', file_path)
        r.click('Upload File')
        r.wait(15)
        if r.exist('Upload successful'):
            print("upload done")
        else:
            r.wait(25)
    r.close()


for file in newfiles:
    os.remove('C:\\Users\\j.kravitz\\Python\\CUCM\\MOH\\files\\' + file)



'''
for file in newfiles:
    #logging.info("Starting 1st for loop")
    for server in server_ips:
        file_path = 'C:\\Users\\j.kravitz\\Python\\CUCM\\MOH\\files\\' + file
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

        r.upload('#FILE', file_path)
        r.click('Upload File')
        r.wait (10)
        
        if r.exist('Upload successful'):
            r.close()
        else:
            r.wait(25)
            r.close()
'''
   #os.remove(file_path)
