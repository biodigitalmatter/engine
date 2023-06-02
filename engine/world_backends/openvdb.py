import pyopenvdb as vdb
from compas.geometry import Point


class Grid:
    """Syntactic sugar for pyopenvdb.FloatGrid where inactive voxels are 0"""

    def __init__(self, transform=None):
        self.vdb = vdb.FloatGrid()
        self.vdb.transform = transform or vdb.createLinearTransform()
        self.accessor = self.vdb.getAccessor()

    def world_to_index(self, xyz: [float]):
        ijk = self.vdb.transform.worldToIndex(xyz)
        return [int(f) for f in ijk]

    def __getitem__(self, xyz):
        ijk = self.world_to_index(xyz)
        value, on = self.accessor.probeValue(ijk)

        return value if on else 0.0

    def __setitem__(self, xyz, value):
        ijk = self.world_to_index(xyz)
        self.accessor.setValueOn(xyz, value=value)

    def __delitem__(self, xyz):
        ijk = self.world_to_index(xyz)
        self.accessor.setValueOff(ijk)


class OpenVDBBackend:
    def __init__(self):
        self.grids: Grid = {}
        self.transform = vdb.createLinearTransform()

    def __getitem__(self, key):
        self._raise_if_grid_doesnt_exist(key)
        return self.grids[key]

    def _raise_if_grid_doesnt_exist(self, name):
        if name not in self.grids:
            raise RuntimeError(f"No grid named {name}.")

    def update_transform(self, transform):
        # TODO: Convert input xform to pyopenvdb xform
        self.transform = transform
        for name in self.grids:
            self.grids[name].transform = self.transform

    def create_new_grid(self, name):
        if name in self.grids:
            raise RuntimeError(f"Grid with name {name} already exists.")
        self.grids[name] = Grid(transform=self.transform)
