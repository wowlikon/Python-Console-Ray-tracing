import math, random

def step(a, b):
    return b > a

class vec2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return vec2(self.x + other.x, self.y + other.y)
        return vec2(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return vec2(self.x - other.x, self.y - other.y)
        return vec2(self.x - other, self.y - other)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return vec2(self.x * other.x, self.y * other.y)
        return vec2(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            return vec2(self.x / other.x, self.y / other.y)
        return vec2(self.x / other, self.y / other)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        return self.x == other and self.y == other
    
    def make_int_turple(self):
        return int(self.x), int(self.y)

    def set(self, vect):
        self.x = vect.x
        self.y = vect.y

    def dot(vect1, vect2):
        return vect1.x * vect2.x + vect1.y * vect2.y

    def angle_between(vect1, vect2):
        return math.acos(vec2.dot(vect1, vect2))

    def angle(self):
        return math.acos(self.dot(vec2(1, 0)))

    def lenght(vect):
        return math.sqrt(vect.x**2 + vect.y**2)

    def dist(vect1, vect2):
        vect = vect1 - vect2
        return vect.lenght()

    def normalize(vect):
        vect_len = lenght(vect)
        if vect_len < 0.00001:
            return vec2(0, 1)
        return vec2(vect.x/vect_len, vect.y/vect_len)

    def reflect(incident, normal):
        return incident - dot(normal, incident) * 2 * normal

    def negate(vect):
        return vec2(-vect.x, -vect.y)

    def right(vect):
        return vec2(-vect.y, vect.x)

    def left(vect):
        return negate(right(vect))

    def random_vector():
        return vec2(random.random()*2-1, random.random()*2-1)

    def random_direction():
        return normalize(random_vector())

    def copy(vect):
        return vec2(vect.x, vect.y)

    def rotate(self, a: float):
        a = float(a.x)
        new_x = ( self.x * math.cos(a)) - (-self.y * math.sin(a))
        new_y = (-self.y * math.cos(a)) + ( self.x * math.sin(a))
        return vec2(new_x, new_y)

class vec3:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        return vec3(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        return vec3(self.x - other, self.y - other, self.z - other)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        return vec3(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            return vec3(self.x / other.x, self.y / other.y, self.z / other.z)
        return vec3(self.x / other, self.y / other, self.z / other)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return self.x == other and self.y == other and self.z == other
    
    def make_int_turple(self):
        return int(self.x), int(self.y), int(self.z)

    def set(self, vect):
        self.x = vect.x
        self.y = vect.y
        self.z = vect.z

    def dot(vect1, vect2):
        return vect1.x * vect2.x + vect1.y * vect2.y + vect1.z * vect2.z

    def angle_between(vect1, vect2):
        return math.acos(vec3.dot(vect1, vect2))

    def lenght(vect):
        return (vect.x**2 + vect.y**2 + vect.z**2)**(1/2)

    def dist(vect1, vect2):
        vect = vect1 - vect2
        return vect.lenght()

    def normalize(vect):
        vect_len = vect.lenght()
        if vect_len < 0.00001:
            return vec3(0, 1, 0)
        return vec3(vect.x/vect_len, vect.y/vect_len, vect.z/vect_len)

    def reflect(incident, normal):
        return incident - normal * (2*vec3.dot(normal, incident))

    def negate(vect):
        return vec3(-vect.x, -vect.y, -vect.z)

    def right(vect):
        return vec3(-vect.y, vect.x, vect.z)

    def left(vect):
        return negate(right(vect))

    def random_vector():
        return vec3(random.random()*2-1, random.random()*2-1, random.random()*2-1)

    def random_direction():
        return normalize(random_vector())

    def copy(vect):
        return vec3(vect.x, vect.y, vect.z)

    def rotateX(self, angle):
        return vec3(X, self.x*math.cos(angle)-self.y*math.sin(angle), self.x*math.sin(angle)+self.y*math.cos(angle))

    def rotateY(self, angle):
        return vec3(self.x*math.cos(angle)-self.y*math.sin(angle), Y, self.x*math.sin(angle)+self.y*math.cos(angle))

    def rotateZ(self, angle):
        return vec3(self.x*cos(angle)-self.y*math.sin(angle), self.x*math.sin(angle)+self.y*math.cos(angle), Z)

    def rotate(self, angles):
        vector = self
        vector = vector.rotateX(angles.x)
        vector = vector.rotateY(angles.y)
        vector = vector.rotateZ(angles.z)
        return vector

    def sign(self):
        return vec3(sign(self.x), sign(self.y), sign(self.z))

    def step(self, edge):
        return vec3(step(edge.x, self.x), step(edge.y, self.y), step(edge.z, self.z))