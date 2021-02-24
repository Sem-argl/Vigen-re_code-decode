alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
key = "friends"
message_splited = message.split(" ")
message_stripped = message.replace('!', '').replace('?', '') # eliminate non leters characters from the message
message_no_space = message_stripped.replace(' ', '')  # make all words in message be  en one long string with no " "
key_message = key * int(len(message)/(len(key))) + key[0:int(len(message) % len(key))]

def Vigenère_decoder(message, key):
  message_decoded = ""
  message_decoded_sp = ""
  
# -------------- message_decoding
  for i in range(len(message_no_space)):
   f ((message_no_space[i] == '!') or (message_no_space[i] == '.') or (message_no_space[i] == '?')):
      message_decoded += message_no_space[i]
# -------------- decoded string splits in to words
  for i in range(len(message)):
    if message[i] in alphabet:
      j += 1           # set a separate counter for this part of for loop so it not missmach when i meets not leter character in message
      message_decoded_sp += message_decoded[j - 1]
    if (message[i] in alphabet) == False:
      message_decoded_sp += message[i]
           
  return (message_decoded_sp)
print(Vigenère_decoder(message, key))