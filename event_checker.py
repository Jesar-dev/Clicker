import pygame
from check_accelerators import check_accelerators
import param


class event_checker:
    def __init__(self, screen):
        # На каком экране надо будет обновлять
        self.screen = screen

    # Сеттер для ивента
    def event_setter(self, event_type):
        self.event_type = event_type

    # Проверяем тип события
    def event_check(self):
        if self.event_type.type == pygame.QUIT:
            self.event_quit()
        if self.event_type.type == pygame.KEYDOWN:
            self.event_keydown(self.event_type.key)
        if self.event_type.type == pygame.KEYUP:
            self.event_keyup(self.event_type.key)
        if self.event_type.type == pygame.MOUSEBUTTONDOWN:
            self.event_mousebuttondown(self.event_type.button,
                                       self.event_type.pos)

    # Проверка выхода из игры
    def event_quit(self):
        param.game_running = False

    # Проверка нажатия на клавишу
    def event_keydown(self, key):
        if key == pygame.K_SPACE:
            # Уменьшаем радиус круга на 5
            param.RADIUS_CIRCLE -= 5
            # Увеличиваем количество очков на 1
            param.score += 1
            # Рисуем получившийся круг
            pygame.draw.circle(self.screen, (255, 0, 0),
                               (param.WIDTH_WINDOW//2, param.HEIGHT_WINDOW//2),
                               param.RADIUS_CIRCLE)
            # Обновляем экран
            pygame.display.update()

    # Проверка отжатия от клавиши
    def event_keyup(self, key):
        if key == pygame.K_SPACE:
            # Увеличиваем радиус круга обратно на 5
            param.RADIUS_CIRCLE += 5
            # Рисуем получившийся круг
            pygame.draw.circle(self.screen, (255, 0, 0),
                               (param.WIDTH_WINDOW//2, param.HEIGHT_WINDOW//2),
                               param.RADIUS_CIRCLE)
            # Обновляем экран
            pygame.display.update()

    # Проверка нажатия на кнопку мыши
    def event_mousebuttondown(self, button, pos):
        # Нажатие на левую кнопку мыши
        if button == 1:
            # Проверяем по координатам нажатия 0 - по ширине 1 - по длине
            x = pos[0]
            if x >= param.WIDTH_WINDOW - 120 and x <= param.WIDTH_WINDOW:
                score_and_speed = [param.score, param.speed]
                if pos[1] >= 100 and pos[1] <= 150:
                    # Проверяем что нам хватает очков
                    # для покупки ускорителя
                    score_and_speed = check_accelerators(param.accelerations,
                                                         "Schoolboy",
                                                         param.score,
                                                         param.speed)
                if pos[1] >= 155 and pos[1] <= 205:
                    score_and_speed = check_accelerators(param.accelerations,
                                                         "Teacher",
                                                         param.score,
                                                         param.speed)
                if pos[1] >= 210 and pos[1] <= 260:
                    score_and_speed = check_accelerators(param.accelerations,
                                                         "Director",
                                                         param.score,
                                                         param.speed)
                if pos[1] >= 265 and pos[1] <= 315:
                    score_and_speed = check_accelerators(param.accelerations,
                                                         "Einstein",
                                                         param.score,
                                                         param.speed)
                param.score = score_and_speed[0]
                param.speed = score_and_speed[1]
