# Разработка Тетрис.
import pygame as pg
import random, time, sys
from pygame.locals import *
#Затем определяем основные константы – кадровую частоту fps, высоту и ширину окна программы, размер базового элемента фигур-букв block (20 х 20 пикселей), параметры стакана, символ для обозначения пустых ячеек на игровом поле:
fps = 25
window_w, window_h = 600, 500
block, cup_h, cup_w = 20, 20, 10
#Параметры side_freq и down_freq задают время, которое затрачивается на перемещение фигуры в сторону или вниз, если игрок удерживает клавишу нажатой:
side_freq, down_freq = 0.15, 0.1
#Для размещения стакана и информационных надписей, а также для конвертации координат нам также понадобятся константы side_margin и top_margin – первая задает дистанцию между правой и левой сторонами окна программы и стаканом; вторая определяет расстояние между верхней границей стакана и окном:
side_margin = int((window_w - cup_w * block) / 2)
top_margin = window_h - (cup_h * block) - 5
#Цвета фигур задаются двумя кортежами: colors и lightcolors. Последний включает чуть более светлые оттенки тех же цветов, что и colors – для создания псевдо 2.5 D эффекта.
colors = ((0, 0, 225), (0, 225, 0), (225, 0, 0), (225, 225, 0)) # синий, зеленый, красный, желтый
lightcolors = ((30, 30, 255), (50, 255, 50), (255, 30, 30), (255, 255, 30)) # светло-синий, светло-зеленый, светло-красный, светло-желтый
white, gray, black  = (255, 255, 255), (185, 185, 185), (0, 0, 0)
brd_color, bg_color, txt_color, title_color, info_color = white, black, white, colors[3], colors[0]
#Поскольку каждая фигура состоит из 4 блоков, размер шаблона должен быть 5 х 5: 
fig_w, fig_h = 5, 5
empty = 'o'
#Поскольку каждую фигуру-букву можно поворачивать на 90 градусов, все возможные варианты поворотов описаны в словаре figures с помощью вложенных списков, элементы которых состоят из строк: символом x отмечены занятые ячейки, o – пустые. Количество вращений зависит от формы буквы: у O, к примеру, будет всего один вариант:
figures = {'S': [['ooooo',
                  'ooooo',
                  'ooxxo',
                  'oxxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxxo',
                  'oooxo',
                  'ooooo']],
           'Z': [['ooooo',
                  'ooooo',
                  'oxxoo',
                  'ooxxo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'oxxoo',
                  'oxooo',
                  'ooooo']],
           'J': [['ooooo',
                  'oxooo',
                  'oxxxo',
                  'ooooo',
                  'ooooo'],
                 ['ooooo',
                  'ooxxo',
                  'ooxoo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'oxxxo',
                  'oooxo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxoo',
                  'oxxoo',
                  'ooooo']],
           'L': [['ooooo',
                  'oooxo',
                  'oxxxo',
                  'ooooo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxoo',
                  'ooxxo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'oxxxo',
                  'oxooo',
                  'ooooo'],
                 ['ooooo',
                  'oxxoo',
                  'ooxoo',
                  'ooxoo',
                  'ooooo']],
           'I': [['ooxoo',
                  'ooxoo',
                  'ooxoo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'xxxxo',
                  'ooooo',
                  'ooooo']],
           'O': [['ooooo',
                  'ooooo',
                  'oxxoo',
                  'oxxoo',
                  'ooooo']],
           'T': [['ooooo',
                  'ooxoo',
                  'oxxxo',
                  'ooooo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxxo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'oxxxo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'oxxoo',
                  'ooxoo',
                  'ooooo']]}
#Заливку сплошным цветом реализовать очень просто, но полупрозрачную заставку сделать сложнее – как ни странно, метод draw в Pygame до сих пор не поддерживает эту опцию. Есть несколько способов решения этой проблемы. Мы воспользуемся методом, который предусматривает создание дополнительной поверхности с попиксельным альфа-смешением, и последующую заливку экрана паузы цветом с наложением на поверхность окна игры:
def pauseScreen():
    pause = pg.Surface((600, 500), pg.SRCALPHA)
    pause.fill((0, 0, 255, 127))
    display_surf.blit(pause, (0, 0))
