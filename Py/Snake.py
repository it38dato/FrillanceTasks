# Разработка Snake.
import pygame, random, sys, time
"""print("hello")
def privet():
    error = pygame.init()
    if error[1]==0:
        print("Hello! It's been a rain, weather")
    else:
        print("error detected!")
        sys.exit()
privet()
#выводит, что было выполненно 6 команд, и 0 ошибок
"""
playSurface=pygame.display.set_mode((800,600)) # Создаем экран
pygame.display.set_caption("Snake") # Даем имя экрану
#time.sleep(56)
position=[50, 50] # Координаты змейки
body=[[80,50],[70,50],[60,50]] # Структура тела змейки
bait=[random.randrange(1,80)*10, random.randrange(1,60)*10] # Пища
baitVisible=True
fpsController=pygame.time.Clock()
direction='RIGHT' # Направление движения
changeto=direction # Изменение направления
score=0 # Игровой счет
"""
Нужно еще создать цвета, таблица цветов rgb - google
color=pygame.Color(r,b,a)
"""
white=pygame.Color(255,255,255) # Фон
black=pygame.Color(0,0,0) # Конец игры
red=pygame.Color(255,0,0) # Шрифт
green=pygame.Color(0,255,0) # Змейка
blue=pygame.Color(0,0,255)
lightslateblue=pygame.Color(132,112,255) # Пища для змейки
def gameOver():
    '''Сделаем надпись, которая будет появляться в конце игры.
    Чтобы несколько раз не писать pygame, мы объекту передаем дополнительные
    параметры'''

    gaOFont=pygame.font.SysFont('Garamond', 48)
    # Объект, который отвечает за шрифт, и то, какой будет шрифт
    gaOSurface=gaOFont.render('Game over!', True, white)
    """
    Здесь нужно было создать надпись GAMEOVER. Для этого мы используем Функцию render,
    которая отвечает за то, чтобы создать саму надпись
    """
    gaORectangular=gaOSurface.get_rect()
    gaORectangular.midtop=(400, 25) # Тут задаем координаты для надписи
    playSurface.blit(gaOSurface, gaORectangular)
    """ blit отвечает за то, что бы нарисовать 1 объект поверх другого, т.е.
    поверх gaOSurface нужно разместить gaORectangular
    """
    showScore(2) # Строим счетчик
    pygame.display.flip()
    """
    Выводим на экран воображаемые объекты. Если эту строку не писать, то мы увидим
    пустой экра. flip - прописывает то, что мы написали в коде
    """
    time.sleep(8) # Задержка
    pygame.quit()
    # Чтобы игра была завершена технически, нужно закончить pygame 
    sys.exit() # Чтобы закончить саму программу в Питоне
def showScore (choice=1):
    scoreFont=pygame.font.SysFont('Garamond', 24)
    scoreSurface=scoreFont.render('Score: {0}'.format(score), True, red)
    #   scoreSurface=scoreFont.render('Score:'+str(score), True, red)
    scoreRectangular=scoreSurface.get_rect()
    if choice==1:
        scoreRectangular.midtop=(50, 25)
    else:
        scoreRectangular.midtop=(400, 125)
    # Два варианта, которые будут позиционировать блок со шрифтом
    playSurface.blit(scoreSurface, scoreRectangular)
    pygame.display.flip()
    #                       Создаем осноной элемент игры
while True:
    """
    Сделаем бесконечную игру с помощью цикла.
    Игра ждет действие игрока, т.е. во время бесконечного цикла мы будем забирать
    событие event
    """
    for event in pygame.event.get(): # очередь событии, т.е. последовательности
    """
    Для работы с последовательностью, чтобы работать с каждым элементом в поисках
    элемента только с определенным типом. Поэтому используем цикл for
    """
        if event.type == pygame.QUIT:
# Мы каждый раз проверяем не хочет ли игрок выйти из игры
            pygame.guit()
            sys.exit()
# Если хочет игрок выйти, тогда мы закрываем программу
        elif event.type == pygame.KEYDOWN:
# Проверяем на нажатие клавиши, но мы должны посмотреть какую именно клавишу
            if event.key==pygame.K_RIGHT or event.key == ord('d'):
                changeto='RIGHT'
# Если K_RIGHT, то нужно изменить направление
# ord('d') - Кодировка клавиши - 100
            if event.key==pygame.K_LEFT or event.key == ord('a'):
                changeto='LEFT'
            if event.key==pygame.K_UP or event.key == ord('w'):
                changeto='UP'
            if event.key==pygame.K_DOWN or event.key == ord('d'):
                changeto='DOWN'
            if event.key==pygame.K_ESCAPE:
# и рассмотрим случаи, когда работает кнопка ESC
#               pygame.event.post(pygame.event.Event(QUIT))
# Для этого Сделаем метод post, чтобы отправить в очередь событие
                gameOver()
