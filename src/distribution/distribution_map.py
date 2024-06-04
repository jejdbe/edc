
class DistributionMap:
    
    data = []    # Данные распределения

    def addElement(self, value):
        self.data.append(value)

    def draw(self):
        print(self.data)


