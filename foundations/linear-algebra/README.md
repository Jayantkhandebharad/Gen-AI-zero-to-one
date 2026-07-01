# Linear Algebra, Intuitively

Companion code for the lesson **[Linear Algebra, Intuitively](https://jayantkhd.vercel.app/blog/gen-ai-zero-to-one/linear-algebra)** — *Gen AI: Zero to One · Phase 0*.

Three ideas — vectors, the dot product, and matrix multiplication — and how they add up to
what a Transformer computes in attention.

## Run

```bash
pip install -r ../../requirements.txt   # just needs numpy
python foundations/linear-algebra/vectors.py
```

Prints toy-embedding similarities, a linear-layer projection, and an attention-score matrix.

## Files

| File | What it is |
|------|------------|
| `vectors.py` | Vectors, cosine similarity, a linear layer, and `Q @ K.T` attention scores in ~30 lines |
| `linear_algebra.ipynb` | The same, cell by cell |
