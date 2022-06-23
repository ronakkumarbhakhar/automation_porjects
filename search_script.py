import os ,platform ,string
req_file = input("enter name of file to search:")
files = [] 
dirs = []
#script which will run if it is windows
if  str(platform.system()).lower() == 'windows':
    path_sep = ':\\'
    drive= list(string.ascii_uppercase) # returns list of alphabates as windows does not have root path as linux have '/' . 
                                        #so we have to make logic so that it can access each partition of drive.
    no_of_files=0
    no_of_dirs=0
    count=0
    for dri in drive:
        for a,b,c in os.walk(f"{dri}:\\"):
            print([a,b,c])
            if os.path.isfile(req_file):     
                for cf in c :                # as 'c' is list of all files present at that path so we have to chose each file specificly
                    if cf== req_file :
                        no_of_files+=1
                        count+=1  
                        files.append(str(os.path.join(a,req_file)))
            elif os.path.isdir(req_file):
                for bd in b :                   # as 'c' is list of all files present at that path so we have to chose each file specificly
                    if bd == req_file :
                        no_of_dirs+=1
                        count+=1 
                        dirs.append(str(os.path.join(a,req_file)))
#script which will run if it is linux
elif str(platform.system()).lower() == 'linux':
    count=0
    no_of_files=None
    no_of_dirs=None
    for a,b,c in os.walk('/'):
        print([a,b,c])
        if os.path.isfile(req_file):    
            for cf in c:
                if cf == req_file:
                    no_of_files+=1
                    count+=1
                    files = str(os.path.join(a,req_file))
        elif os.path.isdir(req_file):
            for bd in b:
                if bd == req_file:
                    no_of_dirs+=1
                    count+=1 
                    files.append(str(os.path.join(a,req_file)))
print("----------------------------------------------------------------------------")
print(f"total no. of results found         : {count}")
print(f"total no. of files in results      : {no_of_files}")
print(f"total no. of directories in results : {no_of_dirs}")
print("----------------------------------------------------------------------------")
if len(files) > 0:
    print("files in result are :")
    print(files)
else:
    print(f"no file with name {req_file} found !")
print("----------------------------------------------------------------------------")
if len(dirs)>0:
    print("directories in result are :")
    print(dirs)
else:
    print(f"no directory with name {req_file} found !")
print("----------------------------------------------------------------------------")
input("press enter to exit")