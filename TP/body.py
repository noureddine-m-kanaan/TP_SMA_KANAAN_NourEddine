import random

from pygame import Vector2

import core
from TP.epidemie import Epidemie
from fustrum import Fustrum


class Body(object):
    def __init__(self):
        self.position=Vector2(random.randint(0,core.WINDOW_SIZE[0]),random.randint(0,core.WINDOW_SIZE[1]))
        self.vitesse = Vector2()
        self.vMax=2
        self.accMax=10
        self.mass=10
        self.fustrum=Fustrum(150,self)
        self.acc=Vector2()
        self.epidemie = Epidemie()
        self.parent=None
        self.incub = False
        self.cont = False
        self.die = False
        self.gueri = False

        self.incubDuration = self.epidemie.dict["incubDuration"]
        self.preContagiousDuration=self.epidemie.dict["preContagiousDuration"]
        self.contagPerc=self.epidemie.dict["contagPerc"]
        self.durationBeforeDeath=self.epidemie.dict["durationBeforeDeath"]
        self.deathPourcentage=self.epidemie.dict["deathPourcentage"]
        self.distanceContagion=self.epidemie.dict["distanceContagion"]


    def update(self):
        if self.acc.length() > self.accMax/self.mass:
            self.acc.scale_to_length(self.accMax/self.mass)

        self.vitesse=self.vitesse+self.acc

        if self.vitesse.length() > self.vMax:
            self.vitesse.scale_to_length(self.vMax)

        self.position=self.position+self.vitesse

        self.acc=Vector2()

        self.edge()

        if (self.parent.statut == 'I'):

            if(self.incub):
                self.preContagiousDuration = self.preContagiousDuration-1
                self.durationBeforeDeath = self.durationBeforeDeath -1
                if(self.durationBeforeDeath == 0) :
                    proba = random.uniform(0, 1)
                    if (proba < self.deathPourcentage):
                        self.die = True
                    else:
                        self.gueri = True

                self.contagPerc = 0

                if(self.preContagiousDuration == 0):
                    self.contagPerc = self.epidemie.dict["contagPerc"]

                    self.cont = True

            if(self.cont):
                self.durationBeforeDeath = self.durationBeforeDeath - 1
                if (self.durationBeforeDeath == 0):
                    proba = random.uniform(0, 1)

                    if (proba < self.deathPourcentage):
                        self.die = True
                    else:
                        self.gueri = True



    def show(self, color):
        core.Draw.circle(color,self.position,self.mass)


    def edge(self):
        if self.position.x <=self.mass:
            self.vitesse.x *= -1
        if self.position.x+self.mass >= core.WINDOW_SIZE[0]:
            self.vitesse.x *= -1
        if self.position.y <= self.mass:
            self.vitesse.y *= -1
        if self.position.y +self.mass>= core.WINDOW_SIZE[1]:
            self.vitesse.y *= -1