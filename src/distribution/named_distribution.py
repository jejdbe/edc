
from .distribution_map import DistributionMap

class NamedDistribution(DistributionMap):

    data = {}

    def addElement(self, key, value):
        if key in self.data:
            raise Exception("Key", key, "already exists!")
        self.data[key] = value

    # Форматированный вывод в консоль
    def draw(self):
        max_k_len = 0
        max_v_len = 0
        for key in self.data.keys():
            max_k_len = max(max_k_len, len(key))
        for value in self.data.values():
            while value >= 1000:
                value /= 1000
            value = str(round(value, 1))
            max_v_len = max(max_v_len, len(value))

        for key, value in self.data.items():
            prefix = str(key) + ":"
            prefix += " " * (1 + max_k_len - len(prefix))
            
            units = ["кДж", "МДж", "ГДж", "ТДж", "ПДж", "ЭДж", "ЗДж", "ИДж"]
            unit = "Дж"
            for ux in units:
                if value >= 1000:
                    value /= 1000
                    unit = ux
                else:
                    break
            
            value = str(round(value, 1))
            value = " " * (max_v_len - len(value)) + value
            print(prefix, value, unit)


