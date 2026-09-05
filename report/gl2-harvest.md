# GL(2) harvest

`gp` is the command-line of **PARI/GP** (Université de Bordeaux).
It evaluates L-functions of elliptic curves and modular forms
(`lfunzeros`). It is not the Dirichlet script.

## Install

Linux (server Threadripper):

    sudo apt install pari-gp          # Debian/Ubuntu
    sudo dnf install pari             # Fedora
    conda install -c conda-forge pari

Windows:

    https://pari.math.u-bordeaux.fr/download.html
    add the directory of gp.exe to PATH, then `gp --version`.

Check: `gp -q <<< 'print(Pi)'` should print 3.14…

## Run (after chi31)

Smoke, one curve:

    python3 code/harvest_gl2.py 11a1 80

Eight curves in parallel, T=320:

    python3 code/harvest_gl2.py --all 320 --workers 8

Writes `code/zeros_11a1_weyl.pkl` etc. Same pickle shape as χ.
`scan_s` does **not** know these names yet. Do not scan until
the pkl exist and the Weyl ratio is ~1.

## What this is

Weight-2 newforms over Q, via their elliptic curves. Degree-2
L-functions. GRH for these is “zeros on Re=1”. The first zero
of 11a1 is at t=6.31…, conductor 11, desert ≠ Dirichlet.

Not a replacement for `harvest_weyl_mp.py chi31`.
