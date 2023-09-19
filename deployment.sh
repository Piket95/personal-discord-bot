#!/bin/bash
docker-compose down
docker image rm personal-discord-bot-yuri:latest
docker-compose build --no-cache
docker-compose up -d