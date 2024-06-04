
# https://pypi.org/project/pyshp/
import shapefile
from geographiclib.geodesic import Geodesic

import math

from ..data_reader import DataReader
from ...distribution.vector_distribution import VectorDistribution

# OpenStreetMap
# https://www.openstreetmap.org/
# https://download.geofabrik.de/
class OSMShpReader(DataReader):
    # features - список строк: обозначений того, что находится в каждом полигоне, например, лес, луг или сельскохозяйственные угодья, которые подходят для решения задачи
    def read(path: str, features: list = []) -> VectorDistribution:

        sf = shapefile.Reader(path)
        if sf.shapeType == shapefile.POLYGON:
            print("Reading Shapefile: Meta-Data type is POLYGON")
        else:
            raise RuntimeError("Reading Shapefile: Meta-Data type must be POLYGON")
        print("Reading Shapefile: number of features:", len(sf))
        print("Reading Shapefile: bounding box area:", sf.bbox)

        map = VectorDistribution()
        map.setBounds(sf.bbox[0], sf.bbox[1], sf.bbox[2], sf.bbox[3])
        hasNan = False
        isCorrupted = False
        # c = 0
        for shaperec in sf.iterShapeRecords():
            # print(shaperec.__dict__)
            # print(shaperec.record)
            if shaperec.record[2] in features or len(features) == 0:
                # Считаем на эллипсоиде
                polygon = Geodesic.WGS84.Polygon()
                points = shaperec.shape.points
                # print(points)
                if points[0] != points[-1]:
                    isCorrupted = True
                for x, y in points:
                    polygon.AddPoint(x, y)
                num, perimeter, area = polygon.Compute()
                # print(num, perimeter, area)
                if math.isnan(area):
                    hasNan = True
                else:
                    map.addElement(points, area)
            # c += 1
            # if c == 100:
            #     break
        if isCorrupted:
            print("Часть данных повреждена или имеет необычный формат")
        if hasNan:
            print("Площадь некоторых полигонов вычислить не удалось")
        
        return map
