
from ..distribution.named_distribution import NamedDistribution
from .energy_source import EnergySource

class WindEnergySource(EnergySource):

    def calculateEnergyGenerationDistribution(self, path: str = "") -> NamedDistribution:
        map = NamedDistribution()
        map.addElement('Adygea', 2)
        return map


