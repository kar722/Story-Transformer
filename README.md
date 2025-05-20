[DSS x Mongabay] Story Transformer Technical Reference Guide

🚀 Project Overview
This project extracts, summarizes, and translates Mongabay articles using BeautifulSoup and OpenAI.

📌 Features
Extract content from Mongabay articles using BeautifulSoup and regex    
Simplify and summarize articles with GPT-4  
Translate articles into multiple languages  
Serve processed content via an API  


🛠️ Setup Instructions
1. Clone the Repository
git clone https://github.com/your-username/story-transformer.git
cd story-transformer


2. Pull the Latest Changes
Before making any modifications, always pull the latest changes from GitHub:
git pull origin main


3. Create & Activate a Virtual Environment
Each time you run this project, you should always activate your virtual environment.

Windows (Git Bash)
python -m venv venv
source venv/Scripts/activate


Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate


Mac/Linux
python3 -m venv venv
source venv/bin/activate


4. Install Dependencies
After activating the virtual environment, install the necessary dependencies:
pip install -r requirements.txt


5. Add API Keys
Create a .env file in the root directory with the following format:
OPENAI_API_KEY=your_api_key_here_in_quotes


▶️ Running Instructions
Set up Virtual Environment
Before each session, you must activate your virtual environment:

Windows (Git Bash)
source venv/Scripts/activate


Windows (Command Prompt)
venv\Scripts\activate


Mac/Linux
source venv/bin/activate


Launch the App
1. Activate your virtual environment (see above).

2. Navigate into the `api` folder:
    cd api





3. Run the Streamlit app:
    streamlit run app.py


4. Visit: [http://localhost:8501](http://localhost:8501)

🌎 Translate a Mongabay Article

Before each session, you must activate your virtual environment:

Upload a Mongabay article URL that is in English.
Select your desired language from the dropdown menu.
Click "Translate".
Click "Download Translation (.pdf)" to save the translated article.

🌎 Summarize a Text Article

Upload a Mongabay article URL.
Choose your desired word count and language of the summary.
Click "Summarize".
Click "Download Summary (.pdf)" to save the summary.
