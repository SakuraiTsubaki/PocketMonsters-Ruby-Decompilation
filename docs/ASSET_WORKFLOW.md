# Asset Workflow

1. Identify the exact source target and source location.
2. Extract or reconstruct deterministically.
3. Preserve native source identity and hashes.
4. Produce human-reviewable representations when useful.
5. Convert or normalize only when a defined target requires it.
6. Deduplicate only after byte/hash confirmation.
7. Register source, outputs, method, hashes, and verification state in a manifest.
8. Validate encoding/compression/conversion with round trips where practical.
9. Publish in small, reviewable batches.

For cross-generation conversions, the source repository remains authoritative for source facts. Derived target material must state both source identity and target contract; it must not erase the native source layer.
