# photostgbot
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

A telegram bot for handling only messages with attached photos

## How to run
```shell
export TAG=<Your image tag>
docker image build -t photostgbot:$TAG .
docker run -d --restart=always \
  -e TOKEN=$TOKEN \
  -e SUPPORT_GROUP_ID=$SUPPORT_GROUP_ID \
  --log-driver json-file \
  --log-opt max-size=10m \
  --log-opt max-file=10 \
  photostgbot:$TAG
```

## How to use local pylint pre-commit check (optional)
### Installation
```shell
pre-commit install
```
### Manual usage
```shell
pre-commit run --all-files
```