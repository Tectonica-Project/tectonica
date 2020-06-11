from typing import List
from .vector import Vector
#from vector import Vector
import math

projection_index = lambda vec, axis: vec.rotated(axis.angle).x

# SAT: https://www.metanetsoftware.com/technique/tutorialA.html

def project_points_on_axis(points: List[Vector], axis: Vector):
    # Calculates the "shadow" of a set of connected points
    projected_points = [Vector(*point).project(axis) for point in points] 


    projected_points.sort(key = lambda vec: projection_index(vec, axis))

    # Now projected_points[0] is the start of our shadow
    # and projected_points[-1] is the end of it
    return projected_points


def draw_point_list(self, points: List[Vector], color='red', size=3):
    for i in points:
        self.draw_point(point=i, color=color, size=size)


def check_for_collision_on_1_shape_axis(points1: List[Vector], points2: List[Vector], debug_graph):
    points1 = [Vector(*i) for i in points1]
    points2 = [Vector(*i) for i in points2]


    colliding = True

    # First, check along the axes of the first pointset
    for idx, point_a in enumerate(points1):
        point_b = points1[(idx + 1) % len(points1)]

        line: Vector = point_b - point_a
        axis: Vector = line.rotated(math.pi * 1)

        points1_projected = project_points_on_axis(points1, axis)
        points2_projected = project_points_on_axis(points2, axis)


        """
        debug_graph.draw_line(
            point_from = points2_projected[0],
            point_to = points2_projected[-1],
            color='green',
            width=5,
        )


        debug_graph.draw_line(
            point_from = points1_projected[0],
            point_to = points1_projected[-1],
            color='red',
            width=3,
        )

        draw_point_list(debug_graph, points2_projected, color='blue')
        """
        # Correct floating point errors

        p11 = round(projection_index(points1_projected[0],axis), 100)
        p12 = round(projection_index(points1_projected[-1],axis), 100)
        p21 = round(projection_index(points2_projected[0],axis), 100)
        p22 = round(projection_index(points2_projected[-1],axis), 100)


        #debug_graph.draw_line(point_from = Vector(p21, 55), point_to = Vector(p22, 55))

        # Line collision detection  

        # If:

        # a = p11
        # b = p12
        # c = p21
        # d = p22

        # then this is true whenever the lines (a:b) and (c:d) are overlappnig

        # (a < b) && (c < d) && ( ((c > a) && (c < b)) ||  ((a > c) && (a < d)) || ((a > c) && (b < d))  || ((c > a) && (d < b)) ||  ((c < a) && (c > b)) || ((a < c) && (a > d)))

        # plugging it into wolphramalpha to simplify:

        # p12 > p11, p11 < p21 < p12, p22 > p21
        # p12 > p11, p21 < p11, p22 > p11
        


        if (((p12 > p11) and (p11 < p21 < p12) and (p22 > p21)) or 
            ((p12 > p11) and (p21 < p11) and (p22 > p11))):
            colliding = True
        else:
            colliding = False
            break

    if not colliding:
        return False

    return True


if __name__ == '__main__':
    axis = Vector(2,4)
    a = Vector(-3,0)
    b = Vector(-2,0)
    ap = a.project(axis)
    bp = b.project(axis)
    print(projection_index(ap, axis))
    print(projection_index(bp, axis))