import os
import shutil

from_dir = "C:/Users/HP/Downloads"
to_dir = "C:/Users/HP/Desktop/Yash/Document_Files"
list_Of_Files= os.listdir(from_dir)
print(list_Of_Files)
for filename in list_Of_Files:
    name,extension = os.path.splitext(filename)
    #print(name)
    #print(extension)
    if extension == "":
        continue
    if extension in [".txt","doc",".docx",".pdf"]:
        path1 = from_dir + "/" + filename
        path2 = to_dir + "/" + "Document_Files"
        path3 = to_dir + "/" + "Document_Files" + "/" + filename
        if os.path.exists(path2):
            print("Moving"+ filename + "...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+ filename + "...")
            shutil.move(path1,path3)
