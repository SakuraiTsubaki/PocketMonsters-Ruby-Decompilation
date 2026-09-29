# Ruby target-selection decision

The reconstruction target is the Japanese origin release, product code `AXVJ`, software revision 0. It is the highest-priority locally observed release and is represented by an 8 MiB input whose SHA-1, SHA-256, title, product code, maker code, revision, and GBA header checksum are recorded in `config/target.json`.

English `AXVE` revisions 0, 1, and 2 were also observed, but are retained as comparison candidates rather than the primary reconstruction target. Their existence does not alter the Japanese-first policy.

The identity is `identified`, not `verified`: internal header integrity and repeatable local hashing are strong correspondence evidence but are not independent provenance corroboration or a matching reconstruction build. No ROM bytes are stored.
