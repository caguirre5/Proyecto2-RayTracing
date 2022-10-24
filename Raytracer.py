from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 1080
height = 720

centrox = 0
centroy = -1
centroz = 0

# Materiales

aluminium = Material(diffuse=(0.3, 0.3, 0.3), spec=16, matType=REFLECTIVE)
stone = Material(diffuse=(0.4, 0.4, 0.4), spec=8)
earth = Material(texture=Texture("earthDay.bmp"))
moon = Material(texture=Texture("moon.bmp"))
sun = Material(texture=Texture("sun.bmp"))
saturn = Material(texture=Texture("saturn.bmp"))
jupiter = Material(texture=Texture("jupiter.bmp"))
mars = Material(texture=Texture("mars.bmp"))
venus = Material(texture=Texture("venus.bmp"))
uranus = Material(texture=Texture("uranus.bmp"))
pluton = Material(texture=Texture("pluton.bmp"))
mercury = Material(texture=Texture("mercury.bmp"))
mirror = Material(diffuse=(0.9, 0.9, 0.9), spec=64, matType=REFLECTIVE)
glass = Material(diffuse=(0.9, 0.9, 0.9), spec=64,
                 ior=1.5, matType=TRANSPARENT)

rtx = Raytracer(width, height)
rtx.envMap = Texture("Galaxia.bmp")

rtx.lights.append(AmbientLight(intensity=0.1))
rtx.lights.append(PointLight(point=(-5, 5, -35), attenuation=1.0))
rtx.lights.append(PointLight(point=(-5, 5, -65), attenuation=1.0))
# rtx.lights.append(PointLight(point=(-10, -2, 20), attenuation=0.1))

# Jupiter
rtx.scene.append(Sphere(V3(10, -4, -10), 6, jupiter))

# Earth
rtx.scene.append(Sphere(V3(13, 0, -35), 7, earth))
#       Moon
rtx.scene.append(Sphere(V3(4, -2, -16), 1, moon))

# Mars
rtx.scene.append(Sphere(V3(24, 13, -40), 5.5, mars))

# Venus
rtx.scene.append(Sphere(V3(-3, -4, -12), 1.5, venus))

# Planet2
rtx.scene.append(Sphere(V3(-12, -2, -30), 1.5, uranus))

# Sun
rtx.scene.append(Sphere(V3(-5, 5, -50), 10, sun))

# Saturn
rtx.scene.append(Sphere(V3(-8, 1, -12), 1, saturn))
rtx.scene.append(Torus(position=(-8, 1, -12), radius=2,
                 normal=(0, 1, 0), material=saturn))

# Planet3
rtx.scene.append(Sphere(V3(-8, 4.5, -16), 1, pluton))

# Planet5
rtx.scene.append(Sphere(V3(-8, 11, -25), 1, mercury))

# Satelite
rtx.scene.append(Sphere(V3(-3, -1, -5), 0.5, glass))
rtx.scene.append(AABB(position=(-3, -1.5, -5),
                 size=(1, 1, 1), material=aluminium))
rtx.scene.append(AABB(position=(-3.4, -2.5, -4.6),
                 size=(0.1, 1, 0.2), material=aluminium))
rtx.scene.append(AABB(position=(-3.4, -2.5, -5.4),
                 size=(0.1, 1, 0.2), material=aluminium))
rtx.scene.append(AABB(position=(-2.6, -2.5, -4.6),
                 size=(0.1, 1, 0.2), material=aluminium))
rtx.scene.append(AABB(position=(-2.6, -2.5, -5.4),
                 size=(0.1, 1, 0.2), material=aluminium))

rtx.glRender()

rtx.glFinish("output.bmp")
