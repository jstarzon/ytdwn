from pytube import YouTube, Playlist
import os
import validators

#File saving/checking if exist function
#-------------------------
def save(plikimp4):
    try:
        xx = plikimp4.replace('.mp4','')
        os.rename(plikimp4, xx+'.mp3')
    except OSError as err:
        print(err)
        os.remove(plikimp4)
        
#Downloading main function
#-------------------------
def pobieranie(video):
    print('pobieram  : {} link : {}'.format(video.title, video.watch_url))
    plikimp4 = video.streams.filter(only_audio=True,file_extension="mp4")\
            .first()\
            .download('Download/')
    save(plikimp4)
    
#refering to main function in single file download
def downloadurl(url):
    video = YouTube(url)
    pobieranie(video)
#refering to main function in multi file download
def playlistdwn(url):
    playlist = Playlist(url)
    #list videos in playlist of your choice
    for video in playlist.videos:
        pobieranie(video)
        
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
#MADE BY JULIUSZ STARZONEK



