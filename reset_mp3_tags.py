"""
    Script takes a directory of mp3 files and reseta all of the 'date' tags of each mp3 file.
    Used after write_to_html file changes 'date' tag when run.
    Allows for 'date' tag to be reset for testing or if file needs to be scanned by write_to_html again
"""
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
import mutagen.id3
from mutagen.id3 import ID3, TIT2, TIT3, TALB, TPE1, TRCK, TYER

import os

# Input directory of mp3 files
directory = input("Input a Directory Containing New MP3 Files: ")
# Create list of every mp3 file name in directory
mp3_list = sorted(os.listdir(directory))
# Open html file/define html content to write to file
html_file = open("mp3_links.html", "w")
html_content = ''

# For each file in the directory
for i in mp3_list:
    file = directory + "/" + i
    meta = mutagen.File(file, easy=True)
    
    temp = meta.tags['date']
    temp = [meta.tags['date'][0]]
    meta.tags['date'] = temp
    meta.tags.save(file)
    