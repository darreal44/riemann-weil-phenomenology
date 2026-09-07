# Kronrod weights

Gauss n nodes are the zeros of the orthogonal polynomial P_n for the
weight (Lebesgue on [−1,1] for Legendre). Kronrod seeks n+1 new nodes
such that the 2n+1 node set is exact for degree ≤ 3n+1. Those new nodes
are the zeros of the Stieltjes polynomial E_{n+1} defined by

    ∫_{-1}^1 P_n(x) E_{n+1}(x) x^k dx = 0
    for k = 0,…,n.

Weights then come from the usual interpolatory formula on the combined
nodes (the old Gauss weights are not kept).

None of this is needed to build g_lo or to score #87. The repo does not
compute E_{n+1}.

Not a campaign.
