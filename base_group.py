#-*- coding: utf-8 -*-

from pygame.sprite import RenderUpdates
from exceptions import Exception


class Group(RenderUpdates):
    """Default group.
    
    Same use as RenderUpdates groups.
    Custom use with draw function : Draw child.
    """
    __max_loop = 3
    loop = 0

    def draw(self, surface):
        spritedict = self.spritedict
        surface_blit = surface.blit
        dirty = self.lostsprites
        self.lostsprites = []
        dirty_append = dirty.append
        for s in self.sprites():
            childs = s.childs
            print childs.sprites()
            if childs.sprites() != []:
                dirty_append(childs.draw(surface))
            r = spritedict[s]
            newrect = surface_blit(s.image, s.rect)
            if r is 0:
                dirty_append(newrect)
            else:
                if newrect.colliderect(r):
                    dirty_append(newrect.union(r))
                else:
                    dirty_append(newrect)
                    dirty_append(r)
                    spritedict[s] = newrect
        return dirty
