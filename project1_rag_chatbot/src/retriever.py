import numpy as np

class Retriever:
    def __init__(self):
        self.docs = []
        self.vectors = None

    def add(self, docs, vectors):
        self.docs.extend(docs)
        self.vectors = np.vstack([self.vectors, vectors]) if self.vectors is not None else np.array(vectors)

    def retrieve(self, query_vector, top_k=3):
        if self.vectors is None:
            return []
        sims = self.vectors @ query_vector / (np.linalg.norm(self.vectors, axis=1) * (np.linalg.norm(query_vector) + 1e-12))
        idx = sims.argsort()[::-1][:top_k]
        return [(int(i), float(sims[i]), self.docs[i]) for i in idx]
