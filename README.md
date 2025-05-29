# [DSS x Mongabay] Story Transformer Technical Reference Guide

## 🚀 Project Overview

This project extracts, summarizes, and translates Mongabay articles using BeautifulSoup and OpenAI’s GPT-4.

⸻

## 📌 Features
- 🔍 Extract content from Mongabay articles using BeautifulSoup and regex
- ✏️ Simplify and summarize articles with GPT-4
- 🌍 Translate articles into multiple languages
- 📡 Serve processed content via a Streamlit-powered interface

⸻

## 🛠️ Setup Instructions

1. Clone the Repository

```
git clone https://github.com/kar722/Story-Transformer.git
cd Story-Transformer
```

2. Pull the Latest Changes

```
git pull origin main
```

3. Create & Activate a Virtual Environment

Windows (Git Bash):

```
python -m venv venv
source venv/Scripts/activate
```

Windows (Command Prompt):

```
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```
python3 -m venv venv
source venv/bin/activate
```

4. Install Dependencies

```
pip install -r requirements.txt
```

5. Add API Keys

Create a .env file in the project root with:

```
echo OPENAI_API_KEY="your_api_key_here" > .env
```


⸻

## ▶️ Running Instructions

1. Activate Your Virtual Environment

Before each session:

Windows (Git Bash):

```
source venv/Scripts/activate
```

Windows (Command Prompt):

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

2. Launch the App

```
cd api
streamlit run app.py
```

Then open http://localhost:8501 in your browser.

⸻

🌍 Translate a Mongabay Article
1. Upload a Mongabay article URL (in English)
2. Select your desired language from the dropdown
3. Click Translate
4. Click Download Translation (.pdf) to save the result

⸻

📝 Summarize a Text Article
1. Upload a Mongabay article URL
2. Choose your desired word count and summary language
3. Click Summarize
4. Click Download Summary (.pdf) to save it

⸻
