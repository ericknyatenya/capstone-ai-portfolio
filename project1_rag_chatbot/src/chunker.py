def chunk_text(text: str, chunk_size: int = 100, overlap: int = 20):
    """Simple whitespace chunker for demo purposes."""
    if not text:
        return []
    words = text.split()
    step = max(1, chunk_size - overlap)
    chunks = []
    i = 0
    while i < len(words):
        chunks.append(" ".join(words[i:i+chunk_size]))
        i += step
    return chunks
