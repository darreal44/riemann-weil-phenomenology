<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->

# Session 2026-09-08 — puissances, spectres Q/G, zéros

Journal de la séance après #108. Pas une prise de \(W_L\). Pas RH.

## 1. Le trou \(\mu=5\) était une troncature

`Q_window` ne soustrayait que les premiers. \(\Lambda(4)=\log 2\)
manquait.

χ₃, \(L=\log 5\), primes-only vs \(+T_4\) :

    HEAD   λmin(H) old     λmin(H) new    s_exact    S_lo
       3   −3e-5           +4.6e-5        +8e-6      −0.59
       4   −1.6e-4         +1.4e-5        +8e-6      −1.19

H n'est plus indéfini. S_lo empire (ρ≈0.90) : le majorant
avale |w₄|. Le « décès μ=5 » du journal est T₄ oublié.
μ=3 inchangé (seulement 2). Mergé #108.

W_log5 n'est pas pris. H_4>0 n'est pas la classe PW.

## 2. Atomique T₂, T₃, T₄

    w_p = χ(p) log p / √p,   w_{p^k} = χ(p)^k log p / p^{k/2}

    χ     χ(2) χ(3) χ(4)   w₂      w₃      w₄
    χ₅     −1   −1   +1   −0.490   −0.634  +0.347
    χ₃     −1    0   +1   −0.490    0      +0.347
    χ₇     +1   −1   +1   +0.490   −0.634  +0.347
    χ₄,χ₈   0   −1    0    0       −0.634   0

T₃ est muet sur χ₃ (ramifié). À L=log 5, T₃ *relève* les
χ(3)=−1 (sans T₃, H₄ déjà négatif). T₄ s'oppose à T₂
quand χ(2)=−1 ; c'est lui qui a retourné χ₃.

Drop-T₂ à L=log 5, μ=5 : λmin(χ₃) passe de +1e-5 à −0.52.
T₂ est l'atome dominant (‖T₂‖≈1.07 vs ‖T₄‖≈0.31).

## 3. Matrice Θ(log 2)

L=log 5, sections h=2…32 : ‖Θ‖₂ → √2 (pas la cap 2).
L=log 3 : ‖Θ‖₂ → 1, cap saturée.

Le spectre n'est pas un intervalle rempli. À h=32, cinq
paquets : ±√2 (8 VP), ±1 (17 VP), 0 (4 VP), plus trois
satellites. Trou (0.01, 0.98). Pas pair/impair. Pas
arcsinus d'un seul [−R,R] (W₁ vs arcsinus stagne à 0.17).

T₂ = −w₂ Θ hérite ±|w₂|√2, ±|w₂|, 0.

## 4. Q_h(χ₃) — côté premiers

Q = A − ∑_{n<μ} Λ(n)χ(n) n^{−1/2} Θ(log n).

Q₄ à log 3 : λ = 0.011, 1.24, 1.66, 2.66.
Q₄ à log 5 : λ = 1.4e-5, 0.154, 1.60, 1.96.

Sol isolé (gap λ₁/λ₀ ~ 10² puis 10⁴). Mode
(0.92, 0.40) à log 3, (0.82, 0.57) à log 5.
ψ₀(t) : zéro nœud, bosse en L/2, bords petits
(ψ(0)≈0.01 à log 5). Les excités ont 2, 6, … nœuds.
Sturm-Liouville ne s'applique pas (Q n'est pas un SL ;
nœuds non monotones en k).

Balayage μ, puissances on :

    μ     h=4 λmin      h=8 λmin
    3     1.1e-2        1.0e-2
    5     1.4e-5        1.0e-5
    7     1.2e-6        1.0e-8
   11     1.4e-8        1.6e-12
   13     3.1e-8        1.8e-13
   17     1.6e-9        3e-15   (bruit float)

Aucun flip. h=4 non monotone (13>11). Au-delà de
10^{-12} ce n'est plus un certificat.

À μ=11 le 2-plan a det ~ 6e-6 ; Q₃₃ tient encore à 2.62.
À μ=17 toute la matrice se ramasse (comme G à log 7).

Courant : λmin(Q_h) baisse en h et se fige (plancher
9.7e-3 à log 3, 8e-6 à log 5). Pas c_L*.

## 5. G_h(χ₃) — côté zéros

206 γ, γ₁=8.039737. G = ∑_γ v(γ) v(γ)ᵀ ≽ 0 toujours.

    μ     λmin(G₄)     λmax     rang num.
    5     2.6e-6       0.73     4
   11     5.3e-9       1.45     3
   17     8.7e-10      0.18     3

Même crush 0⁺ que Q, autre mécanisme (phase Lγ).
Les 5 premiers γ portent 94 % de ‖G‖_F à log 3,
43 % à log 7. G n'est pas un multiple de Q
(Q₃₃=2.62 vs G₃₃=1.43 à μ=11).

ω₁=2π/L < γ₁ dès μ=3 : l'échelle cosine est plus
lente que le premier zéro.

## 6. Λ, ψ, S

ψ(μ)=∑_{n<μ} Λ(n) ~ μ déjà à μ=17.
S(μ)=∑ Λ(n)χ₃(n)/√n oscille et reste O(1) :
−0.49, −0.14, −0.86, −0.37, −1.10, −0.90
aux crans 3,5,7,11,13,17. S n'est pas λmin.

## 7. Zéros — vérification, pas RH

ζ : 150 γ jusqu'à T=319. Premiers cinq = Odlyzko
à 3e-11. Weyl unilatère 1.004.
χ₃ : γ₁ = 8.039737 (écart 2e-7). Weyl brut 1.004.

Le moissonneur est juste. Ce n'est pas Platt.
Odlyzko–Schönhage (FFT de polynômes de Dirichlet,
T^{1/3} amorti) n'est pas dans le repo ; PARI
suffit à T=320. OS ne teste pas Re ρ ≠ 1/2.

## 8. Ce qui n'est pas pris

- W_log3, W_log5, (∀L). HEAD et V_h sont Courant
  à l'envers pour le type Paley–Wiener.
- c_L* = inf_{W_L} Q.
- S_lo à μ=5 (majorant pire après T₄).
- Un zéro hors droite : Q_h≥0 sur V_8 jusqu'à
  μ=17 ne le voit pas, et ne l'interdit pas.
- step_is_taken() inchangé.

Scripts : `code/ql_schur_mu5.py` (interior_atoms,
wn, Q_window). Zéros : `code/zeros_chi3_weyl.pkl`,
`code/zeros_zeta_weyl.pkl`.
