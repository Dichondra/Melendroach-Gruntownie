#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:24:10 2021

@author: franek
"""

import random


class fighter():
    def __init__(self):
        self.AC = 17
        self.HP = 12
        
    def attack(self,goblin):
        rzut = random.randint(1,20)+5
        dmg = random.randint(1,12) +3
        if rzut >= goblin.AC:
            goblin.take_dmg(dmg)
        
    def take_dmg(self,dmg):
        self.HP = self.HP - dmg
        #if self.HP <= 0 :
            #print("I am dead")

class goblin():
    def __init__(self):
        self.AC = 15
        self.HP = random.randint(1,6) + random.randint(1,6)
        
    def take_dmg(self,dmg):
        self.HP = self.HP - dmg
        #if self.HP <= 0 :
            #print("I am dead,goblin")
    def attack(self,fighter):
        if self.HP > 0 :
            rzut = random.randint(1,20)+4
            dmg = random.randint(1,6) + 2
            if rzut >= fighter.AC:
                fighter.take_dmg(dmg)
    
def Main():
    count = 0
    Adam = fighter()
    while Adam.HP > 0:
        grześ = goblin()
        while grześ.HP > 0:
            Adam.attack(grześ)
            
            grześ.attack(Adam)
            if Adam.HP <0:
                break
            if grześ.HP < 0:
                break
            #print("Życie wojownika = ",Adam.HP)
            #print("Życie goblina : ",grześ.HP)
        count += 1
    #print(count)
    return count

n = 100000
suma = 0
for i in range(n):
    suma += Main()
suma = suma / n

print(suma)