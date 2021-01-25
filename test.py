# lets test to see if we actually get the data!!!
import twitch_integration

user_login = "ninja"

print("Users Query")
# ...............USER QUERY..............................
query = twitch_integration.get_user_query(user_login)
response = twitch_integration.get_response(query)
#print for debugging
twitch_integration.print_response(response) 
response = response.json()
data = response["data"][0]["id"]
print(data)
# ......................................................

print("Users Streams Query")
# ...............USERS STREAMS QUERY.........................
query = twitch_integration.get_user_streams_query(user_login)
response = twitch_integration.get_response(query)
#print for debugging
twitch_integration.print_response(response) 
# ......................................................

print("USer video query")
# ......................................................
query = twitch_integration.get_user_videos_query(data)
response = twitch_integration.get_response(query)
#print for debugging
twitch_integration.print_response(response) 
# ......................................................

print("Game Query")
# ...............GAMES QUERY.........................
query = twitch_integration.get_games_query(user_login)
response = twitch_integration.get_response(query)
#print for debugging
twitch_integration.print_response(response) 
# ......................................................
