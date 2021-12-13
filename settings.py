#modules
import math, threading
from Vector import *

#values
FPS = 25
width  = 1920
height = 1000
s_width  = 11
s_height = 20
p_width   = int(width/s_width)
p_height  = int(height/s_height)
text_size = 18
aspect  = (width/height)
size = (width, height)
fragments = 1
sphere_pos = vec3(0, 0, 0)
radius = 1
box_pos = vec3(0, 2, 0)
box_size = 1
speed = 0.5

#colors
white  = (255, 255, 255)
black  = (15,  15,  15 )
red    = (255, 0,   0  )
green  = (0,   255, 0  )
blue   = (0,   0,   255)
dark   = (100, 100, 100)
gray   = (200, 200, 200)
purple = (120, 0,   120)
yellow = (120, 120, 0  )
cylan  = (0,   120, 120)

#constants
PI = 3.1415926535

#gradient
l_gradient = ' >`>.>:>~>!>/>r>(>l>1>Z>4>H>9>W>8>$>@'.split('>')
r_gradient = ' >`>.>:>~>!>\>r>)>l>1>Z>4>H>9>W>8>$>@'.split('>')

#3D objects
camera_pos = vec3(-5, 0, 0)
camera_rot = vec3( 0, 0, 0)/360 * PI