import requests, json, sys

Base_url = "https://api.twitch.tv/helix/"
AutURL ="https://id.twitch.tv/oauth2/token"

CLIENT_ID = "v2k6y9ys0enyzu9xc6japu2vrg5615"
CLIENT_SECRET = "g651keamx2n3ohgfes4ml00cks29w0"

AutParams = {'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET, 'grant_type': 'client_credentials'}
INDENT = 2


# get response from twitch API call
def get_response(query):
    AutCall = requests.post(url=AutURL, params=AutParams)
    data1 = AutCall.json()
    print(data1)
    access_token = data1["access_token"]
    HEADERS = {'Client-ID': CLIENT_ID, 'Authorization': "Bearer " + access_token}
    current_url  = Base_url + query
    response = requests.get(url=current_url, headers=HEADERS)
    return response

# used for debugging the result
def print_response(response):
    response_json = response.json()
    print_response = json.dumps(response_json, indent=INDENT)
    print(print_response)

# get the current live stream info, given a username
def get_user_streams_query(user_login):
    return 'streams?user_login={0}'.format(user_login)

def get_user_query(user_login):
    return "users?login={0}".format(user_login)

def get_user_videos_query(user_id):
    return 'videos?user_id={0}&first=5'.format(user_id)

def get_games_query(user_login):
    return 'streams?user_login={0}'.format(user_login)