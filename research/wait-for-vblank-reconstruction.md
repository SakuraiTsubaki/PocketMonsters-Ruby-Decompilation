# WaitForVBlank reconstruction

Target: AXVJ-rev0 (e911caa1ffbf8704cd45bbe064ade40e24efa50dfdce82adf4b2899b5f733852)

The already verified Japanese `AgbMain` map calls `WaitForVBlank` at 0x08000698. A fresh conservative Thumb trace terminates at 0x080006AE, observes a return, and is published without instruction halfwords. The code-only ROM range SHA-256 is `e992a65f8499fd2abe2a7cde25fe952d45f9426edab39735991ef8ee3f0206fa`; no ROM bytes are stored.

The function clears bit 0 of `gMain.intrCheck` at the proven offset `0x1C` before waiting. This build then calls the BIOS-facing `VBlankIntrWait` target 0x081B12CC. The corresponding `VBlankIntr` reconstruction independently shows that the handler sets the same flag, closing the producer/consumer relationship.

Names were aligned with [pret/pokeruby](https://github.com/pret/pokeruby) at commit `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, then checked against this ROM's addresses, control flow, literals, and state accesses. The upstream project is a naming reference, not a substitute for the local ROM evidence.

