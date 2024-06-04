
from ..data_reader.json_reader import JSONReader
from ..distribution.named_distribution import NamedDistribution
from .energy_source import EnergySource
from pathlib import Path

class CowDungEnergySource(EnergySource):

    def calculateEnergyGenerationDistribution(self, path: str = "") -> NamedDistribution:

        # Поголовье коров по данным Росстат на 1 октября 2023 года
        number_of_cows = JSONReader.read(Path(path) / "number_of_cows.json")

        # Прочие данные
        properties = JSONReader.read(Path(path) / "properties.json")
        
        # Масса коровы, кг
        cow_mass = properties["cow_mass"]

        # Масса навоза от одной коровы за сутки, кг
        dung_mass = cow_mass * properties["dung_mass_coefficient"]
        
        # Количество биогаза на килограмм навоза, м^3/кг
        amount_of_biogas_per_kilogram_of_dung = properties["amount_of_biogas_per_kilogram_of_dung"]

        # Доля метана в биогазе
        methane_share_in_biogas = properties["methane_share_in_biogas"]
        
        # Плотность метана, кг/м^3
        density_of_methane = properties["density_of_methane"]
        
        # Удельная теплота сгорания метана, Дж/кг
        calorific_value_of_methane = properties["calorific_value_of_methane"]

        # КПД генератора, сжигающего метан
        efficiency = properties["efficiency"]

        # Объём биогаза, вырабатываемый одной коровой за сутки, м^3
        biogas_volume = dung_mass * amount_of_biogas_per_kilogram_of_dung
        
        # Объём метана, вырабатываемый одной коровой за сутки, м^3
        methane_volume = biogas_volume * methane_share_in_biogas
        
        # Масса метана, вырабатываемая одной коровой за сутки, кг
        methane_mass = methane_volume * density_of_methane

        # Энергия, выделяемая при сгорании метана, вырабатываемого одной коровой за сутки, Дж
        energy_per_day = methane_mass * calorific_value_of_methane

        # Энергия, выделяемая при сгорании метана, вырабатываемого одной коровой за год, Дж
        energy_per_year = energy_per_day * 365

        map = NamedDistribution()
        for k, v in number_of_cows.items():
            map.addElement(k, v * energy_per_year * efficiency)
        return map


