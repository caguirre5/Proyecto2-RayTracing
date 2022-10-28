from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 512
height = 320

centrox = 0
centroy = -1
centroz = 0

# Materiales

aluminium = Material(diffuse=(0.9, 0.9, 0.9))
nasa = Material(texture=Texture("txnasa.bmp"))
stone = Material(diffuse=(0.4, 0.4, 0.4), spec=8)
earth = Material(texture=Texture("txearthDay.bmp"))
moon = Material(texture=Texture("txmoon.bmp"))
sun = Material(texture=Texture("txsun.bmp"))
saturn = Material(texture=Texture("txsaturn.bmp"))
jupiter = Material(texture=Texture("txjupiter.bmp"))
mars = Material(texture=Texture("txmars.bmp"))
venus = Material(texture=Texture("txvenus.bmp"))
uranus = Material(texture=Texture("txuranus.bmp"), diffuse=(0.3, 0.8, 0.8),
                  spec=16, matType=REFLECTIVE)
pluton = Material(texture=Texture("txpluton.bmp"))
mercury = Material(texture=Texture("txmercury.bmp"))
glass = Material(diffuse=(0.7, 0.7, 0), spec=64,
                 ior=1.5, matType=TRANSPARENT)

rtx = Raytracer(width, height)
rtx.envMap = Texture("Galaxia2.bmp")

# Lights
rtx.lights.append(AmbientLight(intensity=0.2))
rtx.lights.append(PointLight(point=(-5, 5, -35), attenuation=1.0))
rtx.lights.append(PointLight(point=(-5, 5, -65), attenuation=1.0))

#               PLANETS

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
rtx.scene.append(Sphere(V3(-3, -0.8, -5), 0.5, glass))
rtx.scene.append(AABB(position=(-3, -1.5, -5),
                 size=(1, 1, 1), material=nasa))
rtx.scene.append(AABB(position=(-3.4, -2, -4.6),
                 size=(0.1, 1, 0.2), material=aluminium))
rtx.scene.append(AABB(position=(-3.4, -2, -5.4),
                 size=(0.1, 1, 0.2), material=aluminium))
rtx.scene.append(AABB(position=(-2.6, -2, -4.6),
                 size=(0.1, 1, 0.2), material=aluminium))
rtx.scene.append(AABB(position=(-2.6, -2, -5.4),
                 size=(0.1, 1, 0.2), material=aluminium))

rtx.glRender()

rtx.glFinish("MateTest.bmp")
