# Video Summarizer (download → transcribe → summarize)

### Try it now - [Checkout on Huggingface](huggingface.co/spaces/ArthPat/video-summarizer)
Note: This project need to store data of transcript and audio file, and Huggingface free space is limited so it will through error if all the storage are used. If so, Please Try it locally.. 

Video Summarizer is an open-source Python application that lets users download, transcribe, and generate summaries of video content (e.g., YouTube videos or local video/audio files). It uses automatic transcription tools and natural language summarization models to convert spoken content into concise text summaries, making video content easier to read, reference, and analyze without watching the full video.

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
