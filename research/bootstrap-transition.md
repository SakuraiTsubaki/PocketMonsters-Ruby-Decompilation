# Bootstrap ARM-to-Thumb transition

Starting at the decoded entry target `0x080000d0`, twelve ARM words lead to `bx r1` at `0x080000fc`. The closest PC-relative load into `r1` reads literal `0x0800024d` from `0x08000244`, proving a Thumb-state transition to aligned address `0x0800024c`. This direct control-flow edge is stronger evidence than regional entropy or opcode-pattern counting.
