# Gen AI: Zero to One

Companion code, notebooks, and experiments for my **Gen AI: Zero to One** course —
building Gen AI from first principles, with runnable code for every lesson.

> 📖 Read the course: **[Gen AI: Zero to One](https://jayantkhd.vercel.app/blog/gen-ai-zero-to-one)**
> · Portfolio: **[jayantkhd.vercel.app](https://jayantkhd.vercel.app)**

Each lesson on the site pairs with a script or notebook here, so you can run and
tweak everything yourself. On the site you can also open these files **live in a
side panel** while you read.

## How this fits together

The writing and the code live in separate places, cross-linked:

- **The writing** lives on my [portfolio site](https://jayantkhd.vercel.app/blog) — each lesson
  explains the idea with text, code, diagrams, and quick multiple-choice checks.
- **The code** lives here, in this public repo — **one repo per course/series**. Lessons link out
  to the matching file; each file links back to its lesson.
- **Your progress is yours.** As you read on the site, your completed lessons, quiz answers, and
  "% complete" are saved in *your own browser* (localStorage) — no account, no server, nothing
  tracked. It sticks on that browser across visits, but it doesn't follow you to another device,
  and clearing site data resets it.

## Lessons

### Foundations (Phase 0)

| Lesson | Code |
|--------|------|
| [Data Management](https://jayantkhd.vercel.app/blog/gen-ai-zero-to-one/data-management) | [`foundations/data-management/`](./foundations/data-management) |
| [Linear Algebra, Intuitively](https://jayantkhd.vercel.app/blog/gen-ai-zero-to-one/linear-algebra) | [`foundations/linear-algebra/`](./foundations/linear-algebra) |

### Transformers from scratch

| Lesson | Code |
|--------|------|
| [What Is a Token?](https://jayantkhd.vercel.app/blog/gen-ai-zero-to-one/what-is-a-token) | [`transformers/tokenization.ipynb`](./transformers/tokenization.ipynb) |
| [Self-Attention, Intuitively](https://jayantkhd.vercel.app/blog/gen-ai-zero-to-one/self-attention) | [`transformers/self_attention.py`](./transformers/self_attention.py) |
| [Putting Order Back In](https://jayantkhd.vercel.app/blog/gen-ai-zero-to-one/positional-encoding) | [`transformers/positional_encoding.py`](./transformers/positional_encoding.py) |

## Getting started

```bash
python -m venv .venv
# Windows:  .venv\Scripts\activate
# macOS/Linux:  source .venv/bin/activate

pip install -r requirements.txt

# Run a lesson's script:
python foundations/data-management/data_utils.py

# Or open the notebooks:
jupyter lab
```

## Layout

```
.
├── foundations/
│   ├── data-management/
│   │   ├── README.md
│   │   ├── data_utils.py            # load / split / convert helper
│   │   ├── data_management.ipynb    # full walkthrough
│   │   └── prompt-data-helper.md
│   └── linear-algebra/
│       ├── README.md
│       ├── vectors.py               # vectors, similarity, matmul, attention
│       └── linear_algebra.ipynb
├── transformers/
│   ├── tokenization.ipynb           # how text becomes token IDs
│   ├── self_attention.py            # scaled dot-product attention in PyTorch
│   └── positional_encoding.py       # sinusoidal positional encodings
└── requirements.txt
```

New lessons land here under their phase/topic folder.

## License

[MIT](./LICENSE) © Jayant Khandebharad
