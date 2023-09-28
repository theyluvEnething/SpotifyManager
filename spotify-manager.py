import os
import subprocess
import cover_scraper
import distrokid_uploader

link = input("Please enter playlist or song link.\n> ")
download_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "songs/")

subprocess.call(f'Savify.exe "{link}" -q best -f mp3 -o "{download_folder}')

cover_scraper.run()
distrokid_uploader.run()
