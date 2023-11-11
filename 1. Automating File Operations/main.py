from actions.CopyFile import CopyFile
from actions.MoveFile import MoveFile
from actions.DeleteFile import DeleteFile
from actions.CopyDirectory import CopyDirectory
from actions.MoveDirectory import MoveDirectory
from actions.DeleteDirectory import DeleteDirectory

import os

choice = -1 
while choice != 0:
    os.system("cls")

    print(""" 
1. Copy file
2. Move file
3. Delete file
4. Copy directory
5. Move directory
6. Delete directory
          """)
    
    choice = int(input("Select a Number : "))


    if choice == 1:
        CopyFile()
    elif choice == 2:
        MoveFile()
    elif choice == 3:
        DeleteFile()
    elif choice == 4:
        CopyDirectory()
    elif choice == 5:
        MoveDirectory()
    elif choice == 6:
        DeleteDirectory()
    else:
        print("Invalid Choice")
        continue
    





