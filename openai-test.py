from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = ""

# Initialize conversation history
history = []

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    submitted_text = None

    if request.method == "POST":
        submitted_text = request.form["textbox"]
        answer = get_response(submitted_text)
        history.append((submitted_text, answer))

    return render_template("test.html", message=history)

@app.route("/app", methods=["GET", "POST"])
def app_response():
    answer = ""
    submitted_text = request.args.get("text")

    if request.method == "POST" or request.method == "GET":
        answer = get_response(submitted_text)
        history.append((submitted_text, answer))

    return answer

def get_response(question):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "you are an Arc'teryx salesperson and you only introduce Arc'teryx products. Recommend the sentinel pants, gamma shorts, rho bottoms, alpine guide, alpha sv jacket, wordmark shadow tshirt, norvan tank, and hallam merino wool hoody."},
            {"role": "user", "content": question},
        ],
    )

    return response.choices[0].message["content"]

if __name__ == "__main__":
    app.run(debug=True)