#Эта функция отвечает за создание нескольких дополнительных глобальных констант, инициализирует модуль Pygame, рисует стартовое окно игры, вызывает запуск Тетриса runTetris() и в случае необходимости отображает сообщение о проигрыше:
def main():
    global fps_clock, display_surf, basic_font, big_font
    pg.init()
    fps_clock = pg.time.Clock()
    display_surf = pg.display.set_mode((window_w, window_h))
    basic_font = pg.font.SysFont('arial', 20)
    big_font = pg.font.SysFont('verdana', 45)
    pg.display.set_caption('Тетрис Lite')
    showText('Тетрис Lite')
    while True: # начинаем игру
        runTetris()
        pauseScreen()
        showText('Игра закончена')
#Код игры располагается в функции runTetris():
def runTetris():
    cup = emptycup()
    last_move_down = time.time()
    last_side_move = time.time()
    last_fall = time.time()
    going_down = False
    going_left = False
    going_right = False
    points = 0
    level, fall_speed = calcSpeed(points)
    fallingFig = getNewFig()
    nextFig = getNewFig()
    #Основной цикл обрабатывает все основные события, связанные с генерацией фигур, движением вниз и показом следующей фигуры:
    while True: 
        if fallingFig == None:
            # если нет падающих фигур, генерируем новую
            fallingFig = nextFig
            nextFig = getNewFig()
            last_fall = time.time()
            if not checkPos(cup, fallingFig):
                return # если на игровом поле нет свободного места - игра закончена
        quitGame()
        for event in pg.event.get(): 
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    pauseScreen()
                    showText('Пауза')
                    last_fall = time.time()
                    last_move_down = time.time()
                    last_side_move = time.time()
                #Цикл обрабатывает паузу и определяет момент, когда пользователь нажимает и отпускает клавиши со стрелками. Если клавиши →, ← и ↓ не нажаты, значения соответствующих переменных меняются на False:
                elif event.key == K_LEFT:
                    going_left = False
                elif event.key == K_RIGHT:
                    going_right = False
                elif event.key == K_DOWN:
                    going_down = False
            #Управление движением фигур происходит в ветке elif event.type == KEYDOWN: если нажата клавиша со стрелкой и функция checkPos() возвращает True, положение фигуры изменяется на один блок в соответствующем направлении:
            elif event.type == KEYDOWN:
                if event.key == K_LEFT and checkPos(cup, fallingFig, adjX=-1):
                    fallingFig['x'] -= 1
                    going_left = True
                    going_right = False
                    last_side_move = time.time()
                elif event.key == K_RIGHT and checkPos(cup, fallingFig, adjX=1):
                    fallingFig['x'] += 1
                    going_right = True
                    going_left = False
                    last_side_move = time.time()                    
                # поворачиваем фигуру, если есть место
                elif event.key == K_UP:
                    fallingFig['rotation'] = (fallingFig['rotation'] + 1) % len(figures[fallingFig['shape']])
                    #При нажатии ↑ происходит вращение фигуры – варианты берутся из словаря figures. Чтобы не получить ошибку IndexError: list index out of range, мы используем конструкцию, которая обнуляет индекс элемента, когда инкремент достигает максимального значения: fallingFig['rotation'] + 1) % len(figures[fallingFig['shape']]. Если функция checkPos() сообщает, что очередное вращение невозможно из-за того, что фигура натыкается на какой-то блок, нужно вернуться к предыдущему варианту из списка:
                    if not checkPos(cup, fallingFig):
                        fallingFig['rotation'] = (fallingFig['rotation'] - 1) % len(figures[fallingFig['shape']])
                #Для ускорения падения игрок нажимает и удерживает клавишу ↓:
                elif event.key == K_DOWN:
                    going_down = True
                    if checkPos(cup, fallingFig, adjY=1):
                        fallingFig['y'] += 1
                    last_move_down = time.time()
                #Если пользователь хочет мгновенно сбросить фигуру на дно, он может нажать Enter. Цикл for здесь определяет максимально низкую свободную позицию в стакане:
                elif event.key == K_RETURN:
                	going_down = False
                	going_left = False
                	going_right = False
                	for i in range(1, cup_h):
                    	    if not checkPos(cup, fallingFig, adjY=i):
                      	        break
                	fallingFig['y'] += i - 1
        #Чтобы определить, удерживает ли пользователь клавишу движения, программа использует условия:
        if (going_left or going_right) and time.time() - last_side_move > side_freq:
            if going_left and checkPos(cup, fallingFig, adjX=-1):
                fallingFig['x'] -= 1
            elif going_right and checkPos(cup, fallingFig, adjX=1):
                fallingFig['x'] += 1
            last_side_move = time.time()
        if going_down and time.time() - last_move_down > down_freq and checkPos(cup, fallingFig, adjY=1):
            fallingFig['y'] += 1
            last_move_down = time.time()
        #Если пользователь никак не вмешивается в управление фигурой, движение вниз происходит так:
        if time.time() - last_fall > fall_speed: # свободное падение фигуры
            if not checkPos(cup, fallingFig, adjY=1): # проверка "приземления" фигуры
                addToCup(cup, fallingFig) # фигура приземлилась, добавляем ее в содержимое стакана
                points += clearCompleted(cup)
                level, fall_speed = calcSpeed(points)
                fallingFig = None
            else: # фигура пока не приземлилась, продолжаем движение вниз
                fallingFig['y'] += 1
                last_fall = time.time()
        #Функцию runTetris() завершает набор функций, обеспечивающих отрисовку игрового поля, вывод названия игры, падающей и следующих фигур, а также информационных надписей:
        display_surf.fill(bg_color)
        drawTitle()
        gamecup(cup)
        drawInfo(points, level)
        drawnextFig(nextFig)
        if fallingFig != None:
            drawFig(fallingFig)
        pg.display.update()
        fps_clock.tick(fps)
