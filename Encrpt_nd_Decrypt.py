# Encrpt and Decrypt Method


alphabet = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(){}:?></;''"
key = 4

encr=' '
decr=' '
#message = input("Enter the message:")
msg =open('message.txt',"r")
message = msg.read()
for char in message:
    position = alphabet.find(char)
    newposition = (position+key)%83
    newchar = alphabet[newposition]
    #print(newchar)
    encr+=newchar
print('The Encripted of the message :',encr)
for enc in encr:
    position = alphabet.find(enc)
    backposition = (position-key)%83
    oldchar = alphabet[backposition]
    decr+=oldchar
print('The Decripted of the message :',decr)

'''
a="asdfghjkl"
k=4
encr=" "
message = "ghjklasdf"
for char in message:
    pos = a.find(char)  //it takes index of the value #for ex pos l = 4
    print(pos)
    npos=(pos-k)%9   //by the way the value is 4 the k value is 4 //(4+4)%9 = 8
    nchar = a[npos]  //it check the index of the position value 8 = f
    encr+=nchar  //it did just add a temprory pos..when condition will be prove that result it can print.
print(encr)
'''
