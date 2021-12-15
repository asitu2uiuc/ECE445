import pyglet
from pyglet.window import key
from pyglet.gl import *





label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=10, y=10)

state1 = 0
state2 = 0
out = ["0" , "1"]
class ToggleWindow(pyglet.window.Window):

    def __init__(self):
        super(ToggleWindow, self).__init__()
        self.color = 1.0

    def toggle(self):
        global label
        if self.color == 1.0:
            self.color = 0.0
            label = pyglet.text.Label(out[state1],
                          font_name='Times New Roman',
                          font_size=36,
                          x=10, y=10)
            label.draw()
        else:
            self.color = 1.0
            label = pyglet.text.Label('2',
                          font_name='Times New Roman',
                          font_size=36,
                          x=10, y=10)
            # print("reached")
            label.draw()
     
    def on_draw(self):
        self.switch_to()
       
        glClear(GL_COLOR_BUFFER_BIT)
        # glLoadIdentity()
        # glColor3f(self.color,self.color,self.color)
        # glBegin(GL_QUADS)
        # glVertex2f(0,0)
        # glVertex2f(self.width,0)
        # glVertex2f(self.width,self.height)
        # glVertex2f(0,self.height)
        # glEnd()
        label.draw()


def main():

    window1 = ToggleWindow()
    window2 = ToggleWindow()

    @window1.event
    @window2.event
    def on_key_press(symbol, modifiers):
        if symbol == key._1:
            print(1)
            window1.toggle()
        elif symbol == key._2:
            print(2)
            window2.toggle()
        else:
            print(symbol)
   
    pyglet.app.run()

           
if __name__ == "__main__":
    main()