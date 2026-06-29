# Data Management

Companion code for the lesson **[Data Management](https://jayantkhd.vercel.app/blog/gen-ai-zero-to-one/data-management)** — *Gen AI: Zero to One · Phase 0*.

## Run

```bash
# from the repo root, with the virtualenv active (see ../../README.md)
pip install -r ../../requirements.txt
python foundations/data-management/data_utils.py
```

`data_utils.py` downloads a small dataset, makes a reproducible 80/10/10 split
(fixed seed), writes the training split to Parquet, and prints a summary.

## Files

| File | What it is |
|------|------------|
| `data_utils.py` | Reusable load / split / convert helper (`make_splits` + a runnable demo) |
| `data_management.ipynb` | The full step-by-step walkthrough (load, stream, convert, split, cache) |
| `prompt-data-helper.md` | A prompt for choosing the right dataset for a task |
