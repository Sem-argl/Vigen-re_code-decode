alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
key = "friends"
message_splited = message.split(" ")
message_stripped = message.replace('!', '').replace('?', '')
message_no_space = message_stripped.replace(' ', '')  # make all words in message be  en one long string with no " "
key_message = key * int(len(message)/(len(key))) + key[0:int(len(message) % len(key))]

def Vigenère_decoder(message, key):
  message_decoded = ""
  message_decoded_sp = ""
  spaces_location = []
  spaces_location_new = []
  #   message_decoded
  for i in range(len(message_no_space)):
    if message_no_space[i] in alphabet:
      message_decoded = message_decoded + alphabet[(alphabet.find(message_no_space[i]) - alphabet.find(key_message[i]))]
    if ((message_no_space[i] == '!') or (message_no_space[i] == '.') or (message_no_space[i] == '?')):
      message_decoded += message_no_space[i]
  #  spaces_location
  for i in range(len(message_stripped)):
    if message_stripped[i] == " ":
      spaces_location += [i] 
  #  spaces_location_new
  for i in range(len(spaces_location)):
    spaces_location_new += [spaces_location[i] - i]
  spaces_location_new = [0] + spaces_location_new + [len(message_no_space)]
  # message_decoded_sp = message decoded and splited
  for i in range(len(message_splited)):
        message_decoded_sp +=  message_decoded[spaces_location_new[i]:spaces_location_new[i +1]] + " "
        
        
  return (message_decoded_sp)
print(Vigenère_decoder(message, key))
