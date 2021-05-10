def check_accelerators(accelerations, name_of_accelerator, score, speed):
    """
    accelerations - словарь ускорителей
    name_of_accelerator - название ускорителя (string)
    score - количество очков
    speed - текущая скорость
    Проверка при нажатии на ускоритель,
      есть ли необходимое количество очков на покупку
    в случае удачи отнять необходимое количество очков
      и добавить скорость производства
    """
    if score >= accelerations[name_of_accelerator]["cost"]:
        score -= accelerations[name_of_accelerator]["cost"]
        accelerations[name_of_accelerator]["amount"] += 1
        speed += accelerations[name_of_accelerator]["speed"]
    return [score, speed]
