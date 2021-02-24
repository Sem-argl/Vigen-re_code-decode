# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
message = "i manage it, keep my mesaage coded!"
key = "friends"
message_stripped = message.replace('!', '').replace('?', '').replace(',', '') # eliminate non leters characters from the message
message_no_space = message_stripped.replace(' ', '')  # make all words in message be  en one long string with no " "
key_message = key * int(len(message)/(len(key))) + key[0:int(len(message) % len(key))]

def Vigenère_coder(message, key):
  message_coded = ""
  message_coded_sp = ""
  j = 0
# -------------- message_decoding
  for i in range(len(message_no_space)):
    if message_no_space[i] in alphabet:
      message_coded += alphabet[(alphabet.find(message_no_space[i]) + alphabet.find(key_message[i]))]
    if ((message_no_space[i] == '!') or (message_no_space[i] == '.') or (message_no_space[i] == '?')):
      message_coded += message_no_space[i]
# -------------- decoded string splits in to words
  for i in range(len(message)):
    if message[i] in alphabet:
      j += 1           # set a separate counter for this part of for loop so it not missmach when i meets not leter character in message
      message_coded_sp += message_coded[j - 1]
    if (message[i] in alphabet) == False:
      message_coded_sp += message[i]
           
  return (message_coded_sp)
print("coded message is: \n",Vigenère_coder(message, key))