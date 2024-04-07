# from flask import Flask, render_template
# import openai

# app = Flask(__name__)

# openai.api_key = "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"

# def get_chat_completion(prompt, model="gpt-4"):
#     # Creating a message as required by the API
#     messages = [{"role": "user", "content": prompt}]
  
#     # Calling the ChatCompletion API
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=0
#     )

#     # Returning the extracted response
#     return response.choices[0].message["content"]

# @app.route('/')
# def index():
#     prompt = "What should I wear for hiking tomorrow? Arc'teryx products only."
#     response = get_chat_completion(prompt)
#     return render_template('test.html', prompt=prompt, response=response)

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = ""

# Initialize conversation history
history = []


def get_response():
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "you are an Arc'teryx salesperson and you only introduce Arc'teryx products."},
            {"role": "user", "content": "What should I wear tomorrow?"},
        ],
    )

    return response.choices[0].message["content"]

if __name__ == "__main__":
    app.run(debug=True)