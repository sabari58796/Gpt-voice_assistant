import speech_recognition as analyze
import pyttsx3 as speak
import openai
import time
listener =analyze.Recognizer()  # speech recognition
voice=speak.init()
different_voices=voice.getProperty("voices")
voice.setProperty("voice",different_voices[0].id)

def fun_speak(words):
    voice.say(words)
    voice.runAndWait()

def fun_Gtp(words):
    openai.api_key = "Your openAi API key "
    # Set up the model and prompt
    model = "text-davinci-002"
    prompt = words
    # Generate a response
    response = openai.Completion.create(engine=model,prompt=prompt,max_tokens=1024,n=1,stop=None,temperature=0.5)
    fun_speak(response.choices[0].text)
    print(response.choices[0].text)

try:
    with analyze.Microphone() as mic:
        fun_speak("Hello")
        time.sleep(0.5)
        fun_speak("Ask some thing... i am ready to help you")
        print("Listening...")
        sound =listener.listen(mic)
        words=listener.recognize_google(sound)   #Sound to text
        words=words.lower()
        fun_Gtp(words)
except:
    pass
