#!/bin/bash
docker-compose down
docker image rm discordbot-twitchdrops_stammtisch-dcbot:latest
docker-compose build --no-cache
docker-compose up -d