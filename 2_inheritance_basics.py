class Dog():
    """ A class to represent a general dog """
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def eat(self):
        if self.gender == 'male':
            print('Here ' + self.name + '! Good Boy! Eat up.')
        else:
            print('Here ' + self.name + '! Good Girl! Eat up.')

    def bark(self, is_loud):
        """Get the dog to speak"""
        if is_loud:
            print('WOOF WOOF WOOF WOOF')
        else:
            print('woof...')

    def compute_age(self):
        """Compute the age in dog years"""
        dog_years = self.age * 7
        print(self.name + ' is ' + str(dog_years) + ' years old in dog years.')


class Beagle(Dog):
    """The class to represnet a specific type of dog: beagle"""

    def __init__(self, my_name, my_gender, my_age, is_gun_shy):
        #call constructor of super class
        super().__init__(my_name, my_gender, my_age)
        self.is_gun_shy = is_gun_shy

    def hunt(self):
        """ If the dog is not sun shy, take them hunting """
        if not self.is_gun_shy:
            self.bark(True)
            print(self.name + ' just brought back a duck.')
        else:
            print(self.name + ' is not a good hunting dog.') 

    def bark(self, is_loud):
            """Get the dog to speak"""
            if is_loud:
                print('HOWL HOWL HOWWWWLLLLLLLLLLLL')
            else:
                print('woof...')



dog_1 = Beagle('Kady', 'female', 10, True)
dog_1.eat()
dog_1.bark(True)
dog_1.compute_age()
print()
dog_1.hunt()

#Dog class can't hunt
dog_2 = Dog('Spotty dog', 'male', 3)
dog_2.bark(True)
#dog_2.hunt()

