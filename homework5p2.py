#Hans Vos
#1003181
#Due final exam
#hw5 set #2

def main():
    sentence={}
    sentence=input("enter a sentence to translate\n")
    text_file = open('textabbv.txt', 'r')
    for line in text_file:
        word,unword=line.split(":")
        if word in sentence:
            sentence = sentence.replace(word, unword)
    print(sentence)

main()

# Hanss-MacBook-Pro:PythonIvcClass hansvos$ python homework5p2.py
# enter a sentence to translate
# r u, lol?
# are
#  you
# , laughing out loud
# ?


# Hanss-MacBook-Pro:PythonIvcClass hansvos$ python homework5p2.py
# enter a sentence to translate
# r we bff?
# are
#  we best friend forever
# ?
