#files
#Text files - data stored in series of characters
            # - can be opened and viewed with notepad or text editor

#Binary files - in codes $#%#@ (not covered)

#File modes - 'r' open file for reading only
#              'n' open file for writing if file already exists, erease all contents. If file dont' exits, create the file
#              'a' open file to be written to. All data written to its end. IF file does not exist, create file.

#3 steps of file operation
# 1 - open file
# 2 - read/write
# 3 - close file

#write data to file
def main():
    outfile = open('photo.txt', 'w')
    outfile.write('John Locke\n')
    outfile.write('Dand Hume\n')
    outfile.write('Arthur Morgan\n')

    outfile.close()
