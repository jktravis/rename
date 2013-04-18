import os, argparse

parser = argparse.ArgumentParser(description="Remove spaces from file names and make them lowercase.")
parser.add_argument("file", nargs='+', help="The file to be renamed")

for f in args.file:
   print "Renaming {} to {}".format(f, f.replace(" ", "_").lower() )
   os.rename(f, f.replace(" ", "_").lower())
