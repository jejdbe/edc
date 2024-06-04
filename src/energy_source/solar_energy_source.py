
from ..distribution.named_distribution import NamedDistribution
from .energy_source import EnergySource

class SolarEnergySource(EnergySource):

    def calculateEnergyGenerationDistribution(self, path: str = "") -> NamedDistribution:
        map = NamedDistribution()
        map.addElement('Adygea', 1)
        return map


