# Version Coverage

This document tracks target versions for the Ruby decompilation project.

## Source policy

Version identities are recorded only after direct inspection of project-owned source material such as locally supplied ROM dumps, extracted headers, hashes, and reproducible analysis output. Public decompilation repositories and third-party reconstruction projects are not used as authoritative inputs for this project.

## Current target inventory

No version is locked yet.

| Status | Region | Language | Revision | Header identity | Hashes | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Pending direct verification | TBD | TBD | TBD | TBD | TBD | Populate from directly analyzed source material |

## Recording rules

1. Record exact revision information from the inspected source.
2. Compute cryptographic hashes locally from the inspected source.
3. Record GBA header fields directly from the inspected source.
4. Do not infer equality between regions, languages, or revisions.
5. Do not commit retail ROM images.
6. Keep provenance for every target identity and verification result.
