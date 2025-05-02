import streamlit as st
from openai import OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
import requests
from dotenv import load_dotenv
import os

# --- LOAD API KEYS FROM .env ---
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# --- HELPER FUNCTIONS ---
def generate_prompt(topic):
    return f"""
Create a podcast-style script (approximately 5 minutes of speech) on the topic: "{topic}".
The script should:
- Be engaging, structured, and conversational in tone
- Explain clearly, using examples if helpful
- Include a surprising fact or thoughtful question at the end
Language: English.
Length: ~600-750 words.
"""

def get_snippet_text(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9
    )
    return response.choices[0].message.content

def generate_audio_elevenlabs(text, voice="Rachel"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.8}
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.content  # MP3 binary

# --- STREAMLIT UI ---
st.set_page_config(page_title="Spotify for Learning", page_icon="🎧")
st.title("🎧 Spotify for Learning")
st.subheader("Your personalized 5-minute podcast playlist")

topics = st.text_area("Enter your learning topics (comma-separated):", placeholder="e.g. History of the Internet, AI avatars, Sea level rise")
snippet_count = st.slider("How many snippets?", 1, 10, 3)

if st.button("Generate Learning Playlist") and topics:
    topic_list = [t.strip() for t in topics.split(",")][:snippet_count]
    for i, topic in enumerate(topic_list):
        st.markdown(f"### 🔹 Topic {i+1}: {topic}")
        with st.spinner("Creating snippet..."):
            prompt = generate_prompt(topic)
            text = get_snippet_text(prompt)
            audio = generate_audio_elevenlabs(text)
            audio_filename = f"snippet_{i}.mp3"
            with open(audio_filename, "wb") as f:
                f.write(audio)
        st.audio(audio_filename)
        with open(audio_filename, "rb") as file:
            st.download_button(label="⬇️ Download MP3", data=file, file_name=audio_filename)