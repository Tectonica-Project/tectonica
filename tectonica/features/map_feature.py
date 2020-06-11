import time
import threading
import math

import PySimpleGUI as sg

from ..physics.vector import Vector
from ..physics.separating_axis_theorem import project_points_on_axis, check_for_collision_on_1_shape_axis

def draw_vector(self, point_from,
        point_to,
        color="black",
        width=1):

    vec_from = Vector(*point_from)
    vec_to   = Vector(*point_to)
    vec_main = Vector(*point_to) - Vector(*point_from)
    
    # Returns tuple of 3 figure IDs
    id1 = self.draw_line(point_from, point_to, color=color, width=width)


    id2_vec = vec_main.rotated(math.radians(135)).normal * 10
    id3_vec = vec_main.rotated(math.radians(-135)).normal * 10

    id2 = self.draw_line(point_to, vec_to + id2_vec, color=color, width=width)
    id3 = self.draw_line(point_to, vec_to + id3_vec, color=color, width=width)

sg.Graph.draw_vector = draw_vector
    

class MapFeature():
    def init_map(self):

        self.points1 = [(20,-20), (20,20), (-20, 20), (-20,-20)]

        self.points2 = [(-40,-20), (10,-10), (-70, 30), (-50,-40)]

        self.shape2 = self.window['map_graph'].draw_polygon(self.points2, line_color='cyan')
        self.shape1 = self.window['map_graph'].draw_polygon(self.points1, line_color='red')
        self.prev_pos_1 = Vector(0,0)

        self.map_timer = 0

        self.map_ticking_thread = threading.Thread(target=self.tick_map)
        self.map_ticking_thread.start()

    map_timer: int

    def map_move_shape(self, pos):

        self.points1 = [(Vector(*i) + -(self.prev_pos_1 - Vector(*pos))) for i in self.points1]


        self.prev_pos_1 = Vector(*pos)


        self.update_shape()


    def update_shape(self):

        collides = check_for_collision_on_1_shape_axis(self.points1, self.points2, self.window['map_graph'])
        collides &= check_for_collision_on_1_shape_axis(self.points2, self.points1, self.window['map_graph'])

        self.window['colliding'].update('Colliding' if collides else 'Not colliding')
    
        self.window['map_graph'].delete_figure(self.shape1)        

        self.shape1 = self.window['map_graph'].draw_polygon(self.points1, line_color='red')
        


    def tick_map(self):
        self.map_timer += 1
        pass
