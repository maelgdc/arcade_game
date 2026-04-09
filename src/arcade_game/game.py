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
          
        self.collision_shoots_enemies()
        
        for enemy in self.enemies:
          if self.is_collision(self.spaceship,enemy):
            self.spaceship.lives-=1
            self.enemies.remove(enemy)

    # =====================================================
    # == DRAW (30FPS)
    # =====================================================
    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""

        # vide la fenetre 30 fois par seconde
        pyxel.cls(0)
        if self.spaceship.lives > 0:

          # affichage des vies            
          pyxel.text(5,5, 'VIES:'+ str(self.spaceship.lives), 7)

          # LE RESTE DE VOTRE CODE
          self.spaceship.draw()
          
          for tir in self.spaceship.shoots:
            tir.draw()
            
          for enemy in self.enemies:
            enemy.draw()

        # sinon: GAME OVER
        else:
          pyxel.text(50,64, 'GAME OVER', 7)

        
          
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
      
    def is_collision(self, obj1, obj2):
      """
      obj1 : une instance d'un objet
      obj2 : une instance d'un objet
      
      retourne True si il y a collision entre les deux objets, False sinon
      """
      if max(obj1.x, obj2.x)<=min(obj1.x+obj1.w, obj2.x+obj2.w) and max(obj1.y, obj2.y)<=min(obj1.y+obj1.h, obj2.y+obj2.h):
        print("col")
        return True
      else : return False
    
    def collision_shoots_enemies(self):
      tirs_a_supprimer =[]
      ennemis_a_supprimer =[]
      for tir in self.spaceship.shoots:
        for enemy in self.enemies:
          if self.is_collision(tir,enemy):
            tirs_a_supprimer.append(tir)
            ennemis_a_supprimer.append(enemy)
      for enemy_a_supprimer in ennemis_a_supprimer:
        self.enemies.remove(enemy_a_supprimer)
      for tir_a_supprimer in tirs_a_supprimer:
        self.spaceship.shoots.remove(tir_a_supprimer)

# instanciation de notre classe
Game()