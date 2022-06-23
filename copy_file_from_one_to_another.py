import os, sys
if os.path.exists('C:\\Users\\91992\\OneDrive - Army Institute of Technology\\Desktop\\speech.txt'):
    og = open('C:\\Users\\91992\\OneDrive - Army Institute of Technology\\Desktop\\speech.txt','r')
    dataog =og.readlines()
    #print(dataog)
    og.close()
    if os.path.exists('C:\\Users\\91992\\Documents\\automation_projects\\copy.txt'):
        cp= open('C:\\Users\\91992\\Documents\\automation_projects\\copy.txt','r')
        datacp = cp.readlines()
        if datacp == dataog:
            print("data already written")
            sys.exit()
        else:
            cp= open('C:\\Users\\91992\\Documents\\automation_projects\\copy.txt','w')
            for data in dataog:
                cp.write(data)
            cp.close()
    else:
        cp= open('C:\\Users\\91992\\Documents\\automation_projects\\copy.txt','w')
        for data in dataog:
            cp.write(data)
        cp.close()
else:
    print('file to be copied not found')

