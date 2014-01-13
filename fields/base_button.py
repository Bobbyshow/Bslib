#-*- coding: utf-8 -*-

from pygame.locals import K_UP as UP

from pygame.sprite import Sprite
from pygame.rect import Rect

from ..base_entity import BaseEntity
from ..base_animation import BaseAnimation

class Event(Exception):
    """Class Event use to clicked (selected) button.

    Extends Exception.
    Use to prevent that a button is clicked by the user.
    The clicked button raise a Event and give a value
    and a message.
    """

    def __init__(self, value, msg):
        self.value = value
        self.msg = msg

    def __str__(self):
        return "Event : %s--<val:%s>" % (self.msg, self.value)

class BaseButtonAnimation(BaseAnimation):
    """Base Class Button Animation.
    
    Default animation for buttons style
    """
    WIDTH = 100
    HEIGHT = 50

    def get_sprite(self, move_direction):
        frame =  self.subsurface(
            0,
            self.HEIGHT * self.frame,
            self.WIDTH,
            self.HEIGHT
        ).convert_alpha()
        return frame
    
    def update_frame(self, state):
        self.frame = state

class BaseButton(BaseEntity):
    """Base Class Button to use for games button.

    Extends BaseEntity
    Use to manage default buttons behaviors 
    with default animation. 
    
    Instance variables:
    - focus : True if button have focus.
    - active : True if button is activate
    - value : Value of the event
 
    A button which focus AND click create a Event, needed to be catched
    by the button's screen.

    Don't forget to create img sprite and
    """

    STATE_INACTIVE = 0
    STATE_FOCUS = 1
    STATE_ACTIVE = 2

    def set_value(self, value):
        self.value = value

    def event_launch(self):
        if self.value:
            raise Event(self.value, 'Event launched')
        else:
            raise Event(-1, 'Empty event')
    
    def is_focused(self):
        return self.focused

    def is_clicked(self):
        return self.clicked

    def check_state(self):
        """Raise a event if button is clicked and focused."""
        if self.is_focused() and self.is_clicked():
            self.event_launch()

    def focus(self):
        self.focused = True
        self.animation.set_frame(self.STATE_FOCUS)

    def clicked(self):
        self.clicked = True
        self.animation.set_frame(self.STATE_ACTIVE)
        self.check_state()
        
    def remove(self):
        self.clicked = False
        self.focused = False
        self.animation.set_frame(self.STATE_INACTIVE)

    def lose_focus(self):
        self.focused = False
        self.animation.set_frame(self.STATE_INACTIVE)

    def init_animation(self, max_frame, max_frame_delay, img=None):
        return BaseButtonAnimation(
            max_frame, 
            max_frame_delay, 
            img
         )

    def update(self, movement=None):
        """Custom Update.

        """
        self.animation.update()
        self.setup_animation()
