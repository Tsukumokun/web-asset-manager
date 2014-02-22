import argparse

parser = argparse.ArgumentParser(description='Web Asset Manager')
parser.add_argument('file', metavar='file', type=str, nargs='1',
                   help='a file for the compiler')
parser.add_argument('-l', dest='language',
                   help='set the language the compiler should use')
parser.add_argument('-m', dest='minify_only'
                   help='only minify, do not concatenate the files')

args = parser.parse_args()

print "Language:" + language;
print "Minify-Only:" + minify_only;
