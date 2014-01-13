+---------------------------+
|                           |
|                           |
|       README.txt  =)      |
|                           |
+---------------------------+

This is some utils classes to use with pygames lib
Use to manage easier some complicated elements.

++ Classes
---> BaseEntity : Use like a Sprite.
     You can move it, stop it, and animate it (with BaseAnimation class)
     Can add your own fuctions to get what you want.

---> BaseAnimation : Use in BaseEntity.
     Help to manage animation of a Sprite.
     Manage max numbers of frame animation, frame duration
     between 2 frame animations, and get the good
     frame animation according to frame's number and frame's duration.
     Hard to manage so need some checks 
     (Depends mostly of your sprite animation)
     
     ########TODO#######
     Manage custom frame duration between each frame animation
     (Today, only the same duration is enable)
     ###################

--> BaseButton :
    Use to create Button with default behavior
    A button is a small (or big) area, where you can click and 
    provok a Event.
    To raise a event with a button, it need to be focused AND clicked
    (You can't click on button without focus, or you're amazing =) ).
     
--> BaseScreen :
    Use to manage screen of games
    Use for exec main_loop, update screen, and draw screen.
    In main file, you need only to use this updated screen.
    Enable to switch screen easier.
    Example :
    +------+         +------+
    | Game |  <----> | Menu |
    +------+      ^^ +------+
       ^^        //
       ||       //
       vv      //
    +-------+ //
    | Pause |//
    +-------+
    
    To do this, you can raise a ChangeScreenException to change screen.
    And catch this Exception in the main loop.

    So, you can change the used screen AND keep the screen in paused state 
    and used again if it's necessary (like game -> pause -> continue game
    or game -> paused -> save and exit)

    That's all for now. Need some checks and more options to manage more easily 
    a game's creation with PYGAME
