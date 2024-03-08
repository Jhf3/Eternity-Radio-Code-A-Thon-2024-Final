Eternity Radio Code-A-Thon 2024

* All files use Mutagen which must be pip installed to python
check_mp3_tags:
	- takes a directory of mp3 files and prints the tags of the mp3 files to the shell

reset_mp3_tags:
	- Script takes a directory of mp3 files and reseta all of the 'date' tags of each mp3 file.
	- Used after write_to_html file changes 'date' tag when run.
	- Allows for 'date' tag to be reset for testing or if file needs to be scanned by 		  write_to_html again

write_mp3_to_html:
	- Script takes a directory as an input and then writes html links to an html file.
	- The script accesses the MP3 tags stored in the metadata of the mp3 file and uses those 	  tags to create the html link and then updates the 'date' tag of the mp3 file.
	- *Important* once a file is run through the script, the 'date' tag on the mp3 file is 	  	  changed.  In order to reset the 'date' tag, use the reset_mp3_tags script.  Also if new 	  mp3 files do not have 'date' tag, use check_mp3_tags script to find sutable mp3 tag to 	  update (lines 39, 43-47).
	- The script uses mutagen library to access the MP3 tags.
	- Mutagen API - https://mutagen.readthedocs.io/en/latest/api/index.html
