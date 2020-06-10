import time
from math import sin

class MapFeature():
    def init_map(self):
        self.circle_figure = self.window['map_graph'].DrawCircle(
            (10,10), 
            radius=30, 
            fill_color="#BADA55"
        )

    def tick_map(self):
        for i in range(30):
            self.global_timer += 1
            time.sleep(1/30)

            self.window['map_graph'].MoveFigure(self.circle_figure, sin(self.global_timer / 6 ) * 10, 0)