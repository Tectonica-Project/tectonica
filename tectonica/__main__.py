import PySimpleGUI as sg
import threading

from .features.map_feature import MapFeature
from .physics.vector import Vector



class MainGame(
    MapFeature,
    ):
    window: sg.Window
    layout: list

    def __init__(self):
        sg.theme('Dark Blue 3')  # please make your windows colorful

    def open_window(self):



        self.layout = [
            [sg.Graph(
                canvas_size=(400,200), 
                # Use latitude/longitude as graph coordinates
                graph_bottom_left=(-180, 90), 
                graph_top_right = (180,-90), 
                enable_events = True,
                key='map_graph'
            )],
            [sg.Text(size=(12,1), key='colliding')],
            [sg.Text('Your typed chars appear here:'), sg.Text(size=(12,1), key='-OUTPUT-')],
            [sg.Input(key='-IN-')],
            [sg.Button('Show'), sg.Button('Exit')]]

        self.window = sg.Window('Window Title', self.layout)
        self.window.Finalize()

        return self

    def run(self):
        self.init_map()



        while True:  # Event Loop
            event, values = self.window.read()
            print(event, values)
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            elif event == 'Show':
                # change the "output" element to be the value of "input" element
                self.window['-OUTPUT-'].update(values['-IN-'])
            elif event == 'map_graph':
                self.map_move_shape(values['map_graph'])


        self.window.close()

        return self


if __name__ == '__main__':
    game = MainGame().open_window().run()