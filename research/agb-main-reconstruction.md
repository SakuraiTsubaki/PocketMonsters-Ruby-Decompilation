# AXVJ revision 0 `AgbMain` reconstruction

The existing entry CFG reaches a non-returning Thumb function at `0x0800024C`.
Its 21 direct call sites, reset mask, wait-state write, soft-reset condition,
three repeated calls to `0x08000348`, and loop back edge at `0x08000342` match
the `AgbMain` control flow in `pret/pokeruby` `src/main.c` at commit
`5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`.

`src/main_loop.c` reconstructs that behavior for the verified Japanese AXVJ
revision 0 ROM. Names for the two link-queue predicates are descriptive because
the public source retains address-derived placeholder names for those routines;
the JSON map preserves their exact Japanese call targets instead of pretending
the English symbol addresses are interchangeable.

The Japanese build also calls `0x08000F90` at `0x08000328`, after clearing new
keys on the receive-queue path and before dispatching callbacks again. That call
is represented conservatively as `LinkRecvPostprocess`; its exact upstream name
is unresolved. The final three calls align with play-time, map-music, and
VBlank-wait processing before the loop back edge. This boundary keeps verified
behavior separate from naming inference. No ROM instruction bytes are included
in this unit.
