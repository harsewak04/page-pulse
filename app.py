from flask import Flask, render_template, request, jsonify
import requests
import os
from bs4 import BeautifulSoup
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    url = data.get("url")
    try:
        response = requests.get(url, timeout=10)
        content_type = response.headers.get("Content-Type", "").lower()
        if "text/html" not in content_type:
            return jsonify({
            "error": "This URL does not point to an HTML webpage."
            }), 400
        soup = BeautifulSoup(response.text, "lxml")
        # Title
        title = soup.title.string.strip() if soup.title else "No title"
        # Meta Description
        meta = soup.find("meta", attrs={"name": "description"})
        meta_description = (
            meta["content"]
            if meta and meta.get("content")
            else "No meta description"
        )
        # H1 Count
        h1_count = len(soup.find_all("h1"))
        # Images missing alt
        images = soup.find_all("img")
        missing_alt = sum(
            1 for img in images
            if not img.get("alt")
        )
        # Approximate Word Count
        words = soup.get_text(separator=" ", strip=True)
        word_count = len(words.split())
        return jsonify({
            "status": response.status_code,
            "response_time": round(response.elapsed.total_seconds(), 3),
            "title": title,
            "meta_description": meta_description,
            "h1_count": h1_count,
            "images_missing_alt": missing_alt,
            "word_count": word_count
        })
    except requests.exceptions.InvalidURL:
        return jsonify({
            "error" : "The URL format is invalid."
        }),400
    except requests.exceptions.MissingSchema:
        return jsonify({
            "error":"Please enter a valid URL starting with http:// or https://"
        }),400
    except requests.exceptions.ConnectTimeout:
        return jsonify({
            "error":"The website took too long to respond."
        }),400
    except requests.exceptions.ConnectionError:
        return jsonify({
            "error":"Unable to reach the website."
        }),400
    except Exception as e:
        return jsonify({
            "error": "An unexpected error occurred."
        }),400
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )