from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = ""

prompt_template = "Based on the weather forecast for Vancouver, which Arc'teryx products should I wear?"

def get_response(question):

    prompt = prompt_template.replace("Vancouver", question)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=100 
    )

    generated_text = response.choices[0].text.strip()
    
    return generated_text

if __name__ == "__main__":
    app.run(debug=True)