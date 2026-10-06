# DoSoftReset reconstruction

Target: AXVJ-rev0 (e911caa1ffbf8704cd45bbe064ade40e24efa50dfdce82adf4b2899b5f733852)

The verified Japanese `AgbMain` map calls `DoSoftReset` at 0x080006B8. A fresh Thumb trace closes at 0x08000714, observes a return, and is published without instruction halfwords. The code-only range SHA-256 is `c9480530fd1cb42dd81f25a59fa3cb67c595a6f75c945306cab5c7fbb737aeb1`; no ROM bytes are stored.

The straight-line routine disables the interrupt master switch, stops sound VSync and the scanline effect, then disables DMA channels 1, 2, and 3 through their control-high registers. This Ruby/Sapphire/Emerald-family build protects the RTC and passes the full `0xFF` reset mask to `SoftReset`.

Names were aligned with [pret/pokeruby](https://github.com/pret/pokeruby) at commit `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, then independently checked against this ROM's function boundary, direct-call targets, hardware addresses, and constants.

