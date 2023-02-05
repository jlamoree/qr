Some QR code experiments.

## Quick Start

- Take a screenshot (or download [sample-screenshot.png](https://raw.githubusercontent.com/jlamoree/qr/main/sample-screenshot.png)) and save it to the Desktop as screenshot.png
- Seek QR codes: `docker run --rm -it --mount type=bind,source="$HOME/Desktop/screenshot.png",target=/data/image_file,readonly jlamoree/qr:0.0.2`

The [zbar](https://zbar.sourceforge.net) library seems to work best when QR codes have a bit of border, for what it's worth.


## Run

While the QR code decoder script is just simple Python, it leverages a barcode library that can be a challenge to compile. At this time, the following works to run the QR code decoder on macOS Ventura:

```shell
brew install python@3.11 zbar
mkdir -p ~/Projects/qrtest && cd ~/Projects/qrtest
git clone git@github.com:jlamoree/qr.git .
/opt/homebrew/bin/python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python decode.py sample-screenshot.png
# Outputs the following:
# https://github.com/jlamoree/qr#quick-start
```

With Docker or similar installed, the following can be performed without messing around with dependencies and stuff:

```shell
image_file=$(mktemp)
curl -s -o $image_file https://raw.githubusercontent.com/jlamoree/qr/main/sample-screenshot.png
docker run --rm --mount type=bind,source="${image_file}",target=/data/image_file,readonly jlamoree/qr:0.0.2
```

## Integration

One option is to use Apple Shortcuts to take a screenshot and pass the file to the QR code decoder. [Find QR Codes](https://www.icloud.com/shortcuts/6c0db5f5e449402f9909a544eb045cb3) can be imported. It does the following:

![Screenshot of Apple Shortcuts showing actions to invoke the QR code decoder](https://jlamoree.github.io/qr/find-qr-codes-shortcut.png "Find QR Codes Shortcut Screenshot")


## Build

The following will construct a new container image with any changes to the Python script.

```shell
tag=0.0.2
username=$(whoami)
op read op://builder/docker-builder-access-token/password | \
  docker login --username $username --password-stdin
docker buildx build --platform linux/amd64,linux/arm64 \
  --tag $username/qr:latest --tag $username/qr:$tag --push .
```
