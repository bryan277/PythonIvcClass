
def main():
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']
    outfile = open('cities.txt', 'w')
    for item in cities:
        outfile.write(item + '\n')
    outfile.close()

main()
# New York
# Boston
# Atlanta
# Dallas
