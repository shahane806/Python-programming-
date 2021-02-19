# open the file .txt
text_file = open("read.txt", "r")
text_file.close()
# read the read.txt
text_file = open("read.txt", "r")

print(text_file.read(5))
text_file.close()
# read the line
text_file = open("read.txt", "r")
print(text_file.readline())
text_file.close()
# read the entire file
text_file = open("read.txt", "r")
print(text_file.read())
text_file.close()
# read the entire file in list
text_file = open("read.txt", "r", "")
print(text_file.readlines())
text_file.close()
