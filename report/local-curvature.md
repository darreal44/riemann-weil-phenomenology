# Local curvature leftover on N=4

m_i = g''(right). Leftover at the left of the slab = g''(left)−m_i is
the curvature the parabola does not use.

    well [0.000,0.102]  9.64 vs 8.69   left 0.95
    [0.102,0.205]  8.69 vs 7.38   left 1.31
    [0.205,0.307]  7.38 vs 5.84   left 1.54
    [0.307,0.410]  5.84 vs 4.22   left 1.62

    rise [0.410,0.500]  4.22 vs 2.86   left 1.36
    [0.500,0.591]  2.86 vs 1.66   left 1.20
    [0.591,0.681]  1.66 vs 0.70   left 0.96
    [0.681,0.772]  0.70 vs 0.00   left 0.70

The leftover is O(1) on every slab of width 0.10. That is the 0.0028: ∫
½ leftover · t² on four plus four slabs, weighted by ½w, order a few
10⁻³. N=8 halves the width and the leftover per slab (g''' bounded) and
is the next legal cut on I_{[0,1]}.

Not Weil.
