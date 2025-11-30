import speech_recognition as sr
import os
import webbrowser
from openai import OpenAI, RateLimitError
from config import apikey
import datetime
import random

# ---------------- OPENAI CLIENT ----------------
# ---------------- OPENAI SARANG ANUPAM CLIENT ----------------
client = OpenAI(api_key=apikey)
chatStr = ""

# ---------------- FUNCTIONS ----------------
def say(text):
    """Use macOS say command for voice output"""
    os.system(f'say "{text}"')

def takeCommand():
    """Listen from microphone and return recognized text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"You said: {query}")
            return query.lower()
        except Exception:
            return "Some Error Occurred. Sorry from Jarvis"

def chat(query):
    """Chat with GPT-4o-mini, handle quota errors gracefully"""
    global chatStr
    chatStr += f"Human: {query}\nJarvis: "
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Jarvis, an intelligent AI assistant."},
                {"role": "user", "content": chatStr}
            ],
            temperature=0.7,
            max_tokens=150
        )
        reply = response.choices[0].message["content"]
        say(reply)
        chatStr += reply + "\n"
        return reply
    except RateLimitError:
        msg = "Sorry sir, my OpenAI quota is used up. Please try later."
        print(msg)
        say(msg)
        return msg

def ai(prompt):
    """Save OpenAI response to a text file, handle quota errors"""
    text = f"OpenAI response for Prompt: {prompt}\n*************************\n\n"
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=100
        )
        reply = response.choices[0].message["content"]
        text += reply

        if not os.path.exists("Openai"):
            os.mkdir("Openai")

        filename = f"Openai/output_{random.randint(1, 9999999)}.txt"
        with open(filename, "w") as f:
            f.write(text)
        say("Prompt saved successfully.")
    except RateLimitError:
        msg = "Sorry sir, my OpenAI quota is used up. Cannot save the prompt."
        print(msg)
        say(msg)

# ---------------- MAIN LOOP ----------------
if __name__ == '__main__':
    print("Welcome to Jarvis A.I")
    say("Jarvis AI activated")

    while True:
        query = takeCommand()

        # ---------------- OPEN WEBSITES ----------------
        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"]
        ]

        opened_site = False
        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
                opened_site = True
                break

        # ---------------- OTHER COMMANDS ----------------
        if not opened_site:
            if "open music" in query:
                musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
                if os.path.exists(musicPath):
                    os.system(f"open {musicPath}")
                    say("Playing music")
                else:
                    say("Music file not found.")

            elif "the time" in query:
                hour = datetime.datetime.now().strftime("%H")
                minute = datetime.datetime.now().strftime("%M")
                say(f"Sir, the time is {hour} bajke {minute} minutes")

            elif "open facetime" in query:
                os.system("open /System/Applications/FaceTime.app")

            elif "open pass" in query:
                os.system("open /Applications/Passky.app")

            elif "using artificial intelligence" in query:
                ai(prompt=query)

            elif "jarvis quit" in query:
                say("Goodbye sir")
                break

            elif "reset chat" in query:
                chatStr = ""
                say("Chat history reset")

            else:
                print("Chatting...")
                chat(query)