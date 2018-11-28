#List and text files
#use writelines() - saves a list of string to files
def main():
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']
    outfile = open('cities.txt', 'w')
    outfile.writelines(cities)
    outfile.close()

main()
# New YorkBostonAtlantaDallas

#prepare saves with line break
