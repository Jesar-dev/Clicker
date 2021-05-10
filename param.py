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
    "Schoolboy": {
        "amount": 0,
        "speed": 1,
        "cost": 10
    },
    "Teacher": {
        "amount": 0,
        "speed": 10,
        "cost": 100
    },
    "Director": {
        "amount": 0,
        "speed": 100,
        "cost": 10000
    },
    "Einstein": {
        "amount": 0,
        "speed": 1000,
        "cost": 100000
    }
}

speed = 0
score = 0
