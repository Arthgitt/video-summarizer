#!/usr/bin/env bash
set -e
if [ -z "$1" ]; then
  echo "Usage: ./run_pipeline.sh VIDEO_URL"
  exit 1
fi
URL="$1"
mkdir -p downloads results

# 1) download & extract audio as WAV
yt-dlp -x --audio-format wav -o "downloads/%(title)s.%(ext)s" "$URL"

wav=$(ls downloads/*.wav | head -n1)
title=$(basename "$wav" .wav)
txt="downloads/${title}.txt"
results_json="results/${title}.summary.json"

# 2) transcribe using whisper (openai-whisper python package)
#    run via python to avoid dealing with binary differences
python - <<PY
import whisper, json,sys
m = whisper.load_model("tiny.en")           # tiny English model = fast
res = m.transcribe("$wav", language="en")
text = res["text"]
with open("$txt","w",encoding="utf-8") as f:
    f.write(text)
print("Transcription saved to $txt")
PY

# 3) summarize
python - <<PY
from summarize_transcript import summarize_transcript
txt = "$txt"
with open(txt,"r",encoding="utf-8") as f:
    text = f.read()
summary = summarize_transcript(text)
out = {"transcript_file": txt, "summary": summary}
import json
with open("$results_json","w",encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved summary to $results_json")
PY

echo "Pipeline finished. See results/ for outputs."
