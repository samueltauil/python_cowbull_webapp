#!/usr/bin/env bash
export BUILD_NUMBER="COMPOSE"; \
  export COWBULL_ENVIRONMENT="Local Compose";\
  export COWBULL_VERSION="v1"; \
  export app_srv="cowbull"; \
  export app_srv_version="1.0.172"; \
  export doclog=dsanderscan; \
  docker-compose \
    -f vendor/docker/docker-compose.yml \
    down
