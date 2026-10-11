<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# La carte des murs : pourquoi chaque méthode finie échoue sur la forme de Weil en fenêtre, avec constantes

Pas covering. Pas RH. Cette note est la synthèse de l'atelier privé
`weil-then-rh` (septembre–octobre 2026). Elle ne revendique ni RH ni
une réduction de RH. Elle dit, classe de méthodes par classe de
méthodes, où chacune s'arrête, avec la constante exacte quand elle
existe. Les notes citées par leur nom vivent dans le sous-module
privé ; sans accès, le lien est mort. Relecture : voir la dernière
section.

## 0. En une phrase

Pour un caractère primitif \(\chi\) mod \(q\) et une fenêtre
\(W_L=L^2[-L,L]\), la positivité de la forme de Weil tronquée
\(Q_\chi\ge0\) sur \(W_L\) **pour tout \(L\)** est RH\((\chi)\). Aucune
méthode finie ne franchit « pour tout \(L\) ». La carte ci-dessous
démontre, pour trois classes de méthodes finies (enveloppes,
planchers ponctuels, positivité sur une sous-classe), un plafond
avec sa constante, chacun relu ; pour cinq autres classes elle nomme
l'obstruction par citation, sans théorème nouveau. Le plafond de la
classe la plus naturelle, les enveloppes \(|\chi(n)|\le1\), est
exactement le pôle de \(\zeta\) : \(L^*(q)=\log\log q+o(1)\), constante 1.

## 1. L'objet, la cible, le compas

**Conventions.** \(g\in W_L=L^2[-L,L]\), \(G(t)=\int g(x)e^{-itx}dx\),
\(h_g(y)=\int g(x)\overline{g(x-y)}\,dx\), \(\mu=e^{2L}\),
\(c_n=2\Lambda(n)/\sqrt n\), \(s_0=\tfrac14\) (\(\chi\) pair) ou \(\tfrac34\)
(\(\chi\) impair),
\[
Q_\chi(g)=\log\tfrac q\pi\,\|g\|^2+\mathrm{Arch}_{s_0}(g)
-\sum_{n<\mu}c_n\,\Re[\chi(n)h_g(\log n)],\qquad
\mathrm{Arch}_{s_0}(g)=\tfrac1{2\pi}\int|G(t)|^2\,\Re\psi(s_0+\tfrac{it}2)\,dt .
\]
Par la formule explicite, \(Q_\chi(g)=\sum_\rho\Phi_g(\rho)\) sur les
zéros de \(L(s,\chi)\). Les notes publiques d'échantillonnage de ce
dépôt écrivent le support \([-L/2,L/2]\) ; on le signale à chaque
citation.

**La cible.** Weil 1952 plus visibilité : \((\forall L)\,Q_\chi\ge0\)
sur \(W_L\) équivaut à RH\((\chi)\). RH est \(\Pi_1\) : aucun calcul
fini ne la démontre. Un résultat à \(L\) fini est un support, jamais
un pas. Un pas est un argument valable pour tous les \(L\) à la
fois.

**Le compas.** Chaque piste porte un tag : (R) réduction à un énoncé
de nature différente non connu équivalent ; (F) conséquence de RH
prouvée au-delà de l'état de l'art ; (M) mécanisme, un théorème qui
plafonne une classe de méthodes avec sa constante ; (S) support
déclaré d'une piste R, F ou M ; (P) phénoménologie. Cette carte est
faite de (M), avec un (F) à la section 2.

## 2. Classe 1 : les enveloppes \(|\chi(n)|\le1\), et le pôle de \(\zeta\)

La classe : tout argument qui n'utilise de \(\chi\) que
\(|\chi(n)|\le1\) et le facteur archimédien (enveloppes de Zhu, cubes,
tores, normes de peigne, planchers ponctuels). Quatre théorèmes :
trois relus par un agent distinct de l'auteur, le quatrième relu
avec cette synthèse.

**Théorème 1 (domination tout-plus, `weil-allplus-2026-09-30.md`).**
Pour tout vecteur \((\chi(n))_{n<\mu}\) avec \(|\chi(n)|\le1\) et toute
\(g\in W_L\) complexe,
\(Q_\chi(g)\ge Q_+(|g|)\ge\lambda_{\min}(Q_+)\,\|g\|^2\), où \(Q_+\) est la
forme de pseudo-caractère \(+1\) en toutes les puissances de premiers.
Un certificat par parité donne donc un seuil uniforme
\(q_0^{\rm all}(L)=\pi e^{-f_a(L)}\), \(f_a=\lambda_{\min}(\mathrm{Arch}_{s_0}+C_+)\),
valable pour tous les caractères primitifs. Le seuil est **exact
pour la classe** : les caractères quadratiques \(\chi_d\) avec
\((d|p)=+1\) pour tout \(p<\mu\) ont \(Q_{\chi_d}=Q_+^{(|d|)}\).

    L        pair f_cert      q0_all | impair f_cert   q0_all
    0,5493   -1,029334866      8,79  | -0,498668569     5,17
    0,8      -2,178843979     27,76  | -1,420505073    13,00
    1,0      -3,185891539     75,99  | -2,269753045    30,40
    1,2      -4,252025307    220,69  | -3,170133244    74,80
    1,4      -5,438799822    723,09  |  non calculé

