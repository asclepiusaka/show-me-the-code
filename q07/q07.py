import os
import fnmatch

__author__ = "saka"
default_dir = "/home/saka/Coding/python"

def fileIter(dirname):
    if not os.path.isdir(dirname):
        print("error"+dirname)
        raise Exception("not a directory")
    Files = os.listdir(dirname)
    for nextTarget in Files:
        if os.path.isdir(os.path.join(dirname,nextTarget)) and nextTarget not in ['env','lib']:
            yield from fileIter(os.path.join(dirname,nextTarget))
        elif os.path.isfile(os.path.join(dirname,nextTarget)):
            yield os.path.join(dirname,nextTarget)



if __name__ == '__main__':
    emptyline = 0
    comment = 0
    code = 0
    d = input("input the directory you want to check python code: ")
    if not d:
        d = default_dir
    d = os.path.expanduser(d)
    for file in fileIter(d):
        if fnmatch.fnmatch(file,'*.py'):
            with open(file,'rt') as f:
                for line in f:
                    if line == "\n":
                        emptyline+=1
                    elif line.startswith('#'):
                        comment+=1
                    else:
                        code+=1

    print("comment line in those python files %d"%comment)
    print("line of Code: %d"%code)
    print("empty line in these codes: %d"%emptyline)



