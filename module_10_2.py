#Задача "За честь и отвагу!":
import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.bots = 100

    def run(self):
        print(f"{self.name}, на нас напали!")

        while self.bots > 0:
            self.bots -= self.power
            self.days += 1
            time.sleep(1)
            print(f"{self.name} сражается {self.days}, осталось {self.bots} воинов.")
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


first_knight = Knight("Sir Lancelot", 5)
second_knight = Knight("Sir Galahad", 3)

first_knight.start()
second_knight.start()

    # Ждем завершения потоков
first_knight.join()
second_knight.join()

print("Все враги повержены!")



