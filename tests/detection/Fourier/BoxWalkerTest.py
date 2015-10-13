from src.detection.fourier.BoxWalker import BoxWalker
import unittest
from src.base.Bbox import Bbox



class TestImageLoader(unittest.TestCase):
    def test_Boxwalker(self):
        bbox = self.Rappi()
        walker = BoxWalker(bbox)
        walker.loadData()
        crosswalkNodes = walker.walk()

        proxy = walker.proxy
        tile = proxy.getBigTile(bbox.getDownLeftPoint(),bbox.getUpRightPoint())
        tile.startDrawing()
        for node in crosswalkNodes:
            point = node.toPoint()
            tile.drawPoint(point)

        tile.stopDrawing()
        tile.plot()


        #print str(len(crosswalkNodes)) + " crosswalks found!"

    def ZurichBellvue(self):
        return Bbox(8.54279671719532, 47.366177501999516, 8.547088251618977, 47.36781249586627)

    def Rappi(self):
        return Bbox(8.814650, 47.222553, 8.825035, 47.228935)
