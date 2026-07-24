# 🚀 Page Pulse

Page Pulse is a Flask-based web application that analyzes a webpage and provides useful SEO insights. Users can enter a webpage URL and receive information such as the page title, meta description, response time, heading count, image accessibility and word count.

---

## Features

- Analyze any valid webpage URL
- HTTP Status Code
- Response Time
- Page Title
- Meta Description
- H1 Tag Count
- Images Missing ALT Text
- Word Count
- User-Friendly Error Handling
- Non-HTML Content Detection

---

## Technologies Used

- Python
- Flask
- Requests
- BeautifulSoup4
- lxml
- HTML
- CSS
- JavaScript

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python app.py
```

### 4. Open in your browser

```
http://127.0.0.1:5000
```

---

# API Contract

## Endpoint

```
POST /analyze
```

## Request Body

```json
{
  "url": "https://example.com"
}
```

## Successful Response

```json
{
  "status": 200,
  "response_time": 0.15,
  "title": "Example Domain",
  "meta_description": "Example description",
  "h1_count": 1,
  "images_missing_alt": 0,
  "word_count": 21
}
```

## Error Response

```json
{
  "error": "Please enter a valid URL starting with http:// or https://"
}
```

---

# Tests

The project includes automated tests using **pytest**.

The tests cover:

- Happy path using a valid webpage
- Invalid URL handling
- Non-HTML content detection (PDF)

Run tests with:

```bash
python -m pytest
```

---

# Design Decisions

## 1. Flask

I chose Flask because it is lightweight and simple to use for small web applications. It allowed me to focus on implementing the webpage analysis logic without unnecessary framework complexity.

## 2. BeautifulSoup with lxml

I used BeautifulSoup together with the lxml parser because it provides reliable HTML parsing and makes extracting SEO-related elements such as titles, meta descriptions, headings and images straightforward.

## 3. Structured Error Handling

Instead of allowing the application to crash, I handled common exceptions such as invalid URLs, HTTP errors, connection timeouts and non-HTML responses. This provides clearer feedback to users and improves the overall reliability of the application.

---

# Future Improvements

- SEO score calculation
- Export report as PDF
- Mobile responsive interface
- Additional SEO metrics
- History of previous analyses

---

# Author

**Harsewak Singh Walia**

Built for Digital Heroes Training Task.