# photostgbot
A telegram bot for handling only messages with attached photos

## How to run
```shell
export TAG=<Your image tag>
docker image build -t photostgbot:$TAG .
docker run -d --restart=always -e TOKEN=$TOKEN -e SUPPORT_GROUP_ID=$SUPPORT_GROUP_ID photostgbot:$TAG
```
