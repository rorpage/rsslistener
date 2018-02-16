# BoltBolt RSS Listener

Be sure to create an .env file with the following information (table names are suggestions):

```
airtable_baseKey=base_key
airtable_blogsTableName=Blogs
airtable_blogPostsTableName=BlogPosts
airtable_apiKey=api_key
pocket_consumer_key=12345-pocket_consumer_key
pocket_access_token=abcdef12-pocket_access_token
```

Head to [Pocket Devs](https://getpocket.com/developer/apps/) and create an app with `Add` permissions and category of `Web`.

Next, head to [Authenticate Pocket](http://reader.fxneumann.de/plugins/oneclickpocket/auth.php), enter your consumer key, and the site will
allow you to authorize your app for your account.

You're all set!
