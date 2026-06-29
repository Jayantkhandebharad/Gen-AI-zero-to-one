"""Scaled dot-product self-attention, from scratch.

Companion code for "Self-Attention, Intuitively":
https://jayantkhd.vercel.app/blog/transformers-from-scratch/self-attention

Run:  python 02_self_attention.py
"""

import torch
import torch.nn.functional as F


def attention(q: torch.Tensor, k: torch.Tensor, v: torch.Tensor) -> torch.Tensor:
    """Scaled dot-product attention.

    Args:
        q, k, v: tensors of shape (seq_len, d_k).

    Returns:
        Tensor of shape (seq_len, d_k): each position is a weighted sum of the
        value vectors, where the weights come from query-key similarity.
    """
    d_k = k.size(-1)
    scores = q @ k.transpose(-2, -1)          # (seq, seq)
    scores = scores / (d_k ** 0.5)            # scale so softmax doesn't saturate
    weights = F.softmax(scores, dim=-1)        # normalize over the key dimension
    return weights @ v                         # weighted sum of values


def demo() -> None:
    torch.manual_seed(0)
    seq_len, d_k = 4, 8
    q = torch.randn(seq_len, d_k)
    k = torch.randn(seq_len, d_k)
    v = torch.randn(seq_len, d_k)

    out = attention(q, k, v)

    # Inspect the attention weights directly.
    scores = (q @ k.transpose(-2, -1)) / (d_k ** 0.5)
    weights = F.softmax(scores, dim=-1)

    print("attention weights (rows sum to 1):")
    print(weights.round(decimals=2))
    print("\nrow sums:", weights.sum(dim=-1).round(decimals=3).tolist())
    print("output shape:", tuple(out.shape))


if __name__ == "__main__":
    demo()
