#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os
import urllib
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(prog='SetBingWallpaper',
                                 description='Set Bing.com Image of the day as your XFCE4 Wallpaper.')
parser.add_argument('-i', default=0,
                    help='Default 0. Number days previous the present day. 0 means current day, 1 means yesterday, etc')
parser.add_argument('-l', default='en-US',
                    help='Default en-US. Denotes your location. e.g. en-US means United States. Put in your country code')
args = parser.parse_args()

BingXML_URL = "http://www.bing.com/HPImageArchive.aspx?format=xml&idx={0}&n=1&mkt={1}".format(args.idx, args.mkt)
page = urllib.request.urlopen(BingXML_URL).read()
BingXML = BeautifulSoup(page, "lxml")

# For extracting complete URL of the image
Images = BingXML.find_all('image')
ImageURL = "https://www.bing.com" + Images[0].url.text
ImageName = Images[0].url.text.split('/')[-1]

username = os.getenv('USER')
path = '/home/' + username + '/Imagens/'
if not os.path.exists(path):
	os.makedirs(path)

os.chdir(path)
if not os.path.isfile(ImageName):
    urllib.request.urlretrieve(ImageURL, ImageName)
    os.system("xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/workspace1/last-image -s " + path + ImageName)
    os.system("xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/workspace0/last-image -s " + path + ImageName)
    os.system('notify-send "'+'Bing Wallpaper updated successfully'+'" "'+ ImageName +'"')
    os._exit(1)
else:
	os.system('notify-send "'+'Bing Wallpaper unchanged'+'" "'+ ImageName + ' Wallpaper already exists in wallpaper directory!'  +'"')
	os._exit(1)
