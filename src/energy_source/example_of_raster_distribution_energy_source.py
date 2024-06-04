
from ..distribution.raster_distribution import RasterDistribution
from .energy_source import EnergySource

class ExampleOfRasterDistributionEnergySource(EnergySource):

    def calculateEnergyGenerationDistribution(self, path: str = "") -> RasterDistribution:
        map = RasterDistribution()
        width = 100
        height = 100
        tmp = {}
        for i in range(0, width*height):
            x = i % height
            y = i // height
            v = x + y
            tmp[(x, y)] = v
        for k, v in tmp.items():
            x, y = k
            map.addElement(x, y, v)
        return map

