#-*- coding: utf-8 -*-

import pygame.image
from pygame.surface import Surface

class ChangeScreenException(Exception):
    """Class ChangeScreenException use to change screen.

    Extends Exception.
    Use to prevent that the screen need to be changed.
    The screen who raised this is interrupted and give a value
    and a message.
    """

    def __init__(self, value, msg):
        self.value = value
        self.msg = msg

    def __str__(self):
        return "ScreenChange : %s--<val:%s>" % (self.msg, self.value)

class BaseScreen():
    """ Base Class Screen.

    Use to manage screen of games
    Use for exec main_loop, update screen.
    Enable to switch screen easier.
    Example :
    +------+         +------+
    | Game |  <----> | Menu |
    +------+         +------+
       ^^
       ||
       vv
    +-------+
    | Pause |
    +-------+
    
    Raise a ChangeScreenException to change screen.
    """
    def __init__(self, width, height, background=None):
        """ Init of baseScreen.
        
        Save the background :
        -  AFTER  init_entities_before ( sprite )
        -  BEFORE init_entities_after 
           (Attach entities or text to background)
        so init_entities save elements with background
        init_entities
        """
        self.surface = Surface((width, height))        
        if background is not None:
            self.surface.blit(background, background.get_rect())
        self.init_entities_before(self.surface)
        self.background = self.surface.copy()
        self.init_entities_after(self.surface)

    def init_entities_after(self, surface):
        """ Create entities after saving background.

        Need to be redefined"""
        pass

    def init_entities_before(self, surface):
        """ Create entities before saving background.

        Need to be redefined"""
        pass
    
    def main_loop(self):
        """ Function to use in main loop.
        
        Return update list of coordinates to refresh.
        """       
        self.execute(self.surface)
        self.erase_all_map()
        return self.draw(self.surface)
    
    def execute(self, surface):
        """ Exec and Update entities of the screen.

        Need to be redefined.
        """ 
        pass
    
    def erase_all_map(self):
        """ Erase all background

        Can redefine this function
        """
        self.surface = self.background.copy()
        
    def draw(self, surface):
        """ Draw entities in the surface.

        Need to be redefined.
        """
        pass
