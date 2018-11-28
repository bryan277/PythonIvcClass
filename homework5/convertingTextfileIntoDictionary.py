f = open('textfile.txt', 'r')
answer = {}
for line in f:
    k, v = line.strip().split('=')
    answer[k.strip()] = v.strip()

print(answer)

f.close()
