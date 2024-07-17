#lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)

from random import choice


#метод _call_:
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def call(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball.call())
print(first_ball.call())
print(first_ball.call())

#замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "a") as file:
            for idx, data in enumerate(data_set, 1):
                file.write(f"{idx}. {data}\n")
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])