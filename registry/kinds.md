# Kind-Term Registry

## Status: Normative

Canonical vocabulary for living-thing and inorganic-matter kind-term classes.
Each base term is a Tonesu root compound; the tree structure reflects compositional
derivation, not an external taxonomy imported wholesale.

Corpus evidence (batch codes and sentence ranges) is listed at each established node.
Nodes marked *compositional-possible* exist by rule but have not yet been corpus-tested.

---

## Living Things (`zo`)

```
zo  (living thing)
│
├── zo-se-[x]  Perceptual organism — axis: defining sensory mode
│   │
│   ├── zo-se-so  Acoustic organism (genus term)
│   │            KNM-001 · S195–S201 · s176-s227.md
│   │   │
│   │   ├── zo-se-so-fe  territorial / cat class (Felidae)
│   │   │                KNM-002 · S202+ · s176-s227.md
│   │   │                KNM-003 · S252–S260 · s252-s278.md
│   │   │
│   │   ├── zo-se-so-li  pack-social / dog class (Canidae)
│   │   │                KNM-002 · S202+ · s176-s227.md
│   │   │                KNM-004 · S261–S278 · s252-s278.md
│   │   │
│   │   ├── zo-se-so-di  directional / bird class (Aves)
│   │   │                KNM-005 · S279–S285 · s279-s334.md
│   │   │
│   │   └── zo-se-so-pa  place-acoustic / whale (Cetacea)
│   │                    KNM-006 · S307–S313 · s279-s334.md
│   │
│   ├── zo-se-ma  matter-perceptual / fish & aquatic vertebrates
│   │            KNM-006 · S307–S313 · s279-s334.md
│   │
│   └── zo-se-ne  social-relational / herd ungulates
│                KNM-007 · S314–S320 · s279-s334.md
│
├── zo-su  structural organism / plants
│         PLT-001 · S286–S292 · s279-s334.md
│
├── zo-pe  component organism / arthropods & invertebrates
│         KNM-008 · S321–S327 · s279-s334.md
│
└── zo-ne  networked organism / fungi
          FNG-001 · S328–S334 · s279-s334.md
```

*`zo-li` (human-class organism) is not a corpus test target — humans appear as
`la-mi`, `la-tu`, `la-ze` throughout the corpus. The form is compositionally
valid but reserved rather than formally established as a kind-term class.*

---

## Inorganic Matter (`ma`)

```
ma  (matter/substance)
├── ma-su  structured matter / rock & mineral
│         MAT-001 · S293–S299 · s279-s334.md
├── ma-pa  place-matter / soil & sediment
│         MAT-001 · S293–S299 · s279-s334.md
└── ma-ki  flowing matter / water
          MAT-002 · S300–S306 · s279-s334.md
```

---

## Discrimination Rule

**The `'` rule applies at any level.** Each node in the tree is a valid base for
further discrimination. A discriminator subcompound prepends with `'` and scopes
over the entire base term:

```
[discriminator]'[base-class]
```

The tree is unbounded in depth — any node can serve as the base for a finer
distinction:

```
zo-se-so                               acoustic organism (genus)
  [behav]'zo-se-so                     a behavioral subgroup
    [feature]'[behav]'zo-se-so         a further-specified member
      [variant]'[feature]'[behav]'zo-se-so   individual variant
```

Corpus maximum depth so far: four apostrophes —
`no-lu'lu-pe'ma-ki'zo-se-so-fe` (melanistic jaguar, S259 KNM-003).
The rule places no upper limit; depth is bounded only by communicative need.

**Discriminating off intermediate nodes.** Organisms that do not cleanly fit
a terminal-class fourth root (`-li`, `-fe`, `-di`, `-pa`) can discriminate directly
off the three-root acoustic genus `zo-se-so`, or off the two-root base `zo-se` —
whichever level captures the relevant distinction. A fox, for instance, is neither
pack-social (`-li`) nor territorial-feline (`-fe`); the fox discriminator attaches to
`zo-se-so` directly (`{fox-discrim}'zo-se-so`), and fox subspecies are further
discriminators on top of that.

---

## Colloquial Stubs

Casual-register contractions for high-frequency kind-term classes. Full forms remain
canonical in formal and written register. See `registry/colloquial.md` for full entries.

| Stub | Full form | Class | Registry entry |
|------|-----------|-------|----------------|
| `zol` | `zo-se-so-li` | canid (dog, wolf, coyote…) | COL-001a |
| `zof` | `zo-se-so-fe` | felid / fox | COL-001b |
| `zod` | `zo-se-so-di` | bird class (Aves) | CLQ-002a |
| `zos` | `zo-su` | plant class | CLQ-002b |
| `zom` | `zo-se-ma` | fish & aquatic vertebrates | CLQ-002c |
| `zop` | `zo-se-so-pa` | whale (Cetacea) | CLQ-002d |
| `zon` | `zo-se-ne` | herd ungulates | CLQ-002e |
| `mas` | `ma-su` | rock & mineral | CLQ-003a |
