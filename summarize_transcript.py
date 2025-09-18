from transformers import pipeline
def chunk_text(text, max_chars=3000):
    words = text.split()
    chunks = []
    cur=[]
    cur_len=0
    for w in words:
        cur.append(w)
        cur_len += len(w)+1
        if cur_len > max_chars:
            chunks.append(" ".join(cur))
            cur=[]
            cur_len=0
    if cur:
        chunks.append(" ".join(cur))
    return chunks

def summarize_transcript(full_text):
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    chunks = chunk_text(full_text)
    chunk_summaries = []
    for c in chunks:
        out = summarizer(c, max_length=120, min_length=20, do_sample=False)[0]['summary_text']
        chunk_summaries.append(out)
    combined = " ".join(chunk_summaries)
    final = summarizer(combined, max_length=150, min_length=25, do_sample=False)[0]['summary_text']
    return final