#ункция txtObjects() принимает текст, шрифт и цвет, и с помощью метода render() возвращает готовые объекты Surface (поверхность) и Rect (прямоугольник). Эти объекты в дальнейшем обрабатываются методом blitв функции showText(), выводящей информационные надписи и название игры.
def txtObjects(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()
#Выход из игры обеспечивает функция stopGame(), в которой используется sys.exit() из импортированного в начале кода модуля sys.
def stopGame():
    pg.quit()
    sys.exit()
def checkKeys():
    quitGame()
    for event in pg.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None
def showText(text):
    titleSurf, titleRect = txtObjects(text, big_font, title_color)
    titleRect.center = (int(window_w / 2) - 3, int(window_h / 2) - 3)
    display_surf.blit(titleSurf, titleRect)
    pressKeySurf, pressKeyRect = txtObjects('Нажмите любую клавишу для продолжения', basic_font, title_color)
    pressKeyRect.center = (int(window_w / 2), int(window_h / 2) + 100)
    display_surf.blit(pressKeySurf, pressKeyRect)
    while checkKeys() == None:
        pg.display.update()
        fps_clock.tick()
def quitGame():
    for event in pg.event.get(QUIT): # проверка всех событий, приводящих к выходу из игры
        stopGame() 
    for event in pg.event.get(KEYUP): 
        if event.key == K_ESCAPE:
            stopGame() 
        pg.event.post(event) 
def calcSpeed(points):
    # вычисляет уровень
    level = int(points / 10) + 1
    fall_speed = 0.27 - (level * 0.02)
    return level, fall_speed
def getNewFig():
    # возвращает новую фигуру со случайным цветом и углом поворота
    shape = random.choice(list(figures.keys()))
    newFigure = {'shape': shape,
                'rotation': random.randint(0, len(figures[shape]) - 1),
                'x': int(cup_w / 2) - int(fig_w / 2),
                'y': -2, 
                'color': random.randint(0, len(colors)-1)}
    return newFigure
#За добавление фигур к содержимому стакана отвечает addToCup():
def addToCup(cup, fig):
    for x in range(fig_w):
        for y in range(fig_h):
            if figures[fig['shape']][fig['rotation']][y][x] != empty:
                cup[x + fig['x']][y + fig['y']] = fig['color']
#Пустой стакан создается функцией emptycup():
def emptycup():
    # создает пустой стакан
    cup = []
    for i in range(cup_w):
        cup.append([empty] * cup_h)
    return cup
def incup(x, y):
    return x >= 0 and x < cup_w and y < cup_h
#Функция checkPos() следит за тем, чтобы падающая фигура оставалась в пределах игрового поля и не накладывалась на предыдущие. На примере слева фигура остается в допустимой области, на примере справа – ошибочно накладывается на предыдущую. Чтобы определить положение фигуры в стакане, нужно суммировать собственные координаты фигуры со «стаканными»:
def checkPos(cup, fig, adjX=0, adjY=0):
    # проверяет, находится ли фигура в границах стакана, не сталкиваясь с другими фигурами
    for x in range(fig_w):
        for y in range(fig_h):
            abovecup = y + fig['y'] + adjY < 0
            if abovecup or figures[fig['shape']][fig['rotation']][y][x] == empty:
                continue
            if not incup(x + fig['x'] + adjX, y + fig['y'] + adjY):
                return False
            if cup[x + fig['x'] + adjX][y + fig['y'] + adjY] != empty:
                return False
    return True
#За обнаружение и удаление заполненных рядов отвечает функция clearCompleted() вместе со вспомогательной isCompleted(). Если isCompleted() возвращает True, программе нужно последовательно переместить вниз все ряды, располагающиеся над удаляемым, после чего заполнить нулевой ряд empty-значениями о:
def isCompleted(cup, y):
    # проверяем наличие полностью заполненных рядов
    for x in range(cup_w):
        if cup[x][y] == empty:
            return False
    return True
def clearCompleted(cup):
    # Удаление заполенных рядов и сдвиг верхних рядов вниз
    removed_lines = 0
    y = cup_h - 1
    while y >= 0:
        if isCompleted(cup, y):
           for pushDownY in range(y, 0, -1):
                for x in range(cup_w):
                    cup[x][pushDownY] = cup[x][pushDownY-1]
           for x in range(cup_w):
                cup[x][0] = empty
           removed_lines += 1
        else:
            y -= 1
    return removed_lines
def convertCoords(block_x, block_y):
    return (side_margin + (block_x * block)), (top_margin + (block_y * block))
#Каждая фигура состоит из 4 элементов – блоков. Блоки рисует функция drawBlock(), которая получает координаты из convertCoords():
def drawBlock(block_x, block_y, color, pixelx=None, pixely=None):
    #отрисовка квадратных блоков, из которых состоят фигуры
    if color == empty:
        return
    if pixelx == None and pixely == None:
        pixelx, pixely = convertCoords(block_x, block_y)
    pg.draw.rect(display_surf, colors[color], (pixelx + 1, pixely + 1, block - 1, block - 1), 0, 3)
    pg.draw.rect(display_surf, lightcolors[color], (pixelx + 1, pixely + 1, block - 4, block - 4), 0, 3)
    pg.draw.circle(display_surf, colors[color], (pixelx + block / 2, pixely + block / 2), 5)
def gamecup(cup):
    # граница игрового поля-стакана
    pg.draw.rect(display_surf, brd_color, (side_margin - 4, top_margin - 4, (cup_w * block) + 8, (cup_h * block) + 8), 5)
    # фон игрового поля
    pg.draw.rect(display_surf, bg_color, (side_margin, top_margin, block * cup_w, block * cup_h))
    for x in range(cup_w):
        for y in range(cup_h):
            drawBlock(x, y, cup[x][y])
def drawTitle():
    titleSurf = big_font.render('Тетрис Lite', True, title_color)
    titleRect = titleSurf.get_rect()
    titleRect.topleft = (window_w - 425, 30)
    display_surf.blit(titleSurf, titleRect)
def drawInfo(points, level):
    pointsSurf = basic_font.render(f'Баллы: {points}', True, txt_color)
    pointsRect = pointsSurf.get_rect()
    pointsRect.topleft = (window_w - 550, 180)
    display_surf.blit(pointsSurf, pointsRect)
    levelSurf = basic_font.render(f'Уровень: {level}', True, txt_color)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (window_w - 550, 250)
    display_surf.blit(levelSurf, levelRect)
    pausebSurf = basic_font.render('Пауза: пробел', True, info_color)
    pausebRect = pausebSurf.get_rect()
    pausebRect.topleft = (window_w - 550, 420)
    display_surf.blit(pausebSurf, pausebRect)
    escbSurf = basic_font.render('Выход: Esc', True, info_color)
    escbRect = escbSurf.get_rect()
    escbRect.topleft = (window_w - 550, 450)
    display_surf.blit(escbSurf, escbRect)
def drawFig(fig, pixelx=None, pixely=None):
    figToDraw = figures[fig['shape']][fig['rotation']]
    if pixelx == None and pixely == None:    
        pixelx, pixely = convertCoords(fig['x'], fig['y'])
    #отрисовка элементов фигур
    for x in range(fig_w):
        for y in range(fig_h):
            if figToDraw[y][x] != empty:
                drawBlock(None, None, fig['color'], pixelx + (x * block), pixely + (y * block))
def drawnextFig(fig):  # превью следующей фигуры
    nextSurf = basic_font.render('Следующая:', True, txt_color)
    nextRect = nextSurf.get_rect()
    nextRect.topleft = (window_w - 150, 180)
    display_surf.blit(nextSurf, nextRect)
    drawFig(fig, pixelx=window_w-150, pixely=230)
if __name__ == '__main__':
    main()