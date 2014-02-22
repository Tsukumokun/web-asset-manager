import os

def pre_compile(in_file,out_file):
    if os.system("gcc -xc -E "+in_file+" -o "+out_file) > 0:
        print("Pre-compiling process failed.");
        exit(1)
    



