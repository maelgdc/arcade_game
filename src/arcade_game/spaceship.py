"""
Un module pour le vaisseau
                                   _     _
                                  | |   (_)
     ___ _ __   __ _  ___ ___  ___| |__  _ _ __
    / __| '_ \ / _` |/ __/ _ \/ __| '_ \| | '_ \
    \__ \ |_) | (_| | (_|  __/\__ \ | | | | |_) |
    |___/ .__/ \__,_|\___\___||___/_| |_|_| .__/
        | |                               | |
        |_|                               |_|
                     `. ___
                    __,' __`.                _..----....____
        __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'
  _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'
,'________________                          \`-._`-','
 `._              ```````````------...___   '-.._'-:
    ```--.._      ,.                     ````--...__\-.
            `.--. `-`                       ____    |  |`
              `. `.                       ,'`````.  ;  ;`
                `._`.        __________   `.      \'__/`
                   `-:._____/______/___/____`.     \  `
                               |       `._    `.    \
                               `._________`-.   `.   `.___
                                                  `------'`
"""

import pyxel

class Spaceship :
    """
    Une classe pour notre vaisseau
    """
    def __init__(self, jeu, x, y):
        """Initialisation du vaisseau

        :param x: L'abscisse du coin supérieur gauche
        :type x: int
        :param y: L'ordonnée du coin supérieur gauche
        :type y: int
        """
        self.jeu = jeu
        # position initiale du vaisseau
        self.x = x
        self.y = y
        # largeur (width) et hauteur du vaisseau (height)
        self.w = 8
        self.h = 8
        self.shoots=[]

    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """Mise à jour du vaisseau (30FPS)
        """
        self._move()
        self._shoot()

    def _move(self):
        """déplacement avec les touches de directions"""
        if pyxel.btn(pyxel.KEY_RIGHT):
            if self.x + self.w < self.jeu.w :
                self.x += 8
        if pyxel.btn(pyxel.KEY_LEFT):
            if self.x > 0:
                self.x += -8
        if pyxel.btn(pyxel.KEY_DOWN):
            if self.y + self.h < self.jeu.h :
                self.y += 8
        if pyxel.btn(pyxel.KEY_UP):
            if self.y >0: 
                self.y += -8

    def _shoot(self):
        if pyxel.btn(pyxel.KEY_SPACE):
            self.shoot = Shoot(self, self.x, self.y) #instanciation du tir
            self.shoots.append(self.shoot)


    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """
        Dessin du vaisseau
        """
        # vaisseau (carre 8x8)
        pyxel.blt(self.x, self.y, 0, 0, 0, 8, 8)


class Shoot :
    """
    Une classe pour notre tir
    """
    def __init__(self, spaceship, x, y):
        """Initialisation du tir

        :param x: L'abscisse du coin supérieur gauche
        :type x: int
        :param y: L'ordonnée du coin supérieur gauche
        :type y: int
        """
        self.spaceship = spaceship        
        # largeur (width) et hauteur du tir (height)
        self.w = 4
        self.h = 6
        # position initiale du tir
        self.x = x + self.spaceship.w/2 - self.w/2
        self.y = y
        
        
    def update(self):
        """Mise à jour du tir (30FPS)
        """
        self._move()
        
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 10, 1, self.w, self.h)

    def _move(self):
        self.y+=-8