Chaque \(f_{\rm cert}\) est une boule Arb (DÉMONTRÉ). Les fenêtres
\(W_{0,5493}\), \(W_{0,8}\), \(W_{1,0}\) sont closes pour tout caractère
primitif, et \(W_{1,2}\) pour tout caractère pair (2245/2245) et tout
impair sauf \(\chi_3\) (272/273), par le seuil uniforme plus des listes
finies certifiées (`w12-cloture-2026-10-02.md`).

**Théorème 2 (le tout-plus est \(\zeta\) sans son pôle,
`weil-allplus-zeta-2026-10-01.md`).** Pour \(g\) réelle,
\(Q_+^{\rm pair}(g)=Q_\zeta(g)+\log q\,\|g\|^2-2\big(C(g)^2-S(g)^2\big)\),
\(C=\int g\cosh\tfrac x2\), \(S=\int g\sinh\tfrac x2\), et
\(\sup(C^2-S^2)/\|g\|^2=L+\sinh L\), atteint en \(g^*=\cosh(x/2)\). Donc,
dès que \(Q_\zeta\ge0\) sur \(W_L\) (certifié pour \(L\le0{,}9729\),
conditionnel au-delà), \(q_0^{\rm all}(L)\le e^{2L+2\sinh L}\) :
77,5 / 225,6 / 741 à \(L=1{,}0/1{,}2/1{,}4\), contre 76,0 / 220,7 / 723
certifiés. Le minimiseur du tout-plus est la fonction du pôle à
0,994–0,9999 près. La négativité du tout-plus **est** le pôle
manquant de \(\zeta\).

**Théorème 3 (constante exacte, analytique,
`comb-norm-analytic-2026-10-02.md`, relecture du 3 octobre).** Sans
ordinateur et sans RH : \(\|C_+\|_{W_L}\le1{,}03883\,e^L+L(1+\tanh\tfrac L2)+1{,}03883\)
(Rosser–Schoenfeld 1962, théorème 12), \(\|C_+\|/\sqrt\mu\to1\) (Dusart,
arXiv:1002.0442v1), d'où \(L^*(q)\ge\log\log q-o(1)\) sans condition.
Dans l'autre sens, inconditionnellement,
\(q_0^{\rm all}(L)\ge e^{2L+2\sinh L-r(L)}\) par évaluation en \(g^*\)
(relecture du théorème 2, point V), d'où \(L^*(q)\le\log\log q+o(1)\)
pour la classe ; le théorème 2 lui-même donne \(L^*(q)\ge L_{\rm pôle}(q)\),
conditionnel à \(Q_\zeta\ge0\) pour \(q>67\). La constante du mur est 1
des deux côtés, sans condition ; le pincement à \(0{,}0032\) près est
conditionnel d'un côté. L'enveloppe \(\ell^1\) donnait \(-\log4\) ; que
le gain soit \(\log4\) et pas plus est mesuré sur la table et
asymptotique par le côté \(r(L)\) (relecture du théorème 2, point V),
pas une conséquence du théorème 3.

**Théorème 4 (frontière, tag F).** Pour tout caractère primitif
\(\chi\) mod \(q\) et tout \(L\) avec \(\log(q/\pi)\ge-f_{\rm cert}(L)\), et
asymptotiquement pour tout \(L\le\log\log q-o(1)\), \(Q_\chi\ge0\) sur
\(W_L\), sans hypothèse. C'est une conséquence de GRH démontrée sans
GRH, uniforme en \(q\). L'existence d'un \(L^*(q)\ge\log\log q-\log4\)
est élémentaire (enveloppe \(\ell^1\), `weil-uniform.md` §3) : la
frontière revendiquée est la constante 1, c'est-à-dire le gain
\(\log4\), obtenu par les entrées classiques citées au théorème 3.
État de l'art connu
de l'atelier : la seule lecture extérieure autorisée par ses règles,
Zhu, arXiv:2608.24827 v2, traite \(\zeta\) seule et propose Dirichlet
comme problème ouvert (section 16 (iv)) sans résultat. Un énoncé
publié à constante égale ou meilleure, s'il existe, retire le tag F
et laisse le mécanisme.

