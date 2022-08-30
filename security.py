from ast import Try
from email import message
from itertools import count
from cryptography.fernet import Fernet
import csv
from datetime import datetime, time

def fernet_branca():
    try:
        with open('keys.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                csv_key = row[0]

        fernet = Fernet(csv_key)
        return fernet
    except OSError as e:
        print('')
        print('Error: 4001')
        print('------------------------------------------------------------------------------------------------------------------------------')
        print(" You'll need to get a license/key, please contact our Services Customer Call Center staff at e-mail: da.torres@redlink.com.ar ")
        print('------------------------------------------------------------------------------------------------------------------------------')
        exit()



def encrypted(text):
    fernet = fernet_branca()
    encMessage = fernet.encrypt(text.encode())
    #print(encMessage)
    return encMessage

def dencrypted(text):
    fernet = fernet_branca()
    message = bytes(text, 'utf-8')
    decMessage = fernet.decrypt(message).decode()
    #print("decrypted string: ", decMessage)
    return decMessage


def get_license():
    try:
        with open('license.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                csv_license = row[0]
                #print(csv_license)
        return csv_license
    except OSError as e:
         print('')
         print('Error: 4002')
         print('------------------------------------------------------------------------------------------------------------------------------')
         print(" You'll need to get a license/key, please contact our Services Customer Call Center staff at e-mail: da.torres@redlink.com.ar ")
         print('------------------------------------------------------------------------------------------------------------------------------')
         exit()

def validating():
    step1 = get_license()
    step2 = dencrypted(step1)
    step3 = step2.split('.')
    if get_word(step3) == dencrypted('gAAAAABicsujxOr21Bwh3Yygb8fMfFQwMb8DwKBCnJZjXFgk736KGB0gn5B1AbIi_57Q61oF1Zsb_MwiMbcHsNFHrJwMTP3jvQ=='):
        current_date = datetime.now()
        license_date = datetime.strptime(get_date(step3), "%d/%m/%Y")
        return(current_date < license_date)
 

def get_word(list):
    for count, value in enumerate(list):
        if count == 0:
            return value

def get_date(list):
    for count, value in enumerate(list):
        if count == 1:
            return value


