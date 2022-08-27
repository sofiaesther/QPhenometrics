from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from PIL import Image
import io
import numpy as np
import matplotlib.pyplot as plt

# Your client credentials
client_id = 'ceb559b7-cbc4-4051-9ad3-ab7bba4ff994'
client_secret = '8K24a:I#Sj,8vW4{//PO9GljH*]-OVtF7Ec~Iz*P8K24a:I#Sj,8vW4{//PO9GljH*]-OVtF7Ec~Iz*P'

# Create a session
client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client_secret)

# Get token for the session
token = oauth.fetch_token(token_url='https://services.sentinel-hub.com/oauth/token',
                          client_secret=client_secret)

# All requests using this session will have an access token automatically added
resp = oauth.get("https://services.sentinel-hub.com/oauth/tokeninfo")
print(resp.content)

bbox = [-87.72171, 17.11848, -87.342682, 17.481674]
start_date = "2020-06-01"
end_date = "2020-08-31"
collection_id = "sentinel-2-l2a"


