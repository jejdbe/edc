
from .distribution_map import DistributionMap

class RasterDistribution(DistributionMap):

    data = {}

    def addElement(self, x, y, value):
        key = (x, y)
        if key in self.data:
            raise Exception("Key", key, "already exists!")
        self.data[key] = value

    def draw(self):
        d = []
        for (x, y), v in self.data.items():
          d.append((x, y, v))

        import seaborn as sns
        import matplotlib.pyplot as plt
        import pandas as pd

        df = pd.DataFrame(d, columns=['x', 'y', 'v'])
        heatmap_data = df.pivot(index='y', columns='x', values='v')
        sns.heatmap(heatmap_data, cmap='icefire', annot=False)
        plt.show()


