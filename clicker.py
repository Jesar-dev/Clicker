import pygame
from Point import Point
from check_accelerators import check_accelerators
from draw_all_accelerators import draw_all_accelerators

HEIGHT_WINDOW = 480
WIDTH_WINDOW = 360
FPS = 30
RADIUS_CIRCLE = 50

# Создаём окно
pygame.init()
# Устанавливаем ширину и высоту окна
screen = pygame.display.set_mode((WIDTH_WINDOW, HEIGHT_WINDOW))
pygame.display.set_caption("Super Clicker")


# Скорость и количество очков
speed = 0
score = 0

clock = pygame.time.Clock()


f1 = pygame.font.Font(None, 36)
f2 = pygame.font.Font(None, 22)

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
# Время для ускорителей
time_elapsed_since_last_action = 0

game_running = True

while game_running:
    # Устанавливаем нужные нам кадры в секунду
    clock.tick(FPS)
    # Закрашиваем экран чёрным цветом
    screen.fill((0, 0, 0))
    # Засекаем время
    dt = clock.tick()
    for event in pygame.event.get():
        # Обрабатываем выход из игры
        if event.type == pygame.QUIT:
            game_running = False
        # Обрабатываем нажатие на клавишу
        if event.type == pygame.KEYDOWN:
            # Обрабатываем нажатие на пробел
            if event.key == pygame.K_SPACE:
                # Уменьшаем радиус круга на 5
                RADIUS_CIRCLE -= 5
                # Увеличиваем количество очков на 1
                score += 1
                # Рисуем получившийся круг
                pygame.draw.circle(screen, (255, 0, 0),
                                   (WIDTH_WINDOW//2, HEIGHT_WINDOW//2),
                                   RADIUS_CIRCLE)
                # Обновляем экран
                pygame.display.update()
        # Обрабатываем отпускание клавиши
        if event.type == pygame.KEYUP:
            # Обрабатываем отпускание пробела
            if event.key == pygame.K_SPACE:
                # Увеличиваем радиус круга обратно на 5
                RADIUS_CIRCLE += 5
                # Рисуем получившийся круг
                pygame.draw.circle(screen, (255, 0, 0),
                                   (WIDTH_WINDOW//2, HEIGHT_WINDOW//2),
                                   RADIUS_CIRCLE)
                # Обновляем экран
                pygame.display.update()
        # Обрабатываем нажатие на кнопку мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Проверяем что нажата левая кнопка мыши
            if event.button == 1:
                # Проверяем по координатам нажатия 0 - по ширине 1 - по длине
                x = event.pos[0]
                if x >= WIDTH_WINDOW - 120 and x <= WIDTH_WINDOW:
                    score_and_speed = [score, speed]
                    if event.pos[1] >= 100 and event.pos[1] <= 150:
                        # Проверяем что нам хватает очков
                        # для покупки ускорителя
                        score_and_speed = check_accelerators(accelerations,
                                                             "Schoolboy",
                                                             score, speed)
                    if event.pos[1] >= 155 and event.pos[1] <= 205:
                        score_and_speed = check_accelerators(accelerations,
                                                             "Teacher",
                                                             score, speed)
                    if event.pos[1] >= 210 and event.pos[1] <= 260:
                        score_and_speed = check_accelerators(accelerations,
                                                             "Director",
                                                             score, speed)
                    if event.pos[1] >= 265 and event.pos[1] <= 315:
                        score_and_speed = check_accelerators(accelerations,
                                                             "Einstein",
                                                             score, speed)
                    score = score_and_speed[0]
                    speed = score_and_speed[1]
    # Прибавляем время
    time_elapsed_since_last_action += dt
    if time_elapsed_since_last_action >= 3:
        # Прибавляем к очкам нашу скорость
        score += speed
        time_elapsed_since_last_action = 0
    pygame.display.update()
    # Создаём строки для очков и для скорости
    Score = f1.render("Your score is: {0}".format(str(score)),
                      True, (255, 255, 255))
    Speed = f1.render("Your speed is: {0}".format(str(speed)),
                      True, (255, 255, 255))

    # Создаём прямоугольники с ускорителями
    draw_all_accelerators(accelerations, f2, screen)

    # Рисуем на экране текст с очками и скоростью
    screen.blit(Score, (70, 50))
    screen.blit(Speed, (70, 20))

    # Рисуем наш круг
    pygame.draw.circle(screen, (255, 0, 0),
                       (WIDTH_WINDOW//2, HEIGHT_WINDOW//2), RADIUS_CIRCLE)

    pygame.display.flip()


pygame.quit()