#                   Обработка направления движения змейки
"""
Что делать при смене определения направления движения. определение направления
движения влиеяет на положение Змейки на карте с координатами POSITION[50,50].
Т.е. direction будет влиять на значение Х или У
Мы должны прописать связку, которая образовывает changeto
Представим, что есть Змейка [][][]. Слева хвост, справа голова. и он сейчас
движется вправо, если игрок нажал RIGHT, а если вверх - UP, а это значит, что
голова будет находиться в других координатах
  []
[][]
а потом так
  []
  []
  []
т.е. голова вверху, а хвост внизу. Но если игрок нажмет в таком слуаче вниз, а
это неправильный ход. Сначала голова же должна повернуться, а потом уже внизу.
Именно это нужно сейчас прописать. Сделаем так, чтобы змея не меняла направление
в таких случаях
"""
    if direction != 'LEFT' and changeto == 'RIGHT':
        direction='RIGHT'
    if direction != 'RIGHT' and changeto == 'LEFT':
        direction = 'LEFT'
    if direction != 'UP' and changeto == 'DOWN':
        direction = 'DOWN'
    if direction != 'DOWN' and changeto == 'UP':
        direction = 'UP'
"""
Если направление движения не было вниз, а мы получили указание двигаться вверх,
то мы двигаемся вверх
"""
#                   Изменение позиции в зависимости от направления
    if direction == 'RIGHT':
        position[0] += 10
"""
Мы производим увеличение оси Х, обращаясь к элементу с индексом 0, т.к. Х идет по
этому индексу, а с индексом 1 - У. Поэтому мы меняем значение Х по списке на 10.
10 это то на что мы делим - длины, позиции, и т.д. кратное 10
"""
    if direction == 'LEFT':
        position[0] -= 10 # Влево, значит уменьшенное на 10
    if direction == 'UP':
        position[1] -= 10
    if direction == 'DOWN':
        position[1] += 10
# Тут надо еще учитывать, что оси Х и У в pygame, не такие ккак в математике
"""
Двигается змейка вправо и состоит из 3х блоков
[][][]
При каждом поедании нужно проверить съел ли он пищу (BAIT), и если съел -
увеличить его на один блок
[][][][]
Увлеличение будем осуществлять методом insert в начало списка. А дальше еда
исчезает, добавляется новый блок и пища появляется в другом месте. в новом теле
будем добавлять новый элемент, потом сразу проверим на совпадение координат тела
и координаты пищи. Если совпадение произошло, то будем оставлять новый добавленный
блок, если нет - просто удаляем
"""
#               Работа над длиной тела змейки, увеличение счета
    body.insert(0, list(position))
    if position[0]==bait[0] and position[1]==bait[1]:
        baitVisible=False
        score+=1
    else:
        body.pop() # pop - удаляет последний элемент из списка
#           Ввдимость пишем на карте
    if baitVisible== False:
# Проверим является пища не видимой, потому что она должна появиться сново
        baitVisible=True # Тут рисуем новую пищу
        bait = [random.randrange(1, 80) * 10, random.randrange(1, 60) * 10]  # primanka
# Тут рисуем пищу в другом координате. этот же код был наверху.
    playSurface.fill(white)
# у нас есть элемент поверхностный - PLAYSURFACE, сделаем белым    
"""
Но нам еще нужно прописать тело змейки (BODY, он  состоит из списка), мы можем
прописать эти элементы в списке по очереди, что делаем с помощью цикла for
"""
    for element in body:
        pygame.draw.rect(playSurface, green, pygame.Rect(element[0], element[1], 10, 10))
"""
В библиотеке pygame есть класс DRAW, в этом классе, есть метод RECT(Рисование
прямоугольника), мы передаем ему 3 элемента: поверхность, цвет, и еще 1 кдасс,
который тоже рисует прямоугольник. у него координата Х (element[0]), У, и
отдельно указываем ширину и высоту прямоугольника
"""
# рисуем пищу
    pygame.draw.rect(playSurface, lightslateblue, pygame.Rect(bait[0], bait[1], 10, 10))
# исправляем проблему, когда змейкка выходит за пределы экрана
    if position[0]>790 or position[0]<0:
        position[0]=400
    if position[1]>590 or position[1]<0:
        position[1]=300
# чтоб змейка себя не съела
    for element in body[1: ]:
        if position[0]==element[0] and position[1]==element[1]:
            position=[50,50] # координаты змейки
            body=[[80,50], [70,50], [60,50]] # структура тела змейки
    showScore()
# чтобы выполнилось функция SCRORE счетчик
    fpsController.tick(12)
# чтобы змейка двигаласчь по медленее
    pygame.display.flip()