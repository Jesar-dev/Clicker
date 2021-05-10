import pygame
from draw_all_accelerators import draw_all_accelerators
from event_checker import event_checker
import param


# Создаём окно
pygame.init()
# Устанавливаем ширину и высоту окна
screen = pygame.display.set_mode((param.WIDTH_WINDOW, param.HEIGHT_WINDOW))
pygame.display.set_caption("Super Clicker")


# Скорость и количество очков
param.speed = 0
param.score = 0

clock = pygame.time.Clock()


font1 = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 22)

# Время для ускорителей
time_elapsed_since_last_action = 0

param.game_running = True

# Создаём объект класса event_checker
to_check_event = event_checker(screen)

while param.game_running:
    # Устанавливаем нужные нам кадры в секунду
    clock.tick(param.FPS)
    # Закрашиваем экран чёрным цветом
    screen.fill((0, 0, 0))
    # Засекаем время
    dt = clock.tick()

    for event in pygame.event.get():
        # При помощи сеттера добавляем в класс ивент
        to_check_event.event_setter(event)
        # Проверяем наш ивент
        to_check_event.event_check()
    # Прибавляем время

    time_elapsed_since_last_action += dt
    if time_elapsed_since_last_action >= 3:
        # Прибавляем к очкам нашу скорость
        param.score += param.speed
        time_elapsed_since_last_action = 0
    pygame.display.update()
    # Создаём строки для очков и для скорости
    Score = font1.render("Your score is: {0}".format(str(param.score)),
                         True, (255, 255, 255))
    Speed = font1.render("Your speed is: {0}".format(str(param.speed)),
                         True, (255, 255, 255))

    # Создаём прямоугольники с ускорителями
    draw_all_accelerators(param.accelerations, font2, screen)

    # Рисуем на экране текст с очками и скоростью
    screen.blit(Score, (70, 50))
    screen.blit(Speed, (70, 20))

    # Рисуем наш круг
    pygame.draw.circle(screen, (255, 0, 0),
                       (param.WIDTH_WINDOW//2, param.HEIGHT_WINDOW//2),
                       param.RADIUS_CIRCLE)

    pygame.display.flip()


pygame.quit()
