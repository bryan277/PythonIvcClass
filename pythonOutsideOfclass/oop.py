

class Dog:

    #Class Attribute
    species = 'mammal'

    #Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Instantiate the Dog object
philo = Dog('Philo', 5)
mikey = Dog('Mikey', 6)

#Access the instance atrritbutes
print("{} is {} and {} is {}.".format(
    philo.name, philo.age, mikey.name, mikey.age))

# Is Philo a mammal?
# Is Philo a mammal?
if philo.species == "mammal":
    print("{0} is a {1}!".format(philo.name, philo.species))
    
# Philo is 5 and Mikey is 6.
# Philo is a mammal!
