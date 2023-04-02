from pytube import YouTube, Playlist
import os
import validators
import os
from moviepy.editor import AudioFileClip

def convert_mp4_to_mp3():
    # Set the directory path to the "download" folder
    directory = 'Download'

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Check if the file is an MP4 file
        if filename.endswith('.mp4'):
            # Set the output file path
            output_filepath = os.path.join(directory, filename[:-4] + '.mp3')

            # Convert the MP4 file to an MP3 file
            try:
                audio = AudioFileClip(filepath)
                audio.write_audiofile(output_filepath, verbose=False, logger=None)
                print(f"Converted {filename} to MP3")
                print(f"Deleting temporary MP4 file...\n {filename}")
                os.remove(filename)
            except Exception as e:
                print(f"Error converting {filename} to MP3: {e}")

#File saving/checking if exist function
#-------------------------
def save(plikimp4):
    try:
        print("Saved..")
    except OSError as err:
        print(err)
        os.remove(plikimp4)
        
#Downloading main function
#-------------------------
def pobieranie(video):
    print('pobieram  : {} link : {}'.format(video.title, video.watch_url))
    plikimp4 = video.streams.filter(only_audio=False,file_extension="mp4")\
        .first()\
        .download('Download/')
    save(plikimp4)

#refering to main function in single file download
def downloadurl(url):
    video = YouTube(url)
    try:
        pobieranie(video)
    except:
        print("Failed to get name. Retrying...")
        video = YouTube(url)

    

#refering to main function in multi file download
def playlistdwn(url):
    playlist = Playlist(url)
    #list videos in playlist of your choice
    for video in playlist.videos:
        try:
            pobieranie(video)
        except:
            print("Failed to get name. Retrying...")
            playlist = Playlist(url)


        
def menu_ui():
    print("1.Single video 2.Playlist")
    menu = input("Choose option: ")
    menu = int(menu)
    if (menu == 2):
        print("Insert link: ")
        url = input()
        if (validators.url(url)==True):
            playlistdwn(url)
        else: 
            print("It must be a link") 
            menu_ui()
        
    if (menu == 1):
        print("Insert link:  ")
        url = input()
        if (validators.url(url)==True):
            downloadurl(url)
        else: 
            print("It must be a link") 
            menu_ui()
        
    if (menu>2 or menu<1):
        print("Choose correct option")
        menu_ui()

#MAIN
#-------------------------
if __name__ == '__main__':
    menu_ui()
    convert_mp4_to_mp3()
#MADE BY JULIUSZ STARZONEK