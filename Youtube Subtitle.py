# importing the libraries
import youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi
from bs4 import BeautifulSoup
import requests, re, pyperclip


# Function
def Copying_to_file(option):
    # Copying subtitle to a file
    try:
        with open(f'{title}.txt', 'w') as file:
            file.write(''.join(List))
    except OSError:
        print('Invalid argument is passed for naming your file in current directory')  # https://youtu.be/h89uOvUDVO4
    else:
        print('File have created in your current directory and ', end="") if option == 3 else print(
            'File have created in your current directory')


def Copying_to_clipboard():
    # Copying subtitle to your clipboard
    pyperclip.copy(' '.join(List))
    print('Texts have copied to your clipboard')


# Getting url from the user & source from server
url = input('Enter the url of youtube video : ')
html_file = BeautifulSoup(requests.get(url).text, "lxml")

# getting transcripts from youtube
try:
    transcripts = YouTubeTranscriptApi.get_transcript(url.split('https://youtu.be/')[1])
# try:
#     transcripts = YouTubeTranscriptApi.get_transcript(url.split('https://youtu.be/')[1], languages=['en-US'])
except youtube_transcript_api._errors.TranscriptsDisabled:  # https://youtu.be/f5yZYVlA_zI
    print(f'Could not retrieve a transcript for the video {url}! This is most likely caused by: '
          'Subtitles are disabled for this video')
    exit()

# Separating text from directories
List = [i['text'] for i in transcripts]

# Obtaining title of video from html_file
title = html_file.title.string.replace('?', ' - ').replace('|', ' - ')
title = re.sub('\\/:*?"<>|', '', title)

# Asking user what they want to do
user_action = int(input(
    'Choose the option listed below to do the required action:\n\t1.Create a file in your current directory\n\t2.Copy to your clipboard\n\t3.Create a file in your current directory & copy to your clipboard\nEnter your choice : '))
if user_action == 1:
    Copying_to_file(1)
elif user_action == 2:
    Copying_to_clipboard()
elif user_action == 3:
    Copying_to_file(3);
    Copying_to_clipboard()
