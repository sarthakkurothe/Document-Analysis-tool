import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API Key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ Gemini API key not found. Please set GEMINI_API_KEY in your .env file.")

# Configure Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-flash")  # or use pro-latest if needed

def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def save_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def revise_document(original_text, suggestions_text):
    prompt = f"""
You are a technical writing assistant.

Below is a MoEngage documentation article followed by a list of improvement suggestions. 
Please revise the article to reflect the suggested changes. Ensure the updated version:
- Maintains accuracy of information
- Improves readability, structure, and clarity
- Applies a helpful and action-oriented tone

---

### ORIGINAL ARTICLE:

{original_text}

---

### SUGGESTIONS TO INCORPORATE:

{suggestions_text}

---

Now output the complete revised article only, formatted as Markdown.
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error revising content with Gemini: {e}"

def main():
    original_path = "original.md"
    suggestions_path = "report.md"
    revised_path = "revised.md"

    print("🔁 Loading original article and suggestions...")
    original_text = load_file(original_path)
    suggestions_text = load_file(suggestions_path)

    print("🧠 Generating revised documentation...")
    revised_text = revise_document(original_text, suggestions_text)

    save_file(revised_path, revised_text)
    print(f"✅ Revised article saved to {revised_path}")

if __name__ == "__main__":
    main()
