#!/usr/bin/env python

import sys, pygame

class RangeViz:
    def __init__(self, max_range, num_arcs=8):
        self.max_range = max_range
        self.num_arcs = num_arcs
        
        # pixel measurements
        robot_radius = 20
        side_len = 500
        outer_arc = 200
        inner_arc = 40
        arc_gap = (outer_arc-inner_arc)/num_arcs
        
        pix_per_unit_dist = outer_arc/max_range
        
        pygame.init()
        
        pygame.display.set_caption('RangeViz')
        
        screen = pygame.display.set_mode((side_len, side_len))
        screen.fill((255,255,255))
        
        x = y = side_len/2
	pygame.draw.circle(screen, (0,0,255), (x,y), robot_radius, 1)
	pygame.draw.line(screen, (0,0,0), (x,y-robot_radius), (x,y), 1)
        
        for arc_num in range(num_arcs):
            pygame.draw.circle(screen, (150,150,150), (x,y), inner_arc+(arc_num*arc_gap), 1)
        
        start = inner_arc+((num_arcs-1)*arc_gap) + 10
        end = inner_arc - 10
        
        pygame.draw.line(screen, (0,0,0), (x,(side_len/2)-start), (x,(side_len/2)-end), 1)
        pygame.draw.line(screen, (0,0,0), ((side_len/2)-start,y), ((side_len/2)-end,y), 1)
        pygame.draw.line(screen, (0,0,0), (x+start,y), (x+end,y), 1)
        pygame.draw.line(screen, (0,0,0), (x,y+start), (x,y+end), 1)
        
        pygame.display.flip()
        
    def update(self, ranges):
    	for (theta, range_val) in ranges:
    	    pass
    	    
    def clear(self):
    	pass


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 1:
        RangeViz(int(args[0]))
    elif len(args) == 2:
    	RangeViz(int(args[0]), int(args[1]))
    else:
    	raise Exception("wrong number of arguments")
    
    while True:
    	for event in pygame.event.get():
    	    if event.type == pygame.QUIT:
    	        sys.exit()
