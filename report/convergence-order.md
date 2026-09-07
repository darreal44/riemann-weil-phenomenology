# Theoretical order

q_i is the order-1 jet plus a constant m_i ≤ inf g''. Let e = g−q_i on a
slab of width h.

    e(y_i)=e'(y_i)=0, e''(t)=g''(t)−m_i ∈ [0, leftover], leftover ≤
    |g'''|_∞ h.

Hence e = O(leftover h²) = O(h²) now (leftover~1) and O(h³) once the
mesh resolves g'''. ∫ e on one slab is O(leftover h³)=O(h³) now, O(h⁴)
resolved. Sum over 1/h slabs: O(h²) now, O(h³) resolved.

That is the whole theory for this g_lo. No hidden O(h⁴) global rate
without matching g'' at both ends. No spectral rate (g is C^∞ but the
element is P2 one-sided).

Empirical N=1→4 followed O(h²) after N=2. The next measurement is N=8,
still one v, still not Weil.
