#!/bin/bash
docker-compose down
docker image rm piket95/personal-discord-bot-yuri
docker-compose build --no-cache
docker-compose up -d