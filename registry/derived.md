# Derived Words

## Status: Draft

Registered compound words built from primitives using the rules in spec/word-formation.md.

These are accepted-standard or proposed entries — not colloquial contractions (see lexicon/colloquial.md).

---

## Entry Format

```
ID:           
Form:         
Type:         derivation | compound
Class:        entity | process | quality | relation
Definition:   
Composition:  
Register:     formal | standard
Domain:       
Status:       proposed | accepted
Examples:     
Related:      
```

---

## Entries

---

### Language Name

**W000**
```
Form:         to-ne-su
Casual form:  tonesu
Type:         meta / language self-reference  ← canonical example; do not refactor as ordinary vocabulary
Class:        entity
Definition:   the language itself; structured patterns of relation
Composition:  to (pattern/thought) + ne (relation/connection) + su (structure/order)
Register:     formal → casual
Domain:       meta
Status:       accepted
Examples:     "this sentence is written in to-ne-su" / "I speak tonesu"
Notes:        The language's own name is a primitive compound with a casual contraction.
              Demonstrates: compositional roots, phonological contraction, dual-register design.
              Pattern → relation → structure = meaning built from parts through connection.
```

---

### People and Roles

**W001**
```
Form:         li-su-li
Type:         compound
Class:        entity
Definition:   one who organizes people into structures; leader, coordinator, administrator
Composition:  li (person) + su (structure) + -li (agent)
Register:     standard
Domain:       social
Status:       proposed
Examples:     "the li-su-li directed the group project"
Related:      li-be-li (creator/founder), li-to-li (teacher/knower)
```

**W002**
```
Form:         su-mu-li
Type:         compound
Class:        entity
Definition:   one who builds or maintains structured systems; engineer, architect
Composition:  su (structure) + mu (object/device) + -li (agent)
Register:     standard
Domain:       general / technical
Status:       proposed
Examples:     "the su-mu-li designed the bridge"
Related:      su-li (anyone organized), mu-ka-li (operator; one who uses tools — see W022)
```

**W003**
```
Form:         to-li
Type:         compound
Class:        entity
Definition:   knower; one whose primary role is knowledge; scholar, expert, scientist
Composition:  to (knowledge) + li (person)
Register:     standard
Domain:       knowledge
Status:       proposed
Examples:     "the to-li studied the pattern"
Related:      to-su-li (one who organizes knowledge; librarian, archivist)
```

---

### Objects and Devices

**W010**
```
Form:         to-su-mu
Type:         compound
Class:        entity
Definition:   knowledge-organization device; filing system, database, library
Composition:  to (knowledge) + su (structure) + -mu (device)
Register:     formal
Domain:       knowledge / computation
Status:       proposed
Examples:     "the to-su-mu held all research logs"
Related:      to-ki-mu (computation device / computer)
```

**W011**
```
Form:         to-ki-mu
Type:         compound
Class:        entity
Definition:   knowledge-processing device; computer, calculator
Composition:  to (knowledge/pattern) + ki (change/process) + -mu (device)
Register:     formal
Domain:       computation
Status:       proposed
Examples:     "the to-ki-mu solved the equation"
Related:      to-su-mu (storage device), to-ki-li (programmer)
```

**W012**
```
Form:         ra-ki-mu
Type:         compound
Class:        entity
Definition:   energy-conversion device; engine, motor, generator
Composition:  ra (energy) + ki (change) + -mu (device)
Register:     standard
Domain:       energy / mechanics
Status:       proposed
Examples:     "the ra-ki-mu powered the vessel"
Related:      ra-su-mu (energy storage / battery)
```

---

### Processes and Actions

**W020**
```
Form:         to-ki
Type:         derivation
Class:        process
Definition:   the act of processing or transforming knowledge; computation, reasoning, learning
Composition:  to (knowledge) + ki (change)
Register:     standard
Domain:       knowledge / computation
Status:       proposed
Examples:     "rapid to-ki solved the problem"
Related:      to-ki-mu (device), to-ki-li (agent)
```

