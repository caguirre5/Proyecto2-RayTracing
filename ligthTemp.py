import glMath as gm 

DIR_LIGHT = 0
POINT_LIGHT = 1
AMBIENT_LIGHT = 2


def reflectVector(normal, direction):
    reflect = 2 * gm.Dot(normal, direction)
    reflect = gm.trans(normal, reflect)
    reflect = gm.Substract(reflect, direction)
    reflect = gm.Normalize(reflect)
    return reflect


def refractVector(normal, direction, ior):
    # Snell's Law
    cosi = max(-1, min(1, gm.Dot(direction, normal)))
    etai = 1
    etat = ior

    if cosi < 0:
        cosi = -cosi
    else:
        etai, etat = etat, etai
        normal = gm.trans(normal,-1)

    eta = etai / etat
    k = 1 - (eta**2) * (1 - (cosi**2))

    if k < 0:  # Total Internal Reflection
        return None

    M1 = gm.trans(direction, eta)
    temp = eta * cosi - k**0.5
    M2 = gm.trans(normal, temp)

    R = gm.Add(M1,M2)
    return R


def fresnel(normal, direction, ior):
    # Fresnel Equation
    cosi = max(-1, min(1, gm.Dot(direction, normal)))
    etai = 1
    etat = ior

    if cosi > 0:
        etai, etat = etat, etai

    sint = etai / etat * (max(0, 1 - cosi**2) ** 0.5)

    if sint >= 1:  # Total Internal Reflection
        return 1

    cost = max(0, 1 - sint**2) ** 0.5
    cosi = abs(cosi)

    Rs = ((etat * cosi) - (etai * cost)) / ((etat * cosi) + (etai * cost))
    Rp = ((etai * cosi) - (etat * cost)) / ((etai * cosi) + (etat * cost))

    return (Rs**2 + Rp**2) / 2


class DirectionalLight(object):
    def __init__(self, direction=(0, -1, 0), intensity=1, color=(1, 1, 1)):
        self.direction = gm.Normalize(direction)
        self.intensity = intensity
        self.color = color
        self.lightType = DIR_LIGHT

    def getDiffuseColor(self, intersect, raytracer):
        light_dir = gm.trans(self.direction,-1)
        intensity = gm.Dot(max(0, intensity))

        diffuseColor = [intensity * self.color[0],
                                 intensity * self.color[1],
                                 intensity * self.color[2]]

        return diffuseColor

    def getSpecColor(self, intersect, raytracer):
        light_dir = gm.trans(self.direction,-1)
        reflect = reflectVector(intersect.normal, light_dir)

        view_dir = gm.Substract(raytracer.camPosition, intersect.point)
        view_dir = gm.Normalize(view_dir)

        spec_intensity = self.intensity * \
            max(0, gm.Dot(view_dir, reflect)) ** intersect.sceneObj.material.spec
        specColor = [spec_intensity * self.color[0],
                              spec_intensity * self.color[1],
                              spec_intensity * self.color[2]]

        return specColor

    def getShadowIntensity(self, intersect, raytracer):
        light_dir = gm.trans(self.direction,-1)

        shadow_intensity = 0
        shadow_intersect = raytracer.scene_intersect(
            intersect.point, light_dir, intersect.sceneObj)
        if shadow_intersect:
            shadow_intensity = 1

        return shadow_intensity


class PointLight(object):
    def __init__(self, point, attenuation, constant=1.0, linear=0.1, quad=0.05, color=(1, 1, 1)):
        self.point = point
        self.attenuation = attenuation
        self.constant = constant
        self.linear = linear
        self.quad = quad
        self.color = color
        self.lightType = POINT_LIGHT

    def getDiffuseColor(self, intersect, raytracer):
        light_dir = gm.Substract(self.point, intersect.point)
        light_dir = gm.Normalize(light_dir)

        intensity = gm.Dot(intersect.normal, light_dir) * self.attenuation
        intensity = float(max(0, intensity))

        diffuseColor = [intensity * self.color[0],
                                 intensity * self.color[1],
                                 intensity * self.color[2]]

        return diffuseColor

    def getSpecColor(self, intersect, raytracer):
        light_dir = gm.Substract(self.point, intersect.point)
        light_dir = gm.Normalize(light_dir)

        reflect = reflectVector(intersect.normal, light_dir)

        view_dir = gm.Substract(raytracer.camPosition, intersect.point)
        view_dir = gm.Normalize(view_dir)

        attenuation = 1.0

        spec_intensity = attenuation * \
            max(0, gm.Dot(view_dir, reflect)) ** intersect.sceneObj.material.spec
        specColor = [spec_intensity * self.color[0],
                              spec_intensity * self.color[1],
                              spec_intensity * self.color[2]]

        return specColor

    def getShadowIntensity(self, intersect, raytracer):
        light_dir = gm.Substract(self.point, intersect.point)
        light_distance = gm.NormLength(light_dir)
        light_dir = light_dir / light_distance

        shadow_intensity = 0
        shadow_intersect = raytracer.scene_intersect(
            intersect.point, light_dir, intersect.sceneObj)
        if shadow_intersect:
            if shadow_intersect.distance < light_distance:
                shadow_intensity = 1

        return shadow_intensity


class AmbientLight(object):
    def __init__(self, intensity=0.1, color=(1, 1, 1)):
        self.intensity = intensity
        self.color = color
        self.lightType = AMBIENT_LIGHT

    def getDiffuseColor(self, intersect, raytracer):
        return gm.trans(self.color, self.intensity)

    def getSpecColor(self, intersect, raytracer):
        return [0, 0, 0]

    def getShadowIntensity(self, intersect, raytracer):
        return 0
