import os
# Location of the files that store the path to the current file and it's extension 
path_location = "/home/yash/.vim/vide/filepath.txt" 
ext_location = "/home/yash/.vim/vide/filetype.txt" 
tail_location = "/home/yash/.vim/vide/tail.txt" 
head_location = "/home/yash/.vim/vide/head.txt" 
# Now we open both files to read their location 
path_file = open(path_location, "r")
ext_file = open(ext_location, "r")
tail_file = open(tail_location, "r")
head_file = open(head_location, "r")
# Now we read the contents(path/extension) of the files and assign it to variables 
""" If the full path of a file is /home/yash/disco/dance.cpp
    then the head is "/home/yash/disco/", tail is "dance.cpp" and ext is "cpp" 
""" 
path = path_file.readline() 
ext = ext_file.readline()
tail = tail_file.readline()
head = head_file.readline()
# Stripping the unncessary newline 
path = path.strip('\n') 
ext = ext.strip('\n') 
tail = tail.strip('\n') 
head = head.strip('\n') 
# Running the program based on the extension 
if(ext == "py"):
    command = "python3 " + path 
    os.system(command) 
elif(ext == "js"):
    command = "node " + path 
    os.system(command) 
elif(ext == "cpp"):
    tail = tail[:-3] 
    command = "cd " + head + " && clear && ./" + tail + "out"
    os.system(command) 
elif(ext == "php"):
    print("php") 
elif(ext == "html"):
    command = "firefox " + path 
    os.system(command) 
elif(ext == "txt"):
    command = "cat " + path 
    os.system(command) 
else:
    print("This type of extension cannot be run") 
