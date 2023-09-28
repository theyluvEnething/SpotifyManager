import os
import eyed3
import os
from PIL import Image

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
                    cover_art_filename = f"{os.path.splitext(filename)[0]}.{image_type}"
                    cover_art_path = os.path.join(root, cover_art_filename)
                    
                    with open(cover_art_path, "wb") as cover_file:
                        cover_file.write(image_data)
                    
                    print(f"Cover art saved for {filename} as {cover_art_filename}")
                else:
                    print(f"No cover art found for {filename}")


def resize_images(directory):

    input_directory = directory
    output_directory = "D:\Programmieren\Python\SpotifyManager\cover-art"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png"): 
      
            img = Image.open(os.path.join(input_directory, filename))
            original_width, original_height = img.size
            new_width = 1280
            new_height = 1280
            resized_img = img.resize((new_width, new_height))
            resized_img.save(os.path.join(output_directory, filename))
            img.close()


def remove_old_images(directory):
    for filename in os.listdir(directory):

        if not filename.endswith(".jpeg"):
            continue

        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

    print("Image resizing complete.")

def run():
    directory = r"D:\Programmieren\Python\SpotifyManager\songs"
    scrape_cover_art(directory)
    resize_images(directory)
    remove_old_images(directory)

if __name__ == "__main__":
    run()
