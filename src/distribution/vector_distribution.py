
from .distribution_map import DistributionMap

class VectorDistribution(DistributionMap):

    data = []
    max_value = 0.0
    x_min = 0.0
    x_max = 1.0
    y_min = 0.0
    y_max = 1.0

    def setBounds(self, x_min, y_min, x_max, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def addElement(self, points: list, value: float):
        self.data.append((points, value))
        self.max_value = max(value, self.max_value)

    def draw(self):
        # matplotlib: Colormap name (e.g., 'viridis', 'plasma', 'inferno', 'magma', 'cividis')
        # https://matplotlib.org/stable/users/explain/colors/colormaps.html
        
        # seaborn: "icefire", "rocket", "mako", "flare", "crest", "magma", "viridus", "cubehelix" ...
        # https://seaborn.pydata.org/tutorial/color_palettes
        

        import matplotlib.pyplot as plt
        import matplotlib.patches as patches
        import seaborn as sns

        # polygons = [
        #     ([(1, 1), (2, 3), (3, 1), (1, 1)], 0.5),
        #     ([(3, 2), (4, 4), (5, 2), (3, 2)], 1.2),
        #     ([(2, 5), (3, 6), (4, 5), (2, 5)], 2.8), 
        # ]
        polygons = self.data

        # sns.set_theme()

        # cmap = plt.cm.cividis
        cmap = sns.color_palette("icefire", as_cmap=True)

        fig, ax = plt.subplots()

        for polygon, value in polygons:
            poly = patches.Polygon(polygon, closed=True)

            # color = cmap(value / 3.0)  # Normalize to [0, 1] range
            color = plt.cm.viridis(value / self.max_value)  # Normalize to [0, 1] range
            poly.set_facecolor(color)

            ax.add_patch(poly)

        # ax.set_xlim(0, 6)
        # ax.set_ylim(0, 7)

        ax.set_xlim(self.x_min, self.x_max)
        ax.set_ylim(self.y_min, self.y_max)

        # sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=0, vmax=3))
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=0, vmax=self.max_value))
        sm.set_array([])  # Dummy array for colorbar
        cbar = fig.colorbar(sm, ax=ax)
        cbar.set_label('Value')

        plt.show()




