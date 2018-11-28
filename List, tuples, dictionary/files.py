# def main():
#     f = open('demofile.txt', "w")
#     f.write('Hello world')
#
# main()
# f = open('demofile.txt', 'a')
# f.write('Now the file has one more line')
# f = open('demofile.txt', 'w')
# f.write('I have deleted the content')
import os
os.remove('demofile.txt')
