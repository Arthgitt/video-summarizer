import os, uuid, json, shutil, subprocess, tempfile
import gradio as gr
import yt_dlp
import whisper
from summarize_transcript import summarize_transcript

# load models once on startup
print("Loading whisper tiny.en model (this may take a minute)...")
whisper_model = whisper.load_model("tiny.en")
print("Whisper loaded.")

def download_audio(url, download_folder="downloads"):
    os.makedirs(download_folder, exist_ok=True)
    outtmpl = os.path.join(download_folder, "%(title)s.%(ext)s")
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": outtmpl,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
            "preferredquality": "192"
        }],
        "quiet": True,
        "no_warnings": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        base = os.path.splitext(filename)[0]
        wav = base + ".wav"
        title = info.get("title", "downloaded_audio")
        return wav, title

def transcribe_file(wav_path):
    res = whisper_model.transcribe(wav_path, language="en")
    return res["text"]

def process(url, audio_file):
    # url takes precedence; audio_file is a tuple (name, fileobj) from Gradio
    tmp_dir = "downloads"
    os.makedirs(tmp_dir, exist_ok=True)

    if url:
        try:
            wav, title = download_audio(url, download_folder=tmp_dir)
        except Exception as e:
            return f"Error downloading audio: {e}", ""
    elif audio_file:
        # save uploaded audio to a file
        name = audio_file.name
        dest = os.path.join(tmp_dir, f"{uuid.uuid4().hex}_{name}")
        with open(dest, "wb") as out:
            out.write(audio_file.read())
        wav = dest
        title = os.path.splitext(name)[0]
    else:
        return "No input provided. Enter a video URL or upload an audio file.", ""

    try:
        transcript_text = transcribe_file(wav)
    except Exception as e:
        return f"Transcription error: {e}", ""

    try:
        summary = summarize_transcript(transcript_text)
    except Exception as e:
        return f"Summarization error: {e}", transcript_text

    # Save results
    os.makedirs("results", exist_ok=True)
    outpath = os.path.join("results", f"{title}.summary.json")
    with open(outpath, "w", encoding="utf-8") as f:
        json.dump({"title": title, "url": url, "transcript": transcript_text, "summary": summary}, f, ensure_ascii=False, indent=2)

    return summary, transcript_text

with gr.Blocks() as demo:
    gr.Markdown("# Video → Transcript → Summary")
    with gr.Row():
        url_input = gr.Textbox(label="Video URL (YouTube etc.)", placeholder="https://youtu.be/...")
        file_input = gr.File(label="Or upload audio file (mp3/wav)")
    run_btn = gr.Button("Run")
    summary_out = gr.Textbox(label="Summary", lines=6)
    transcript_out = gr.Textbox(label="Transcript", lines=15)
    run_btn.click(process, inputs=[url_input, file_input], outputs=[summary_out, transcript_out])

if __name__ == '__main__':
    demo.launch(server_name="0.0.0.0", server_port=7860)
