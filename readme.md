Some QR code experiments.

## Quick Start

- Take a screenshot (or download [sample-screenshot.png](https://raw.githubusercontent.com/jlamoree/qr/main/sample-screenshot.png)) and save it to the Desktop as screenshot.png
- Seek QR codes: `docker run --rm -it --mount type=bind,source="$HOME/Desktop/screenshot.png",target=/data/image_file,readonly jlamoree/qr:0.0.2`

The [zbar](https://zbar.sourceforge.net) library seems to work best when QR codes have a bit of border, for what it's worth.


## Build

```shell
tag=0.0.2
username=$(whoami)
op read op://builder/docker-builder-access-token/password | \
  docker login --username $username --password-stdin
docker buildx build --platform linux/amd64,linux/arm64 \
  --tag $username/qr:latest --tag $username/qr:$tag --push .
```

## Run

```shell
tag=0.0.2
username=$(whoami)
image_file="$HOME/Temp/screenshot.png"
docker run --rm -it --mount type=bind,source="${image_file}",target=/data/image_file,readonly $username/qr:$tag
```
