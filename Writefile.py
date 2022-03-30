teachers = open("Teachers1.txt", "a")
# This command appends directly to the file so after running, whatever you append will be added to the file itseld
# If a w is used instead of an a, the entire file will be overwritten and deleted
teachers.write("Doc - Music")
# Be careful because if you run twice, it will incorrectly add what you append and not go to the next line
# \n will add a new line to the added string
teachers.close()
