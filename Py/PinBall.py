# Разработка Pin Ball.
#1) создать поле
from tkinter import *#1
import random #44) Содаем отскок
WIDTH=900#2 настройки окна глоб переменная
HEIGHT=300#3 настройки окна глоб переменная
PAD_W=10#ракетка
PAD_H=100#ракетка
BALL_RADIUS=40#мяч
#15) двигаем мяч
BALL_X_CHANCGE=20#16 переменная для скорости мяча, горизонтально и вертикально
BALL_Y_CHANCGE=0#16
root=Tk()#7
root.title("Ping-pong")#8
c=Canvas(root,
         width=WIDTH,
         height=HEIGHT,
         background="#008B8B")#9 создаем область, в котором все это делается
c.pack()#10 ставим наш канвас
c.create_line(PAD_W,
              0,
              PAD_W,
              HEIGHT,
              fill="white")#11 Сделаем левую и правую ракетку на поле, мяч и линию, он будет касаться
c.create_line(WIDTH-PAD_W,
              0,
              WIDTH-PAD_W,
              HEIGHT,
              fill="white")#11 Вычитаем, потому что с обратной стороны, для правой ракетки
c.create_line(WIDTH/2,
              0,
              WIDTH/2,
              HEIGHT,
              fill="white")#12 сделаем линию, которая разделяет игровое поле
BALL=c.create_oval(WIDTH/2-BALL_RADIUS/2,
                   HEIGHT/2-BALL_RADIUS/2,
                   WIDTH/2+BALL_RADIUS/2,
                   HEIGHT/2+BALL_RADIUS/2, fill="#FF4500")#13 создаем мяч
LEFT_PAD=c.create_line(PAD_W/2,
                       0,
                       PAD_W/2,
                       PAD_H,
                       width=PAD_W,
                       fill="#DA70D6")#13 создаем левую и правую ракетку, чтоб они просто были
RIGHT_PAD=c.create_line(WIDTH-PAD_W/2,
                        0,
                        WIDTH-PAD_W/2,
                        PAD_H,
                        width=PAD_W,
                        fill="#DA70D6")#13
PLAYER1_SCORE=0#66) считаем очки и возвращаем мяч на изначальную точку
PLAYER2_SCORE=0
#68 нужны функции смена счета и функции смены положения мяча
INITIAL_SPEED=20#69 переменная для счета скорости
p_1_text=c.create_text(WIDTH-WIDTH/6,
                       PAD_H/4,
                       text=PLAYER1_SCORE,
                       font='Arial 20',
                       fill='aqua')#67 создаем текст очков
p_2_text=c.create_text(WIDTH/6,
                       PAD_H/4,
                       text=PLAYER2_SCORE,
                       font='Arial 20',
                       fill='aqua')
#22) создаем упраление ракетами
PAD_SPEED=20#23 задаем сначала общую скорость ракетки
LEFT_PAD_SPEED=0#24  скорость левой и правой ракетки, задаем 0, ибо изначально она не двигается
RIGHT_PAD_SPEED=0#24
BALL_SPEED_UP=1.00#45 скорость мяча с каждым ударом
BALL_MAX_SPEED=30#46 максимальная скорость мяча
BALL_X_SPEED=20#47 начальная скорость по горизонтали
BALL_Y_SPEED=20#48 po vertikali
right_line_distance=WIDTH-PAD_W#49 расстояние да правого края
def update_score(player):#70  создадим функцию, которая будет обнвлять счет
    global PLAYER1_SCORE, PLAYER2_SCORE
    if player=='right':
        PLAYER1_SCORE+=1
        c.itemconfig(p_1_text, text=PLAYER1_SCORE)
    else:
        PLAYER2_SCORE+=1
        c.itemconfig(p_2_text, text=PLAYER2_SCORE)
def spawn_ball():#71 respoun
    global BALL_X_SPEED#72
    c.coords(BALL,
             WIDTH/2-BALL_RADIUS/2,
             HEIGHT/2-BALL_RADIUS/2,
             WIDTH/2+BALL_RADIUS/2,
             HEIGHT/2+BALL_RADIUS/2)#73
    BALL_X_SPEED=-(BALL_X_SPEED*INITIAL_SPEED)/abs(BALL_X_SPEED)#74
def bounce(actiom):#50 напишем функию, которая будет отскакиать мяч
    global BALL_X_SPEED, BALL_Y_SPEED#51 переменные, которые понадобятся для мяча
    if actiom=='strike':#52 если ужарим ракеткй, то мы повернем в случайном направлении от -10 дo +10
        BALL_Y_SPEED=random.randrange(-10, 10)#52
        if abs(BALL_X_SPEED)<BALL_MAX_SPEED:#53 и если скорость мяча < скорости максимального мяча, то мы эту скорость увеличим
            BALL_X_SPEED *= -BALL_SPEED_UP
        else:#54 иначе оставляем ее на месте
            BALL_X_SPEED= -BALL_X_SPEED
    else:#55
        BALL_Y_SPEED= -BALL_Y_SPEED#56
