#-*- coding: utf-8 -*-

from pygame.locals import K_UP as UP

from pygame.sprite import Sprite
from pygame.rect import Rect

from base_animation import BaseAnimation
from base_group import Group

class BaseEntity(Sprite):
    """Base Class Entity to use for games entity.

    Extends pygame.Sprite class
    Use to manage entities, for space collapsing
    and draw animation space.
    
    Instance variable:
    - rect : pygame.Rect class 
    Use for collapse beetween entities
    - direction : direction state 
        UP = 273
        DOWN = 274
        RIGHT = 275
        LEFT = 276
    - speed : list of speed mvt : [abs, ord]
    """

    STATUS = []

    def __init__(
        self,
        name,
        rect_data,
        speed,
        max_frame,
        max_frame_delay,
        img,
        direction=None
    ):
        """ Init.
        - rect_data : list contains =>
        - x : position x
        - y : position y
        - w : width of rect_collapse
        - h : height of collase
        """
        super(BaseEntity, self).__init__()
        self.name = name
        self.rect = None
        self.image = None
        self.childs = Group()
        self.rect_collapse = Rect(rect_data)
        self.speed = speed
        if direction is None:
            self.direction = UP
        else:
            self.direction = direction
        self.actual_state = 'STOP'
        self.state = ['STOP','MOVE']
        for state in self.STATUS:
            self.state.append(state)
        
        # Create animation for the entity
        self.animation = self.init_animation(max_frame, max_frame_delay, img)
        
    def add_child(self, child):
        """Add a child entity."""
        self.childs.add(child)

    def remove_child(self, child):
        """Remove a child entity."""
        self.childs.remove(child)
    
    def direction_get(self):
        return self.direction

    def direction_set(self, direction):
        self.direction = direction

    def get_rect(self, value=0):
        """Return rect 
        
        0 = rect(actual rect to use)
        1 = rect_animation
        2 = rect_collapse
        """
        if value == 1:
            return self.image.get_rect()
        elif value == 2:
            return self.rect_collapse
        else:
            return self.rect

    def init_animation(self, max_frame, max_frame_delay, img):
        """Function for animation initialisation.
        
        Need to be defined.
        """
        pass

    def __str__(self):
        """Custom __str__."""
        string = (
            u"<Entity : %s -- Pos (%s,%s)>\n" % (
                str(self.name),
                str(self.rect_collapse[0]),
                str(self.rect_collapse[1]),
            )           
        )
        return string

    def move(self, move_direction):
        """Basic mouvement.

        Basic calcul tomove the entity, defined by direction parameter
        Reimplements if you need to change move's pattern
        """
        pass

    def stop(self):
        """Basic stop.
        
        Stop the mouvement of the entity
        Reimplements if you need to change move's pattern
        """
        pass

    def update(self, direction=None):
        """Update function.
        
        Basic update position of the entity (move or stop)
        Redefine it for your own purpose
        Action use by pygame.sprite.Group.update() function.
        """
        if direction is None:
            self.stop()
            self.animation.stop()
        else:
            self.move(direction)
            self.animation.update()
        
        self.setup_animation(direction)
        self.childs.update()

    def setup_collapse(self):
        """Setup variable.
                
        Set up rect attribute for collapse eval"""
        self.rect = self.rect_collapse
        for sprite in self.childs:
            sprite.setup_collapse()
    
    def setup_animation(self, direction=None):
        """Setup variable.

        Set up rect attribute for animation draw
        Be careful :: is function move anim_sprite to center
        with rect_collapse
        Catch image.get_rect directly will give you the wrong coordinate
        """
        if direction is None:
            if self.direction is None:
                raise Exception('Direction is not defined')
            else:
                direction = self.direction
        self.image = self.animation.get_sprite(direction).convert_alpha()
        rect_anim_position = self.image.get_rect()
        rect_anim_position.center = self.rect_collapse.center
        self.rect = rect_anim_position
        
