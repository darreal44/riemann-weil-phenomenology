# Even characters at μ=16 share the χ₅ integral

a=0 ⇒ s₀=1/4 ⇒ the same a(y)
as χ₅. CST = log(q/π)−γ−log(1−1/256).
P is the prime-power sum
with that χ, n≤16.

    python3 code/av_enclose_even.py

    name     q     Qlo     Qhi
    χ₅       5   0.0040  0.0065
    χ₈       8   0.0853  0.0878
    χ₁₂     12   0.1979  0.2004
    χ₁₃     13   0.3907  0.3932
    χ₁₇     17   0.2448  0.2473
    χ₂₁     21   0.9451  0.9476
    χ₂₄ᵉ    24   0.6679  0.6703
    χ₂₉     29   1.5629  1.5653

χ₅ is the tight window.
Larger q lifts CST and
often drops the 2-power
terms (ramified), so Q
grows. Judge:
`tests/test_av_enclose_even.py`.

Odd characters are a
different integrand.
