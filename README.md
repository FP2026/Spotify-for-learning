# 🎧 Spotify for Learning

**Learn anything in 5 minutes – by listening, not reading.**

Spotify for Learning is a microlearning generator that transforms any topic into a short, podcast-style audio explanation. Just type a topic, and the app generates a spoken snippet in real time using GPT-3.5 and ElevenLabs voice synthesis.

---

## 🚀 Features

- 🧠 LLM-powered content generation (GPT-3.5 via OpenAI API)  
- 🎙️ Realistic AI voice output (via ElevenLabs TTS)  
- 🖥️ Streamlit web interface (deployed serverlessly)  
- 🎧 Instant MP3 playback + download  
- 🧹 Audio-optimized cleaning logic (removes [brackets], cues like "Host:")

---

## 🛠 Tech Stack

- Python  
- OpenAI API (GPT-3.5)  
- ElevenLabs API (TTS)  
- Streamlit (frontend + deployment)  
- Regex (text preprocessing for voice)

---

## ⚙️ How to Run Locally

1. Clone the repo  
```bash
git clone https://github.com/yourname/spotify-for-learning.git
cd spotify-for-learning
```

2. Install requirements  
```bash
pip install -r requirements.txt
```

3. Add a `.env` file or `secrets.toml` with your API keys:
```env
OPENAI_API_KEY=your-openai-key
ELEVENLABS_API_KEY=your-elevenlabs-key
```

4. Run the app  
```bash
streamlit run app.py
```

---

## 🌍 Live Demo

🔗 Try the live app on **Streamlit Cloud**:  
👉 [https://spotify-for-learning.streamlit.app](https://spotify-for-learning.streamlit.app)

---

## 🧪 Example Prompts

- How does the immune system work?  
- Why do whales sing?  
- What is quantum computing?

---

## 🧭 What's Next?

- Voice personalization and tone selection  
- Multilingual learning output (German, Spanish…)  
- Multi-topic playlists and memory tracking

---

## 📄 License

MIT – free to use, remix, and learn from.

---

## 👤 Built by
Fynn Pape – submitted as part of MIT Global AI Hackathon
