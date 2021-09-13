class Vehicle:
    def __init__(self, started=False, speed=0):
        self.started = started
        self.speed = speed

    def start(self):
        self.started = True
        print("Started, let's ride!")

    def stop(self):
        self.speed = 0

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vrooooom!")
        else:
            print("You need to start me first")


class Car(Vehicle):
    trunk_open = False

    def open_trunk(self):
        self.trunk = True

    def close_trunk(self):
        self.trunk = False


class Motorcycle(Vehicle):
    def __init__(self, center_stand_out=False):
        self.center_stand_out = center_stand_out
        super().__init__()

    def start(self):
        print('This is motorcycle speaking')

def funkcja(arg1, arg2):
    print(arg1, arg2)


rodzina = {'Karol': '723-412-073',
           'Agnieszka': '723-534-243'
}

imiona = rodzina.keys()

rodzina ['Jacek'] = 'dupa-dupa-dupa'
print(len(rodzina))
print('Drukuje numer Jacka')
print(rodzina['Jacek'])
print('Drukuje wszystkich z listy')
print(imiona)
print('Teraz drukuje numer Karola')
print(rodzina['Karol'])
del(rodzina['Jacek'])
print('Skasowalem kogos, zobacz')
print(rodzina)
print(imiona)
print('A teraz posortuje')
print(sorted(rodzina))
print('Czy Karol jest w rodzinie?')
print('Karol' in rodzina)
print('Ile rodzina ma teraz czlonkow?')
print(len(rodzina))
print('Inny program\n\n')

print('Tutaj podalem do funkcji wartosci uzywajac nazwy klucza? Chodzi o Keyword.')
funkcja(arg1=100,arg2=200)
print('A teraz bedzie forced uzycie argumentow\n')
rodzina ['arg1'] = 1
rodzina ['arg2'] = 2
print('Sprawdzam czy nadpisalem nazwy kluczy')
print(rodzina.keys())
print(type(rodzina))
del(rodzina['Karol'],rodzina['Agnieszka'])
funkcja(**rodzina)
lista = [1, 2]
print(type(lista))
print(lista)
funkcja(*lista)