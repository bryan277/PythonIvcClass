
new_list = []

for i in old_list:
    if filter(i):
        new_list.append(expressions(i))
print(new_list)


new_list = [expressions(i) for i in old_list if filter(i)]