**Ce que la classe ne peut pas faire.** Toute méthode de la classe a
un seuil \(\ge q_0^{\rm all}(L)\), donc ne couvre \(W_L\) pour tout
\(\chi\) que si \(L\le L^*(q)=\log\log q+o(1)\). Elle ne touche pas
\((\forall L)\). Il reste \(r(L)\) entre la borne du pôle et le
certificat, \(r(L)\le0{,}13\) mesuré, \(r(L)<0{,}37\) pour \(L\le10\) par
Platt–Trudgian ou sous RH (relecture du théorème 2, point III) ; ce
jeu est \(Q_\zeta(g^*)/\|g^*\|^2\), pas une marge à gagner. Affûter les constantes de cette classe est interdit par les
règles de l'atelier (`regles-vers-rh-2026-10-02.md` §2).

## 3. Classe 2 : les certificats par plancher ponctuel

La classe : tout certificat qui prouve \(Q_\chi\ge0\) sur \(W_L\) par la
réduction en un coup de Zhu (théorème 1.1 de arXiv:2608.24827) avec un
plancher ponctuel du symbole
\(\Psi_\chi(t)=\log\frac q\pi+\Re\psi(s_0+\tfrac{it}2)-P_\chi(t)\),
\(P_\chi(t)=\sum_{n<\mu}c_n\Re[\chi(n)n^{-it}]\), au-delà d'une hauteur
\(T^\sharp\). Deux sous-classes : l'enveloppe, qui majore \(P_\chi\) par la
constante \(A_L^{(q)}=\sum_{n<\mu,(n,q)=1}c_n\) ; le plancher exact du
dépôt, qui certifie \(\inf\Psi_\chi\) en boules. Soit \(T_0(\chi,L)\) le
dernier point négatif du plancher ; tout certificat a \(T^\sharp\ge T_0\).

