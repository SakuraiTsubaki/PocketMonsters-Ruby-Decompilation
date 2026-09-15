# Project Standards

## Naming and identity

- Prefer stable, descriptive, ASCII-safe machine paths unless the verified source format requires otherwise.
- Preserve technically meaningful original identifiers and document aliases rather than silently renaming them.
- Record version, language, revision, region, update, and form distinctions whenever they materially differ.

## Source and generated data

- Prefer editable source plus reproducible generation steps over opaque generated output.
- Generated material must identify source inputs and generation method when practical.
- Keep tools required to reproduce committed derived data whenever practical.
- Do not invent missing metadata; use `unknown`, `TBD`, or `null`.

## Evidence and provenance

- Separate confirmed observation from hypothesis.
- Prefer hashes and stable identifiers over filenames alone.
- Record source archive/container, offset/index/symbol, tool or command, and verification state when relevant.

## Assets

- Human-viewable previews may be committed when they improve review or verification.
- Byte-identical assets may be stored once and referenced by manifests only after hash or byte-level confirmation.
- Do not deduplicate merely because two assets look the same.
- Preserve meaningful regional, language, revision, form, palette, frame, or update differences.

## Repository stability

- One current live structure only.
- Do not create repository-wide `vN`, `PRE-VN`, `MIGRATED`, or parallel legacy trees.
- Git history is the historical record.
- A project or artifact has one canonical home; indexes may reference it, but must not create competing ownership.

## Repository boundaries

Do not commit retail ROMs, modified/rebuilt ROMs, decrypted full-game images, console keys, or disguised complete game images. Reconstructed source, analysis, manifests, tooling, documentation, patches, and reviewable derived assets are allowed when appropriate.

Platform-specific rules may extend these standards only after the target architecture is verified.
