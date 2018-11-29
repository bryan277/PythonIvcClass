
def show():

    tea_file = open('tea.txt', 'r')
    teaDict = {}
    descr = tea_file.readlines()
    for line in descr:
        k, v = line.strip().split(':')
        teaDict[k.strip()] = v.strip()

    print(teaDict)
    # split1 = descr.split(':')
    # print(split1)
    # print(descr)
    # total = int(split1[1]) + int(split1[2]) + int(split1[3])
    # print(split1[0], split1[1], split1[2], split1[3], total)
    

show()



# f = open('textfile.txt', 'r')
# answer = {}
# for line in f:
#     k, v = line.strip().split('=')
#     answer[k.strip()] = v.strip()
