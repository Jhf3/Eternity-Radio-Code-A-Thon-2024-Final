"""
    Script takes a directory of mp3 files and prints the tags of the mp3 files to the shell
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
mp3_list = os.listdir(directory)
# Open html file/define html content to write to file
html_file = open("mp3_links.html", "w")
html_content = ''

for i in mp3_list:
    # Set 'file' as path to file (directory/fileName) -> gives path to mp3 file
    file = directory + "/" + i
    # Use mutagen to get mp3 file ID3 metadata
    # mutagen.File creates mutagen.easyid3.EasyID3 object (see link)
    # https://mutagen.readthedocs.io/en/latest/api/id3.html#mutagen.easyid3.EasyID3
    meta = mutagen.File(file, easy=True)
    print(meta)
