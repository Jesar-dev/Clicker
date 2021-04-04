import pygame

HEIGHT = 480
WIDTH = 360
FPS = 30
RADIUS_CIRCLE = 50
# Создаём окно
pygame.init()
# Устанавливаем ширину и высоту окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Clicker")

clock = pygame.time.Clock()
# Скорость и количество очков
speed = 0
score = 0

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
									(WIDTH//2, HEIGHT//2), RADIUS_CIRCLE)
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
									(WIDTH//2, HEIGHT//2), RADIUS_CIRCLE)
				# Обновляем экран
				pygame.display.update()
		# Обрабатываем нажатие на кнопку мыши
		if event.type == pygame.MOUSEBUTTONDOWN:
			# Проверяем что нажата левая кнопка мыши
			if event.button == 1:
				# Проверяем по координатам нажатия 0 - по ширине 1 - по длине
				if (event.pos[0] >= WIDTH - 120 and event.pos[0] <= WIDTH):
					if (event.pos[1] >= 100 and event.pos[1] <= 150):
						# Проверяем наличие очков на покупку ускорителя
						if (score >= accelerations["Schoolboy"][2]):
							# Уменьшаем количество очков на стоимость ускорителя
							score -= accelerations["Schoolboy"][2]
							# Увеличиваем количество ускорителя
							accelerations["Schoolboy"][0] += 1
							# Увеличиваем общую скорость
							speed += accelerations["Schoolboy"][1]
					if (event.pos[1] >= 155 and event.pos[1] <= 205):
						if (score >= accelerations["Teacher"][2]):
							score -= accelerations["Teacher"][2]
							accelerations["Teacher"][0] += 1
							speed += accelerations["Teacher"][1]
					if (event.pos[1] >= 210 and event.pos[1] <= 260):
						if (score >= accelerations["Director"][2]):
							score -= accelerations["Director"][2]
							accelerations["Director"][0] += 1
							speed += accelerations["Director"][1]
					if (event.pos[1] >= 265 and event.pos[1] <= 315):
						if (score >= accelerations["Einstein"][2]):
							score -= accelerations["Einstein"][2]
							accelerations["Einstein"][0] += 1
							speed += accelerations["Einstein"][1]
	# Прибавляем время
	time_elapsed_since_last_action += dt
	if (time_elapsed_since_last_action >= 3):
		# Прибавляем к очкам нашу скорость
		score += speed
		time_elapsed_since_last_action = 0
	pygame.display.update()
	# Создаём строки для очков и для скорости
	Score = f1.render("Your score is: {0}".format(str(score)),
		              True, (255, 255, 255))
	Speed = f1.render("Your speed is: {0}".format(str(speed)),
					  True, (255, 255, 255))

	# Создаём прямоугольник для первого ускорителя
	pygame.draw.rect(screen, (0, 100, 0), 
		             (WIDTH - 120, 100, 120, 50), width=1)
	# Создаём строки для первого ускорителя
	Schoolboy = f2.render("Schoolboy: {0}".format(
		accelerations["Schoolboy"][0]), True, (0, 100, 0))
	Schoolboy_Cost = f2.render("Cost: {0}".format(
		accelerations["Schoolboy"][2]), True, (0, 100, 0))
	Schoolboy_Speed = f2.render("Speed: {0}".format(
		accelerations["Schoolboy"][1]), True, (0, 100, 0))
	# Вставляем строки в наш прямоугольник по координатам на экране
	screen.blit(Schoolboy, (WIDTH - 115, 105))
	screen.blit(Schoolboy_Cost, (WIDTH - 115, 120))
	screen.blit(Schoolboy_Speed, (WIDTH - 115, 135))

	# Аналогично с первым ускорителем
	pygame.draw.rect(screen, (0, 100, 0), 
		             (WIDTH - 120, 155, 120, 50), width=1)
	Teacher = f2.render("Teacher: {0}".format(
		accelerations["Teacher"][0]), True, (0, 100, 0))
	Teacher_Cost = f2.render("Cost: {0}".format(
		accelerations["Teacher"][2]), True, (0, 100, 0))
	Teacher_Speed = f2.render("Speed: {0}".format(
		accelerations["Teacher"][1]), True, (0, 100, 0))
	screen.blit(Teacher, (WIDTH - 115, 160))
	screen.blit(Teacher_Cost, (WIDTH - 115, 175))
	screen.blit(Teacher_Speed, (WIDTH - 115, 190))

	# Аналогично
	pygame.draw.rect(screen, (0, 100, 0), 
		             (WIDTH - 120, 210, 120, 50), width=1)
	Director = f2.render("Director: {0}".format(
		accelerations["Director"][0]), True, (0, 100, 0))
	Director_Cost = f2.render("Cost: {0}".format(
		accelerations["Director"][2]), True, (0, 100, 0))
	Director_Speed = f2.render("Speed: {0}".format(
		accelerations["Director"][1]), True, (0, 100, 0))
	screen.blit(Director, (WIDTH - 115, 215))
	screen.blit(Director_Cost, (WIDTH - 115, 230))
	screen.blit(Director_Speed, (WIDTH - 115, 245))

	# Аналогично
	pygame.draw.rect(screen, (0, 100, 0), 
		             (WIDTH - 120, 265, 120, 50), width=1)
	Einstein = f2.render("Einstein: {0}".format(
		accelerations["Einstein"][0]), True, (0, 100, 0))
	Einstein_Cost = f2.render("Cost: {0}".format(
		accelerations["Einstein"][2]), True, (0, 100, 0))
	Einstein_Speed = f2.render("Speed: {0}".format(
		accelerations["Einstein"][1]), True, (0, 100, 0))
	screen.blit(Einstein, (WIDTH - 115, 270))
	screen.blit(Einstein_Cost, (WIDTH - 115, 285))
	screen.blit(Einstein_Speed, (WIDTH - 115, 300))

	# Рисуем на экране текст с очками и скоростью
	screen.blit(Score, (70, 50))
	screen.blit(Speed, (70, 20))
	# Рисуем наш круг
	pygame.draw.circle(screen, (255, 0, 0),
						(WIDTH//2, HEIGHT//2), RADIUS_CIRCLE)

	pygame.display.flip()


pygame.quit()
