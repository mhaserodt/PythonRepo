# -*- coding: utf-8 -*-
"""
Created on Thu May 28 16:20:16 2020

@author: mhaserodt
A quick tool created to download and preserve a YouTube video.
"""

#importing the module 
from pytube import YouTube 
  
#where to save 
#SAVE_PATH = "C:/" #to_do 
  
#link of the video to be downloaded 
#video = YouTube('https://www.youtube.com/watch?v=KVc5RXXBbbU')
  

video_url = 'https://www.bigmarker.com/thinkful/Thinkful-Webinar-Intro-to-JavaScript-Build-a-Virtual-Pet3-2020-04-06-07-00-pm?bmid=a9ba7f557a22' # paste here your Youube videos' url
youtube = YouTube(video_url)
video = youtube.streams.first()
video.download('/Users/Marc/Desktop') # path, where to video download.
