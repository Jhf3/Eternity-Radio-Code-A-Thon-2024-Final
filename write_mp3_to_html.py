"""
    Script takes a directory as an input and then writes html links to an html file.
    The script accesses the MP3 tags stored in the metadata of the mp3 file and uses those tags to create the html link and then updates the 'date'
    tag of the mp3 file.
    *Important* once a file is run through the script, the 'date' tag on the mp3 file is changed.  In order to reset the 'date' tag, use the reset_mp3_tags
    script.  Also if new mp3 files do not have 'date' tag, use check_mp3_tags script to find sutable mp3 tag to update (lines 39, 43-47).
    The script uses mutagen library to access the MP3 tags.
    Mutagen API - https://mutagen.readthedocs.io/en/latest/api/index.html
"""
# *Mutagen needs to be pip installed to python*
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
import mutagen.id3
from mutagen.id3 import ID3, TIT2, TIT3, TALB, TPE1, TRCK, TYER

# os module
import os

"""
    *For future sorting potential, use glob and numpy to split and sort files by book and verse, currently files are sorted by 'sorted' function which just
    sorts alphabetically and does not work with file names that have leading numbers/characters ex: 1_23_Luke: 10-7
    import glob
    import numpy as np
"""

# Input directory of mp3 files
directory = input("Input a Directory Containing New MP3 Files: ")
# Create list of every mp3 file name in directory, sort using sorted function
mp3_list = sorted(os.listdir(directory))
# Open html file/define html content to write to file
html_file = open("mp3_links.html", "w")
html_content = ''

# For each file in the directory
for i in mp3_list:
    # Set 'file' as path to file (directory/fileName) -> gives path to mp3 file
    file = directory + "/" + i
    # Use mutagen to get mp3 file ID3 metadata
    # mutagen.File creates mutagen.easyid3.EasyID3 object (see link)
    # https://mutagen.readthedocs.io/en/latest/api/id3.html#mutagen.easyid3.EasyID3
    meta = mutagen.File(file, easy=True)
    
    # Check if 'date' tag len is != 2 or if 'date'[1] is not '', if true, add to html_content and update tag
    if ((len(meta.tags['date']) != 2) or (meta.tags['date'][1] != '')):
        # Update html content string
        html_content += '<a href="' + file + '"style="font-family: Arial, Verdana; font-size: 16px;">' + meta.tags['title'][0] + '</a><br>\n'
        
        # update 'date' tag to ['0', '']
        # Since mp3 tags seem to be imutable, create temp list, then rewrite tag
        temp = meta.tags['date']
        temp.append('')
        meta.tags['date'] = temp
        meta.tags.save(file)
        
# Write html_content to html_file and close file
html_file.write(html_content)
html_file.close()
