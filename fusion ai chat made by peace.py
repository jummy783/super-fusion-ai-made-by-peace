from flask import Flask, render_template, request
import random, pyttsx3, threading

app = Flask(__name__)
engine = pyttsx3.init()

# Bot brain
def bot_reply(user):
    user = user.lower()
    if "hello" in user or "hi" in user:
        return random.choice(["Hey Peace! 😊", "Hello there 💫", "Hi friend 🤖"])
    elif "how are you" in user:
        return random.choice(["I’m feeling awesome! ⚡", "Running at 100%! 💥"])
    elif "bye" in user:
        return "Goodbye Peace 👋"
    elif "joke" in user:
        return random.choice([
            "Why did Python go broke? Because it couldn’t find its class 😂",
            "I told a variable a joke, but it didn’t get the reference 😅"
        ])
    else:
        return random.choice(["Hmm, interesting 💭", "Tell me more 😎", "Nice one 🔥"])

def speak(text):
    engine.say(text)
    engine.runAndWait()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.form["msg"]
    reply = bot_reply(msg)
    threading.Thread(target=speak, args=(reply,)).start()
    return reply


if __name__ == "__main__":
    app.run(debug=True)
