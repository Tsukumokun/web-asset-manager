#
# WAM - a web asset manager
# Copyright (C) 2014 Christopher Kelley   <tsukumokun(at)icloud.com>
# 
# This work is licensed under the 
# Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 
# International License. To view a copy of this license, visit 
# http://creativecommons.org/licenses/by-nc-nd/4.0/deed.en_US.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# 

import argparse
import os
import fileinput
import re

# Display message and exit on error
def die(message):
    print("wam: error: " + message)
    exit(1)

# Set up arguments
parser = argparse.ArgumentParser(prog="wam",description='Web Asset Manager')
parser.add_argument('file', type=str,
                   help='a file for the compiler')
parser.add_argument('-l', '--lang', choices=("js","css"),type=str, dest='language',
                   help='set the language the compiler should use')
parser.add_argument('-m', '--minify-only', dest='minify_only', action='store_true',
                   default=False,
                   help='only minify, do not compile the file')
parser.add_argument('-M', '--no-minify', dest='no_minify', action='store_true',
                   default=False,
                   help='do not minify, only compile the file')
parser.add_argument('-d', '--destination', metavar='dest', dest='dest', type=str,
                   help='destination folder for output')
parser.add_argument('-D', '--define', metavar='macro', dest='defines', 
                   action='append',
                   help='defines to be added to the compiler')
parser.add_argument('-o', '--output', metavar='output', dest='output', type=str,
                   help='destination file to output')
parser.add_argument('-w', '--no-warnings', dest='no_warnings', action='store_true',
                   default=False,
                   help='suppress warnings on compile')

# Parse current arguments
args = parser.parse_args()

# Separate name and extention information from the passed file
fileName, fileExtension = os.path.splitext(args.file)

# If no language is specified and there is no extention to take from, error
if args.language == None:
    fileExtension != '' or die("no language or extension found, ambiguous file")
    args.language = fileExtension[fileExtension.index('.')+1:]

# If the language is not js or css, error
args.language in ("js","css") or die("unsupported language - " + args.language)

# If the user specified to minify and not minify, error
args.minify_only and args.no_minify and die("minify-only and no-minify are mutually exclusive")

# If there is no destination spcified, use the current directory
if args.dest == None:
    args.dest = os.getcwd()
# Otherwise ensure relativity of the path
elif not os.path.isabs(args.dest):
    args.dest = "./"+args.dest

# If the destination is a file, error
os.path.isfile(args.dest) and die("destination is a file")
# If the destination is not writable (permission issues), error
os.access(os.path.dirname(args.dest), os.W_OK) or die("destination is not writable")

# If the destination does not exist, make it
if not os.path.exists(args.dest):
    os.makedirs(args.dest)

# If there is no output file, interpret a name from the given file
if args.output == None:
    args.output = fileName+".o"+fileExtension
# Prepend the specified destination
args.output = args.dest+"/"+args.output

def _compile(in_file,out_file):
    """
    @brief compiles a given input file into the output file.
    
    This method (this program) uses gcc's built in preprocessor
    to handle all of the directives.
    
    @param[in] in_file  File to compile from.
    @param[in] out_file File to compile into.
    """
    
    # Set default necessary flags and interpret arguments for additional flags
    flags = "-xc -C -E"
    if args.no_warnings:
        flags += " -w"
    if args.defines != None:
        for define in args.defines:
            flags += " -D "+define
    
    # Make a system call for gcc to compile the file, error if gcc does
    os.system("gcc "+flags+" "+in_file+" -o "+out_file) > 0 \
    and die("compiling process failed")

    # Remove the preprocessing directives gcc leaves behind
    for line in fileinput.FileInput(out_file,inplace=1):
        if not line.startswith("#"):
            print line

def _minify(in_file,out_file):
    """
    @brief minify the given input file into the given output file.
    
    This method uses yui-compressor to handle minification of the file.
    
    @param[in] in_file  File to minify from.
    @param[in] out_file File to minify into.
    """
    
    # Make a system call to yui to minify the file, error if yui does.
    os.system("java -jar "+os.path.dirname(os.path.realpath(__file__))+'/yuicompressor.jar --type '+args.language+' '+in_file+' -o '+out_file) > 0 \
    and die("minification process failed")

# If minify only is set, minify and exit
if args.minify_only:
    args.output = args.output.replace(".o.o",".o")
    _minify(args.file,args.output.replace(".o",".min"))
    exit(0)

# Compile the file into the output specified
_compile(args.file,args.output)
if not args.no_minify:
    _minify(args.output,args.output)
    
# If the language was css replace the $ with # again
# TODO: switch this process, have all directives start with $
#       and parse before entering the compile stage.
#       Drawback: must know all required files first.
#       TODO:     look for another way to do this.
if args.language == "css":
    for line in fileinput.FileInput(args.output,inplace=1):
        line = re.sub('\$(?:(?=[^\)])|(?<=[^\(]\$))','#',line)
        print line

# Remove any empty lines and trailing spaces.
for line in fileinput.FileInput(args.output,inplace=1):
    line = line.rstrip()
    if line != '':
        print line
