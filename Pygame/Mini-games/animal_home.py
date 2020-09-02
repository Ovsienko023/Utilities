class Critter(object):
    total = 0

    def __str__(self):
        rep = 'Objekt classa Critter\n'
        rep += f'Имя: {self.name}\nГолод:{self.hunger}\nСамочувствие: {self.boredom}'
        return rep

		
    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    
    def __pass_time(self):
        self.hunger += 1
        self.boredom +=1
    

    @property
    def mod(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            health = 'прекрасно'
        elif unhappiness < 10:
            health = 'неплохо'
        elif unhappiness <= 15:
            health = 'не очень хорошо'
        else:
            health = 'ужасно'
        return health


    def talk(self):
        print(f"Моё имя {self.name}, я чувствую себя {self.mod}")
        self.__pass_time() 


    def eat(self, food=4):
        print("MMM вкусно")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

		
    def play(self, fun=4):
        print("Ураа")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

		
def main():
    animal_name = input("Введи имя животного: ")
    animal = Critter(animal_name)

    choice = None
    while choice != '0':
        print(
            """
            Животное
            0 - Выйти
            1 - Узнать самочувствие
            2 - Покормить
            3 - Поиграть

            """
        )
        choice = input("Ваш выбор: ")
        print()
        if choice == '0':
            print('The end')
        elif choice == '1':
            animal.talk()
        elif choice == '2':
            animal.eat()
        elif choice == '3':
            animal.play()
        elif choice == 'info':
            print(animal)

main()
