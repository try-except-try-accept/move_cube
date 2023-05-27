from os import system
import msvcrt
# w d h

ANSI = "\033[38;2;r;g;bm"
BLOCK = "██"

def get_colours():
    for i in range(1, 7):
        def mul(x):
            return str(int(x) * 255)
        r,g,b = map(mul, bin(i)[2:].zfill(3))
        col = ANSI
        col = col.replace("r", r)
        col = col.replace("g", g)
        col = col.replace("b", b)
        print(col)
        
COLOURS = ('''[38;2;0;0;255m
[38;2;0;255;0m
[38;2;0;255;255m
[38;2;255;0;0m
[38;2;255;0;255m
[38;2;255;255;0m'''.splitlines())


     

MAX_W = 96
MAX_D = 111
MAX_H = 100

box = [30, 40, 50]
t = 0



class Box:   
    def __init__(self, w, h, d):
        global t
        self.w = w
        self.h = h
        self.d = d
        t += 1
        self.colour = COLOURS[t]

        self.x, self.y, self.z = 0, 0, 0

    def rotate(self):
        temp = self.w
        self.w = self.h
        self.h = self.d
        self.d = temp

    def move(self, direction):
        if direction == "a":
            self.x -= 1
        elif direction == "d":
            self.x += 1
        elif direction == "w":
            self.y -= 1
        elif direction == "s":
            self.y += 1
        elif direction == "z":
            self.z -= 1
        elif direction == "e":
            self.z += 1

            
    def get_across(self):
        return range(self.x, self.x+self.w+1)

    def get_down(self):
        return range(self.y, self.y+self.h+1)

class Model:

    def __init__(self):
        self.boxes = []
        self.w = MAX_W
        self.h = MAX_H
        self.d = MAX_D
        self.selected = None


    def get_dims(self):
        w, h, d = -1, -1, -1

        while w < 0 or w > MAX_W:
            w = int(input("Enter new box width: "))
        while h < 0 or h > MAX_H:
            h = int(input("Enter new box height: "))
        while d < 0 or d > MAX_D:
            d = int(input("Enter new box depth: "))

        return w, h, d

    def move_box(self, direction):
        self.boxes[self.selected].move(direction)

    def add_box(self):        
        self.boxes.append(Box(*self.get_dims()))
        if model.selected is None:
            model.selected = 0

    def rotate(self):
        temp = self.w
        self.w = self.h
        self.h = self.d
        self.d = temp

    def select_previous(self):
        self.selected -= 1
        if self.selected < 0:
            self.selected = 0

    def select_next(self):
        self.selected += 1
        if self.selected >= len(self.boxes):
            self.selected = len(self.boxes) - 1
        
    def display(self):
        s = ""

        for y in range(self.h):

            for x in range(self.w):
                box = None
                for b in self.boxes:
                    if x in b.get_across() and y in b.get_down():
                        box = b.colour + BLOCK
                if not box:
                    s += "  "
                else:
                    s += box

            s += "\n"
            


        print(s)
                        
system("cls")
model = Model()    
while True:
    x = msvcrt.getwch()
    if x == "n":
        model.add_box()
        model.display()
    elif x == "q":
        quit()
    else:
        if model.selected is not None:
            if x == "z":
                model.select_previous()
            elif x == "x":
                model.select_next()
            elif x in "wasd":
                model.move_box(x)
                system("cls")
                model.display()
            
    
        
        

# 10 boxes stacked   50 x 80 x 150
# space above boxes  50 x 80 x 35
# TV box  108 x 68 x 15
# computer box 32 x 53 x 51
# table 120 x 60 x 4
# table legs 71 x 10 x 10
# thai seat thing 47 x 53 x 53
# guitar 110 x 40 x 15
# bike wheels 70 x 70 x 12
# bike frame 145 x 60 x 25






