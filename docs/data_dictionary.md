# Data Dictionary (Case Schema)

Field | Type | Description
---|---|---
id | string | anima:domain:case_id
domain | enum | craft|commerce|law|philosophy|painting|architecture|poetry|physics|mathematics|computing
title | string | Short case label
locale | string | Place/region
t0_interval | string | YYYY or YYYY-YYYY
predecessors_Ot | string[] | 3–7 predecessors
closures_R | object | doctrinal/material/discursive arrays
evidence | object | per criterion (NO, NOT_RC, NN, IF, Ctrl)
Lstar | object | binary per-criterion + score
sources | object | primary/secondary identifiers

**Note:** Signals in this repo are placeholders for demonstration; swap for domain-appropriate metrics in production.
