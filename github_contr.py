import os,sys,subprocess
import numpy  as np
from character_set import *
from datetime import datetime  
from datetime import timedelta  


CHAR_WIDTH = 5
CHAR_HIGHT = 7


if len(sys.argv) != 4:
    print("Invalid arguments.")
    print("Example to use:\n github_contr.py 'C:\myRepo' 'MyMessage' 10")
    exit()
path_to_repo = sys.argv[1]
message = sys.argv[2]
num_of_commits = sys.argv[3]

if len(message.replace(" ", ""))>10:
    print("String is too long.")
    exit()
if os.path.isdir(path_to_repo) == False:
    print("Folder does not exist.")
    exit()

if num_of_commits.isdigit() == False:
    print("The number of commits is not a digit.")
    exit()


num_of_commits = int(sys.argv[3])
message = message.upper()
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


os.chdir(path_to_repo)
subprocess.call("git init",stdout=subprocess.DEVNULL)
fd = open(os.path.join(path_to_repo,'FakeCommits.txt'), 'w')
fd.close()

print("The Art takes time to accomplish, please wait...")
for x in range(collab_matrix.shape[1]):
    for y in range(collab_matrix.shape[0]):
        collab_array = collab_matrix.tolist()
        if collab_array[y][x] == '1':
            commit_date = current_date.strftime("%d.%m.%Y")
            for z in range(num_of_commits):
                fd = open(os.path.join(path_to_repo,'FakeCommits.txt'), 'w')
                fd.write(str(x) + '  ' + str(y) + ' ' + str(z))
                fd.close()
                subprocess.call("git add .",stdout=subprocess.DEVNULL)
                subprocess.call('git commit --message="' + 'fake commit' + '" --date="' + commit_date + '"',stdout=subprocess.DEVNULL)
        current_date = current_date + timedelta(days=1)

print("Done. Now, publish your repository to GitHub.")



        
    
    

        