def move_ball():#17 Сделаем функцию движения мяча
    #57c.move(BALL, BALL_X_CHANCGE, BALL_Y_CHANCGE)#18 двигаем мяча по определенному скорости
    ball_left, ball_top, ball_right, ball_bot=c.coords(BALL) # 58 нужно переписать движение мяча с учетом движения, которое мы написали в функции bounce. то есть нужно определять координаты мяча oт центра
    ball_center=(ball_top+ball_bot)/2#59 теперь нужно это все определеить, например центр
    if ball_right + BALL_X_SPEED < right_line_distance and  ball_left +BALL_X_SPEED > PAD_W:#60 теперь нужно сделатьь так, чтоб вертикально отскакивал
        c.move(BALL, BALL_X_SPEED, BALL_Y_SPEED)#61 тогда двигаем дальше
    elif ball_right==right_line_distance or ball_left==PAD_W:#62 проверяем, проверим какой именно стороны поля мы коснулись, если правой стороны -сравниваем позицию центра мяча, и если мяч в пределах ракетки, то делаем отскок
        if ball_right>WIDTH/2:
            if c.coords(RIGHT_PAD)[1]<ball_center<c.coords(RIGHT_PAD)[3]:
                bounce('strike')#63 тогда мы делаем отскок
            else:
                #76pass
                update_score('left')#77
                spawn_ball()#78
        else:
            if c.coords(LEFT_PAD)[1]<ball_center<c.coords(LEFT_PAD)[3]:
                bounce('strike')#63 тогда мы делаем отскок
            else:
                #76pass
                update_score('right')#77
                spawn_ball()#78    else:#64 теперь нужно проверить момент, когда мяч выходит за пределы игрового поля
    else:
        if ball_right > WIDTH/2:
            c.move(BALL,
                   right_line_distance-ball_right,
                   BALL_Y_SPEED)
        else:
            c.move(BALL,
                   -ball_left+PAD_W,
                   BALL_Y_SPEED)
    if ball_top+BALL_Y_SPEED<0 or ball_bot+BALL_Y_SPEED>HEIGHT:
        bounce('ricochet')
        #65 на экране мы должны увидеть отскок
def move_pads():#25 напишим функию двжиения обих ракеток сразу
    PADS={LEFT_PAD: LEFT_PAD_SPEED,
          RIGHT_PAD: RIGHT_PAD_SPEED}#26 нужно сделать так чтоб левая ракеткка двигалась ско скорость левой ракеткой, а праввая - правой. для этого создаим словарик
    for pad in PADS:#27 теперь нужно перебррать ракетки, и двигать с заданной скоростью, черех цикл FOR
        c.move(pad, 0, PADS[pad])#27
        if c.coords(pad)[1]<0:#28 Если ракетка входит выше поля, то мы ее возращаем на место
            c.move(pad, 0, -c.coords(pad)[1])#29 отталкиваем нашу ракетку
        elif c.coords(pad)[3]>HEIGHT:#30 если снизу, то отталкиваем вниз
            c.move(pad, 0, HEIGHT-c.coords(pad)[3])#30
def main():#19  main вызывает функию move_ball при помощи рекурсии
    move_ball()#19
    move_pads()# 31 вставим move_pads в функцию main,  чтоб когда мы вызывали эту функциюу нас не только летел, но идвигались наши ракетки
    root.after(30, main)#20
c.focus_get()#32 фокус на сanvas, чтоб реагировал на нажатие клавиши
def moveent_hadeler(event):#33 функция обработки нажатия клавиш
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED#34
    if event.keysym=='w':#35
        LEFT_PAD_SPEED= -PAD_SPEED#36 когда мы нажимаем верх, ракетка должна идти верх
    elif event.keysym=='s':#36
        LEFT_PAD_SPEED= PAD_SPEED#36
    elif event.keysym=='Up':#37 для 2ой ракетки
        RIGHT_PAD_SPEED= -PAD_SPEED
    elif event.keysym=='Down':#37 для 2ой ракетки
        RIGHT_PAD_SPEED= PAD_SPEED
c.bind("<KeyPress>", moveent_hadeler)#38 теперь нужно привязывать Сanvas  эту функцию
#39 po idee na ekrane dlojni reagirovat uje raketki, klavishi, a zdes ERROR 15:46
def stop_pad(event):#40 сделаем функцию реагирования на отпускания
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED#41
    if event.keysym in 'ws':#42 если эти клавиши не нажаты, то мы ставим скорость 0
        LEFT_PAD_SPEED=0
    elif event.keysym in ('Up', 'Down'):
        RIGHT_PAD_SPEED=0
c.bind("<KeyRelease>", stop_pad)#43 делаем привязку этой функцииdelaem privyazku etoi funkcii
main()#21 запуск самого двжиения
root.mainloop()#14 запуск окна