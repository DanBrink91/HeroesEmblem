from Tile import *


class Water(Tile):
    Image = "images/water.png"
    DefenseBoost = 1
    AccuracyPenalty = 0
    MovementCost = 5
    Altitude = 0

    def __init__(self, spawn):
        Tile.__init__(self, Water.Image, Water.DefenseBoost, Water.AccuracyPenalty, Water.MovementCost, Water.Altitude,
                      spawn)

    def draw(self, surface, x, y):
        super(Water, self).draw(surface, x, y)