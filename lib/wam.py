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

def die(message):
    print("wam: error: " + message)
    exit(1)

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
parser.add_argument('-d', '--destination', metavar="dest", dest='dest', type=str,
                   help='destination folder for output')
parser.add_argument('-o', '--output', metavar="output", dest='output', type=str,
                   help='destination file to output')
parser.add_argument('-w', '--no-warnings', dest='no_warnings', action='store_true',
                   default=False,
                   help='suppress warnings on compile')

args = parser.parse_args()

fileName, fileExtension = os.path.splitext(args.file)

if args.language == None:
    fileExtension != '' or die("no language or extension found, ambiguous file")
    args.language = fileExtension[fileExtension.index('.')+1:]

args.language in ("js","css") or die("unsupported language - " + args.language)

args.minify_only and args.no_minify and die("minify-only and no-minify are mutually exclusive")

if args.dest == None:
    args.dest = os.getcwd()
elif not os.path.isabs(args.dest):
    args.dest = "./"+args.dest

os.path.isfile(args.dest) and die("destination is a file")
os.access(os.path.dirname(args.dest), os.W_OK) or die("destination is not writable")

if not os.path.exists(args.dest):
    os.makedirs(args.dest)

if args.output == None and args.output.find(".o") < 0:
    args.output = fileName+".o"+fileExtension
args.output = args.dest+"/"+args.output


def _compile(in_file,out_file):
    if args.no_warnings:
        os.system("gcc -xc -C -E -w "+in_file+" -o "+out_file) > 0 \
        and die("compiling process failed")
    else:
        os.system("gcc -xc -C -E "+in_file+" -o "+out_file) > 0 \
        and die("compiling process failed")

    for line in fileinput.FileInput(out_file,inplace=1):
        if not line.startswith("#"):
            print line

def _minify(in_file,out_file):
    os.system('java -jar /usr/local/lib/wam/yuicompressor.jar --type '+args.language+' '+in_file+' -o '+out_file) > 0 \
    and die("minification process failed")

if args.minify_only:
    _minify(args.file,args.output.replace(".o",".min"))
    exit(0)

_compile(args.file,args.output)
if not args.no_minify:
    _minify(args.output,args.output)
if args.language == "css":
    for line in fileinput.FileInput(args.output,inplace=1):
        line = re.sub('\$(?:(?=[^\)])|(?<=[^\(]\$))','#',line)
        print line

for line in fileinput.FileInput(args.output,inplace=1):
    line = line.rstrip()
    if line != '':
        print line



