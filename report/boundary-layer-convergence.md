# Convergence of the y_min layer

The worst N=4 slab is [0.307,0.410], leftover 1.62, h=0.103. Cap h³/6 ×
1.62 ≈ 2.9×10⁻⁴ unweighted on that slab alone. Four well slabs are the
same order. The rise slabs shrink as g''→0.

Refining only near y_min (one extra split of the last well slab and the
first rise slab) is a 2-node budget that should cut those two caps by ~8
if O(h³) per slab holds, i.e. a few 10⁻⁴ off the gap. Not the whole
0.0028.

A true boundary-layer coordinate (stretched variable near y_min) is
overkill: g'' is smooth there, just steep in leftover because m_i is the
right-end value. Matching g'' at the left as well would be Hermite.

N=8 uniform or two local splits: same order. Not Weil.
