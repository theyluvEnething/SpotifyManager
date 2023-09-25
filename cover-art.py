import os
import eyed3

def scrape_cover_art(directory):
    # Iterate through all files in the directory
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.mp3'):
                mp3_path = os.path.join(root, filename)
                audiofile = eyed3.load(mp3_path)
                
                # Check if the MP3 file has embedded cover art
                if audiofile.tag is not None and audiofile.tag.images:
                    image_data = audiofile.tag.images[0].image_data
                    image_type = audiofile.tag.images[0].mime_type.split('/')[-1]
                    
                    # Save the cover art to a file
                    cover_art_filename = f"{os.path.splitext(filename)[0]}_cover.{image_type}"
                    cover_art_path = os.path.join(root, cover_art_filename)
                    
                    with open(cover_art_path, "wb") as cover_file:
                        cover_file.write(image_data)
                    
                    print(f"Cover art saved for {filename} as {cover_art_filename}")
                else:
                    print(f"No cover art found for {filename}")


directory = r"D:\Programmieren\Python\SpotifyDownloader\downloads"
scrape_cover_art(directory)
