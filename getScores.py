def main():
    scores = get_scores()
    total = get_total(scores)
    lowest = min(scores)
    total -= lowest
    average = total / (len(scores) -1)
    print(average)




# def get_scores(): #get scores from user
#     scores = input(int('Enter a test score: '))
#     print('Do you want to add another score?')
#     print('y = yes, anything else = no: ')
#     while
#
# def get_total(value_list): #calculate the total of the scores
#     total = 0
#
#
# def main():
