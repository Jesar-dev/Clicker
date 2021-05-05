def check_accelerators(accelerations, name_of_acc, score, speed):
    """
    accelerations - словарь ускорителей
    name_of_acc - название ускорителя (string)
    score - количество очков
    speed - текущая скорость
    Проверка при нажатии на ускоритель,
      есть ли необходимое количество очков на покупку
    в случае удачи отнять необходимое количество очков
      и добавить скорость производства
    """
    if score >= accelerations[name_of_acc][2]:
        score -= accelerations[name_of_acc][2]
        accelerations[name_of_acc][0] += 1
        speed += accelerations[name_of_acc][1]
    return [score, speed]
