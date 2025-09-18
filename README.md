# Video Summarizer (download → transcribe → summarize)

Quick start:
1. Install system deps: ffmpeg, Python3, git
2. Run `./run_local.sh` (mac/linux) to create venv and install Python packages
3. Run web UI: `source .venv/bin/activate && python app.py`
4. Open http://localhost:7860 in your browser, paste a YouTube URL or upload audio

To run CLI pipeline:
./run_pipeline.sh "https://youtube.com/..."

Notes:
- I use `whisper` (tiny.en) for local transcription and `sshleifer/distilbart-cnn-12-6` for summarization.
- To deploy: push this repo to GitHub and create a Hugging Face Space (Gradio) from this repository. Add `apt.txt` to install ffmpeg on Spaces.
