import pygame
from Point import Point


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

# def decresse_score(val)
# 	score -= val if score >= accelerations[name_of_acc][2]

# def increase_speed(val)


def check_accelerators(name_of_acc, score, speed):
	"""
	name_of_acc - название ускорителя (string)
	Проверка при нажатии на ускоритель, есть ли необходимое количество очков на покупку
	в случае удачи отнять необходимое количество очков и добавить скорость производства
	"""
	if score >= accelerations[name_of_acc][2]:
		score -= accelerations[name_of_acc][2]
		accelerations[name_of_acc][0] += 1
		speed += accelerations[name_of_acc][1]
	return [score, speed]

def rect_accelerators(left_upper_corner, width, height, name_of_acc):
	"""
	left_upper_corner - координаты точки левого угла прямоугольника (объект класса Point)
	width - ширина прямоугольника (int)
	height - высота прямоугольника (int)
	name_of_acc - название ускорителя (String)
	Рисует прямоугольник и заполняет его информацией об ускорителе
	"""
	pygame.draw.rect(screen, (0, 100, 0), 
		             (left_upper_corner.x, left_upper_corner.y, width, height), width=1)
	# Создаём строки для ускорителя
	Accelerator = f2.render("{0}: {1}".format(name_of_acc,
		accelerations[name_of_acc][0]), True, (0, 100, 0))
	Accelerator_Cost = f2.render("Cost: {0}".format(
		accelerations[name_of_acc][2]), True, (0, 100, 0))
	Accelerator_Speed = f2.render("Speed: {0}".format(
		accelerations[name_of_acc][1]), True, (0, 100, 0))
	# Вставляем строки в наш прямоугольник по координатам в прямоугольнике
	screen.blit(Accelerator, (left_upper_corner.x + 5, left_upper_corner.y + 5))
	screen.blit(Accelerator_Cost, (left_upper_corner.x + 5, left_upper_corner.y + 20))
	screen.blit(Accelerator_Speed, (left_upper_corner.x + 5, left_upper_corner.y + 35))



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
									(WIDTH_WINDOW//2, HEIGHT_WINDOW//2), RADIUS_CIRCLE)
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
									(WIDTH_WINDOW//2, HEIGHT_WINDOW//2), RADIUS_CIRCLE)
				# Обновляем экран
				pygame.display.update()
		# Обрабатываем нажатие на кнопку мыши
		if event.type == pygame.MOUSEBUTTONDOWN:
			# Проверяем что нажата левая кнопка мыши
			if event.button == 1:
				# Проверяем по координатам нажатия 0 - по ширине 1 - по длине
				if event.pos[0] >= WIDTH_WINDOW - 120 and event.pos[0] <= WIDTH_WINDOW:
					if event.pos[1] >= 100 and event.pos[1] <= 150:
						score_and_speed = check_accelerators("Schoolboy", score, speed)
						score = score_and_speed[0]
						speed = score_and_speed[1]
					if event.pos[1] >= 155 and event.pos[1] <= 205:
						score_and_speed = check_accelerators("Teacher", score, speed)
						score = score_and_speed[0]
						speed = score_and_speed[1]
					if event.pos[1] >= 210 and event.pos[1] <= 260:
						score_and_speed = check_accelerators("Director", score, speed)
						score = score_and_speed[0]
						speed = score_and_speed[1]
					if event.pos[1] >= 265 and event.pos[1] <= 315:
						score_and_speed = check_accelerators("Einstein", score, speed)
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

	# Создаём прямоугольник с первым ускорителем
	left_upper_corner_rect = Point(WIDTH_WINDOW - 120, 100)
	width_rect = 120
	height_rect = 50
	rect_accelerators(left_upper_corner_rect, width_rect, height_rect, "Schoolboy")

	# Со вторым ускорителем
	left_upper_corner_rect = Point(WIDTH_WINDOW - 120, 155)
	rect_accelerators(left_upper_corner_rect, width_rect, height_rect, "Teacher")

	# Третий ускоритель
	left_upper_corner_rect = Point(WIDTH_WINDOW - 120, 210)
	rect_accelerators(left_upper_corner_rect, width_rect, height_rect, "Director")

	# Аналогично 4 ускоритель
	left_upper_corner_rect = Point(WIDTH_WINDOW-120, 265)
	rect_accelerators(left_upper_corner_rect, width_rect, height_rect, "Einstein")

	# Рисуем на экране текст с очками и скоростью
	screen.blit(Score, (70, 50))
	screen.blit(Speed, (70, 20))

	# Рисуем наш круг
	pygame.draw.circle(screen, (255, 0, 0),
						(WIDTH_WINDOW//2, HEIGHT_WINDOW//2), RADIUS_CIRCLE)

	pygame.display.flip()


pygame.quit()