"""checking point"""

__author__ = "730649788"

from CQs.cq09.point import Point

original_point = Point(3.0, 4.0)

original_point.scale_by(2)
print(f"After scale_by(2): x= {original_point.x}, y={original_point.y}")

new_point = original_point.scale(2)
print(f"Original point after scale(2): x = {original_point.x}, y= {original_point.y}")
print(f"New scaled point: x = {new_point.x}, y= {new_point.y}")
