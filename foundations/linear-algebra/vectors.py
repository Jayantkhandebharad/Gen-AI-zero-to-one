"""Linear algebra intuition — vectors, dot products, matmul, attention.

Companion code for "Linear Algebra, Intuitively":
https://jayantkhd.vercel.app/blog/gen-ai-zero-to-one/linear-algebra

Run:  python foundations/linear-algebra/vectors.py
"""

import numpy as np


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Direction-only similarity: the dot product with lengths divided out."""
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def main() -> None:
    # Toy 4-D "embeddings" — real ones have hundreds/thousands of dimensions.
    king = np.array([0.9, 0.8, 0.1, 0.7])
    queen = np.array([0.9, 0.2, 0.1, 0.8])
    apple = np.array([0.1, 0.1, 0.9, 0.2])

    print("Vectors are points in space:")
    print(f"  king shape={king.shape}  length={np.linalg.norm(king):.3f}")

    print("\nDot product = similarity (cosine):")
    print(f"  king vs queen: {cosine_similarity(king, queen):.3f}  (similar)")
    print(f"  king vs apple: {cosine_similarity(king, apple):.3f}  (different)")

    print("\nMatrix x vector = a transformation (a linear layer, y = W x):")
    W = np.array([[1.0, 0.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0, 0.0]])   # (2, 4): project 4-D -> 2-D
    print(f"  projected king: {W @ king}")

    print("\nMatrix x matrix = many dot products at once (attention scores):")
    Q = np.stack([king, queen, apple])     # (3, 4): one query per token
    K = Q.copy()                            # (3, 4): the keys
    scores = Q @ K.T                        # (3, 3): every query vs every key
    print(f"  scores shape: {scores.shape}")
    print(np.round(scores, 2))


if __name__ == "__main__":
    main()
