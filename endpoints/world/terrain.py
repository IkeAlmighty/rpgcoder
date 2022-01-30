from perlin_noise import PerlinNoise

WORLD_WIDTH, WORLD_HEIGHT = (10000, 10000)

def get_height(x, y): 
    noise = PerlinNoise()
    return noise([x/WORLD_WIDTH, y/WORLD_HEIGHT]) #TODO: idk if this works

def get_height_matrix(x, y, width, height): pass

def get_height_radius(x, y, width, height): pass

