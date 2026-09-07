# Neural pruning, and why it is not drop-p

Pruning a net: delete
weights or channels,
keep the task. Families:

- Magnitude (Han 2015,
  GMP): drop small |w|.
- IMP / lottery ticket
  (Frankle–Carbin):
  prune + rewind to
  init. Cost 3–4× dense.
- At init: SNIP, GraSP.
- Structured: channels /
  heads (Slimming, AMC).
- Progressive: one
  training cycle, sparsity
  schedule.
- Growth (2025): start
  sparse, add edges
  until a plateau.

2025–26 (COLT, continuous
sparsification) stay in
that game: mask + score
+ retrain.

## Quorum drop-p is not a mask

Drop 3 on 37a1: delete
Hecke prime 3 from P,
read the sign of λ₀.
Necessary / optional is
a sign, not |a_p|.
No rewind, no loss, no
training. Small |a_p|
can be necessary; a_p=0
is mute.

κ / Fmat drop a *scale*
in a trace, not a neuron.

Import that survives:
prune one object, measure
one scalar, do not fit a
line through two windows.
IMP will not compute c_L^*.
