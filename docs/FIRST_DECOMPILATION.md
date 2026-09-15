# First Decompilation Unit — Calendar Day Count

Direct comparison of the supplied retail revisions found a repeated four-byte delta. Two bytes are the GBA header revision/checksum. The two executable bytes change Thumb conditional branches in the same function:

- old: `BLE` before the prior-year loop and `BGT` at the loop back-edge
- fixed: `BLT` before the prior-year loop and `BGE` at the loop back-edge

This changes the prior-year iteration domain from `y > 0` to `y >= 0`.

The function calls a leap-year predicate and accumulates a directly observed 12-entry month table:

`31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31`

Old boundary behavior occurs in `jp-r0`, `en-us-r0`, `en-eu-r1`, `fr-r0`, `de-r0`, `de-debug-r0`, `it-r0`, and `es-r0`. Corrected behavior occurs in `en-us-eu-r2`, `fr-r1`, `de-r1`, `it-r1`, and `es-r1`.

The initial semantic C reconstruction is at `src/calendar_day_count.c`, following the repository's established top-level source layout. It preserves Japanese Rev 0 behavior and separately documents the later corrected boundary. Compiler matching has not started yet.
