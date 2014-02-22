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

parser = argparse.ArgumentParser(prog="wam",description='Web Asset Manager')
parser.add_argument('file', type=str,
                   help='a file for the compiler')
parser.add_argument('-l', '--lang', choices=("js","css"),type=str, dest='language',
                   help='set the language the compiler should use')
parser.add_argument('-m', '--minify-only', dest='minify_only', action='store_const',
                   const=True, default=False,
                   help='only minify, do not compile the file')
parser.add_argument('-M', '--no-minify', dest='no_minify', action='store_const',
                   const=True, default=False,
                   help='do not minify, only compile the file')
parser.add_argument('-d', '--destination', metavar="dest", dest='dest', type=str,
                   help='destination folder for output')
parser.add_argument('-o', '--output', metavar="output", dest='output', type=str,
                   help='destination file to output')
parser.add_argument('-w', '--no-warnings', dest='no_warnings', action='store_const',
                   const=True, default=False,
                   help='suppress warnings on pre-compile')

args = parser.parse_args()

if args.language == None:
    if args.file.find(".") < 0:
        print "wam: error: no language or extension found, ambiguous file"
        exit(1)
    args.language = args.file[args.file.index(".")+1:]

if args.language != "js" and args.language != "css":
    print "wam: error: unsupported language - " + args.language
    exit(1)

if args.minify_only and args.no_minify:
    print "wam: error: minify-only and no-minify are mutually exclusive"
    exit(1)

if args.dest == None:
    args.dest = os.getcwd()
elif not os.path.isabs(args.dest):
    args.dest = "./"+args.dest

if os.path.isfile(args.dest):
    print "wam: error: destination is a file"
    exit(1)
if not os.access(os.path.dirname(args.dest), os.W_OK):
    print "wam: error: destination is not writable"
    exit(1)
if not os.path.exists(args.dest):
    os.makedirs(args.dest)

if args.output == None:
    args.output = args.file
    index = args.output.find(".")
    if index < 0:
        args.output += ".o"
    else:
        args.output = args.output[:index]+".o"+args.output[index:]
args.output = args.dest+"/"+args.output

def pre_compile(in_file,out_file):
    if args.no_warnings:
        if os.system("gcc -xc -C -E -w "+in_file+" -o "+out_file) > 0:
            print("Pre-compiling process failed.")
            exit(1)
    else:
        if os.system("gcc -xc -C -E "+in_file+" -o "+out_file) > 0:
            print("Pre-compiling process failed.")
            exit(1)
    for line in fileinput.FileInput(out_file,inplace=1):
        if not line.startswith("#"):
            print line

def minify(in_file,out_file):
    if os.system('java -jar /usr/local/lib/wam/yuicompressor.jar --type '+args.language+' '+in_file+' -o '+out_file) > 0:
        print("Minification process failed.")
        exit(1)

if args.minify_only:
    minify(args.file,args.output.replace(".o",".min"))
    exit(0)

pre_compile(args.file,args.output)
if not args.no_minify:
    minify(args.output,args.output)

for line in fileinput.FileInput(args.output,inplace=1):
    if line.rstrip() != '':
            print line



