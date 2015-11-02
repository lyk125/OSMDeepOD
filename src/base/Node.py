from geopy import Point
from geopy.distance import vincenty
from src.data.globalmaptiles import GlobalMercator


class Node(Point):
    def __init__(self, lat = 0.0, lon = 0.0, osm_id = 0):
        super(self.__class__, self).__init__(lat, lon)
        self.osm_id = osm_id

    def __str__(self):
        return "Node " + str(self.osm_id) + ": Lat " + str(self.latitude) + ", Lon " + str(self.longitude)

    def copy(self):
        return Node(self.latitude, self.longitude, self.osm_id)

    def addMeter(self, verticalDistance, horizontalDistance):
        mercator = GlobalMercator()
        copy = self.copy()
        lat, lon = mercator.MetersToLatLon(horizontalDistance,verticalDistance)
        copy.latitude += lat
        copy.longitude += lon
        return copy


    def getDistanceInMeter(self, node):
        return vincenty(self,node).meters

    def stepTo(self, targetNode, distance):
        distanceBetween = self.getDistanceInMeter(targetNode)

        part = distance / distanceBetween

        latDiff = targetNode.lat - self.lat
        lonDiff = targetNode.lon - self.lon

        newLat = self.lat + latDiff * part
        newLon = self.lon + lonDiff * part
        return Node.create(Point(newLat, newLon))