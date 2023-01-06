import random

from pygame import Vector2

from obstcle import Obstacle

import core
from body import Body


class Agent(object):
    def __init__(self, body, statut):
        self.body=body
        self.uuid=random.randint(100000,999999999)
        self.statut = statut
        if(self.statut == 'I'):
            self.body.incub = True
        self.body.parent = self


    def filtrePerception(self):
        creeps=[]
        obstacles=[]
        danger=[]
        manger=[]
        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)
            if isinstance(i,Obstacle):
                obstacles.append(i)
            if isinstance(i,Body):
                if i.mass > self.body.mass:
                    danger.append(i)
                else:
                    manger.append(i)

        return creeps,obstacles,danger,manger

    def update(self):
        target = Vector2(random.randint(-2, 2), random.randint(-2, 2))
        while target.length() == 0:
            target = Vector2(random.randint(-2, 2), random.randint(-2, 2))

        self.body.acc = self.body.acc + target

        for b in core.memory("agents"):
            if (self.body.position.distance_to(b.body.position)<self.body.distanceContagion):
                if(self.statut == "I"):
                    if(b.statut == "S"):
                        proba = random()
                        if(proba < self.body.contagPerc):
                            b.statut = "I"
                            b.body.incub=True





    def show(self):
        color = (255, 255, 255)
        if (self.statut == "I"):
            color = (255, 0, 0)
        elif (self.statut == "R"):
            color = (0, 255, 0)
        self.body.show(color)