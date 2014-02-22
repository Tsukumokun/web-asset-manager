import argparse
import os

import wam_js
#import wam_css

parser = argparse.ArgumentParser(prog="wam",description='Web Asset Manager')
parser.add_argument('file', type=str,
                   help='a file for the compiler')
parser.add_argument('-l', '--lang', choices=("js","css"),type=str, dest='language',
                   help='set the language the compiler should use')
parser.add_argument('-m', '--minify-only', dest='minify_only', action='store_const',
                   const=True, default=False,
                   help='only minify, do not concatenate the files')
parser.add_argument('-M', '--no-minify', dest='no_minify', action='store_const',
                   const=True, default=False,
                   help='do not minify, only concatenate the files')
parser.add_argument('-d', '--destination', metavar="dest", dest='dest', type=str,
                   help='destination folder for output')

args = parser.parse_args()

if args.language == None:
    if args.file.find(".") < 0:
        print "wam.py: error: no language or extension found, ambiguous file"
        exit(1)
    args.language = args.file[args.file.index(".")+1:]

if args.language != "js" and args.language != "css":
    print "wam.py: error: unsupported language - " + args.language
    exit(1)

if args.minify_only and args.no_minify:
    print "wam.py: error: minify-only and no-minify are mutually exclusive"
    exit(1)

if args.dest == None:
    args.dest = os.getcwd()
elif not os.path.isabs(args.dest):
    args.dest = "./"+args.dest

if os.path.isfile(args.dest):
    print "wam.py: error: destination is a file"
    exit(1)
if not os.access(os.path.dirname(args.dest), os.W_OK):
    print "wam.py: error: destination is not writable"
    exit(1)
if not os.path.exists(args.dest):
    os.makedirs(args.dest)

if args.language == "js":
    compile_js(args)
elif args.language == "css":
    print "not yet supported"

