class World:
    def __init__(self, xsize, ysize, zsize, resolution, backend):
        self.model = backend(xsize, ysize, zsize, resolution)