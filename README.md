# Virtual Voice Assistant - Nova

A Python-based virtual voice assistant capable of opening websites, playing music, and fetching news. It uses speech recognition and text-to-speech to interact with the user.

## Features

- **Voice Commands**
  - Open popular websites: Google, YouTube, Facebook, Spotify, LinkedIn, etc.
  - Play music from a predefined list of songs (Bollywood, Hollywood, Nepali, and more).
  - Fetch top news headlines (US or Nepal) using NewsAPI.
  - Stop the assistant using a voice command.

- **Text-to-Speech**
  - Reads responses and news headlines aloud using `pyttsx3`.

## Technologies Used

- Python 3.x
- `speech_recognition` for converting speech to text
- `pyttsx3` for text-to-speech
- `webbrowser` for opening websites
- `requests` for fetching news from NewsAPI
