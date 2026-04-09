import pyxel

class Enemy :
    """
    Une classe pour notre ennemie
    """
    def __init__(self, jeu, x, y):
        """Initialisation de l'ennemie

        :param x: L'abscisse du coin supérieur gauche
        :type x: int
        :param y: L'ordonnée du coin supérieur gauche
        :type y: int
        """
        self.jeu = jeu
        # position initiale de l'ennemie
        self.x = x
        self.y = y
        # largeur (width) et hauteur de l'ennemie (height)
        self.w = 8
        self.h = 8
    
      # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """
        Dessin d'un ennemi
        """
        nb_frame=pyxel.frame_count
        if nb_frame%15<5:
            pyxel.blt(self.x, self.y, 0, 0, 8, 8, 8)
        elif nb_frame%15<10:
            pyxel.blt(self.x, self.y, 0, 0, 16, 8, 8)
        else :
            pyxel.blt(self.x, self.y, 0, 0, 24, 8, 8)
        
    
    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """Mise à jour de l'ennemie (30FPS)
        """
        self.y+=1