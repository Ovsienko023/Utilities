class Subject:
    observers = list()

    def __init__(self):
        pass

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)
        print('User delete')


    def notify_observer(self):
        for obs in self.observers:
            print("Oповещение: ", obs.__class__.__name__)
            obs.update()

    def some_business_logic(self):
        print("set data...")
        self.notify_observer()

class Concrere_observer:
    def __init__(self):
        pass

    def update(self):
        print('update!')

def main():
    us1 = Concrere_observer()
    us2 = Concrere_observer()

    sub = Subject()
    sub.register_observer(us1)
    sub.register_observer(us2)

    sub.some_business_logic()

main()
