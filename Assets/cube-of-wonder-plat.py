# this is the cube of wonder click the cube

from ursina import * # you have to do "pip install ursina" first
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController()

class Cube():
    def __init__(self, x, y, z, color=color.gray):
        Entity(model="cube", color=color, collider="box", ignore=True, position = (x, y, z), parent=scene, origin_y = 0.5, texture="white_cube")

Cube(5, 2, 4)
Cube(8, 3, 5)
Cube(8, 2, 5)
Cube(10, 4, 7)
Cube(10, 3, 7)
Cube(10, 2, 7)
Cube(11, 5, 8)
Cube(12, 6, 10)
Cube(12, 6, 11)
Cube(11, 7, 12)
Cube(12, 9, 12)
Cube(12, 8, 12)
Cube(10, 10, 12)
Cube(9, 12, 12)
Cube(8, 14, 12)
Cube(7, 15, 11)
Cube(6, 16, 10)
Cube(5, 17, 9)

for i in range(4):
    Cube(6, i+20, 7, color=color.light_gray)
    Cube(7, i+20, 7, color=color.light_gray)
    Cube(7, i+20, 6, color=color.light_gray)
    Cube(7, i+20, 5, color=color.light_gray)
    Cube(7, i+20, 4, color=color.light_gray)
    Cube(7, i+20, 3, color=color.light_gray)
    Cube(6, i+20, 3, color=color.light_gray)
    Cube(5, i+20, 3, color=color.light_gray)
    Cube(4, i+20, 3, color=color.light_gray)
    Cube(3, i+20, 3, color=color.light_gray)
    Cube(3, i+20, 4, color=color.light_gray)
    Cube(3, i+20, 5, color=color.light_gray)
    Cube(3, i+20, 6, color=color.light_gray)
    Cube(3, i+20, 7, color=color.light_gray)
    Cube(4, i+20, 7, color=color.light_gray)

Cube(5, 23, 7, color=color.light_gray)
Cube(5, 23, 6, color=color.light_gray)
Cube(6, 23, 6, color=color.light_gray)
Cube(4, 23, 6, color=color.light_gray)
Cube(5, 23, 5, color=color.light_gray)
Cube(6, 23, 5, color=color.light_gray)
Cube(4, 23, 5, color=color.light_gray)
Cube(5, 23, 4, color=color.light_gray)
Cube(6, 23, 4, color=color.light_gray)
Cube(4, 23, 4, color=color.light_gray)

Entity(model="cube", collider="box", ignore=True, position = (5, 20, 5), parent=scene, origin_y = 0.5, texture="ham.png")

for i in range(20):
    for j in range(20):
        Entity(model="cube", color=color.dark_gray, collider="box", ignore=True, position = (j, 0, i), parent=scene, origin_y = 0.5, texture="white_cube")

for i in range(5):
    for j in range(5):
        Entity(model="cube", color=color.light_gray, collider="box", ignore=True, position = (j+3, 19, i+3), parent=scene, origin_y = 0.5, texture="white_cube")


class TextureBox(Button):
    def __init__(self, position=(5,25,5)):
        super().__init__(parent=scene, position=position, model="cube", origin_y=0.5, texture="windows.png", color=color.color(0,0,1))

        self.texture_choice = 0
        self.textures = ["windows.png", "earth.jpg", "space.png", "duplo_train.jpg"]

    def input(self, key):
        y = player.position[1] > 22
        x = player.position[0] < 7
        z = player.position[2] < 7
        if self.hovered and x and y and z:
            if key == 'left mouse down':
                self.texture_choice += 1
                self.texture_choice %= len(self.textures)
                self.texture = self.textures[self.texture_choice]

TextureBox()

app.run()
