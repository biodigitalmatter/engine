import pytest
import pyopenvdb as vdb
from engine.world_backends.openvdb import OpenVDBBackend, Grid


class TestGrid:
    def test_init(self):
        # Test if Grid initializes correctly
        transform = vdb.createLinearTransform()
        g = Grid(transform=transform)
        assert isinstance(g.vdb, vdb.FloatGrid)

    def test_set_get(self):
        # Test if Grid sets and gets values correctly
        transform = vdb.createLinearTransform()
        g = Grid(transform=transform)
        assert g[0, 0, 0] == 0.0
        g[0, 0, 0] = 1.0
        assert g[0, 0, 0] == 1.0

    def test_remove(self):
        # Test if Grid removes values correctly
        transform = vdb.createLinearTransform()
        g = Grid(transform)
        g[0, 0, 0] = 1.0
        del g[0, 0, 0]
        assert g[0, 0, 0] == 0


class TestOpenVDBBackend:
    def test_constructor(self):
        backend = OpenVDBBackend()
        assert isinstance(backend.transform, vdb.Transform)
        assert backend.grids == {}

    def test_get_grid(self):
        backend = OpenVDBBackend()
        backend.create_new_grid("test_grid")
        grid = backend["test_grid"]
        assert isinstance(grid, Grid)
        assert "test_grid" in backend.grids
        assert grid.vdb.transform == backend.transform
        assert grid[0, 0, 0] == 0.0

    def test_set_value(self):
        backend = OpenVDBBackend()
        backend.create_new_grid("test_grid")
        backend["test_grid"][1, 2, 3] = 2.0
        grid = backend["test_grid"]
        assert grid[1, 2, 3] == 2.0

    def test_remove_value(self):
        backend = OpenVDBBackend()
        backend.create_new_grid("test_grid")
        backend["test_grid"][1, 2, 3] = 2.0
        del backend["test_grid"][1, 2, 3]
        grid = backend["test_grid"]
        assert grid[1, 2, 3] == 0.0

    def test_remove_value_raises(self):
        backend = OpenVDBBackend()
        with pytest.raises(RuntimeError):
            del backend["not_a_grid"][1, 2, 3]
