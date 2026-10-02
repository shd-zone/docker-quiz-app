from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "question": "If I steal a kiss right now, what's your immediate reaction? 😉",
        "options": ["Kiss back harder 😘", "Blush and bite lip 😳", "Act surprised 😜", "Demand one more ❤️"],
        "answer": "Kiss back harder 😘"
    },
    {
        "question": "What's the most dangerous thing about me according to you? 🔥",
        "options": ["My eyes 👁️", "My smile 😁", "My flirty texts 💬", "My entire existence 🙈"],
        "answer": "My smile 😁"
    },
    {
        "question": "If we were trapped in a room alone for 1 hour, what would we do? 🤫",
        "options": ["Late night talks 💬", "Cuddle tightly 🫂", "Make out 😏", "Play a risky game 🎲"],
        "answer": "Cuddle tightly 🫂"
    },
    {
        "question": "What's your weak spot when it comes to romance? 💖",
        "options": ["Forehead kisses 💋", "Back hugs 🤗", "Whispering in ear 👂", "Holding hands tight 🤝"],
        "answer": "Forehead kisses 💋"
    },
    {
        "question": "If I text you 'I miss you' at 2 AM, what are you doing? 🌙",
        "options": ["Replying in 1 sec ⚡", "Calling immediately 📞", "Smiling at phone 😊", "Coming over 🚗"],
        "answer": "Replying in 1 sec ⚡"
    },
    {
        "question": "What kind of outfit looks best on me? 🔥",
        "options": ["Casual Hoodie 🧥", "Black Dress/Shirt 🖤", "Traditional 🥻", "Whatever you wear 😍"],
        "answer": "Black Dress/Shirt 🖤"
    },
    {
        "question": "How long can you hold eye contact with me without smiling? 👀",
        "options": ["Not even 2 sec 😂", "A few seconds 😏", "Until you kiss me 💋", "I'll win for sure 😎"],
        "answer": "Not even 2 sec 😂"
    },
    {
        "question": "What's your favorite way to be woken up? ☀️",
        "options": ["Morning kisses 😘", "Hot coffee ☕", "Tight cuddle 🫂", "A flirty text 📱"],
        "answer": "Morning kisses 😘"
    },
    {
        "question": "If I pull you close by your waist, you will... 🙈",
        "options": ["Wrap arms around my neck 🥰", "Look into my eyes 👀", "Heartbeat speeds up 💓", "All of the above 🔥"],
        "answer": "All of the above 🔥"
    },
    {
        "question": "Finally... Am I officially your favorite distraction? 💖",
        "options": ["Yes, 100% 😍", "Obsessed already 🙈", "Maybe a little 😏", "Definitely ❤️"],
        "answer": "Yes, 100% 😍"
    }
]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions=questions)


@app.route("/result", methods=["POST"])
def result():
    score = 0

    for i, q in enumerate(questions):
        user_answer = request.form.get(f"q{i}")

        if user_answer == q["answer"]:
            score += 1

    total = len(questions)
    percentage = round((score / total) * 100)

    return render_template(
        "result.html",
        score=score,
        total=total,
        percentage=percentage
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)