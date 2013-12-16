#-*- coding: utf-8 -*-

import pygame.image
from pygame.surface import Surface

class ChangeScreenException(Exception):
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
        """ Init of baseScreen."""
        self.surface = Surface((width, height))        
        if background is not None:
            self.background = background
            bg = pygame.image.load(background).convert_alpha()
            self.surface.blit(bg, bg.get_rect())
        self.init_entities(self.surface)

    def init_entities(self, surface):
        """ Create entities. Need to be redefined"""
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
        bg = pygame.image.load(self.background).convert_alpha()
        self.surface.blit(bg, bg.get_rect())
        
    def draw(self, surface):
        """ Draw entities in the surface.

        Need to be redefined.
        """
        pass
