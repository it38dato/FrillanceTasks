# Разработка Paint.
from kivy.app import App #1
from kivy.uix.widget import Widget #1
from kivy.graphics import (Color, Ellipse, Rectangle, Line) #3 чтобы начать что то рисовать нужны граф инструкци
#google -kivy graphics
from random import random
from kivy.uix.button import Button #23
from kivy.core.window import Window#34 чтоб узнать ширину и высоту окна
class PainterWidget(Widget): #2
    #4 pass #2
    ''' #12 Можем удалить
    def __init__(self, **kwargs):#5 теперь можем начать рисовать, сначала сделаемм инициализацию
        super(PainterWidget, self).__init__(**kwargs) #5

        with self.canvas:#6 после этого нужно обратиться к self canvas
            Color(0,1,0,1)#7 можно уже начать перечислять нужные граф инструкции, Цвет
            #9 Ellipse(pos=(100,100), size=(50,50))#7 адрессовать круг, если запусти увидим зеленый круг
            #9 Line(points=(100, 100, 150, 200, 200, 100), close=True, width=5)#7 Нарисуется треугольник
            self.line=Line(points=(), width=10, joint='miter', cap='square')#8 Можно сделать по другому. создадим линию
    '''
    def on_touch_down(self, touch):#10 Сделаем еще событие, которая вызывается тогда когда нажимается мышь или как при андроеде. touch содержит инфу о клике.
        #12 self.line.points += (touch.x, touch.y)#11 линию которую мы создали в #10, дополняемя точками, которым мы кликаем. на окошке мы увидим черный экран, и когда нажмем один раз и второй раз в другом есте пояится линия
        with self.canvas:#13 нарисуем круг зеленого цвет  с радиусом 30
            Color(random(),random(),random(),1)#13
            rad=30#13
            Ellipse(pos=(touch.x-rad/2, touch.y-rad/2), size=(rad,rad))#13 -rad/2 это чтоб рисовался по центру мыши
            #13 на экране при клике на любое место появится точки
            touch.ud['line']=Line(points=(touch.x, touch.y), width=15)#15 Теперь уже хотим нарисовать. с помощью ud можем передавать определенную инфу меж событиями on_touch_move и on_touch_down. И создадим ячейку line            
    def on_touch_move(self, touch):#14 добавим еще одно событие, 
        #16 pass
        touch.ud['line'].points += (touch.x, touch.y)#17 на эране теперь уже что то рисуем
class PaintApp(App): #1
    def build(self): #1
        #pass #1
        #19 return PainterWidget() #2
        #18 Хотим теперь чтоб наши данные записывались
        parent=Widget() #20
        #27 parent.add_widget(PainterWidget()) #21
        self.painter=PainterWidget()#28
        parent.add_widget(self.painter)#29
        parent.add_widget(Button(text='Ochistit', on_press=self.clear_canvas, size=(100, 50))) #24
        parent.add_widget(Button(text='Save', on_press=self.save, size=(100, 50), pos=(100,0))) #29
        parent.add_widget(Button(text='Screen', on_press=self.screen, size=(100, 50), pos=(200,0))) #33        
        return parent #22
    def clear_canvas(self, instance):#25 Объявим эту функцию clear_canvas
        #27 pass #26 на окошке появится кнопка
        self.painter.canvas.clear()#30 очистит
    def save(self, instance):#31 Объявим эту функцию save
        self.painter.size=(Window.size[0], Window.size[1])#33 изменим размер виджета, так как сохраняет только маленькую часть. 0 -по оси х, 1 - по оси у
        self.painter.export_to_png('image.png') #32 идет сохранение
    def screen(self, instance):#35
        Window.screenshot('screen.png')
if __name__ == '__main__': #1
    PaintApp().run() #1