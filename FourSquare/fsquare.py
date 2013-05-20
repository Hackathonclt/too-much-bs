import oauth2 as oauth
import urllib2 as urllib
import json
import time

# TODO: unscomment and set id and secret
#client_id = ""
#client_secret = ""
search_command = "https://api.foursquare.com/v2/venues/search?"
date_part = "&v=20130511"
limit_part = "&limit=50"

_debug = 0

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"

http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
'''
def thereq(url, method, parameters):

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url)

  return response

def FetchSample(lat, lon):
  strURL = search_command + "ll=" + str(lat) + "," + str(lon) + limit_part + client_id + client_secret + date_part

  parameters = []
  jsonVenueList = []
  intResultNumForQuery = 0
  time.sleep(.7)
  response = thereq(strURL, "GET", parameters)
  ret = []
  for line in response:
    jsonObj = json.loads(line)
    if "venues" in jsonObj["response"]:
      for venue in jsonObj["response"]["venues"]:
        ret.append(venue)
  return ret

def FetchSamples():
  # do 70x70 to get about 5k queries
  #fltMAXLat = 35.50
  #fltMINLat = 35.00
  #fltMINLong = -81.00
  #fltMAXLong = -80.50
  (fltMINLong, fltMAXLong, fltMINLat, fltMAXLat) = (-79.8847, -79.7278, 36.0158, 36.1537 )

  fi = open('foursquare.out', 'w')

  import numpy
  lats = numpy.linspace(fltMINLat, fltMAXLat, 70)
  lons = numpy.linspace(fltMINLong, fltMAXLong, 70)

  for lat in lats:
    for lon in lons:
      venues = FetchSample(lat, lon)
      for venue in venues:
        try:
          fi.write("{}\t{}\t{}\t{}\n".format(venue["id"], venue["name"].encode('ascii', 'ignore'), venue["location"]["lat"], venue["location"]["lng"]))
        except:
          pass
  fi.close()

if __name__ == '__main__':
  FetchSamples()
