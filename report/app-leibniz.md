# a'' by Leibniz

    a = ½ w g
    w = 2 e^{-y/2}/(1−e^{-2y})
    a'' = ½ (w'' g + 2 w' g' + w g'')

w' and w'' are elementary
(`code/av_app.py`):

    w'/w = −½ − 2 e^{-2y}/(1−e^{-2y})
    w''  = product rule on
           2 e^{-y/2} (1−e^{-2y})^{-1}

Checked against a second
difference of a at y=1.2
(−0.775354 vs −0.775356).

## Sampled envelopes

              [1, 1.59]         [1.59, L]
    w         [0.94, 1.40]      [0.50, 0.94]
    w'        [−1.14, −0.55]    [−0.55, −0.25]
    w''       [0.50, 1.94]      [0.14, 0.50]
    g         [−0.223, 0]       [0, 0.056]
    g'        [0.24, 0.55]      [−0.056, 0.24]
    g''       [−0.707, −0.411]  [−0.552, 0.148]
    a''       [−1.336, −0.345]  [−0.345, 0.055]

## Termwise majorant

    |a''| ≤ ½ (|w''||g| + 2|w'||g'| + |w||g''|)

    [1, 1.59]  ≤ 1.341     (sampled |a''|=1.336)
    [1.59, L]  ≤ 0.407     (sampled |a''|=0.345)

Almost tight on the first
half: the three terms do
not cancel.

## Eight slabs with this M

    err₁ = 8·h₁³/12·1.341 = 3.59×10⁻⁴
    err₂ = 8·h₂³/12·0.407 = 8.76×10⁻⁴

    I_{[1,L]} ∈ [−0.02013, −0.01766]
    A(v)      ∈ [−0.82939, −0.82692]

still inside [−0.8303, −0.8244].

The majorant is termwise
in the *values* of w,g and
their derivatives, which
are still sampled envelopes.
w is monotone so |w|,|w'|
peak at an endpoint and
are elementary numbers
(w(1), w'(1)). g(1)=2e^{-3/2}−θ_v(1)
is elementary. The remaining
sampled pieces are max|g'|
and max|w''|.
