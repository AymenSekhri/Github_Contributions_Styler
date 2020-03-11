import os
import numpy  as np
from character_set import *
from datetime import datetime  
import subprocess
from datetime import timedelta  
#os.system('git')
#max = 52

CHAR_WIDTH = 5
CHAR_HIGHT = 7
NUM_OF_COMMITS = 50

message = "AYMEN";
message = message.upper()

if len(message.strip())>11:
    print("String is too long")
    exit()
collab_matrix = np.zeros((CHAR_HIGHT,0))
for x in message:
    if x == " ":
        empty_column = np.matrix(np.zeros((CHAR_HIGHT,2)))
        collab_matrix = np.concatenate((collab_matrix,empty_column),axis=1)
    else:
        empty_column = np.matrix(np.zeros((CHAR_HIGHT,1)))
        char_ascii = ord(x) - 0x41
        char_vector = character_set[char_ascii]
        char_matrix = np.matrix(np.zeros((0,CHAR_WIDTH)))
        for char_row_encoded in char_vector:
            char_row_decoded = np.matrix(list(format(char_row_encoded, '08b'))[(8-CHAR_WIDTH):])
            char_matrix = np.concatenate((char_matrix,char_row_decoded))
        collab_matrix = np.concatenate((collab_matrix,char_matrix,empty_column),axis=1)


today_date = datetime.now()
end_date = today_date - timedelta(days=today_date.weekday()+2)  
start_date = end_date - timedelta(days=7*52-1)
current_date = start_date


path_to_repo = "C:\\Users\\0xCC\\Desktop\\FakeRepo3"

os.chdir(path_to_repo)
subprocess.call("git init",stdout=subprocess.DEVNULL)
fd = open(path_to_repo + '\\FakeCommits.txt', 'w')
fd.close()

print("The Art takes time to accomplish, please wait...")
for x in range(collab_matrix.shape[1]):
    for y in range(collab_matrix.shape[0]):
        collab_array = collab_matrix.tolist()
        if collab_array[y][x] == '1':
            commit_date = current_date.strftime("%d.%m.%Y")
            for z in range(NUM_OF_COMMITS):
                fd = open(path_to_repo + '\\FakeCommits.txt', 'w')
                fd.write(str(x) + '  ' + str(y) + ' ' + str(z))
                fd.close()
                subprocess.call("git add .",stdout=subprocess.DEVNULL)
                #print('git commit --message = "' + 'fake commit' + '" --date = "' + commit_date + '"')
                subprocess.call('git commit --message="' + 'fake commit' + '" --date="' + commit_date + '"',stdout=subprocess.DEVNULL)
        current_date = current_date + timedelta(days=1)

print("Done. Now, publish your repository to GitHub.")



        
    
    

        