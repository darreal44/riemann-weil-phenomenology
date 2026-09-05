# Dump the Q-mode on the server

    git pull
    export DUMP_MODE=1
    python3 code/scan_s.py chi29 22 36 50
    python3 code/scan_s.py chi29 38 66 42
    python3 code/scan_s.py chi17 22 36 50
    python3 code/scan_s.py chi5 38 66 42

Writes report/mode_{name}_mu{mu}.json : v0, N_eff, kbar, l1/l0, lam.
Same windows as the slope runs. Commit the json.

Recognition (already computed here on the Gram):
N_eff < 4, kbar < 3, λ1/λ0 > 100.
χ₂₉ μ=22, χ₁₇ μ=11 and 22, χ₅ μ=11: OK.
χ₂₉ μ=11: λ1/λ0 = 6, not isolated yet.
