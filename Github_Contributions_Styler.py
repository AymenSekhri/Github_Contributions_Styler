import os
import numpy  as np
from character_set import *
from datetime import datetime  
from datetime import timedelta  
#os.system('git')
#max = 52

CHAR_WIDTH = 5
CHAR_HIGHT = 7

message = "AYMEN ROCKS";
message = message.upper()

if len(message.strip())>11:
    print("String is too long")
    exit()
collab_matrix = np.zeros((CHAR_HIGHT,CHAR_WIDTH))
for x in message:
    if x == " ":
        empty_column = np.matrix(np.zeros((CHAR_HIGHT,1)))
        collab_matrix = np.concatenate((collab_matrix,empty_column),axis=1)
    else:
        char_ascii = ord(x) - 0x41
        char_vector = character_set[char_ascii]
        char_matrix = np.matrix(np.zeros((0,CHAR_WIDTH)))
        for char_row_encoded in char_vector:
            char_row_decoded = np.matrix(list(format(char_row_encoded, '08b'))[:-(8-CHAR_WIDTH)])
            char_matrix = np.concatenate((char_matrix,char_row_decoded))
        collab_matrix = np.concatenate((collab_matrix,char_matrix),axis=1)


today_date = datetime.now()
end_date = today_date - timedelta(days=today_date.weekday()+2)  
start_date = end_date - timedelta(days=7*52-1)
current_date = start_date


path_to_repo = "C:\\Users\\0xCC\\Desktop\\FakeRepo"

os.system("cd " + path_to_repo)
os.system("git init")

fd = open(path_to_repo + '\\FakeCommits.txt', 'w')
fd.close()

commit_date = current_date.strftime("%d.%m.%Y")
fd = open(path_to_repo + '\\FakeCommits.txt', 'w')
fd.write("565454")
fd.close()
os.system("git add .")
os.system('git commit --message="' + 'fake commit' + '" --date="' + commit_date + '"')


fd = open(path_to_repo + '\\FakeCommits.txt', 'w')
fd.write("14865468")
fd.close()
os.system("git add .")
os.system('git commit --message="' + 'fake commit' + '" --date="' + commit_date + '"')



        
    
    

        