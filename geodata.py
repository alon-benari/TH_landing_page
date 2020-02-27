from geojson import Point, Feature, FeatureCollection,dump

class geodata:
  '''
  A method to create a feature
  '''

  def __init__(self, lon, lat,text):
    self.lon = lon
    self.lat = lat
    self.text = text
    self.feature = [ Feature(geometry = Point((self.lon,self.lat)),properties = {'description':self.text, 'icon':'music', }) ]
    self.fc = FeatureCollection(self.feature)


  def get_feature(self):
    '''
    return the feature
    '''
    return self.feature


  def save_geodata(self, collection ):
    '''
    save the geojson to a file
    collection is a list of features
    '''
    with open('th.geojson','w') as outfile:
      dump(Feature(collection),outfile)
    outfile.close()


gdata = geodata( -122.2330 ,40.3511, 'ReddingTH') 