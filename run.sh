#!/bin/bash
docker build -t rorpage/rsslistener .
docker service rm rsslistener
docker service create --env-file=.env --name rsslistener rorpage/rsslistener