**W021**
```
Form:         si-ne-ki
Type:         compound
Class:        process
Definition:   signal-transmission process; communication, broadcasting, networking
Composition:  si (signal) + ne (relation) + ki (change/process)
Register:     formal
Domain:       communication
Status:       proposed
Examples:     "si-ne-ki failed during the storm"
Related:      si-ne-mu (communication device), si-ne-su (communication structure / network)
```

**W022**
```
Form:         mu-ka
Type:         compound
Class:        process
Definition:   operate or use an artifact; use, operate, employ a tool or device
Composition:  mu (artifact/object) + ka (action) — head-final: an action characterized by its
              relationship to an artifact; the act of putting an artifact to work
Register:     standard
Domain:       general
Status:       proposed
Examples:     "la-tu  ka-mu-ka  lo-mu" — you operate the machine
              "la-mi  ka-be-past  lo-mu  wi [la-tu  ka-mu-ka]" — I built the machine for you to use (S016)
Notes:        Registered to resolve placeholder gloss `ka-use` in S016. Candidate form was
              identified during corpus work. Head-final rule satisfied: the artifact (mu) specifies
              the domain of the action (ka). Contrast with su-mu-li where mu describes the object
              produced; here mu describes the object acted upon.
Related:      mu-ka-li (operator, one who uses tools), mu-ka-mu (tool for operating another tool)
```

**W023**
```
Form:         si-ki
Type:         compound
Class:        process
Definition:   transmit; send a signal or message; directed point-to-point signal motion
Composition:  si (signal/representation) + ki (motion) — the motion of a signal toward a recipient
Register:     standard
Domain:       communication
Status:       proposed
Examples:     "la-ze  lo-si  ka-si-ki" — she sent the message (S017)
Notes:        Distinct from W021 si-ne-ki (communication/networking): si-ki is directed one-way
              transmission (signal + motion); si-ne-ki is relational communication
              (signal + relation + motion), implying a maintained connection or broadcast.
              Use si-ki for "send"; si-ne-ki for "communicate / network."
Related:      si-ne-ki (W021), si-ki-mu (transmitter / sender device)
```

**W024**
```
Form:         fe-si
Type:         compound
Class:        process / entity
Definition:   warn; issue a warning or alert; a signal that marks a boundary or limit condition
Composition:  fe (boundary/limit) + si (signal) — head-final: a signal characterized as
              boundary-marking; a signal that a limit is approaching, present, or has been crossed
Register:     standard
Domain:       general
Status:       proposed
Examples:     "ka-fe-si  ne-yu" — warn them / issue a warning to them
              "la-ze  lo-si  ka-si-ki-past  wi [ka-fe-si  ne-yu]" — she sent the message to warn them (S017)
Notes:        fe (boundary) characterizes warnings precisely: a warning signals that a limit exists,
              is approaching, or has been crossed. Preferred over de-si (decay-signal), which
              conflates the warning with the harm itself. head-final: si is the head (it is a signal);
              fe specifies what kind.
Related:      fe-si-mu (warning device / alarm), fe-ki (to reach a limit / become bounded)
```

---

### Abstract Concepts

**W030**
```
Form:         to-su
Type:         compound
Class:        entity / concept
Definition:   organized knowledge; system, model, framework, theory
Composition:  to (knowledge/pattern) + su (structure)
Register:     standard
Domain:       general
Status:       proposed
Examples:     "the to-su explained the phenomenon"
Related:      to-su-mu (device), to-su-li (expert)
```

**W031**
```
Form:         ne-su
Type:         compound
Class:        entity
Definition:   structured set of relations; network, society, web, organization
Composition:  ne (relation) + su (structure)
Register:     standard
Domain:       social / technical
Status:       proposed
Examples:     "the ne-su of traders spanned three regions"
Related:      li-ne-su (social network), si-ne-su (communication network)
```

---

## Open Questions

- [ ] Resolve whether compound forms use hyphens in writing or run together
- [ ] Review W002 (su-mu-li) — does it conflict with the derivational marker stack order?
- [ ] Develop domain-specific sub-lists once domains are finalized (see ontology/domains.md)
