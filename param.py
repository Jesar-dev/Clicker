HEIGHT_WINDOW = 480
WIDTH_WINDOW = 360
FPS = 30
RADIUS_CIRCLE = 50

# Статус работы игры
game_running = True

# Словарь ускорений
# 1 - количество ускорителей
# 2 - скорость ускорителя
# 3 - стоимость ускорителя
accelerations = {
    "Schoolboy": [0, 1, 10],
    "Teacher": [0, 10, 100],
    "Director": [0, 100, 10000],
    "Einstein": [0, 1000, 100000]
}

speed = 0
score = 0
