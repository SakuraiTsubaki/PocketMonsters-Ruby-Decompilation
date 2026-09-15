# Repository Structure

The repository uses a stable, purpose-based live tree. Directories should be created only when they contain real project material.

Recommended long-term areas:

```text
docs/        documentation and research records
manifests/   machine-readable identity, provenance, coverage, and asset records
src/         reconstructed or decompiled source when appropriate
data/        editable structured game data
assets/      reviewable reconstructed/extracted/converted assets
tools/       reproducible project tooling
tests/       validation, regression, and round-trip tests
patches/     non-ROM patch artifacts when appropriate
```

A verified platform may require different names or additional directories. Extend the tree locally rather than redesigning the repository root.

Forbidden live-tree patterns include repository-wide structure-version roots, migration-history trees, and duplicated canonical homes. Historical layouts remain available through Git history.
