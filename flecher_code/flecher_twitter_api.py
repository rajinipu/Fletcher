import requests
from pprint import pprint
from requests_oauthlib import OAuth1
from pymongo import MongoClient

client = MongoClient()
db = client.tweetdb
posts = db.posts
min_id = db.posts.aggregate({"$group": {"_id":"", "min_id": {"$min": "$id"}}})['result'][0]['min_id']

consumer_key = "i3aGf97N5Jx6FmVfkVXXW0ZJf"
consumer_secret = "AyRPBl3znDXi2LwjumQBi07Lw9HxfAqsq8OGGjKwUNXeNfeF4O"
access_token = "18925330-e3ohuDbwJMa14DpNj60LoMeilBUGIsNbKzIp34yln"
access_secret = "8uVxukGHBpiWi0QcfLONUhd9ED4nr4z86dKiRgA0vCSln"

oauth = OAuth1(consumer_key, client_secret = consumer_secret, 
               resource_owner_key = access_token, resource_owner_secret = access_token_secret)

search_url = "https://api.twitter.com/1.1/search/tweets.json"
parameters = {"q": "MongoDB", "count":100, "max_id":min_id}
response = requests.get(search_url, params=parameters, auth=oauth)

tweets = response.json()['statuses']

for tweet in enumerate(tweets):
	if tweet['user']['default_profile_image'] == False:
		if tweet['retweeted'] == False:
            
				tid = tweet['id']
				name = tweet['user']['screen_name']
				text = tweet['text']
				favcount = tweet['favorite_count']
				rtcount = tweet['retweet_count']
				hashtags = [h['text'] for h in tweet['entities']['hashtags']]
				location = tweet['user']['location']
				date = tweet['created_at']
  
				new_post = {'tid': tid,
					'name': name,
					'party': '',
					'text': text,
					'favcount': favcount,
					'rtcount': rtcount,
					'hashtags': hashtags,
					'location': location,
					'date': date}
	
				posts.insert(new_post)
				print new_post
				#pprint(tweet)

n = 0
while n < 180:
	min_id = db.posts.aggregate({"$group": {"_id":"", "min_id": {"$min": "$id"}}})['result'][0]['min_id']
	parameters = {"q": "iasen", "count":100, "max_id":min_id}
	response = requests.get(search_url, params=parameters, auth=oauth)
	#next_page_url = search_url + response.json()['search_metadata']['next_results']
	#response = requests.get(next_page_url, params=parameters, auth=oauth)
	tweets = response.json()['statuses']
	for tweet in enumerate(tweets):
        	if tweet['user']['default_profile_image'] == False:
                	if tweet['retweeted'] == False:

					tid = tweet['id']
                       			name = tweet['user']['screen_name']
                			text = tweet['text']
                      			favcount = tweet['favorite_count']
                       			rtcount = tweet['retweet_count']
                        		hashtags = [h['text'] for h in tweet['entities']['hashtags']]
                        		location = tweet['user']['location']
                        		date = tweet['created_at']
 
                        		new_post = {'tid': tid,
						'name': name,
                               			'party': '',
                                		'text': text,
                                		'favcount': favcount,
                              			'rtcount': rtcount,
                            			'hashtags': hashtags,
                                		'location': location,
                                		'date': date}

	                       		posts.insert(new_post)
       	  	               		print new_post
					#pprint(tweet)
	n = n + 1

