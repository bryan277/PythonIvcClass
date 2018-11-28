thisdict = {
"brand":"Ford",
"model":"Mustang",
"year": 1964
}
print(thisdict)

x = thisdict['model']
print(x)
# Mustang

x = thisdict.get('model')
print(x)
# Mustang

thisdict["year"] = 2018
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

for x in thisdict:
    print(x)
# brand
# model
# year

for x in thisdict:
    print(thisdict[x])
# Ford
# Mustang
# 2018

for x in thisdict.values():
    print(x)
# Ford
# Mustang
# 2018

for x, y in thisdict.items():
    print(x, y)
# brand Ford
# model Mustang
# year 2018

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in thisdict dictionary")
else:
    print('NO')

print(len(thisdict))
#3

thisdict['color'] = 'red'
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2018, 'color': 'red'}

thisdict.pop('model')
print(thisdict)
# {'brand': 'Ford', 'year': 2018, 'color': 'red'}

thisdict.clear()
print(thisdict)
# {}
