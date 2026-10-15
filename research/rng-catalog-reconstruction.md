# Pokémon Ruby RNG release-catalog reconstruction

The existing Japanese RNG reconstruction remains the origin reference. Twelve additional catalog identities were SHA-256 gated and independently matched to the complete adjacent `Random`/`SeedRng` compiler layout and a shared IWRAM state. The resulting scope is 13 identities: Japanese, three English revisions, German debug plus two German retail revisions, and two revisions each for French, Italian, and Spanish.

Every build implements `state = 1103515245 * state + 24691`, returns bits 31..16, and seeds the same 32-bit state used by `Random`. Function and state addresses remain release-specific. The German debug build retains `build_kind=debug` and is never treated as a retail baseline.

The existing `src/random.c` is reused because its semantics match every verified identity. Names and behavior follow `pret/pokeruby@5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, `src/random.c`. All CFGs omit ROM halfwords.
