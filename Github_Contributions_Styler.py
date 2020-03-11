import os
import numpy  as np
from character_set import *
#os.system('git')


message = "AYMEN ROCKS";
message = message.upper()

if len(message)>11:
    print("String is too long")
    exit()
collab_matrix = np.zeros((0,7))
for x in message:
    if x == " ":
        pass
    else:
        char_ascii = ord(x) - 0x41
        m = np.matrix(character_set[char_ascii])
        collab_matrix = np.concatenate((collab_matrix, m))

for x in range(7):
    for x in collab_matrix.:
        pass
        
    
    
print(collab_matrix);

        