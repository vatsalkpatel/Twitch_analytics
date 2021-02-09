# lets test to see if we actually get the data!!!
import twitch_integration
import numpy as np
import pandas as pd
import csv
root_path = r"C:\Users\vkpat\Desktop\Vatsal\SEMESTER3\Jobs\Twitch Project\2016-01\2016_jan_"
full_data = pd.read_csv(root_path+str(0)+".csv")
# for i in range(1,1371,1):
for i in range(1,2,1):
    print(root_path+str(i)+".csv")
    data = pd.read_csv(root_path+str(i)+".csv")
    full_data = pd.concat([full_data,data])
print(full_data.shape)
user_details = []
video_details = []
for user_login in full_data.Channel: 
    print(user_login)
    # user_login = "ninja"
    try:
        print("Users Query")
        # ...............USER QUERY..............................
        query = twitch_integration.get_user_query(user_login)
        response = twitch_integration.get_response(query)
        #print for debugging
        twitch_integration.print_response(response) 
        response = response.json()
        user_details.append(response["data"][0])
        data = response["data"][0]["id"]
        print(data)

        # ......................................................

        # print("Users Streams Query")
        # # ...............USERS STREAMS QUERY.........................
        # query = twitch_integration.get_user_streams_query(user_login)
        # response = twitch_integration.get_response(query)
        # #print for debugging
        # twitch_integration.print_response(response) 
        # # ......................................................

        print("USer video query")
        # ......................................................
        query = twitch_integration.get_user_videos_query(data)
        response = twitch_integration.get_response(query)
        response = response.json()
        video_details = video_details + response["data"]
        # print(video_details)
        #print for debugging
        twitch_integration.print_response(response) 
        # ......................................................
    except:
        print("An exception occurred")
# print(user_details)
print(video_details)
csv_file = "Users.csv"
csv_columns = ['id','login','display_name','type','broadcaster_type', 'description', 'profile_image_url','offline_image_url','view_count','created_at']
try:
    with open(csv_file, 'w',encoding="utf-8",errors="surrogateescape") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for row in user_details:
            writer.writerow(row)
except IOError:
    pass
csv_file = "Videos.csv"
video_csv_columns = ['id','user_id','user_login','user_name','title', 'description', 'created_at','published_at','url','thumbnail_url', 'viewable', 'view_count', 'language', 'type', 'duration']
try:
    with open(csv_file, 'w',encoding="utf-8",errors="surrogateescape") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=video_csv_columns)
        writer.writeheader()
        for row in video_details:
            writer.writerow(row)
except IOError:
    pass
