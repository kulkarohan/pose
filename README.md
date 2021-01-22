# pose-cli

A simple, intuitive tool for scientists to capture a timelapse of their microscopic cells.

Unintuitive software is a common pattern among digital USB microscopes. Researchers are faced with executing tasks manually or writing software themselves.

This app automates capturing and storing images so that more time can be spent analyzing images and less capturing them.

## Hardware
- Raspberry Pi
- Digital USB microscope ([this](https://www.amazon.com/Microscope-Magnification-Compatible-Smartphone-Mac-Black/dp/B082SVF8SB) one helped inspire the project)

## Installation

[fswebcam](https://github.com/fsphil/fswebcam) is where the real magic happens. 
```
sudo apt install fswebcam
```
Pose wraps fswebcam to achieve its functionality more intuitively.
```
pip install pose-cli
```

## Usage
```
pose
```
