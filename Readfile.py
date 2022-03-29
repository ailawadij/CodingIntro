# open(filename): open("file.txt", "r (read)/w (write)/a(append)/+(read and write)" )
teachers = open("Teachers.txt", "r")
print(teachers.readlines()[3])
# By using readlines you can access a specific index within the array
# .readable() returns a boulean value
teachers.close()
# Must close file for whe finished
