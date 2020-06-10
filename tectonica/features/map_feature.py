import time
import threading
import math

import PySimpleGUI as sg

from ..physics.vector import Vector

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

        v1 = Vector(40, 20)
        v2 = Vector(100, 10)

        self.window['map_graph'].draw_vector(
            point_from=(0,0),
            point_to=v1,
            color="red",
        )
        self.window['map_graph'].draw_vector(
            point_from=(0,0),
            point_to=v2,
            color="#BADA55",
        )
        self.window['map_graph'].draw_vector(
            point_from=(0,0),
            point_to=v1.project(v2),
            color="orange",
        )

        self.map_timer = 0

        self.map_ticking_thread = threading.Thread(target=self.tick_map)
        self.map_ticking_thread.start()

    map_timer: int

    def tick_map(self):
        self.map_timer += 1
        pass
