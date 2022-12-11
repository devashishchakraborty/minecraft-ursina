from ursina import *

def update():
    if held_keys['a']:
        test_square.x -= 2 * time.dt

app = Ursina()

test_square = Entity(model="quad", color=color.red, scale=(1,4), position=(2,2))

sans_texture = load_texture('assets/Sans.png')
sans = Entity(model="quad", texture=sans_texture)

app.run()