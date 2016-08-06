# xfce-set-Bing-Wallpaper
Set Bing.com Image of the day as your XFCE4 Wallpaper 
## Requirement
  - python3-bs4

Install with : `pip3 install bs4`
## Usage
```
$./main.py -h

usage: SetBingWallpaper [-h] [-i I] [-l L]

Set Bing.com Image of the day as your XFCE4 Wallpaper.

optional arguments:
  -h, --help  show this help message and exit
  -i I        Default 0. Number days previous the present day. 0 means current
              day, 1 means yesterday, etc
  -l L        Default en-US. Denotes your location. e.g. en-US means United
              States. Put in your country code
```
## Tip
If you want the script to run automatically on startup you can add it to Start Up Applications, entering the following in the command field:
```
python3 /path/to/bing/main/py
```
