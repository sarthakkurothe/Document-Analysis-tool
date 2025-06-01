import os
import time
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import google.generativeai as genai

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ Gemini API key not found. Please set GEMINI_API_KEY in your .env file.")

# Configure Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-flash")  # Gemini 2.0 Flash

def fetch_article_text(url):
    """Fetch article content using a headless browser."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    print("🚀 Launching headless browser to fetch content...")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        time.sleep(3)  # Let JS content load

        soup = BeautifulSoup(driver.page_source, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()

        text = soup.get_text(separator="\n")
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        cleaned_text = "\n".join(lines)

        return cleaned_text
    except Exception as e:
        print(f"❌ Selenium fetch error: {e}")
        return ""
    finally:
        driver.quit()

def analyze_with_gemini(url, text):
    """Use Gemini to analyze the article and return improvement suggestions."""
    prompt = f"""
You are an expert in improving product documentation. Analyze the following MoEngage article:

URL: {url}

---

{text}

---

Please analyze the article for these criteria and return structured Markdown output:

1. **Readability for non-technical marketers**
2. **Structure and logical flow**
3. **Completeness of information and clarity of examples**
4. **Adherence to style guidelines** (tone, clarity, action-oriented language)

For each criterion, include:
- A brief assessment
- Specific, actionable suggestions for improvement
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error analyzing content with Gemini: {e}"

def main():
    url = input("Enter MoEngage documentation URL: ").strip()
    print("\n🔍 Fetching and analyzing the article...")

    article_text = fetch_article_text(url)
    if not article_text:
        print("⚠️ No article text found. Exiting.")
        return

    # Save the original article content for use in reviser.py (Task 2)
    with open("original.md", "w", encoding="utf-8") as f:
        f.write(article_text)

    result = analyze_with_gemini(url, article_text)

    # Save Gemini's suggestions
    output_file = "report.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"\n✅ Analysis complete. Suggestions saved to {output_file}")
    print(f"📄 Original article saved to original.md")

if __name__ == "__main__":
    main()
    