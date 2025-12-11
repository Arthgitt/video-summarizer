# Video Summarizer (download → transcribe → summarize)

### Try it now - [Checkout on Huggingface](huggingface.co/spaces/ArthPat/video-summarizer)
Note: Hugging Face blocks external network calls for application like Youtube etc. to access, so need to upload video from local machine, or try locally for full capabilities with youtube link feature...

Video Summarizer is an Python application that lets download, transcribe, and generate summaries of video content (e.g., YouTube videos or local video/audio files). It uses automatic transcription tools and natural language summarization models to convert spoken content into concise text summaries, making video content easier to read, reference, and analyze without watching the full video.

 - Video download and audio extraction — automatically retrieves video or audio files from a given video source.

 - Transcription pipeline — uses Whisper-based speech-to-text to convert spoken dialogue into a transcript.

 - Text summarization — applies a language model to shorten the transcript into a human-readable summary.

 - Web UI & CLI support — offers both an interactive web interface (e.g., Gradio/Streamlit style) and command-line pipeline scripts for flexible usage.

 - Easy setup & local deployment — ready to run locally with Python and standard dependencies like FFmpeg for media processing.

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
