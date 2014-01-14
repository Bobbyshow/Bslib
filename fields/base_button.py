#-*- coding: utf-8 -*-

from pygame import mouse as Mouse
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
        frame = self.subsurface(
            0,
            self.HEIGHT * self.frame,
            self.WIDTH,
            self.HEIGHT
        ).convert_alpha()
        return frame
    
    def set_frame(self, state):
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

    Don't forget to create img sprite
    """

    STATE_INACTIVE = 0
    STATE_FOCUS = 1
    STATE_ACTIVE = 2
    
    def __init__(self, name, rect_data, speed, max_frame, max_frame_delay, img):
        super(BaseButton, self).__init__(name, rect_data, speed, max_frame, max_frame_delay, img)
        self.focused = False
        self.clicked = False
        self.value = None

    def set_value(self, value):
        self.value = value

    def event_launch(self):
        """Launch a Event exception."""
        if self.value:
            raise Event(self.value, 'Event launched')
        else:
            raise Event(-1, 'Empty event')
    
    def is_focused(self):
        """Return True if the button is focused."""
        x, y = Mouse.get_pos()
        return ( 
            x > self.rect_collapse.left and
            x < self.rect_collapse.right and
            y > self.rect_collapse.top and
            y < self.rect_collapse.bottom
        )

    def is_clicked(self):
        """Return True if mouse click is pressed.

        Default : only use left-click
        """
        return Mouse.get_pressed()[0] == 1

    def focus(self):
        """Check state focus"""
        if self.is_focused():
            self.focused = True
            self.animation.set_frame(self.STATE_FOCUS)
        else:
            self.lose_focus()

    def click(self):
        """Check state click (active)"""
        if self.is_clicked():
            self.clicked = True
            self.animation.set_frame(self.STATE_ACTIVE)
        else:
            self.lose_click()

    def remove(self):
        """Update state to inactive"""
        self.clicked = False
        self.focused = False
        self.animation.set_frame(self.STATE_INACTIVE)

    def lose_focus(self):
        """When the button lose the focus.

        Update state to inactive.
        """
        self.focused = False
        self.animation.set_frame(self.STATE_INACTIVE)

    def lose_click(self):
        """When the bouton is unclicked.

        Update state to focus.
        """
        self.clicked = False
        self.animation.set_frame(self.STATE_FOCUS)

    def update_state(self):
        """Check the actual state of the button and update it"""
        self.focus()
        if self.focused and not self.clicked:
            self.click()
            if self.clicked:
                self.event_launch()
        elif self.focused:
            self.click()

    def init_animation(self, max_frame, max_frame_delay, img=None):
        return BaseButtonAnimation(
            max_frame, 
            max_frame_delay, 
            img
        )

    def update(self, movement=None):
        """Custom Update.

        """
        self.setup_animation()
