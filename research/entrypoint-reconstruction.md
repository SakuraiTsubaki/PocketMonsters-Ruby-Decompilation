# Japanese ROM entrypoint reconstruction

The selected Japanese target begins with ARM word `0xea000032`. ARM PC+8 branch semantics resolve it from `0x08000000` to `0x080000d0`. `src/rom_entry.s` preserves the exact word while documenting the decoded control-flow target. The JSON evidence is reproducible with the shared Decompilation entrypoint tool and exact target SHA-256; no ROM bytes beyond this instruction representation are stored.
