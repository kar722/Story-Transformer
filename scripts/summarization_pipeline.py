from openai import OpenAI

def get_openai_client(api_key):
    return OpenAI(api_key=api_key)

def summarize_text_narrative(text, word_limit=200, client=None):
    if not text.strip():
        return ""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a skilled writer who summarizes text in a clear and narrative style. "
                    "Preserve the logical flow and tone of the original text. Use transitions to make the summary feel cohesive. "
                    f"Keep the summary around {word_limit} words."
                )
            },
            {
                "role": "user",
                "content": f"Summarize this text:\n\n{text}"
            }
        ]
    )
    return response.choices[0].message.content.strip()

def translate(text, language="Spanish", client=None):
    if not text.strip():
        return ""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    f"You are a professional {language}-language science and environmental journalist. "
                    "You write with clarity and impact for general Latin American audiences. "
                    "Use natural phrasing and journalistic tone."
                )
            },
            {
                "role": "user",
                "content": f"Translate the following English text to {language}:\n\n{text}"
            }
        ]
    )
    return response.choices[0].message.content.strip()

def summarize_and_translate(text, word_limit=200, language="english", api_key=None):
    client = get_openai_client(api_key)
    summary = summarize_text_narrative(text, word_limit=word_limit, client=client)
    if language.lower() != "english":
        summary = translate(summary, language, client=client)
    return summary