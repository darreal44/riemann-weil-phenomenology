# Modular symbols vs our a_p

Cremona / LMFDB tables of modular symbols for Γ0(N)
compute T_p on the symbol space; the eigenvalues are
the a_p of the newform. For 11a1 that space is
1-dimensional, so the table is a single list of a_p.

PARI: `msfromell`, `mshecke`. Same numbers as `ellap`.

    E = ellinit("11a1");
    M = msfromell(E, 0);
    forprime(p=2, 40, print(p, " ", mshecke(M, p), " ", ellap(E,p)));

The two columns must match. We already checked ellap
against Hecke recurrence and Deligne up to p=2000.
A symbols table is not a third source of zeros and
does not change Q.

Higher level: dim S2(Γ0(N))>1, the symbols space
splits into newforms. `mfinit([N,2])` lists them;
each newform has its own a_p row. We only harvested
the Cremona curve labels, i.e. one row per class.
