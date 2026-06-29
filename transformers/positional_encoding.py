"""Sinusoidal positional encodings, from scratch.

Companion code for "Putting Order Back In":
https://jayantkhd.vercel.app/blog/transformers-from-scratch/positional-encoding

Run:  python 03_positional_encoding.py
      python 03_positional_encoding.py --plot   # saves positional-encoding.png
"""

import argparse

import torch


def sinusoidal(seq_len: int, d_model: int) -> torch.Tensor:
    """Return a (seq_len, d_model) matrix of sinusoidal positional encodings."""
    pos = torch.arange(seq_len).unsqueeze(1)              # (seq, 1)
    i = torch.arange(d_model).unsqueeze(0)                # (1, d_model)
    angle = pos / (10000 ** (2 * (i // 2) / d_model))
    pe = torch.zeros(seq_len, d_model)
    pe[:, 0::2] = torch.sin(angle[:, 0::2])               # even dims -> sin
    pe[:, 1::2] = torch.cos(angle[:, 1::2])               # odd dims  -> cos
    return pe


def demo(plot: bool) -> None:
    pe = sinusoidal(seq_len=64, d_model=128)
    print("positional encoding shape:", tuple(pe.shape))
    print("first position, first 8 dims:", pe[0, :8].round(decimals=3).tolist())

    if plot:
        import matplotlib.pyplot as plt

        plt.figure(figsize=(8, 4))
        plt.imshow(pe.numpy(), aspect="auto", cmap="viridis")
        plt.xlabel("dimension")
        plt.ylabel("position")
        plt.title("Sinusoidal positional encoding")
        plt.colorbar()
        plt.tight_layout()
        plt.savefig("positional-encoding.png", dpi=120)
        print("saved positional-encoding.png")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--plot", action="store_true", help="save a heatmap to PNG")
    args = parser.parse_args()
    demo(plot=args.plot)
