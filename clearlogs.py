import os, sys
from fnmatch import fnmatch
import argparse

Banner="""

               |))    |))
 .             |  )) /   ))
 \\   ^ ^      |    /      ))
      \\(((  )))   |   /        ))
   / G    )))  |  /        ))
  |o  _)   ))) | /       )))
   --' |     ))`/      )))
    ___|              )))
   / __\             ))))`()))
  /\@   /             `(())))
  \/   /  /`_______/\   \  ))))
       | |          \ \  |  )))
       | |           | | |   )))
       |_@           |_|_@    ))
      /_/           /_/_/
Valkyrie
	Nothing to see here, go ahead.


"""

def add_banner(file):
    with open(file, 'w+') as f:
        f.write(Banner)

def shred(file, remove=False, banner=False):
    if not remove:
        os.system("shred --force --exact -z {}".format(file))
    else:
        os.system("shred --force --exact -z --remove {}".format(file))
        
    if banner:
        add_banner(file) 

def shred_dir(directory, pattern="*.*", verbose=True, remove=False, banner=False):
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if fnmatch(file, pattern):
                shred(file, remove=remove, banner=banner)
            if verbose:
                print("[+]File {} got shreded!".format(file))


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
    parser.add_argument("path", type=str, help="The file or directory path to shred")
    parser.add_argument("-p", "--pattern", type=str, default="*.*", help="Only shred files that match this pattern")
    parser.add_argument("-r", "--remove", help="Remove the file/files after shredding them", action="store_true")
    parser.add_argument("-b", "--banner", help="Put a banner into every shreded file", action="store_true")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    pos_args = args()

    print("[-]Starting to shred")
    if os.path.isfile(pos_args.path):
        shred(pos_args.path, pos_args.remove, pos_args.banner)
        if pos_args.verbose:
            print("[+]File {} got shreded!".format(pos_args.path))
    else:
        shred_dir(pos_args.path, pos_args.pattern, pos_args.verbose, pos_args.remove, pos_args.banner)

    print("[-]Finished shreding")
