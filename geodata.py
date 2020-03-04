from geojson import Point, Feature, FeatureCollection,dump

class geodata:
  '''
  A method to create a feature
  '''

  def __init__(self):
    self.locs = [
        {'lon':-121.7885736, 'lat':39.7307071,'text':'chicoTH'},
        {'lon':-122.3668926, 'lat':40.5652945, 'text':'ReddingTH'},
        {'lon': -121.0999447, 'lat':389416621,'text':'AuburnTH'},
        {'lon':-121386462, 'lat':38.664369, 'text':'MCC'},
        {'lon':-1212964218,'lat':38.5726366,'text':'Mather'},
        {'lon':-122.9330412,'lat':38.8251999,'text':'YubaTH'},
        {'lon':-123.1198088,'lat':38.5636711,'text':'FairfieldTH'},
        {'lon':-122.6336637,'lat':38.3518217,'text':'MartinezTH'},
        {'lon':-122.451016,'lat':38.0999162,'text':'OaklandTH'},
         {'lon':-122.6407037,'lat':41.15727,'text':'YrekaTH'},       
    ]
   
    # self.fc = FeatureCollection(self.feature)

  def pack_features(self):
    '''
    return  Features collection
    '''
    th_list =[]
    for l in self.locs:
        th_list.append(self.get_feature(l['lon'],l['lat'],l['text']))
    return th_list




  def get_feature(self, lon, lat, text):
    '''
    return the feature
    '''

    return Feature(geometry = Point((lon,lat)),properties = {'description':text, 'icon':'music', }) 

    



  def save_geodata(self, collection ):
    '''
    save the geojson to a file
    collection is a list of features
    '''
    with open('./assets/th.geojson','w') as outfile:
      dump(collection,outfile)
    outfile.close()



gdata = geodata()
