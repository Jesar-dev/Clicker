import pygame


def rect_accelerators(accelerations, font2, screen,
                      left_upper_corner, width, height, name_of_accelerator):
    """
    accelerations - словарь ускорителей
    f2 - шрифт для текст
    screen - экран на который надо всё переносить
    left_upper_corner - координаты точки левого угла
       прямоугольника (объект класса Point)
    width - ширина прямоугольника (int)
    height - высота прямоугольника (int)
    name_of_acc - название ускорителя (String)
    Рисует прямоугольник и заполняет его информацией об ускорителе
    """
    pygame.draw.rect(screen, (0, 100, 0),
                     (left_upper_corner.x, left_upper_corner.y,
                     width, height), width=1)
    # Создаём строки для ускорителя
    Accelerator = font2.render("{0}: {1}".format(name_of_accelerator,
                               accelerations[name_of_accelerator]["amount"]),
                               True, (0, 100, 0))
    Accelerator_Cost = font2.render("Cost: {0}".format(
        accelerations[name_of_accelerator]["cost"]), True, (0, 100, 0))
    Accelerator_Speed = font2.render("Speed: {0}".format(
        accelerations[name_of_accelerator]["speed"]), True, (0, 100, 0))
    # Вставляем строки в наш прямоугольник по координатам в прямоугольнике
    screen.blit(Accelerator, (left_upper_corner.x + 5,
                              left_upper_corner.y + 5))
    screen.blit(Accelerator_Cost, (left_upper_corner.x + 5,
                                   left_upper_corner.y + 20))
    screen.blit(Accelerator_Speed, (left_upper_corner.x + 5,
                                    left_upper_corner.y + 35))
