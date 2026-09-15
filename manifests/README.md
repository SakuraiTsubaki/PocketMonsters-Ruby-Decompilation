# Manifests

Manifests provide machine-readable identity, provenance, coverage, and verification records.

Useful fields include:

- logical ID / asset ID
- repository path
- target version, region, language, revision, update, form, or frame
- source container/archive/bank/section
- source offset/index/symbol/record ID
- file size
- cryptographic hash
- extraction or generation tool/command
- verification state
- deduplication relationship
- notes and known differences

Use JSON, YAML, CSV, or another reviewable structured format appropriate to the dataset. Unknown values remain explicit; they are never guessed.
