#  Cryptography Project Day 5

from cryptography.fernet import Fernet
def generatepPasskey():
    key = Fernet.generate_key()
    print(key)
    print(type(key))
    abc = open("passkey.key",'wb')
    abc.write(key)
    abc.close()
#Get the Key
def getMykey():
    abc = open("passkey.key","r")
    key = abc.read()
    abc.close()
    return (key)
#Get the content from the user
def getcontentfromuser():
    return input("Enter the content you want :")
    getcontentfromuser()
#encrypt the massage
def encryptmessage(message_normal):
    k = fernet()
    key = getMykey()
    encrypted_message =k.encrypt(message_normal)
    return encrypted_message
    encryptmessage(b"My Mobile no is 7385587828")
#Decrypt the message
def decryptMessage(message_secret):
	key = getMyKey()
	k = Fernet(key)
	decrypted_Message = k.decrypt(message_secret)
	return decrypted_Message
