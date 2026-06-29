"""Reusable data loading, conversion, and splitting utility.

Companion code for the "Data Management" lesson:
https://jayantkhd.vercel.app/blog/gen-ai-zero-to-one/data-management

Run:  python foundations/data-management/data_utils.py

It downloads a small dataset, makes a reproducible 80/10/10 split, writes the
training split to Parquet, and prints a summary.
"""

from __future__ import annotations

from datasets import Dataset, load_dataset


def make_splits(
    dataset: Dataset,
    *,
    seed: int = 42,
    val_frac: float = 0.1,
    test_frac: float = 0.1,
) -> tuple[Dataset, Dataset, Dataset]:
    """Return (train, val, test) using a fixed seed so the split is reproducible.

    val_frac and test_frac are fractions of the *original* dataset.
    """
    first = dataset.train_test_split(test_size=test_frac, seed=seed)
    rest, test = first["train"], first["test"]

    # Scale val_frac to the remaining rows after test was carved off.
    val_size = val_frac / (1.0 - test_frac)
    second = rest.train_test_split(test_size=val_size, seed=seed)
    return second["train"], second["test"], test


def main() -> None:
    print("Loading imdb (train split)…")
    dataset = load_dataset("imdb", split="train")

    train, val, test = make_splits(dataset)
    print(f"Split -> train={len(train)}  val={len(val)}  test={len(test)}")

    out_path = "imdb_train.parquet"
    train.to_parquet(out_path)
    print(f"Wrote {out_path} ({len(train)} rows)")


if __name__ == "__main__":
    main()
