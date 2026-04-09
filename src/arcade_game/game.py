"""
le module principal du projet arcade_game

                  :: ::::: ::
                  :: ::::: ::
                  :: ::::: ::
                  :: ::::: ::
                  :: ::::: ::


                 .:: ::::: ::.
                .::: ::::: :::.
               .:::' ::::: ':::.
              .::::' ::::: '::::.
             .::::'  :::::  '::::.
           .:::::'   :::::   ':::::.
         .::::::'    :::::    '::::::.
    ...:::::::'      :::::      ':::::::...
    :::::::''        :::::        '':::::::
    ::::''           :::::           ''::::

      _______ _______ _______ ______  ___
     |   _   |       |   _   |   _  \|   |(R)
     |.  1   |.|   | |.  1   |.  l   |.  |
     |.  _   `-|.  |-|.  _   |.  _  <|.  |
     |:  |   | |:  | |:  |   |:  |   |:  |
     |::.|:. | |::.| |::.|:. |::.|:. |::.|
     `--- ---' `---' `--- ---`--- ---`---'

"""

import pyxel
from arcade_game.spaceship import Spaceship
from arcade_game.enemy import Enemy
from random import randint

class Game:
    """
    Une classe pour notre jeu
    """
    def __init__(self):
        """
        Initialisation du jeu
        """
        self.w = 128 #largeur de l'écran
        self.h = 256 #hauteur de l'écran
        self.enemies=[] 
        self.spaceship = Spaceship(self, self.w//2, self.h-8) #instanciation du vaisseau
        pyxel.init(self.w, self.h, title="Arcade Game")
        # chargement des images
        pyxel.load("images.pyxres")
        # --> appel de la fonction principale
        pyxel.run(self.update, self.draw)
        

    # =====================================================
    # == UPDATE (30FPS)
    # =====================================================
    def update(self):
        """mise à jour des variables (30 fois par seconde)"""

        # deplacement du vaisseau
        self.spaceship.update()
        
        for tir in self.spaceship.shoots:
          tir.update()
          
        for enemy in self.enemies :
          enemy.update()
          
        self.update_shoots()
        
        if pyxel.frame_count%30==0:
          enemy = Enemy(self, randint(0,120), -8)
          self.enemies.append(enemy)
                
        self.update_enemies()
          

    # =====================================================
    # == DRAW (30FPS)
    # =====================================================
    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""

        # vide la fenetre 30 fois par seconde
        pyxel.cls(0)

        self.spaceship.draw()
        
        for tir in self.spaceship.shoots:
          tir.draw()
          
        for enemy in self.enemies:
          enemy.draw()
          
    def update_shoots(self):
      visible_shoots=[]
      for tir in self.spaceship.shoots:
          if (tir.y+tir.h>0):
            visible_shoots.append(tir)
      self.spaceship.shoots=visible_shoots
      
    def update_enemies(self):
      visible_enemies=[]
      for enemie in self.enemies:
          if enemie.y + enemie.h < enemie.jeu.h :
            visible_enemies.append(enemie)
      self.enemies=visible_enemies

# instanciation de notre classe
Game()