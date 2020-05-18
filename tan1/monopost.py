#!/usr/bin/python
import logging
import threading
import time
import os
import sys
import random

go = True
msg = ""

class Monopost(threading.Thread):

    def __init__(self, name, parts, obstacole, health):
        threading.Thread.__init__(self)
        self.name = name
        # tank speed
        self.viteza = 20
        self.flag1=True
        self.flag2=True
        # distance to reach in order to start shooting
        self.lungimeTraseu = 40
        # tank health 
        self.he = health
        # tank parts
        self.dict = parts
        # obstacole
        self.obstacole = obstacole
        
      
    def run(self):
        """
        Threads - Abrams and Panzer
        accessing this function
        """
        global go # flag - detect if game (thread) is finished
        global msg 
        if not go: # reset for the next session
            go = True

        self.move(distParcurs=0)
        time.sleep(0.1)
        self.shoot(hel=0)
        

    def move(self, distParcurs):
        """
        Each tank (thread) must complete "lungimeTraseu=40" by default
        Obstacole are provided randomly 
        Each obstacol has a value to be added to the "lungimeTraseu"
        So each obstacol will delay the tank (thread) to finish early
        Each log is saved in the variable "msg" in order to be saved,
        in a text file at the end of the session
        """
        global msg
        msg += "{} enter the game. War zone is at {} \n".format(self.name, self.lungimeTraseu)
        print("{} enter the game. War zone is at {}".format(self.name, self.lungimeTraseu))
        
        global go
        while (distParcurs < self.lungimeTraseu):
            
            asd = random.randint(0, 1)
            # randomly provide obstacole if asd=1 and add them to the lungimeTraseu
            if asd==1:
                obst, dist = random.choice(list(self.obstacole.items()))
                msg += "{} has a {} in front, total distance increase with {} \n".format(self.name, obst, dist)
                print("{} has a {} in front, total distance increase with {}".format(self.name, obst, dist))
                self.lungimeTraseu += dist
            # Show when the tank almost reach the shooting area
            if distParcurs>self.lungimeTraseu-self.lungimeTraseu / 5 and self.flag1:
                msg += self.name + " has nearly finished the race " + "\n"
                print("\n" + self.name + " has nearly finished the race " + "\n")
                self.flag1=False
            elif distParcurs>self.lungimeTraseu-self.lungimeTraseu / 2 and self.flag2:
                msg += self.name + " has less than half " + "\n"
                print("\n" + self.name + " has less than half " + "\n")
                self.flag2=False
            time.sleep(0.1)
            distParcurs += self.viteza 
            if not go: # check is any thank WON
                sys.exit(0)
            msg += "{}, distance made {} total ramas={} \n".format(self.name, distParcurs, self.lungimeTraseu-distParcurs) 
            print("{}, distance made {} total ramas={}".format(self.name, distParcurs, self.lungimeTraseu-distParcurs))
            print("=====================")
        if not go: # check is any thank WON
                sys.exit(0)
        msg += "{} Prepared to shoot \n".format(self.name)     
        print("{} Prepared to shoot".format(self.name))

    def shoot(self, hel):
        """
        Here the tank start shooting till the health is consumed 
        """
        global go
        global msg
        while (hel < self.he):
            
            time.sleep(0.1)
            # randomly select a tank part and shoot
            # every tank part has its value
            tool, shot = random.choice(list(self.dict.items()))            
            hel += shot
            if not go: # check is any thank WON
                sys.exit(0)
                
            msg += "{} shoot {} pts in {}, total ramas {} \n".format(self.name, shot, tool, self.he-hel) 
            print("{} shoot {} pts in {}, total ramas {}".format(self.name, shot, tool, self.he-hel))
            print("=====================")
        if not go: # check is any thank WON
            sys.exit(0)

        if "WON!!!" not in msg: # avoid having 2 winners in the text file    
            msg += "{} WON!!! \n".format(self.name) 
        print("{} WON!!!".format(self.name))
        print("#################")
        # write the entire logs to file
        with open("logs.txt", "w") as f:
            f.write(msg)
        print(msg)
        msg = ""
        go = False
        