import speech_recognition as speechR
import pyttsx3
import webbrowser
from playMusic import music
import requests


recog = speechR.Recognizer() # creating new instance of recognizer for audio
engine = pyttsx3.init()
newsAPI = "ae78e1d98ec84948ac6041e6be73760c" #please don't use this api key

 
def speakText(text):
    engine.say(text) # adds the text to the queue
    engine.runAndWait() # processes the text to speech from queue and plays it
    
def workWithCommand(openCmd):
    if "open google" in openCmd.lower():
        webbrowser.open("https://www.google.com")

    elif "open youtube" in openCmd.lower():
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in openCmd.lower():
        webbrowser.open("https://www.facebook.com")

    elif "open spotify" in openCmd.lower():
        webbrowser.open("https://www.spotify.com")

    elif "open linkedin" in openCmd.lower():
        webbrowser.open("https://www.linkedin.com")

    elif "open twitter" in openCmd.lower():
        webbrowser.open("https://www.twitter.com")

    elif "open instagram" in openCmd.lower():
        webbrowser.open("https://www.instagram.com")

    elif "open reddit" in openCmd.lower():
        webbrowser.open("https://www.reddit.com")

    elif "open github" in openCmd.lower():
        webbrowser.open("https://www.github.com")

    elif "open whatsapp" in openCmd.lower():
        webbrowser.open("https://web.whatsapp.com")

    elif "open telegram" in openCmd.lower():
        webbrowser.open("https://web.telegram.org")

    elif "open netflix" in openCmd.lower():
        webbrowser.open("https://www.netflix.com")

    elif "open amazon" in openCmd.lower():
        webbrowser.open("https://www.amazon.com")

    elif "open stackoverflow" in openCmd.lower():
        webbrowser.open("https://stackoverflow.com")

    elif "open gmail" in openCmd.lower():
        webbrowser.open("https://mail.google.com")
        
    elif "open yahoo" in openCmd.lower():
        webbrowser.open("https://www.yahoo.com")

    elif "open bing" in openCmd.lower():
        webbrowser.open("https://www.bing.com")

    elif "open quora" in openCmd.lower():
        webbrowser.open("https://www.quora.com")

    elif "open discord" in openCmd.lower():
        webbrowser.open("https://discord.com")

    elif "open pinterest" in openCmd.lower():
        webbrowser.open("https://www.pinterest.com")

    elif "open tiktok" in openCmd.lower():
        webbrowser.open("https://www.tiktok.com")

    elif "open skype" in openCmd.lower():
        webbrowser.open("https://www.skype.com")

    elif "open dropbox" in openCmd.lower():
        webbrowser.open("https://www.dropbox.com")

    elif "open drive" in openCmd.lower():
        webbrowser.open("https://drive.google.com")

    elif "open zoom" in openCmd.lower():
        webbrowser.open("https://zoom.us")

    elif "open outlook" in openCmd.lower():
        webbrowser.open("https://outlook.live.com")

    elif "open apple" in openCmd.lower():
        webbrowser.open("https://www.apple.com")

    elif "open microsoft" in openCmd.lower():
        webbrowser.open("https://www.microsoft.com")

    elif "open adobe" in openCmd.lower():
        webbrowser.open("https://www.adobe.com")

    elif "open canva" in openCmd.lower():
        webbrowser.open("https://www.canva.com")

    elif "open twitch" in openCmd.lower():
        webbrowser.open("https://www.twitch.tv")

    elif "open imdb" in openCmd.lower():
        webbrowser.open("https://www.imdb.com")

    elif "open coursera" in openCmd.lower():
        webbrowser.open("https://www.coursera.org")

    elif "open udemy" in openCmd.lower():
        webbrowser.open("https://www.udemy.com")

    elif "open khan academy" in openCmd.lower():
        webbrowser.open("https://www.khanacademy.org")
        
        #playing music
    
    elif openCmd.lower().startswith("play"):
        song = openCmd.lower().replace("play ", "").strip()  # removes play from the start of the command
        if song in music:
            webbrowser.open(music[song])
        else:
            speakText(f"Sorry, I could not find the song {song}")
            print(f"Song '{song}' not found in your music library.")
            
         # for news headlines   
    elif "news" in openCmd.lower():
        try:
            req = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=ae78e1d98ec84948ac6041e6be73760c")
            data = req.json() # parses JSON request into python script
            articles = data.get("articles", []) # creates a list of newss
            if not articles:
                speakText("Sorry, no news found right now.")
            else:
                speakText("Here are the top headlines:")  #trigger by  saying "nova, give me the news"
                for article in articles[:5]:  # limit to first 5
                    headline = article.get("title")
                    print(headline)
                    speakText(headline)
        except Exception as e:
            print("Error fetching news:", e)
            speakText("Sorry, I could not fetch the news.")


        
        
if __name__ == "__main__":
    
    speakText("starting the engine........")
    
    #obtain audio from the microphone
    while True:
        
        

        # recognize the speech 
        try :
            with speechR.Microphone() as source:  # Opens the microphone as the audio source
               
                print("Say the command....\n")
                audio = recog.listen(source , timeout = 5 , phrase_time_limit = 4) # listens for 4 sec
                print("Recognizing your prompt...")
            
            command = recog.recognize_google(audio) #converts speech to text
            print(command)
            
            # check if the word "jarvis" exists in the recognized text
            if(command.lower() == "nova"):
                print("Yes sir, how can I help")
                
                
                
                # listening for command
                with speechR.Microphone() as source:
                    print("\n Nova activated... \n")
                    audio = recog.listen(source)
                    newCommand = recog.recognize_google(audio) 
               
            # stops the whole tasks     
            if(newCommand.lower() == "nova stop"):
                print("Stopping the task sir....")
                break

            workWithCommand(newCommand)
        

        
        except speechR.UnknownValueError:
            print("Sorry, I could not understand what you said.")  
                      
        except speechR.RequestError as e:
            print("Error; {0}".format(e))
                