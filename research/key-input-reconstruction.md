# AXVJ revision 0 key-input reconstruction

`AgbMain` calls `InitKeys` at `0x08000404` and `ReadKeys` at `0x0800042C`.
The ROM functions prove the five initialized key fields, repeat delays 5 and
40, active-low `REG_KEYINPUT` mask `0x03FF`, repeat-counter branches, L-to-A
option remapping, and watched-key latch.

The accesses establish `gMain` input offsets `0x28` through `0x36` and the
button-mode byte at `gSaveBlock2 + 0x13`. `src/key_input.c` reconstructs this
behavior while the JSON map preserves exact Japanese addresses and literals.
Names are grounded in the control-flow-equivalent `pret/pokeruby` `main.c`;
no ROM instruction bytes are published.
