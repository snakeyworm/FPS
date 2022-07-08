
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from math import cos, sin, radians, copysign
from random import random

GUN_MOVE_LIMIT = 5

app = Ursina()
Sky()

ground = Entity(
    model="cube",
    scale=(100, 10, 100),
    color=color.green.tint(0.6),
    collider="box",
)

player = FirstPersonController(
    speed=10,
    y=100,
)


class Gun(Entity):

    def __init__(self ):

        super().__init__(
            model="models/G17_gun.glb",
            color=color.black,
            scale=0.04,
            rotation_z=90,
            rotation_x=90,
        )

        self.sway = 0
        self.swayFactor = 1

    def update(self):

        # Gun Sway update
        if abs(self.sway) > GUN_MOVE_LIMIT:
            self.sway = copysign( GUN_MOVE_LIMIT, self.sway )
            self.swayFactor = -self.swayFactor

        # Calculate sway factors
        self.sway += self.swayFactor*random()
        posSway = self.sway*0.05 * time.dt
        rotSway = self.sway * time.dt

        # Position gun

        self.position = player.position
        self.y += 1.75 + posSway
        self.x += sin(radians(player.rotation.y + 15)) + posSway
        self.z += cos(radians(player.rotation.y)) + posSway

        # Rotate gun

        self.look_at_2d(player, axis="y")
        
        self.rotation_y += rotSway 
        self.rotation_z += rotSway 
        self.rotation_x += rotSway

gun = Gun()

app.run()
