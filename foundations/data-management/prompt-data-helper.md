# Prompt — find the right dataset for a task

Paste this into any capable LLM to scope a dataset before you start building.

---

You are a senior ML engineer. I'm working on the following task:

- **Task:** <describe it — e.g. "classify support tickets into 5 categories">
- **Constraints:** <language(s), domain, license needs, max size, modality>

Recommend **3 candidate datasets**. For each, give:

1. Name + Hugging Face Hub id (the exact `load_dataset("...")` call)
2. Size, number of examples, and license
3. Schema (fields and types) and a one-line sample
4. Why it fits — and one risk or caveat (bias, staleness, label noise)
5. The exact `datasets` snippet to load it and split 80/10/10 with `seed=42`

Prefer openly licensed datasets small enough to iterate on locally. End with a
one-line recommendation of which to start with, and why.
