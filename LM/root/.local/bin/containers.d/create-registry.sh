#!/usr/bin/env bash
# https://www.techrepublic.com/article/how-to-set-up-a-local-image-repository-with-podman/
mkdir -p /var/lib/registry
podman run --privileged -d --name registry -p 5000:5000 -v \
  /var/lib/registry:/var/lib/registry --restart=always registry:2

