from Point import Point
from rect_accelerators import rect_accelerators

HEIGHT_WINDOW = 480
WIDTH_WINDOW = 360


def draw_all_accelerators(accelerations, f2, screen):
    """
    accelerations - словарь ускорителей
    f2 - шрифт для текста
    screen - экран на который надо всё переносить
    Функция рисует все прямоугольники с ускорителями на экране
    """
    width_rect = 120
    height_rect = 50
    # Создаём левую верхнюю точку прямоугольника
    left_upper_corner_rect = Point(WIDTH_WINDOW - 120, 100)
    # Рисуем на экране прямоугольник с текстом первого ускорителя
    rect_accelerators(accelerations, f2, screen, left_upper_corner_rect,
                      width_rect, height_rect, "Schoolboy")

    # Со вторым ускорителем
    left_upper_corner_rect = Point(WIDTH_WINDOW - 120, 155)
    rect_accelerators(accelerations, f2, screen, left_upper_corner_rect,
                      width_rect, height_rect, "Teacher")

    # Третий ускоритель
    left_upper_corner_rect = Point(WIDTH_WINDOW - 120, 210)
    rect_accelerators(accelerations, f2, screen, left_upper_corner_rect,
                      width_rect, height_rect, "Director")

    # Аналогично 4 ускоритель
    left_upper_corner_rect = Point(WIDTH_WINDOW-120, 265)
    rect_accelerators(accelerations, f2, screen, left_upper_corner_rect,
                      width_rect, height_rect, "Einstein")
