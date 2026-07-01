# Linear Algebra, Intuitively

Companion code for the lesson **[Linear Algebra, Intuitively](https://jayantkhd.vercel.app/blog/gen-ai-zero-to-one/linear-algebra)** — *Gen AI: Zero to One · Phase 0*.

Vectors, the dot product, matrix multiplication, and linear independence / rank — and how they
add up to what a Transformer computes in attention (and why LoRA works).

## Run

```bash
pip install -r ../../requirements.txt   # just needs numpy
python foundations/linear-algebra/vectors.py
```

Prints toy-embedding similarities, a linear-layer projection, and an attention-score matrix.

## Files

| File | What it is |
|------|------------|
| `vectors.py` | Vectors, cosine similarity, a linear layer, `Q @ K.T` attention scores, and matrix rank |
| `linear_algebra.ipynb` | The same, cell by cell |
