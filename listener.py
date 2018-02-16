#!/usr/bin/env python

from airtable import Airtable
import feedparser
import json
import os
import requests
import sys

airtable_baseKey = os.environ.get("airtable_baseKey")
airtable_blogsTableName = os.environ.get("airtable_blogsTableName")
airtable_blogPostsTableName = os.environ.get("airtable_blogPostsTableName")
airtable_apiKey = os.environ.get("airtable_apiKey")

blogsTable = Airtable(airtable_baseKey, airtable_blogsTableName, airtable_apiKey)
blogPostsTable = Airtable(airtable_baseKey, airtable_blogPostsTableName, airtable_apiKey)

pocket_consumer_key = os.environ.get("pocket_consumer_key")
pocket_access_token = os.environ.get("pocket_access_token")
pocket_headers = { "Content-Type": "application/json; charset=UTF-8" }

for blog in blogsTable.get_all():
  print blog['fields']['Name']
  feed_url = blog['fields']['FeedUrl']
  d = feedparser.parse(feed_url)

  for post in d.entries:
      results = blogPostsTable.search('Url', post.link.encode('ascii', 'ignore'))
      if len(results) == 0:
        payload = {
          'title': post.title,
          'url': post.link,
          'consumer_key': pocket_consumer_key,
          'access_token': pocket_access_token
        }

        try:
          res = requests.post('https://getpocket.com/v3/add', headers=pocket_headers, data=json.dumps(payload))
        except Exception as e:
          sys.stderr.write('An error occurred when trying to deliver the message:\n{0}'.format(e.message))
        else:
          if res.ok:
            blogPostsTable.insert({'Title': post.title, 'Url': post.link.encode('ascii', 'ignore')})
