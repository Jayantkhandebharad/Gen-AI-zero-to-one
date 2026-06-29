# Gen AI: Zero to One

Companion code, notebooks, and experiments for my Gen AI writing — building the
ideas behind modern language models from first principles, with runnable code.

> 📖 Read the series: **[Transformers from Scratch](https://jayantkhd.vercel.app/blog/transformers-from-scratch)**
> · Portfolio: **[jayantkhd.vercel.app](https://jayantkhd.vercel.app)**

Each post on the site is paired with a script or notebook here, so you can run
and tweak everything yourself.

## How this fits together

I keep the writing and the code in separate places, cross-linked:

- **The writing** lives on my [portfolio site](https://jayantkhd.vercel.app/blog) — each post
  explains the idea with text, code, diagrams, and quick multiple-choice checks.
- **The code** lives in public repos like this one — **one repo per series**. Posts link out to
  the matching file here; each file links back to its post.
- **Your progress is yours.** As you read on the site, your completed posts, quiz answers, and
  per-series "% complete" are saved in *your own browser* (localStorage) — no account, no server,
  nothing tracked. It sticks on that browser across visits, but it doesn't follow you to another
  device, and clearing site data resets it.

This repo covers the **Transformers from Scratch** series; new series get their own repos.

## Series — Transformers from Scratch

| # | Post | Code |
|---|------|------|
| 01 | [What Is a Token?](https://jayantkhd.vercel.app/blog/transformers-from-scratch/what-is-a-token) | [`01_tokenization.ipynb`](./01_tokenization.ipynb) |
| 02 | [Self-Attention, Intuitively](https://jayantkhd.vercel.app/blog/transformers-from-scratch/self-attention) | [`02_self_attention.py`](./02_self_attention.py) |
| 03 | [Putting Order Back In](https://jayantkhd.vercel.app/blog/transformers-from-scratch/positional-encoding) | [`03_positional_encoding.py`](./03_positional_encoding.py) |

## Getting started

```bash
python -m venv .venv
# Windows:  .venv\Scripts\activate
# macOS/Linux:  source .venv/bin/activate

pip install -r requirements.txt

# Run a script:
python 02_self_attention.py

# Or open the notebooks:
jupyter lab
```

## Layout

```
.
├── 01_tokenization.ipynb        # how text becomes token IDs
├── 02_self_attention.py         # scaled dot-product attention in PyTorch
├── 03_positional_encoding.py    # sinusoidal positional encodings
└── requirements.txt
```

New posts in the series land here as new scripts/notebooks.

## License

[MIT](./LICENSE) © Jayant Khandebharad
