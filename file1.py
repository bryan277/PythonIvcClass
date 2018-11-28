#read data from file.text
def main():
    infile = open('phile.txt', 'r')
    file_contents = infile.read()
    infile.close()
    print(file_contents)

main()