**Hérité (Zhu, théorème 1.4).** Pour l'enveloppe, \(T^\sharp>T_1=2\pi e^{A_L}\),
\(A_L=(4+o(1))e^L\). Pour \(\chi\) mod \(q\) la même preuve donne
\(T_1(\chi,L)=(2\pi/q)\,e^{A_L^{(q)}}(1+o(1))\) (extension démontrée dans
la note du dépôt, trois lignes ; Zhu n'a aucun résultat Dirichlet).
Zhu laisse ouvert le cas du
plancher exact (section 7) et dit qu'un seuil plus fin « est un énoncé
sur les formes linéaires en \(\log p\) » (section 14.3).

**Théorème 5 (`mur-classe-2-plancher-2026-10-11.md`).** La constante du
plancher exact est celle de l'enveloppe. (i) Séparabilité : les \(\log p\)
étant \(\mathbb Q\)-indépendants, \(\sup_{t\ge T}P_\chi(t)=A_L^{(q)}\) pour
tout \(T\) (Kronecker–Weyl, toutes les phases alignées). (ii)
\(T_0\le T_1(\chi,L)(1+O(1/T_1))\). (iii) Pour tout \(\delta>0\) il existe
\(T(\delta,\mu,\chi)<\infty\), ineffectif (minimalité du flot linéaire,
Gottschalk–Hedlund), tel que
\(T_0\ge(2\pi/q)e^{A_L^{(q)}-\delta}(1-C'/t_1^2)-T(\delta,\mu,\chi)\), \(C'=1/24\).
Aucune constante \(\beta<A_L^{(q)}\) ne majore le peigne sur aucune
demi-droite ; le gain du plancher exact sur \(T_0\) lui-même n'est
borné par la note ni par en haut ni par en bas. Table (boules Arb
pour \(A_L\) et \(T_1\) ; \(T_0\) mesuré par balayage flottant ; dernière
colonne : modèle avec \(T_0\approx T_1\)) :

    L      A_L            T1 = 2π e^{A_L}    T_0 mesuré   T_0/T1   N_2 (modèle)
    1,0    5,852468364    2187,13            1550         0,709    3·10^3
    1,2    8,520990884    31 535,46          19 900       0,631    5·10^4
    1,4    10,29034239    185 020,05         132 000      0,713    3,5·10^5
    1,6    14,32324546    1,04·10^7          —            —        2,3·10^7
    2,0    24,38329184    2,44·10^11         —            —        6,6·10^11

Au dernier point négatif à \(L=1\), \(P(t^*)=A_L-0{,}03\) : c'est un retour
de Kronecker vers « toutes phases nulles » (mesuré). L'ouverture du cycle
avait conjecturé une constante plus petite, \(\sup(-P)=A_L-O(L)\) ; c'est
le mauvais signe du peigne, réfuté par une boule certifiée
(\(\Psi(1549{,}9078)<0\) avec \(2\pi e^{\sup(-P)}=975{,}9\)). Un modèle de
Cramér sur le tore, étiqueté modèle, prédit
\(\log(T_0/2\pi)\approx\min(A_L,8L^2)\), croisement vers \(L\approx2{,}9\) ;
au-delà, \(T_0\) resterait \(e^{8L^2}\) et la matrice hors de toute machine.

**Mur de précision (hérité).** Sous RH, \(-\ln\lambda^*(L)\ge1{,}0974\,Le^L(1+o(1))\)
(Zhu, théorème 1.3 et remarque 13.5) : tout certificat à \(L\) doit
résoudre \(\lambda_{\min}\) en dessous ; sans hypothèse, les majorants
certifiés de Zhu (\(3{,}2\cdot10^{-283}\) à \(L=2\)) exigent plus de 940 bits
pour le seul puits. Dans le dépôt, \(\ell\approx11\,D_{\max}\) (mesuré,
`the-well`) ; \(\chi_3\) à \(W_{1,2}\) est exactement un puits sous la
résolution (\(-8\cdot10^{-12}\) contre une erreur \(8\cdot10^{-12}\)).

**Ce que la classe ne peut pas faire, et ce qui est démontré.** La
constante du plancher est \(A_L^{(q)}\), la même pour l'enveloppe et pour
le plancher exact (démontré) ; le majorant \(T_0\le T_1\) est démontré et
doublement exponentiel en \(L\) ; le minorant de \(T_0\) est mesuré jusqu'à
\(L=1{,}4\) (\(T_0/T_1\) entre 0,63 et 0,71) et modèle au-delà : aucun
minorant effectif n'est démontré, c'est un énoncé sur les formes
linéaires en \(\log p\) (relecture
`mur-classe-2-plancher-review-2026-10-11.md`, ACCEPT avec corrections).
Le mur tient par la constante et par la précision, pas par un minorant
de hauteur. Rien sur une méthode non ponctuelle en \(t\) (fenêtre lisse,
lemme B de `zhu-tail-opnorm-2026-10-01.md`, non certifié). Rien sur
\((\forall L)\).

## 4. Positivité sur une sous-classe : la dichotomie de clôture

La classe : prouver \(Q\ge0\) sur une sous-classe \(S\) de \(W_L\) (un cône,
un hyperplan, un sous-espace, une contrainte sur des valeurs aux nœuds),
pour tout \(L\), et en tirer quelque chose sur \(W_L\). Une cinquantaine de
notes des 3 et 5 octobre traitent chacune un \(S\). Un théorème les
contient (`dichotomie-cloture-2026-10-11.md`).

**L'espace.** \(E\) = fonctions réelles paires de \(W_L\) d'énergie finie,
norme \(N(g)^2=\frac1{2\pi}\int|G(t)|^2w(t)\,dt\),
\(w(t)=1+\Re\psi(s_0+\tfrac{it}2)-\psi(s_0)\ge1\), \(w\le C(1+\log(1+|t|))\)
(série de \(\psi\)). \((E,N)\) est un Hilbert (image fermée dans \(L^2(w)\)),
\(N(g)^2=\|g\|^2+D(g)\) avec \(D\) la forme de Dirichlet archimédienne, et
\(Q_\chi\) est une forme quadratique continue sur \((E,N)\) :
\(|B(f,g)|\le C_LN(f)N(g)\), \(C_L=|\log\tfrac q\pi+\psi(s_0)|+1+A_L\). Hors
de \(E\), \(Q=+\infty\).

**Théorème 6 (dichotomie).** Soit \(S\subset E\) et \(K\) l'adhérence de
\(\mathbb R\cdot S\) pour \(N\). (a) \(Q\ge0\) sur \(S\) équivaut à \(Q\ge0\) sur
\(K\). (b) Si \(K=E\), « \(Q\ge0\) sur \(S\) » est « \(Q\ge0\) sur \(E\) » mot pour
mot : la cible sous un autre nom. (c) Si \(K\ne E\), avec \(\hat e\notin K\)
unitaire et \(\rho=\sup\{|\langle g,\hat e\rangle_N|:g\in K,N(g)=1\}<1\), la
forme \(Q'=N^2-(1+\varepsilon)\langle\cdot,\hat e\rangle_N^2\),
\((1+\varepsilon)\rho^2<1\), est continue, positive sur \(K\) et négative en
\(\hat e\). Donc tout argument invariant par remplacement de \(Q\) par une
forme quadratique continue de même signe sur \(S\) ne signe pas \(E\) ; de
même pour « un morceau de \(Q\) est positif » ou « une identité sur un
ingrédient ». Les formes continues positives sur \(S\) sont exactement
celles positives sur \(E\) si et seulement si \(K=E\).

**Lemme des bosses.** Une bosse continue de hauteur 1 et de largeur
\(\eta\) a \(N^2\le C\eta(1+\log(1/\eta))\to0\) : l'évaluation en un point
n'est pas continue pour \(N\). Toute contrainte sur le triplet
\((f(0),f(L/2),f(L))\) définit donc un \(S\) avec \(K=E\) : case (b).

**Bilan des 46 instances.** Neuf en case (c), \(K\) fermé propre : cône
positif, moyenne nulle, hyperplan du pôle, secteur impair, diagonale des
cosinus, section de dimension fixée, cône croissant, cône des moitiés,
retard 2. Vingt en case (b), cible renommée : les dix-sept contraintes
aux nœuds du 5 octobre, le cône compensé, le même signe aux trois nœuds,
et l'objet 1 (clôture pleine). Ces dix-neuf notes de nœuds avaient la
bonne ligne de compas et la mauvaise case : leur phrase « ne donne pas
\((\forall L)\,Q_L\ge0\) » est fausse, leur « mort si » part, l'énoncé
qu'elles disaient plus faible est la cible mot pour mot (relecture
`dichotomie-cloture-review-2026-10-11.md`, ACCEPT avec corrections,
lemme des bosses redémontré). Dix-sept « par morceaux » (Arch seul,
peigne seul, norme, parallélogramme, plafond de Cauchy, etc.), hors
dichotomie au sens strict, tuées par le principe d'invariance, dont
les carrés critiques hors du cadre des formes continues, par le
principe seul.

**Ce que le théorème ne dit pas.** Il ne dit pas que \(Q\) est négative
quelque part. Une positivité sur \(S\) avec \(K\ne E\) peut être une vraie
conséquence partielle (une région sans zéro par visibilité), tag F si
elle dépasse l'état de l'art. Un argument qui utilise la structure de
\(Q\) (formule explicite, équation fonctionnelle, produit d'Euler, zéros)
n'est pas dans la classe tuée. La lecture jointe en \(L\) de la case (c)
n'est pas écrite pour deux instances (diagonale des cosinus, section
fixée) ; elle ne change pas la ligne de compas.

## 5. Classe 3 : la comparaison au Gram des zéros

Prouver \(|Q_L-\mathrm{Gram}_L|<\lambda_{\min}(\mathrm{Gram}_L)\) avec un
Gram sur tous les zéros (`rh-routes-2026-09-23.md`, route C). Sous
RH, \(Q_L(f)=\sum_\gamma|F(\gamma)|^2\) est un Gram d'échantillons réels
(`sampling-floor`, théorème 1). Sans RH, une paire de zéros hors
droite apporte \(\hat f(\rho)\hat f(1-\bar\rho)\), qui n'est pas un
carré (`sampling-debranges-route`). Obstruction exacte : le terme de
comparaison est le terme de visibilité lui-même ; le poser petit à
tout \(L\) pose les zéros sur la droite. Constante :
\(\lambda_{\min}(\mathrm{Gram}_L)=c_L\), \(-\ln c_L\approx11\,D_{\max}\)
(mesuré, `the-well`), donc la comparaison doit être exacte à
\(e^{-11D_{\max}}\) près : le mur de précision de la section 3.

## 6. Classe 4 : Krein, échantillonnage, de Branges

Convention de `sampling-floor` : support \([-L/2,L/2]\), son \(L\) vaut
\(2L\) dans celle de cette note. Sous RH, \(c_L\) est la constante
inférieure d'échantillonnage de l'ensemble des zéros pour
\(PW_{L/2}\) (soit \(PW_L\) ici), \(c_L>0\) par Beurling–Landau
(`sampling-floor`, théorème 1). Sans RH, Beurling ne s'applique pas :
un ensemble d'échantillonnage est un ensemble de points réels, et la
réalité des points est la cible. Aucune borne quantitative :
Duffin–Schaeffer et Bernstein perdent exactement l'exposant du
désert \(e^{-L\gamma_1}\) dans sa convention (\(e^{-2L\gamma_1}\) ici),
\(\gamma_1=14{,}13\) ; Slepian ne donne qu'un majorant ; la loi
géométrique \((a,b)\approx(1{,}69,\,0{,}82)\) est une conjecture
semi-empirique (`sampling-floor`, conjecture ; testée dans
`one-set-sampling`). L'espace de Paley–Wiener n'est
pas l'espace de \(\xi\). Les fonctions vis de Krein (Suzuki,
arXiv:2606.09096) sont un équivalent connu. Obstruction exacte : la
position des points.

## 7. Classe 5 : Connes–Consani, semi-local

Connes–Consani 2021 : positivité pour le support \([2^{-1/2},2^{1/2}]\)
par une trace de Sonin positive moins un reste compact,
\(\varepsilon'(1^+)=22{,}9965\), une valeur propre au-dessus de 1
(\(1{,}0516\)) neutralisée par une condition linéaire. Où cela s'arrête
(`semilocal-step.tex`, `log2-log3-step.md`, mesuré) : une seconde
valeur propre au-dessus de 1 à la longueur 1,01 ; le terme du
premier 2 ne rejoint pas le reste compact ; transporté à
\(\{\infty,2\}\), la compression n'est pas à trace et le signe est
renversé (20/20 à \(\log2\), 13/20 à \(\log3\)). Le mécanisme de Connes
1999 (théorème 4) rend, après soustraction du volume, le pairing de
Weil lui-même, pas un opérateur compact sous 1. Conducteur
(`connes-consani-conducteur-2026-10-02.md`) : le théorème 1 de CC
équivaut à \(Q_\zeta\ge0\) sur le sous-espace sans pôle de
\(W_{\frac12\log2}\) ; le théorème 4 de la section 2 paie la même direction,
celle du pôle, avec \(\log q\) (Galerkin \(-1{,}29\), borne du pôle
\(-1{,}40\)). Aucune propriété structurelle n'y donne \((\forall L)\).

## 8. Classe 6 : crible et second moment sur \(\chi\)

Théorème : la moyenne de \(Q_\chi(g)\) sur \(\chi\) à \(g\) fixé
(`sieve-complex-mean.md`). Trou : \(\sup_{g\in W_L}\) de la norme
d'opérateur, sans interpolation de \(k\) premiers à \(\pi(\mu)\)
(`sieve-wall.md`) ; l'uniformité en \(g\) coûte un réseau de \(W_L\) de
taille exponentielle en la dimension du certificat. Exceptions : les
primitifs réels, au plus deux par conducteur
(`sieve-exception-quadratic.md`), masse structurelle
\(\sum_{p<\sqrt\mu}c_{p^2}\sim2L\), un problème de liste, pas de
moyenne ; et les \(\chi_d\) à \((d|p)=+1\) pour \(p<\mu\) ont
\(Q_{\chi_d}=Q_+^{(|d|)}\) exactement, donc aucune moyenne ne descend
sous \(q_0(L)\) pour eux. Mesuré, pas théorème : annulation d'un
facteur 0,43 sur grille à \(k=4\). Obstruction exacte : le
quantificateur \((\forall g)\) et la liste réelle.

## 9. Classe 7 : Li et le 2-adique

Li : \(\lambda_n\ge0\) pour tout \(n\) équivaut à RH ; équivalent connu ;
les tests de Li ne sont pas à support compact en \(\log\), un
certificat à \(\mu\) fini ne dit rien sur \(\lambda_n\) (`li-vs-QL.md`).
2-adique : masses de coquilles exactes \(1/\sqrt2\), \(\sqrt2\),
\((\log2)/\sqrt2\) (`2adic-shells.md`) ; le pic de la grille Fmat monte
à travers 0,49 sans Dirac (mesuré) ; l'orbite identité s'annule en
\(\Lambda=1\) et les deux logarithmes ne sont pas interchangeables
(`log2-log3-step.md`). Obstruction exacte : l'équivalence pour Li, le
pas \((\log2,\log3]\) pour le 2-adique.

## 10. Degré \(d\) : le même mur pour les formes automorphes

Convention du code courant du dépôt (`weil_gl2.py`, jugée par le
comptage des zéros, `gl2-convention-facteur2.md`) : pour une newform
\(f\) de poids 2 et niveau \(N\),
\(Q_f(g)=(\log N-2\log2\pi)\|g\|^2+2\,\mathrm{Arch}^{(2)}(g)-\sum_{n<\mu}\tfrac{2\Lambda_f(n)}n\Re h_g(\log n)\),
\(\mathrm{Arch}^{(2)}(g)=\tfrac1{2\pi}\int|G|^2\Re\psi(1+it)\,dt\). L'en-tête
de `weil-gl2-window.md` (\(\tfrac12\log N\), un seul \(\Re\psi\)) est le
symbole legacy, écarté par le dépôt.

**Théorème 7 (`mur-degre-d-2026-10-11.md`).** (i) Noyau :
\(\Re\psi(1+it)-\psi(1)=\int(1-\cos ty)\,k^{(2)}(y)\,dy\),
\(k^{(2)}(y)=1/(2(e^{|y|}-1))>0\), donc
\(\mathrm{Arch}^{(2)}(g)=\psi(1)\|g\|^2+\tfrac12\iint|g(x)-g(x-y)|^2k^{(2)}\) sur
tout \(W_L\). (ii) Domination : pour tout vecteur de coefficients avec
\(|\Lambda_f(p^k)|\le2p^{k/2}\log p\) (Deligne aux bons premiers,
\(a_p\in\{0,\pm1\}\) aux mauvais, hérité) et toute \(g\in W_L\) complexe,
\(Q_f(g)\ge Q_{+,2}(|g|)\), où \(Q_{+,2}\) porte le peigne de \(\zeta^2\)
(coefficient \(2c_n\)). Vérifié sur grille avec les \(a_p\) de 11a1, dix
\(g\) complexes, 10/10, chaque morceau séparément. (iii) Seuil uniforme
\(N_0(L)=(2\pi)^2e^{2\gamma+2A_+(L)}\) avec \(A_+=\|C_+\|\) certifié :

    L        A_+         N0 (enveloppe)   N0 (avec bord)   N0 (pôle, conditionnel)
    0,5493   0,490129       334               60                 91
    0,8      1,219138     1 434              435                856
    1,0      1,949224     6 177            2 468              6 008
    1,2      2,716060    2,86·10^4        1,40·10^4          5,09·10^4
    1,4      3,711770    2,10·10^5        1,19·10^5          5,50·10^5
    1,6      4,903308    2,27·10^6        1,45·10^6          8,06·10^6

Cette table remplace la table « hull » GL₂ de `weil-uniform.md` §5,
invalide deux fois (minorant, exposant legacy). (iv) Asymptote :
\(L^*(N)=\log\log N-\log2+o(1)\) ; le degré \(d\) ne coûte qu'un \(\log d\)
(sous Ramanujan et paramètres archimédiens réels \(>-\tfrac12\),
\(L^*=\log\log N-\log d+o(1)\) par les mêmes trois lignes). (v) Pôle :
\(Q_{+,2}=2Q_\zeta+(\log N-2\log2)\|g\|^2+2[\mathrm{Arch}^{(2)}-\mathrm{Arch}_{1/4}]-4(C^2-S^2)\),
le multiplicateur \(\Re\psi(1+it)-\Re\psi(\tfrac14+\tfrac{it}2)\) tend vers
\(\log2\) et reste au-dessus de \(\log2\) pour tout \(t\) (démontré par
la relecture : sa différence à \(\log2\) est la transformée d'un noyau
positif, minorée par \((\pi/2)\,\mathrm{sech}(\pi t)\)), ce qui compense
exactement le conducteur, d'où \(N_0^{\rm pôle}(L)=e^{4(L+\sinh L)}\),
conditionnel au seul \(Q_\zeta\ge0\) sur \(W_L\) (inconditionnel pour
\(L\le0{,}9729\)). Le mur est celui de la méthode, pas de la famille :
aucune newform rationnelle ne sature Deligne en tout premier. Formes
de Maass : non traité ; le plancher ponctuel survit, mais Ramanujan
n'est pas connu sur le peigne, et le noyau porte \(\cos(\nu y)\), de
signe variable, donc la domination n'est pas acquise. Relecture :
`mur-degre-d-review-2026-10-11.md`, ACCEPT avec corrections (8),
noyau, convention, théorème et table recalculés.

## 11. Régions sans zéro et visibilité

Trois formes de région sans zéro ne donnent pas \((\forall L)\,Q_L\ge0\)
(`largeur-nulle`, `ecart-fixe`, `hauteur-finie`, 3 octobre) : une
région \(\Re s\ge1-\varepsilon(|t|)\) avec \(\varepsilon\to0\) laisse
chaque droite \(\Re s=\tfrac12+\delta\) libre ; une région d'écart fixé
laisse le milieu ouvert ; une absence de zéro jusqu'à une hauteur
finie laisse les ordonnées supérieures libres. La majoration de
densité \(N(\sigma,T)\) laisse un zéro hors droite. Dans l'autre sens,
visibilité (`visibility-mur-entrees-2026-10-03.md`) : les six entrées
autorisées (support premier, convolution logarithmique, triangle,
polylog, profil, poids de Fejér) majorent le sommet de phase par
\(e^{L/2}/\eta(L)\) avec \(\log\eta=o(L)\), au-dessus du tilt
\(\sigma^2e^{cL|\sigma|}\) dès que \(2c|\sigma|<1\) ; passer dessous
exige \(U(L)\le e^{\varepsilon L}\) pour tout \(\varepsilon\), qui est
l'équivalent connu \(|E(t)|\le K_\varepsilon t^{1/2+\varepsilon}\). Une
fenêtre certifiée ne donne donc aucune région sans zéro au-delà de
l'état de l'art ; l'estimation de l'atelier est qu'il faudrait
\(L\approx2{,}6\), hors de portée par la section 3.

## 12. Le recensement : ce qui est la cible sous un autre nom

Proposés comme (R) ou (F) et refusés le 3 octobre, chacun en une
note avec sa raison :
la croissance en moyenne de \(\log|\xi|\) (un comptage de zéros) ; les
routes A, B, C (forme de Weil entière, borne uniforme en \(L\),
comparaison au Gram) ; Wiener–Hopf sur le demi-axe (route A) ; le
régulateur de Borel ; le poids de \(\xi\) (Laguerre–Pólya) ; la
diffusion des séries d'Eisenstein ; la fonction de Riesz ; la
moyenne quadratique de Mertens ; Balazard–Saias–Yor ; Bagchi ;
Franel–Landau ; Liouville ; \(\Re(\xi'/\xi)\) ; la somme de \(|\mu|\) ;
la condition de Turán ; Davenport–Heilbronn ; Redheffer ; Robin pour
\(\psi\) de Dedekind ; la somme de \(\varphi\) ; Volchkov ;
Bender–Brody–Müller ; les zéros de tous les \(L(s,\chi)\) ; les écarts
\(O(\gamma^\varepsilon)\) ; le cup-produit étale ; le transport
optimal ; le champ d'équilibre ; et le 8 octobre, la fonction vis de
Suzuki et la transformée de Cauchy du second membre de de Branges.
Chaque refus dit : équivalent connu, ou ne signe pas \(Q_L\), ou lien
aux zéros par la formule explicite seule. Trois objets du 5 octobre
(clôture quadratique, constante pour tout \(L\), plan mobile) :
aucun ne mène à Weil.

## 13. Ce que la carte dit, et ne dit pas

Elle dit : trois classes de méthodes finies (enveloppes, planchers
ponctuels, positivité sur une sous-classe) ont un plafond démontré
et relu, la classe la plus naturelle à constante exacte, le pôle de
\(\zeta\) ; cinq autres ont une obstruction nommée par citation, dont
deux sont la cible sous un autre nom, une est mesurée, une est sans
borne quantitative. Toute preuve de \((\forall L)\,Q_\chi\ge0\) doit
utiliser les zéros ou l'équation fonctionnelle ailleurs que dans une
borne de taille, et ne peut pas conclure de \(Q\ge0\) sur une
sous-classe \(S\) à \(Q\ge0\) sur \(W_L\) par la seule algèbre des formes
quadratiques continues, sauf si la clôture de \(S\) est \(W_L\), et
alors c'est la cible.

Elle ne dit pas qu'il ne reste rien d'imaginable. Elle ne dit rien
d'une méthode qui n'est pas finie. Elle ne dit pas qu'une fenêtre de
plus apporte quelque chose : aucune n'est lancée sans chaîne (S).

RH se réduit à : \((\forall L)\,Q_\chi\ge0\) sur \(W_L\). Connu
équivalent. Inchangé.

## 14. Sources, reproduction, relecture

Notes du sous-module : `etat-des-lieux-2026-10-03.md` (compas du
cycle enveloppe), `regles-vers-rh-2026-10-02.md` (règles et cycle du
8 octobre), `ouverture-cycle-2026-10-11.md` (les sept énoncés de ce
cycle, avec erratum), `mur-classe-2-plancher-2026-10-11.md` et sa
relecture, `dichotomie-cloture-2026-10-11.md` et sa relecture,
`mur-degre-d-2026-10-11.md` et sa relecture,
`plafonds-classes-3-7-2026-10-11.md`, et les notes citées section par
section. Reproduire les constantes des sections 2, 3 et 10 :

    python code/weil_allplus.py --L 1.0 --parity even
    python code/weil_allplus_zeta.py
    python code/comb_majorant.py
    python code/torus_max_comb.py
    python code/allplus_degree_d.py

Relecture de cette synthèse : `carte-des-murs-review-2026-10-11.md`,
ACCEPT AVEC CORRECTIONS (14, toutes d'étiquette, de sens d'inégalité
ou d'attribution ; aucune ne touche un théorème), corrections
appliquées. Le seuil \(L\approx2{,}6\) de la section 11 vient de
`regles-vers-rh-2026-10-02.md` §4.

Pas covering. Pas RH.
