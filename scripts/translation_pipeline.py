import re
from openai import OpenAI

def get_openai_client(api_key):
    return OpenAI(api_key=api_key)

def translate_structured_text(text: str, target_language: str = "French", api_key=None) -> str:
    if target_language.lower() == "english" or not text.strip():
        return text

    client = get_openai_client(api_key)

    label_to_ph = {
        "Title:": "<__TITLE__>",
        "Key Ideas:": "<__KEY_IDEAS__>",
        "Body:": "<__BODY__>",
        "Section Header:": "<__SECTION_HEADER__>",
        "Banner image:": "<__BANNER_IMAGE__>",
        "Image Captions:": "<__IMAGE_CAPTIONS__>",
    }

    safe_text = text
    for label, ph in label_to_ph.items():
        safe_text = re.sub(rf"(?m)^{re.escape(label)}", ph, safe_text)

    prompt = f"""
Translate the following text into {target_language}.  

🛑 DO NOT translate or alter any of these placeholders:
  {', '.join(label_to_ph.values())}

For any line beginning with a placeholder like <__TITLE__>, translate only what comes *after* it,
and leave the placeholder itself unchanged.

For all other lines (paragraph text, bullets), translate normally.
Preserve ALL line breaks, bullets, and overall formatting. 
Do NOT add Markdown or extra symbols.

BEGIN TEXT
{safe_text}
END TEXT
""".strip()

    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    translated = resp.choices[0].message.content.strip()

    for label, ph in label_to_ph.items():
        translated = translated.replace(ph, label)

    return translated