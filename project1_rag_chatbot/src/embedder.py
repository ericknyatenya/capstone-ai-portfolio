import numpy as np

class Embedder:
    """Demo embedder — uses a hash-based vector for reproducible small demos."""

    def embed(self, texts):
        vectors = []
        for t in texts:
            h = abs(hash(t))
            vec = np.array([((h >> i) & 255) / 255.0 for i in range(8)], dtype=float)
            vectors.append(vec)
        return np.vstack(vectors)
