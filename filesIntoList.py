#read the files into a list
def main():
    infile = open('cities.txt','r')
    cities = infile.readlines()
    infile.close()
    print(cities)
    index = 0
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
    print(cities)

main()

# ['New York\n', 'Boston\n', 'Atlanta\n', 'Dallas\n']
