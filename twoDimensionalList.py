def main():
    #create 2 - to list
    values = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]

    #fill the list with random number
    for r in range(Rows):
        for c in range(clos):
            values[r][c] = random.randint(1,100)
    #display list
    print(values)

    values = []
    for r in range(Rows):
        values.append([])
        for c in range(cols):
            values[r].appned(0)

    print(values)
