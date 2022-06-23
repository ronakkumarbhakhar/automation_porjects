from genericpath import isfile
import os
cd =os.getcwd()
os.chdir(cd)
ls =os.listdir()
f =[]
d =[]
for g in ls:
    if isfile(g):
        
        f.append(g)
    else:
        
        d.append(g)
print("\n list of files\n")
for f in f:
    print(f)
print('\n list of dirs\n')
for d in d:
    print(d)