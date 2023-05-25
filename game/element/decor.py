#******************************* Importations : ********************************

# Built-in modules :
from typing import Optional

# Modules persos :
import game.Game as Gme
from .elem import Element
from . import creature as Crtr

from utils import statically_typed_function


#********************************** Classes : **********************************

#-------------------------------------------------------------------------------
#                               'DECOR' ELEMENT
#-------------------------------------------------------------------------------

class FixedElement (Element) : #Classe abstraite
    """ Représente l'ensemble des objets fixes ET irrécupérable sur la Map """
    
    def __init__ (self, name:str, abbrv:str) :
        Element.__init__(self, name, abbrv)
    
    @staticmethod
    def action () :
        raise NotImplementedError


class Stairs (FixedElement) :
    def __init__ (self , name: Optional[str] = 'Stairs') :
        FixedElement.__init__(self, name, 'E')
    
    @staticmethod
    def action () :
        G = Gme.theGame() #Optimise le code en réduisant le nmbre d'appel
        G._level += 1
        G.buildFloor()
        G.addMessage(f"The {G.hero._name} goes down")


class Wall (FixedElement) :
    def __init__ (self , name: Optional[str] = 'Obstacle') :
        FixedElement.__init__(self, name, '#')
    
    @staticmethod
    def action () : # Ne fait rien
        return