# Verification Guide

Use explicit validation states:

- **Unverified** — planned, imported, or reported without local confirmation.
- **Observed** — directly confirmed in an identified target or source.
- **Reproduced** — a documented tool or procedure deterministically reproduces the result.
- **Matched** — output is proven identical to the intended reference at the required byte/hash/build level.

Visual similarity alone is not a match. Deduplication requires byte/hash evidence where identity matters. Compression, encoding, conversion, and reconstruction workflows should use round-trip tests whenever practical.

When a result fails validation, keep the failure documented if it is useful evidence, but do not present it as current canonical output.
