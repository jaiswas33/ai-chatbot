import os
from flask import Flask, render_template, request
import google.generativeai as genai


app = Flask(__name__)

# Configure your API key (set GOOGLE_API_KEY as an environment variable or replace here)
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)


# Use the working model
model = genai.GenerativeModel("models/gemini-1.5-pro")

# Route for the homepage
@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    if request.method == "POST":
        user_input = request.form.get("prompt")
        if user_input:
            try:
                response = model.generate_content(user_input)
                response_text = response.text
            except Exception as e:
                response_text = f"Error: {str(e)}"
    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
