def encrypt(word,code):
    for i in word:
        print (chr(ord(i)+code),end='')
string = input("\nEnter a word to be encrypted:")
num = int(input("Enter a code number for encryption:"))
encrypt(string,num)


def decrypt(word,code):
    for i in word:
        print (chr(ord(i)-code),end='')
string = input("\nEnter a word to be decrypted:")
num = int(input("Enter a code number for decryption:"))
decrypt(string,num)