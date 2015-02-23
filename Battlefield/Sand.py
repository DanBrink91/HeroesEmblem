from Tile import *


class Sand(Tile):
    Image = "images/sand.png"
    DefenseBoost = -1
    AccuracyPenalty = -5
    MovementCost = 3
    Altitude = 1

    def __init__(self, spawn):
        Tile.__init__(self, Sand.Image, Sand.DefenseBoost, Sand.AccuracyPenalty, Sand.MovementCost, Sand.Altitude,
                      spawn)

    def draw(self, surface, x, y):
        super(Sand, self).draw(surface, x, y)