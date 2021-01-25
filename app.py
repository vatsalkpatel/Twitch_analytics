import requests, json, sys, time

Base_url = "https://api.twitch.tv/helix/streams"
AutURL ="https://id.twitch.tv/oauth2/token"
ClientId = "v2k6y9ys0enyzu9xc6japu2vrg5615"
Secret = "g651keamx2n3ohgfes4ml00cks29w0"

AutParams = {'client_id': ClientId, 'client_secret': Secret, 'grant_type': 'client_credentials'}
AutCall = requests.post(url=AutURL, params=AutParams)

data1 = AutCall.json()
print(data1)
# time.sleep(100)
access_token = data1["access_token"]
Headers = {'Client-ID': ClientId, 'Authorization': "Bearer " + access_token}

StreamsCall = requests.get(url=Base_url, headers=Headers)
# print(StreamsCall.json())