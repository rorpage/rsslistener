#!/bin/bash
docker service create --env-file=.env --name rsslistener rorpage/rsslistener
