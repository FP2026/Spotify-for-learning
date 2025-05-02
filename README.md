# 🎧 Spotify for Learning

A hackathon-ready app that generates personalized, podcast-style learning playlists. Just enter your topics — the app creates 5-minute audio episodes using GPT-4 and ElevenLabs.

## 🚀 Features

- Input multiple learning topics
- Generate ~5 min scripts using GPT-4
- Convert text into audio using ElevenLabs
- Stream or download as MP3
- All in one click

## 🛠 Tech Stack

- Streamlit (frontend)
- OpenAI GPT-4 (text generation)
- ElevenLabs API (text-to-speech)
- dotenv (key management)

## 🧪 How to Run

1. Clone this repo
2. Create a `.env` file:
    ```env
    OPENAI_API_KEY=your-key
    ELEVENLABS_API_KEY=your-key
    ```
3. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the app:
    ```bash
    streamlit run app.py
    ```

## 💡 Roadmap

- [ ] Personalized recommendations
- [ ] Playlist export (Spotify or RSS)
- [ ] Save snippet history

Made in under 24h.