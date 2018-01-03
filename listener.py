#!/usr/bin/env python

from airtable import Airtable
import feedparser
import json
import os
import requests
import sys

feed_url = os.environ.get("feed_url")
d = feedparser.parse(feed_url)

webhook_url = os.environ.get("webhook_url")

airtable_baseKey = os.environ.get("airtable_baseKey")
airtable_tableName = os.environ.get("airtable_tableName")
airtable_apiKey = os.environ.get("airtable_apiKey")
airtable = Airtable(airtable_baseKey, airtable_tableName, airtable_apiKey)

for post in d.entries:
    results = airtable.search('Url', post.link.encode('ascii', 'ignore'))
    if len(results) == 0:
      payload = {
        'title': post.title,
        'url': post.link
      }

      try:
        res = requests.post(webhook_url, data=json.dumps(payload))
      except Exception as e:
        sys.stderr.write('An error occurred when trying to deliver the message:\n{0}'.format(e.message))
      else:
        if res.ok:
          airtable.insert({'Title': post.title, 'Url': post.link.encode('ascii', 'ignore')})

