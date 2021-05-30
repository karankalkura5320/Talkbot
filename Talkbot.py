# Import all the libraries which is required
import speech_recognition as sr
import pyttsx3
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create the bot
Bot = ChatBot('MyBot')

# All of the magic in SpeechRecognition happens with the Recognizer class
# Create object for speech recognition
a1 = sr.Recognizer()
a2 = sr.Recognizer()

# Set the trainer
Bot.set_trainer(ChatterBotCorpusTrainer)

# Train the bot
Bot.train('chatterbot.corpus.english')

# Initialize python text to speech converter
stranger = pyttsx3.init()

# An infinite loop to take the voice input from the user
while True:
    with sr.Microphone() as source:
        print('Listening')
        try:
            audio = a1.listen(source)                   # Record the audio data
            # my_input = a2.recognize_sphinx(audio)     # Recognise the audio input
            my_input = a1.recognize_google(audio)       # Recognise the voice
        except:
            my_input = 'hi'
            # print('You: ', my_input)
        print('You: ', my_input)
        if my_input == 'quit':                  # If input is quit, then quit
            break

        reply = Bot.get_response(my_input)    # Response by the model
        print('Bot: ', reply)
        stranger.say(reply)                       # Response said by the bot
        stranger.runandWait()
