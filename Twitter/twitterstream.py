import oauth2 as oauth
import urllib2 as urllib

# TODO: uncomment and assign key and secret here!
# See Assignment 1 instructions or README for how to get these credentials
#access_token_key = ""
#access_token_secret = ""

# TODO: uncomment and assign key and secret here!
#consumer_key = ""
#consumer_secret = "4zpQwlCbqQ7f6Mepv5EqeQYwmsqDvo7auxxjKOelk"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples(fi, n):
  url = "https://stream.twitter.com/1/statuses/sample.json"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  count = 0
  for line in response:
    twitterJSON = line.strip()
    fi.write(twitterJSON + "\n")
    count += 1
    if count == n:
      break

if __name__ == '__main__':
  baseDir = 'files'
  fileNum = 0
  totalSize = 0
  while True:
    fi = open("temp", 'w')
    fetchsamples(fi, 50000)
    fi.close()

    # tar gz and increment
    import subprocess
    import shlex
    import os.path
    tarName = baseDir + '/file' + str(fileNum) + '.tgz'
    subprocess.call(shlex.split("tar czvf " + tarName + ' temp'), stdout=None)

    totalSize += os.path.getsize(tarName)
    if totalSize >= 1024 * 1024 * 1024 * 100: # 100 gb
      break
    
    print str(fileNum) + ": " + str(totalSize)
    fileNum += 1


