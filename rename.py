import os, argparse, sys

parser = argparse.ArgumentParser(description="Remove spaces from file names and make them lowercase.")
name_change_group = parser.add_argument_group("Name change options")
parser.add_argument("file", nargs='+', help="The file to be renamed")
parser.add_argument("-p", "--printonly", help="Print the output, but make no changes", action="store_true")
name_change_group.add_argument("-n", "--new", help="Set a new file name to be used for all files. Must be used with --ext.")
name_change_group.add_argument("-x", "--ext", help="Set the new file extension to be used for all files. Must be used with --new.")

args = parser.parse_args()

if args.new and not args.ext:
   sys.stderr.write("Error: Must use --ext [-e] if using --new [-n]\n")
   parser.print_help()
   sys.exit(1)

if args.ext and not args.new:
   sys.stderr.write("Error: Must use --new [-n] if using --ext [-e]\n")
   parser.print_help()
   sys.exit(1)

if args.new and args.ext:
   if args.printonly:
      for i, f in enumerate(args.file):
         print "Renaming {} to {}". format(f, args.new + str(i) + '.' + args.ext)
   else:
      for i, f in enumerate(args.file):
         print "Renaming for realz {} to {}". format(f, args.new + str(i) + '.' + args.ext)
         os.rename(f, args.new + str(i) + '.' + args.ext)
else:
   if args.printonly:
      for f in args.file:
         print "Renaming {} to {}".format(f, f.replace(" ", "_").lower() )
   else:
      for f in args.file:
         print "Renaming for realz {} to {}".format(f, f.replace(" ", "_").lower() )
         os.rename(f, f.replace(" ", "_").lower())
