import math, pygame

from settings import *
from  Vector  import *

def sphere(ro: vec3, rd: vec3, r: float):
    b = vec3.dot(ro, rd)
    c = vec3.dot(ro, ro) - r**2
    h = b**2 - c
    if h < 0:
        return vec2(-1, -1)
    h = math.sqrt(h)
    return vec2(-b - h, -b + h)

def box(ro: vec3, rd: vec3, Bsize: vec3, norm: vec3):
    m = vec3(1, 1, 1) / rd
    n = m * ro
    k = vec3(abs(m.x), abs(m.y), abs(m.z)) * Bsize
    t1 = -n -k
    t2 = -n + k
    tN = max(max(t1.x, t1.y), t1.z)
    tF = min(min(t2.x, t2.y), t2.z)
    if tN > tF or tF < 0:
        return vec2(-1, -1, -1)
    yzx = vec3(t1.y, t1.z, t1.x)
    zxy = vec3(t1.z, t1.x, t1.y)
    norm = -sign(rd) * step(yzx, t1) * step(zxy, t1)
    return vec2(tN, tF)

def plane(ro: vec3, rd: vec3, p: vec3, w: float):
    return -(vec3.dot(ro, p) + w) / vec3.dot(rd, p)

def clamp(value, vmin, vmax):
    return max(min(value, vmax), vmin)

def render(window, font, t, fragment, camera_pos):
    light = vec3(math.sin(t*0.25), math.cos(t*0.25), 1).normalize()
    y = p_height//fragments * fragment
    for y in range(int(p_height)):
        for x in range(int(p_width)):
            uv = vec2((x/p_width*2-1)* aspect, y/p_height*2-1)
            ray_vel = vec3(1, uv.x, uv.y).normalize()
            diff = 1
            minIt = 99999
            for k in range(5):
                intersection = sphere(camera_pos - sphere_pos, ray_vel, radius)
                n = vec3(0, 0, 0)
                albedo = 1
                if intersection.x > 0:
                    itPoint = camera_pos - shere_pos + ray_vel * intersection.x
                    minIt = intersection.x
                    n = itPoint.norm()
                boxN = vec3(0, 0, 0)
                intersection = box(camera_pos - box_pos, ray_vel, box_size, boxN)
                if intersection.x > 0 and intersection.x < minIt:
                    itPoint = camera_pos - sphere_pos + ray_vel * intersection.x
                    n = boxN
                intersection = plane(camera_pos, ray_vel, vec3(0, 0, -1), 1)
                if intersection.x > 0 and intersection.x < minIt:
                    minIt = intersection.x
                    albedo = 0.5
                    n = vec3(0, 0, -1)
                if minIt < 99999:
                    diff *= float(vec3.dot(light, n) * 0.5 + 0.5) * albedo
                    camera_pos += ray_vel * (minIt - 0.01)
                    ray_vel = vec3.reflect(ray_vel, n)
                else:
                   break
            c = color(clamp(diff, 0, 1), x >= (p_width/2))
            CMD_screen = font.render(c, True, green, black)
            window.blit(CMD_screen, (x*s_width+(s_width/2), y*s_height))

def color(v: float, r: bool):
    if r:
        return r_gradient[int(clamp(v*len(r_gradient), 0, len(r_gradient)-1))]
    else:
        return l_gradient[int(clamp(v*len(l_gradient), 0, len(l_gradient)-1))]
