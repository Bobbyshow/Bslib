#-*- coding: utf-8 -*-

from pygame.locals import K_LEFT as LEFT
from pygame.locals import K_DOWN as DOWN 
from pygame.locals import K_UP as UP
from pygame.locals import K_RIGHT as RIGHT

from pygame.surface import Surface
from pygame.rect import Rect

import pygame.image

class BaseAnimation(Surface):
    """base Class Animation.
    
    Extends pygame.Surface class
    Use to manage animation's entities

    Instance variable:
    -  rect_animation : pygame.Rect class
    Use for animation display
    -  max_frame : max number of animation frame
    -  frame : actual frame animation
    -  max_frame_delay : max number of frames between 2 animations frame
    -  frame_delay : actual number of frames between 2 animations frame
    -  image : image to use for the animation

    Its functions called by its class owner : BaseEntity
    """
    
    def __init__(self, m_f, m_f_d, image):
        """ Custom init 
        /!\ TODO : Some check

        """
        image = pygame.image.load(image).convert_alpha()
        super(BaseAnimation,self).__init__(image.get_size(),pygame.SRCALPHA, 32)
        self.convert_alpha()
        self.blit(
            image,
            image.get_rect()
        )
        self.max_frame = m_f
        self.max_frame_delay = m_f_d
        self.frame = 0 
        self.frame_delay = 0

    def update(self):
        """ Basic animation update."""
        if self.frame_delay < 0:
            self.frame = (self.frame + 1) % self.max_frame   
            self.frame_delay = self.max_frame_delay
        else:
            self.frame_delay = self.frame_delay - 1
            

    def stop(self):
        """Basic animation update.
        
        Stop animation
        """
        self.frame = 0
        self.frame_delay = 0

    def get_sprite(self, direction):
        """Custom get_rect_anim

        Return SubSurface (Surface) for the animation.
        Need to be defined 
        (Depends of sprite's image)
        """
        pass
