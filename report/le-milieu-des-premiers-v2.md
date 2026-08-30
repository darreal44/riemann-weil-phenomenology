# Le milieu des nombres premiers — v2
## Rapport d'exploration : du crible d'Ératosthène à la conjecture de forme de Suzuki

*Exploration conjointe, 30 août 2026 (v2). Document de synthèse : analyse, algorithmes, code, résultats numériques et références. La v2 ajoute les sections 8 à 11 : lectures comparatives de la littérature (Connes-Consani, Suzuki, Connes 2026, Groskin), expérience de raccordement des régimes de positivité, et premier test quantitatif de la convergence de forme de la conjecture (1.2) de Suzuki — avec une loi mesurée, R ≈ e^(−L)/3.*

---

## Résumé

Partis d'une intuition simple — chaque nombre premier trouvé par le crible d'Ératosthène ajoute une « dimension » à l'espace de recherche — nous avons déroulé le fil jusqu'à une reconstruction expérimentale, modeste mais chiffrée, du programme Hilbert-Pólya. Le parcours passe par la dualité position/fréquence des premiers (formule explicite de Riemann), l'analogie avec les gouttelettes marcheuses de Couder-Fort (mémoire de chemin, onde-pilote), le portrait-robot du « milieu » hypothétique dont les zéros de zêta seraient le spectre, puis quatre campagnes numériques qui mesurent : l'émergence des zéros depuis les premiers, l'installation de la statistique GUE, la sélection de la droite critique par un critère de blancheur spectrale, la structure du « mode dangereux » de la forme de Weil, et la vitesse de fermeture de la marge de positivité — y compris la violation effective de cette positivité par tout milieu tronqué, écho quantitatif d'un théorème de Montgomery.

Rien ici ne constitue une preuve de quoi que ce soit. C'est un rapport de reconnaissance de terrain : des observables, des constantes mesurées, et un cahier des charges affiné pour un objet que personne n'a encore construit.

---

## 1. Le point de départ : le crible comme empilement de dimensions

### 1.1 L'intuition et sa formalisation

L'observation initiale : trouver un premier avec le crible revient à ajouter à chaque étape une dimension nouvelle — la classe de congruence modulo le premier qu'on vient de trouver. Formellement, c'est le **théorème des restes chinois** : tout entier n est un point de coordonnées (n mod 2, n mod 3, n mod 5, ...), et un survivant du crible est un point qui évite l'hyperplan « coordonnée = 0 » dans chaque dimension. C'est le principe de la factorisation par roue (*wheel factorization*).

Correction quantitative importante : pour atteindre le n-ième premier p_n, il ne faut pas n−1 dimensions mais seulement **π(√p_n)** — les premiers sous la racine. Le 100e premier (541) demande 9 dimensions (les premiers jusqu'à 23) ; le 10 000e (104 729) en demande 66 ; le 1 000 000e (15 485 863) environ 546.

### 1.2 La croissance du nombre de dimensions

En combinant p_n ≈ n·ln n et le théorème des nombres premiers π(x) ≈ x/ln x :

```
dimensions(n) ≈ 2·√(n·ln n) / ln(n·ln n)   —   croissance ~ √n à facteurs log près
```

La fraction de survivants après criblage par les premiers ≤ x suit le produit ∏(1−1/p) ~ e^(−γ)/ln x (théorème de Mertens) : chaque dimension nouvelle « paie » pour un intervalle de plus en plus vaste, d'où l'économie du crible.

### 1.3 Géométrie : un tore, pas un espace ouvert

Chaque dimension modulaire est un **cercle** (Z/pZ), pas un axe : l'espace du crible est un produit de cercles de circonférences 2, 3, 5, 7, ... — un tore compact de dimension croissante. Cette compacité jouera un rôle central plus loin (le « confinement » qui manque à Berry-Keating). La version rigoureuse de ce collage de toutes les dimensions modulaires avec la dimension continue est l'espace des **adèles**, cadre de travail de Connes.

---

## 2. La seconde couche : le spectre

### 2.1 La formule explicite de Riemann

Les dimensions modulaires disent où les premiers *ne peuvent pas* être. Une seconde famille de « dimensions » gouverne comment les survivants fluctuent autour de leur densité moyenne : les **zéros non triviaux de la fonction zêta**. La formule explicite (Riemann 1859, von Mangoldt 1895) s'écrit, sous forme lissée :

```
ψ(x) = x − Σ_ρ x^ρ/ρ − log(2π) − ½·log(1−x^{−2}),   ρ = ½ + iγ (sous RH)
```

Chaque zéro contribue une oscillation x^(1/2)·cos(γ·log x)/|ρ| : une onde de fréquence γ **en échelle logarithmique**. Les premiers sont un signal 1D dont le spectre habite la droite critique — la structure d'un hologramme.

### 2.2 Les trois faits qui dessinent le portrait-robot du milieu

Si les zéros sont le spectre d'un système dynamique (programme **Hilbert-Pólya**), les contraintes connues dressent le portrait suivant.

Le temps du système est un zoom : les oscillations sont périodiques en log x, donc le flot est un flot de **dilatations** — l'hamiltonien candidat de Berry-Keating est H = xp, générateur des changements d'échelle (Berry & Keating 1999).

Le système est chaotique à temps orienté : les corrélations des zéros suivent la statistique **GUE** des matrices aléatoires hermitiennes complexes (conjecture de Montgomery 1973, vérifiée numériquement par Odlyzko sur des milliards de zéros), et non GOE — en physique, GUE signale une symétrie par renversement du temps **brisée**.

Les premiers sont ses orbites périodiques : la formule explicite a exactement la structure de la **formule des traces de Gutzwiller** (1971) reliant spectre quantique et orbites classiques d'un système chaotique. Dictionnaire : orbite de période log p pour chaque premier, répétitions p^k pour les retours multiples.

Ce qui manque à H = xp seul : un confinement (son spectre est continu). Notre tore de cribles fournit un candidat naturel de fermeture — l'arithmétique modulaire elle-même.

### 2.3 L'univers parallèle où tout cela est démontré

Pour les **corps de fonctions** (courbes sur corps finis), l'hypothèse de Riemann est un théorème (Weil années 1940, Deligne 1974 pour les variétés générales) — et la preuve est de type Hilbert-Pólya : les zéros sont les valeurs propres du **Frobenius** agissant sur la cohomologie de la courbe. Le « milieu » y est la courbe elle-même. Ce qui force les zéros sur la droite critique est une **positivité** géométrique (inégalité de Castelnuovo, forme d'intersection).

Transposé aux entiers : Spec Z ressemble à une courbe, mais au-dessus de quoi ? D'où le programme du « corps à un élément » **F₁** (Tits, Soulé, Borger, Lorscheid, Connes-Consani et leur *site arithmétique*), et le rêve de Deninger d'un système dynamique feuilleté dont le flot reproduirait la formule explicite.

### 2.4 Le critère de Weil : la positivité est le nerf de la guerre

Weil (1952) : **RH équivaut à la positivité d'une forme quadratique explicite** Q(g) calculable depuis les premiers, pour toutes les fonctions test de la forme g = f ⋆ f̃. La leçon des cas démontrés : la positivité n'est jamais prouvée abstraitement, elle est *incarnée* — la quantité se révèle être un carré (∫|ψ|², forme d'intersection) dans un espace concret. Trouver le milieu et prouver Riemann seraient le même acte : construire l'espace où la forme de Weil s'écrit comme une énergie. C'est la stratégie de la formule des traces de Connes (1999).

---

## 3. L'analogie hydrodynamique : les gouttelettes marcheuses

### 3.1 Le système de Couder-Fort

Une gouttelette d'huile rebondissant sur un bain vibrant (juste sous le seuil d'instabilité de Faraday) est guidée par l'onde de surface qu'elle a elle-même créée : une réalisation macroscopique d'une mécanique de type **onde-pilote** (de Broglie-Bohm). Reproduits expérimentalement : quantification des orbites, effet tunnel, states liés (Couder & Fort 2005-2010 ; revue : Bush 2015). Point d'honnêteté : la reproduction des **fentes de Young** est contestée — l'expérience refaite par l'équipe de Tomas Bohr (Andersen et al. 2015) n'a pas retrouvé les franges de Couder.

### 3.2 Ce que l'analogie apporte structurellement

La clé du système est la **mémoire de chemin** : le champ d'ondes encode l'histoire des rebonds passés, et cette mémoire globale produit des statistiques « quantiques » depuis une dynamique déterministe. Analogie structurelle avec le crible : chaque premier trouvé laisse une empreinte ondulatoire (sa progression arithmétique) qui contraint tous les survivants futurs.

Deux distinctions affinées en cours de route. D'abord, l'espace des états du bain ne grandit pas : il est de dimension infinie d'emblée et se **remplit** progressivement — de même, toutes les dimensions modulaires « existent » d'avance (les adèles) et le criblage ne fait que les activer. Ensuite, une différence de nature : la mémoire du bain *influence* les rebonds futurs ; la mémoire du crible *dicte* le prochain premier, sans aucune liberté. Degré de rigidité de la boucle mémoire-futur : question ouverte de savoir si un milieu physique peut incarner une mémoire qui dicte.

Enfin, la leçon de méthode qui a guidé toute la partie numérique : **l'huile n'a pas été conçue, elle a été trouvée** — et son secret est un réglage critique (proximité d'une transition de phase, d'où la mémoire longue). D'où l'idée de chercher non pas un espace abstrait parfait, mais un système critique dont les temps caractéristiques seraient les log p. Le **gaz de Riemann** existe en physique statistique (Julia 1990 ; système de Bost-Connes 1995, avec brisure spontanée de symétrie faisant émerger la structure de Galois) : sa fonction de partition est ζ(β), avec transition de phase au pôle β = 1. Personne ne sait quel paramètre physique correspondrait à « s'asseoir » sur Re = ½.

### 3.3 L'émergence : le spectre n'existe qu'à la limite

Fait dur : le produit d'Euler tronqué aux n premiers premiers est une fonction quasi-périodique lisse, **sans zéros dans la bande critique**, à tout étage fini. Les zéros surgissent seulement dans l'objet limite — émergence au sens fort, structurellement analogue à une transition de phase (pas de point de fusion net pour un nombre fini de particules). Conséquence : toute méthode de calcul est une troncature, et la propriété à prouver vit exactement là où toute troncature la détruit. Les campagnes numériques ci-dessous mesurent les deux faces de ce théorème : les *ombres* des zéros apparaissent très tôt, mais la *positivité* de Weil est effectivement violée à tout étage fini.

---

## 4. Campagnes numériques : algorithmes et résultats

Environnement : Python 3 / NumPy / mpmath, machine standard. Code complet en annexe. Complexité totale du pipeline : O(M·k·N) — linéaire ; le mur n'est pas le calcul mais la convergence en 1/log N (atteindre une précision ε coûte N ≈ e^(1/ε)).

### 4.1 Campagne 1 — Le champ de mémoire spectral : les zéros émergent du crible

**Algorithme.** (1) Crible d'Ératosthène jusqu'à N = 10⁶ (78 498 premiers, 78 734 modes p^k). (2) Construction du champ

```
S_N(t) = − Σ_{n ≤ N} Λ(n)·w(n)·n^{−1/2}·cos(t·log n),    w(n) = 1 − log n/log N  (fenêtre de Cesàro)
```

où Λ est la fonction de von Mangoldt. La théorie (formule explicite « retournée ») prédit des pics aux ordonnées γ des zéros. (3) Détection de pics, dépliage, statistiques.

**Résultats.**

| Observable | Mesure | Attendu |
|---|---|---|
| Pics détectés sur t ∈ [10, 310] | 143 | 144 zéros (formule de Riemann-von Mangoldt) |
| Position des 15 premiers pics | écart ≤ ±0.015 des zéros vrais | 14.1347, 21.0220, 25.0109, ... |
| Premier zéro avec N = 10³ (168 premiers !) | 14.136 (erreur 0.0013) | 14.134725 |
| Espacements dépliés : MSE vs GUE | **0.0017** | — |
| Espacements dépliés : MSE vs Poisson | 0.1541 | — |
| Premier bin de l'histogramme (répulsion) | 0.000 | GUE : 0.080 ; Poisson : 0.852 |
| Largeur des pics | suit 2π/log N (0.75 → 0.35 pour N : 10³ → 10⁶) | résolution spectrale de la troncature |

**Lecture.** Aucun zéro n'existe à étage fini, mais leur silhouette statistique est visible presque immédiatement — l'émergence est un flou qui se résorbe, pas un mur. La signature chaotique (GUE, répulsion des niveaux) est déjà installée à N = 10⁶. Le coût d'une décimale de netteté supplémentaire est une exponentiation de N : mesure directe du « mur en 1/log N ».

### 4.2 Campagne 2 — Le noyau vu de près : blancheur, dualité, orbites

**Correction d'artefact (honnêteté expérimentale).** Une première diagonalisation du noyau K(t_j−t_k) sur grille grossière (pas 2.4) avait donné un spectre quasi plat (valeurs propres 274–304), interprété comme « milieu blanc ». Diagnostic sur grille dense (pas 0.2) : le spectre n'est pas plat — ratio hautes/basses fréquences = **11.75**, croissance ~ e^(ω/2) conforme à la densité des poids Λ(n)/√n. La platitude venait du repliement spectral : Nyquist = π/2.4 = 1.31 face à des fréquences jusqu'à log N = 13.8. Le milieu nous avait renvoyé notre propre échantillonnage.

**Scan de l'exposant de blancheur.** Noyau de poids Λ(n)·n^(−β), Toeplitz dense, pas 0.2, τ ≤ 60 ; pente de log λ vs fréquence propre ω mesurée par régression :

| β | pente mesurée | pente théorique (1−β) |
|---|---|---|
| 0.6 | +0.752 | +0.4 |
| 0.8 | +0.548 | +0.2 |
| 1.0 | +0.413 | 0.0 |
| 1.2 | +0.094 | −0.2 |

La décroissance de la pente suit la théorie au rythme ≈ −1 par unité de β (décalage systématique ~+0.35 attribuable à la zone ω < 3 où les orbites sont isolées, avant le quasi-continuum). **La blancheur exponentielle sélectionne β = 1, c'est-à-dire le carré de l'exposant n^(−1/2) : la normalisation de la droite critique est l'unique exposant rendant le champ de mémoire stationnaire** (blanc à facteur logarithmique près — la couleur résiduelle vient du poids arithmétique Λ). Version spectrale, mesurée, de l'heuristique « RH = compensation en racine carrée ». Les vecteurs propres sont délocalisés (IPR ≈ 0.008 contre 0.005 pour une onde plane pure) : le milieu conduit, pas de localisation d'Anderson.

**La dualité rendue visible.** Le même champ S(t), calculé sur t ∈ [0, 1200] (N = 10⁵) puis transformé de Fourier, montre des raies exactement aux longueurs d'orbites :

| Orbite | position théorique | pic mesuré | puissance relative |
|---|---|---|---|
| log 2 | 0.6931 | 0.6912 | 0.537 |
| log 3 | 1.0986 | 1.0996 | 0.965 |
| log 4 = 2·log 2 | 1.3863 | 1.3875 | 0.264 |
| log 5 | 1.6094 | 1.6074 | 0.971 |
| log 7 | 1.9459 | 1.9478 | 0.966 |
| log 8 = 3·log 2 | 2.0794 | 2.081 | 0.120 |
| log 9 = 2·log 3 | 2.1972 | 2.207 | 0.227 |
| log 11 | 2.3979 | 2.3981 | 1.000 |
| log 13 | 2.5649 | 2.553 | 0.914 |

Les répétitions d'orbites de Gutzwiller (p²، p³) sont visibles avec leurs amplitudes réduites. La hiérarchie des intensités suit Λ(p)/√p = log p/√p, **maximale à p = e² ≈ 7.39** : les orbites les plus « sonores » du milieu sont 7, 11, 13 ; l'orbite 2 chante plus faiblement. Un seul signal, deux lectures : en position → les zéros ; en fréquence → les orbites. Les deux faces de la formule des traces sur un objet calculé depuis le crible.

### 4.3 Campagne 3 — La forme de Weil et le mode dangereux

**Construction.** Fonctions test en peigne gaussien : f_j centrées en u_j = j·δ (δ = 0.5, J = 20, support U = 9.5 < log N), largeur s = 0.05 ; g_jk = f_j ⋆ f̃_k, transformée h_jk(r) = e^(ir(u_j−u_k))·e^(−s²r²). Forme de Weil par la formule explicite (convention Iwaniec-Kowalski, th. 5.12) :

```
W_jk = [h(i/2) + h(−i/2)]  +  (1/2π)∫ h(r)·Ω(r) dr  −  Σ_n Λ(n) n^{−1/2} [g(log n) + g(−log n)]
     =  2·cosh(Δ/2)·e^{s²/4}  +  terme archimédien      −  côté premiers,        Δ = u_j − u_k
```

RH ⟺ W ⪰ 0 (sur toutes les fonctions test, tout support). Le **mode dangereux** est le vecteur propre de la plus petite valeur propre : la direction où la positivité tient de plus juste — le détecteur le plus sensible constructible, celui qui verrait en premier un zéro hors-ligne.

**Validation croisée.** Le terme archimédien correct s'est imposé par calibration contre le côté zéros (40 zéros via mpmath) :

| Variante Ω(r) | résidu ‖W_premiers − W_zéros‖/‖W_zéros‖ |
|---|---|
| **Re ψ(¼ + ir/2) − log π** | **0.0012** |
| ½·Re ψ(¼ + ir/2) − ½·log π | 0.2376 |
| Re ψ(½ + ir) − log π | 0.8621 |

Accord entrée par entrée à 4 décimales (ex. W[0,0] : 2.7461 vs 2.7461). L'objet calculé depuis les premiers est bien la forme de Weil.

**Résultats.** Spectre côté premiers (N = 10⁶) : λ_min = **0.00047**, λ_max = 12.80 — la positivité tient par un fil de 3.7×10⁻⁵ relatif. Le mode dangereux a une stratégie en trois volets, tous lisibles :

Premièrement, ses coefficients sont exactement **antisymétriques** (c_j = −c_{19−j}) : un mode impair, orthogonal au terme du pôle (pair, en cosh) — il commence par esquiver le théorème des nombres premiers.

Deuxièmement, son profil spectral F(γ) = |ĉ(γ)|²·e^(−s²γ²) s'annule sur **chacun** des dix premiers zéros (F ≤ 0.0006 en chaque γ_k) : anti-accordé sur tout le spectre, avec lobes résiduels calés entre les zéros.

Troisièmement, toute sa puissance est réfugiée à γ ≈ 1, **dans la bande infrarouge [0, γ₁ = 14.13[** — le désert spectral sous le premier zéro, seul territoire sans zéro pour le punir. Ce qui y maintient la positivité n'est pas un zéro mais le pôle : le flot moyen des premiers. La zone fragile de RH est dans les graves ; un zéro anormalement bas (type Landau-Siegel) serait détecté d'abord par ce mode.

### 4.4 Campagne 4 — Fermeture de la marge et frontière de certification

**Protocole.** Marge = λ_min(W) en fonction du support U = (J−1)·δ, côté zéros exact (40 zéros) et côté premiers poussé à N = 10⁷ (664 579 premiers ; écart max premiers/zéros sur la table : 0.0018).

| J | U | marge (zéros exacts) | marge (premiers, N = 10⁷) |
|---|---|---|---|
| 6 | 2.5 | 7.08×10⁻¹ | 7.08×10⁻¹ |
| 10 | 4.5 | 1.45×10⁻¹ | 1.43×10⁻¹ |
| 14 | 6.5 | 4.11×10⁻² | 3.86×10⁻² |
| 18 | 8.5 | 8.24×10⁻³ | 5.00×10⁻³ |
| 20 | 9.5 | 5.23×10⁻³ | 4.69×10⁻⁴ |
| 22 | 10.5 | 9.67×10⁻⁴ | **−1.68×10⁻³** |
| 24 | 11.5 | 2.39×10⁻⁴ | **−3.44×10⁻³** |
| 26 | 12.5 | 1.18×10⁻⁴ | **−3.99×10⁻³** |

**Résultat 1 : fermeture exponentielle, et sa vraie variable.** Côté exact : marge ≈ 14·e^(−0.83·U) (corrélation 0.986) pour δ = 0.5. Test de robustesse en densité de peigne : α = 1.69 (δ = 0.25), 0.83 (δ = 0.5), 0.63 (δ = 0.75) — mais **α·δ ≈ 0.42–0.47, quasi constant**. La marge décroît donc comme e^(−0.43·J) : la variable n'est pas la fenêtre physique mais le **nombre de degrés de liberté**. Chaque fonction test ajoutée multiplie la marge par ≈ 0.65 — un taux de fermeture par dimension, mesuré. (Interprétation : résidu de moindres carrés d'un problème de concentration type Slepian contre le repère fini des zéros effectifs ; la valeur ~0.43/dimension reste à expliquer théoriquement.)

**Résultat 2 : le milieu tronqué viole réellement la positivité.** Au-delà de U ≈ 10, la marge côté premiers devient négative — de l'ordre de l'erreur de troncature (0.0018), qui dépasse alors la vraie marge. Lecture profonde : ce n'est pas seulement une incapacité à certifier ; le gaz tronqué a **réellement** des pseudo-zéros hors-ligne, écho quantitatif du théorème de Montgomery (1983) sur les zéros des sommes partielles de zêta à droite de la droite critique (problème de Turán). Le sismographe fonctionne : il a détecté la maladie, présente à chaque étage fini, dont seul l'objet complet guérit. C'est le théorème d'émergence du §3.3, muni d'un détecteur.

**Résultat 3 : la frontière de certification, avec ses constantes.** Croisement marge/bruit : U_max = (ln 14 − ln bruit)/0.83, soit 10.8 prédit pour N = 10⁷ — casse observée entre 9.5 et 10.5. Le bruit chute d'environ 8× par décade de N, donc chaque décade de premiers achète ≈ 2.5 unités de fenêtre : **la défense de la positivité par un milieu de taille N s'arrête à U ≈ 0.65·log N**, avant la limite naïve U < log N.

---

## 5. Synthèse : le portrait-robot, avec des constantes dessus

Le milieu cherché, s'il existe, doit : vivre dans l'espace des échelles (flot de dilatations, H ~ xp) ; être compact — le tore adélique des dimensions modulaires fournit la fermeture ; être chaotique à temps orienté (GUE mesuré ici dès N = 10⁶, MSE 0.0017) ; avoir les premiers pour orbites fermées de périodes log p (raies mesurées ici à ±0.002, hiérarchie en Λ(p)/√p culminant à p ≈ e²) ; porter une structure de carré rendant la forme de Weil positive — l'équivalent de l'énergie ∫|champ|² du bain d'huile ou de l'inégalité de Castelnuovo chez Weil. Nos mesures ajoutent : la normalisation Re = ½ est celle qui blanchit le champ de mémoire ; la réserve de positivité se ferme à taux ≈ 0.65 par degré de liberté de test ; sa zone fragile est l'infrarouge sous γ₁, gardé par le pôle (le théorème des nombres premiers) et non par les zéros ; et tout milieu tronqué est effectivement malade (positivité violée), la guérison n'advenant qu'à la limite.

## 6. Pistes ouvertes (état v1 — plusieurs sont exécutées dans les sections 8-10)

Expliquer théoriquement le taux ≈ 0.43 par dimension (lien probable avec les problèmes de concentration de Slepian et la densité du repère des zéros). Suivre la migration des pseudo-zéros hors-ligne du gaz tronqué quand N croît (vitesse de retour vers la droite critique — dialogue avec les résultats de Montgomery et Gonek sur les sommes partielles). Chercher le paramètre critique du gaz de Riemann/Bost-Connes correspondant à Re = ½ (l'analogue du seuil de Faraday de Couder). Réaliser des « milieux ratés » physiques (graphes quantiques à arêtes log p, cavités chaotiques) et lire dans leurs défauts le cahier des charges du bon — chaque écart au spectre de zêta est une mesure de ce qui manque à l'huile. Explorer la piste F₁ / site arithmétique comme construction du support géométrique du tore adélique.

---

## 8. Lectures comparatives : où le fil a atterri

### 8.1 Connes-Consani, « Spectral triples and ζ-cycles » (2021/2023)

La lecture du papier central a livré un verdict double. D'abord, notre exploration avait reconstruit son paysage : le radical approché de la forme de Weil y est engendré par l'image, via l'application E(f)(x) = x^(1/2)·Σ_{n>0} f(nx) (une somme sur les entiers — le crible transformé en fonction test), de combinaisons de fonctions prolates de Slepian-Pollak ; notre « mode dangereux » (§4.3) en est la description spectrale duale. Leur sensibilité arithmétique dépasse la nôtre : à L = log 3, remplacer le premier 2 par une variable p ne préserve la positivité que dans un intervalle de taille < 10⁻³ autour de p = 2, et chaque franchissement d'une puissance de premier dont on omet la contribution rend la forme négative. Ensuite, un désaccord quantitatif fécond : leur plus petite valeur propre décroît de façon **doublement exponentielle** dans le support (−ln λ_min ≈ 10·µ, jusqu'à 2.389×10⁻⁴⁸ à µ = 11), quand notre campagne 4 mesurait un simple e^(−0.83U) — désaccord résolu par l'expérience de raccordement (§9).

Le prix principal : le **théorème 6.4 (ζ-cycles)** réalise notre portrait-robot pièce par pièce. Un ζ-cycle est un cercle de longueur L = log µ tel que ΣµE(S₀ᵉᵛ) n'est pas dense dans L²(C) ; le spectre de l'action de R*₊ sur l'orthogonal est formé de parties imaginaires de zéros, et tout cercle de longueur multiple entier de 2π/s (avec ζ(½+is) = 0) est un ζ-cycle. Cercle compact en échelle logarithmique (notre tore-paroi), flot de dilatation (notre temps-zoom), sous-espace arithmétique découpé par la somme sur les entiers (notre crible), zéros comme résonances de cavité — jusqu'à leur spéculation finale d'un « cusp » mystérieux dont les géodésiques fermées correspondraient aux ζ-cycles : nos orbites, cherchant leur variété.

### 8.2 Suzuki, « Weil's quadratic form via the screw function » (juin 2026)

Suzuki intègre deux fois la distribution de Weil pour obtenir une **fonction vis** g(t) continue et explicite (rampe Λ(n)/√n·(|t|−log n), termes en digamma et Hurwitz-Lerch), telle que l'opérateur A_a de Connes-Consani-Moscovici est l'extension de Friedrichs de B_a = D*·G_a·D (dériver, convoluer par g, re-dériver), et que **RH équivaut à ce que g soit une fonction vis au sens de Krein-Langer** — la fonction de structure d'une hélice dans un espace de Hilbert. Sa conjecture (1.2) : quand a → ∞, la transformée de Fourier de l'état fondamental converge, à normalisation c_a près, vers **ξ(½+iz)**. Révélation rétroactive pour nous : notre mode dangereux de la campagne 3 — encoches sur chaque zéro, refuge infrarouge — était le portrait à fenêtre finie de |ξ(½+iγ)|², dont les zéros sont les zéros de zêta et que le facteur Γ écrase super-exponentiellement sous γ₁.

### 8.3 Connes 2026 et l'état du champ

La « Lettre à travers le temps » de Connes (février 2026) cristallise la question : pour tout cutoff c, l'état fondamental de la forme de Weil tronquée sur L²([0, log c]) a des zéros de Fourier-Mellin **prouvés sur la droite critique** (Connes-van Suijlekom, th. 6.1) ; seule la *convergence* de ces zéros vers les zéros de Riemann quand c → ∞ est ouverte — et si elle tient, RH suit par Hurwitz. Toute la difficulté du problème s'est concentrée dans un mot : convergence.

### 8.4 Groskin (mai-juin 2026) : l'occupation du terrain « positions »

Première implémentation publique indépendante de la matrice de Galerkin ; seize cutoffs (c = 13 à 67, plus 100) ; erreur sur γ₁ de ~2×10⁻⁵⁵ à ~1.5×10⁻¹⁶⁸ ; extraction de γ₁...γ₁₀ à **307-329 chiffres** (c = 100, N = 250, dps = 500) ; extrapolation d'Aitken compatible avec l'heuristique de Connes §6.4 (−533.7 vs −530.4). Leçon méthodologique : des blocs de valeurs propres négatives, stables en précision, sont des artefacts du cutoff archimédien fini T. Restent explicitement ouverts : l'extension Dirichlet (portage partiel à χ₃ seulement), la question « transition Poisson → GUE ? » du spectre de Galerkin en masse, et — notre créneau — la convergence de la *fonction* (pas seulement de ses zéros).

## 9. Expérience de raccordement : les trois régimes de la positivité

Protocole : marge λ_min de la forme de Weil sur peignes gaussiens (côté zéros exact, 280 zéros calculés), en fonction de la bande (s), de la densité du peigne (δ) et du support (U). Résultats.

**Le « 0.83 » n'était pas intrinsèque.** En ouvrant la bande (s : 0.05 → 0.025 → 0.0125, soit 42 → 112 → 280 zéros effectifs), la pente en U s'effondre : α = 0.834 → 0.367 → 0.096. L'invariant est le **taux par degré de liberté** ≈ 0.41 (mesuré 0.413 puis 0.366 à U = 2.5 fixé en densifiant le peigne), déjà identifié en campagne 4 sous la forme α·δ ≈ 0.43.

**Trois régimes, cartographiés à U = 2.5 fixé** (bande s = 0.05, 42 zéros, rang du noyau = 84) : régime générique e^(−0.41·J) jusqu'à J ≈ 41 (marge 3.9×10⁻¹⁰) ; **plongeon de Slepian** à l'approche du mur de rang — taux 0.73 puis ~3.0 par dimension, marge = 2.19×10⁻³⁶ à J = 61 (vérifiée en multiprécision dps = 50, coût : 1 seconde grâce à la structure Toeplitz) ; mur de rang à J = 84. Le régime doublement exponentiel de Connes-Consani est ainsi atteint et raccordé. En float64, J ≥ 51 produit des valeurs propres négatives (−5×10⁻¹⁵) : de fausses violations de RH, purs artefacts.

**La blancheur protège Riemann.** À J fixé, ouvrir la bande fait *remonter* la marge vers 1 (à J = 41 : 3.9×10⁻¹⁰ pour 42 zéros, 0.22 pour 280) : face à une direction de test générique, la décorrélation GUE des zéros (campagne 2) rend le noyau quasi-identité, donc massivement positif. La positivité n'est menacée que quand la résolution rattrape le nombre de zéros — ou par le raccourci arithmétique : l'application E de Connes-Consani fabrique des fonctions test portant le facteur ζ(½−iz), qui s'annulent sur *tous* les zéros d'un coup. Les directions dangereuses sont précisément les directions arithmétiques, celles qui convergent vers ξ. Le milieu se défend par sa blancheur ; son seul adversaire sérieux est son propre reflet arithmétique.

## 10. Test de forme de la conjecture (1.2) de Suzuki : première mesure

### 10.1 Construction et validation

État fondamental de la forme de Weil semi-locale calculé **depuis les premiers seuls** : base réelle paire de Connes-Consani (ζ-cycles, §2.1) avec table de convolution en forme fermée (leur lemme 2.6), pièces ψ# = pôle − archimédien − premiers, quadrature composite Gauss-Legendre à nœuds raffinés par Newton en multiprécision, diagonalisation mp.eigsy (dps 40 à 130 selon µ). Validations : pôle contre la forme fermée 32·sinh²(L/4)/L ; archimédien contre sa définition spectrale Q∞ = ∫|f̂|²·2θ'(t)/2π dt et contre le coefficient 2.00963 de la figure 4 de Connes-Consani ; matrice entière contre le côté zéros (ratios constants ≈ 1.05-1.10, écart = queue de troncature des 280 zéros) ; et surtout **λ_min(µ = 11, base 47) = 3.58×10⁻⁴⁸ contre le 2.389×10⁻⁴⁸ publié par Connes-Consani** — approché par au-dessus, comme Galerkin le doit. L'échelle prolate des états quasi-nuls apparaît proprement (espacement ~e^(−14) par barreau).

Trois artefacts débusqués en route, chacun par une validation indépendante : le regroupement du numérateur archimédien ((e^(y/2)·θ − θ(0)), pas e^(y/2)·(θ − θ(0)) — écart 0.915 attrapé par la confrontation à Q∞) ; la séparation de l'intégrande en deux morceaux quasi-divergents ; et des nœuds de Gauss-Legendre importés de numpy en float64, plafonnant toute la matrice à 10⁻¹⁶. La taxonomie complète des pièges du domaine compte désormais : float64 (valeurs propres), troncature du crible (pseudo-zéros hors-ligne), cutoff archimédien T (Groskin), constantes de quadrature.

### 10.2 Protocole à double limite

Découverte méthodologique : à µ fixé, le résidu de forme converge **par en dessous** quand la base grandit (µ = 16 : 0.64% → 1.13% → 1.37% → 1.69% pour N = 35, 40, 44, 52) — les petites bases flattent le test, leur état fondamental plus lisse ressemblant fortuitement plus à ξ. Il faut extrapoler en N d'abord, en µ ensuite. Une « accélération » apparente de la convergence entre µ = 11 et 16 s'est révélée être un artefact de ce couplage.

### 10.3 Résultats et loi mesurée

Résidu relatif max |c_a·v̂ − Ξ|/max|Ξ| avec Ξ(z) = ξ(½+iz) :

| µ | λ_min (base indiquée) | résidu infrarouge [0,13), extrapolé en N | résidu entre zéros (15,30) | c_a |
|---|---|---|---|---|
| 3.5 | 3.3×10⁻¹⁰ | ≈ 11.3% | 0.65% | 1.217 |
| 5.5 | 4.8×10⁻²⁰ | ≈ 6.6% | 0.26% | 1.180 |
| 7.5 | 9.3×10⁻³⁰ | ≈ 4.7% | 0.16% | 1.165 |
| 9.5 | 4.1×10⁻³⁸ | ≈ 3.4% | 0.10% | 1.155 |
| 11 | 3.6×10⁻⁴⁸ (N=47) | 3.0% (converge : 2.49→2.84→2.96) | ≈ 0.094% | 1.153 |
| 16 | 8.0×10⁻⁶⁸ (N=53) | ≈ 2.2±0.4% (encore croissant) | ≈ 0.05% | ≈ 1.145 |

**Loi : résidu infrarouge ≈ 0.33/µ = (1/3)·e^(−L).** Vérification : 0.33/5.5 = 6.0%, 0.33/11 = 3.0%, 0.33/16 = 2.1%. La forme de ξ s'apprend au rythme e^(−support) — un e-fold par unité de fenêtre — pendant que les positions des zéros convergent en superexponentiel (10⁻⁵⁵ dès c = 13 chez Connes/Groskin) et que λ_min plonge de 58 ordres de grandeur sur la même plage. Le retard se concentre dans la bande infrarouge sans zéros (30 à 40 fois plus d'erreur qu'entre les zéros, à chaque µ) : le bombement en Γ de ξ sous γ₁ est le morceau que les premiers apprennent le plus lentement — la mesure spectrale vit sur les zéros, et hors de son support la contrainte est molle. La constante c_a décroît régulièrement (1.217 → ~1.145), compatible avec une limite finie non identifiée.

Conséquence pratique : la conjecture (1.2) apparaît vraie mais son régime est complémentaire de celui des zéros — tester la forme demande de la portée en µ (0.1% de résidu ≈ µ = 330, base ~300, dps ~1500), pas des centaines de décimales à µ modeste.

## 11. Bilan v2 et programme

Trois contributions phénoménologiques revendicables à l'issue de cette phase, aucune ne prouvant quoi que ce soit : la **loi de forme R ≈ e^(−L)/3** (premier test quantitatif de Suzuki (1.2), avec protocole à double limite) ; la **cartographie des trois régimes de positivité** (0.41/dimension générique, plongeon de Slepian, mur de rang) et la lecture « blancheur protectrice » qui en découle ; la **frontière de certification en N** de la campagne 4 (U_max ≈ 0.65·log N), axe que la littérature lue ne couvre pas. Programme : le scan Dirichlet/Siegel — lancé et moissonné au §13, sa suite est la carte de s(γ₁, parité) sur davantage de conducteurs ; l'identification théorique du taux 0.41/dimension (théorie des prolates) — celle de la limite de c_a est faite au §12 ; la poussée de la loi de forme vers µ ~ 50-330 ; et la publication du tout en notebook reproductible.

## 12. Dénouage des conventions et identification de c_a

### 12.1 Audit et facteur de Fourier

L'audit des conventions du test de forme s'est révélé sain : base orthonormée en L²(dx) (la normalisation ℓ² du vecteur propre est donc canonique), facteur σ = ½·Q_W sans effet sur les vecteurs propres, correspondance a = L/2 avec l'intervalle [−a, a] de Suzuki, et ξ_Suzuki = 2·ξ_classique. La vérification numérique de l'identité de Fourier a en revanche épinglé le facteur exact : avec Φ_c(u) = Σₙ (2π²n⁴e^(9u/2) − 3πn²e^(5u/2))·e^(−πn²e^(2u)) (noyau thêta de Riemann, pair), on mesure ∫Φ_c·e^(itu)du = ½·ξ_classique(½+it), ratio 0.5 exact à tout t testé. Le noyau de la convention Suzuki est donc Φ_S = 4·Φ_c, de norme ‖Φ_S‖_L²(ℝ) = 1.130932.

### 12.2 Identification

Test décisif à µ = 11 (base 47, dps 85) : le recouvrement L² entre l'état fondamental et le noyau thêta normalisé vaut ⟨v, Φ_S⟩/‖Φ_S‖ = **0.99964**. Aucune fuite de masse vers les hautes fréquences : le mécanisme est v_a → Φ_S/‖Φ_S‖ en L², d'où

**c_∞ = ‖Φ_S‖_L²(ℝ) = 1.130932...** — la norme L² de la transformée de Fourier inverse de ξ(½+iz).

Le candidat numérologique 2/√π = 1.12838 est éliminé : l'estimateur par projection donne c = 1.13134 à µ = 11, à 4×10⁻⁴ de ‖Φ_S‖ et à 3×10⁻³ de 2/√π.

### 12.3 Résolution de la dérive et scission de la conjecture (1.2)

Le c_a mesuré au §10 (1.217 → 1.145, ajustement c_∞ + 0.32/µ donnant 1.124) était accroché en z = 0, au cœur de l'infrarouge lent : il héritait du résidu de forme local (1.131 × 1.02 ≈ 1.153 à µ = 11 ✓), et le coefficient 0.32 de sa dérive est celui de la loi de forme — une seule loi, deux observables. Deux estimateurs, deux vitesses : le c ponctuel converge en e^(−L), le c par projection L² converge quadratiquement — déficit 1 − recouvrement = 3.6×10⁻⁴, contre la prédiction résidu²/2 = 4.5×10⁻⁴ ✓. La conjecture (1.2) de Suzuki se scinde donc proprement : sa **version L² est vérifiée numériquement à 4×10⁻⁴ dès µ = 11, constante identifiée** ; sa version uniforme est la lente, gouvernée par le bombement infrarouge en e^(−L)/3.

### 12.4 Prédiction sans paramètre pour le scan Dirichlet

Pour chaque caractère χ, la même identification prédit c_∞(χ) = ‖Φ_χ‖_L², norme du noyau thêta de Λ(s, χ) — calculable à l'avance, dépendant de la parité de χ et du conducteur q. Le scan Dirichlet/Siegel devient ainsi simultanément une chasse aux zéros exceptionnels et un test de l'identification sur une famille entière.

## 13. Le scan Dirichlet : identification en famille, signature de parité, loi d'échelle

### 13.1 Construction

Le portage de la machinerie vers L(s, χ) exige une route archimédienne indépendante du (2.32) de Connes-Consani (spécifique à ζ). La représentation de Frullani du digamma la fournit : W_ψ(F; s₀) = −γF(0) − F(0)·log(1−e^(−2L)) + ∫₀^L 2e^(−2s₀y)·(F(0)e^(−(2−2s₀)y) − F(y))/(1−e^(−2y)) dy, avec s₀ = ¼ + a/2 (a = 0 pour χ pair, 1 pour impair), validée sur ζ contre le pipeline certifié à dix chiffres (rapport 1.0 exact). La forme σ_χ = arch − premiers n'a **pas de terme de pôle** (χ non principal), les premiers sont signés par χ(n), et l'intégrale archimédienne est fermée sur [0, L] : l'artefact du cutoff T de Groskin est impossible par construction. Zéros de contrôle récoltés par changements de signe de Λ(½+it, χ) (réalité vérifiée à 10⁻³¹ près), évaluateur L(s,χ) = q^(−s)·Σᵣ χ(r)·ζ(s, r/q). Optimisation décisive : grille en z partagée entre le test de résidu et la transformée de Fourier de Φ_χ (les runs passent de >17 minutes à quelques secondes). Positivité propre partout — confirmation indépendante du diagnostic « artefact T » de Groskin pour ses violations apparentes à c = 23, 29.

### 13.2 La moisson (cinq caractères réels primitifs, trois µ chacun)

| χ | q | parité | γ₁ | pente s(χ) de −ln λ_min = s·µ (deux segments) | C de la loi de forme | c_proj (µ=16) | ‖Φ_χ‖ |
|---|---|---|---|---|---|---|---|
| χ₈ | 8 | pair | 4.90 | 1.47 (1.42/1.52) | 0.53 | 1.28303 | 1.28252 |
| χ₇ | 7 | impair | 4.48 | 1.58 (1.51/1.64) | 0.43 | 1.87629 | 1.87569 |
| χ₅ | 5 | pair | 6.65 | 2.41 (2.40/2.42) | 0.50 | 0.78725 | 0.78699 |
| χ₄ | 4 | impair | 6.02 | 2.94 (2.89/2.98) | 0.39 | 0.81598 | 0.81580 |
| χ₃ | 3 | impair | 8.04 | 4.00 (3.93/4.06) | 0.41 | 0.51558* | 0.51531 |
| ζ | 1 | (pôle) | 14.13 | ≈ 10 (non linéaire : 11.7/9.1) | 0.33 | 1.13134* | 1.13093 |

(* : à µ = 11.)

### 13.3 Résultats

**Identification confirmée six sur six.** Chaque c par projection tombe sur ‖Φ_χ‖ à mieux que 4×10⁻⁴ à µ = 16 (recouvrements ≥ 0.9992 partout, déficits quadratiques au rendez-vous) : c_∞ = ‖Φ‖ n'est pas une propriété de ζ mais de la famille — la prédiction sans paramètre du §12.4 est vérifiée sur cinq conducteurs et deux parités.

**La loi de forme est universelle, sa constante porte la parité.** R ≈ C·e^(−L) tient pour chaque caractère, avec C ≈ 0.50-0.53 (pairs), 0.39-0.43 (impairs), 0.33 (ζ) — le facteur Γ((s+a)/2) bombe l'infrarouge différemment selon la parité.

**La loi d'échelle est linéaire et sa pente est structurée.** −ln λ_min = s(χ)·µ avec une linéarité remarquable (χ₅ : segments 2.40 puis 2.42). La première lecture « l'abîme est une affaire de pôle » (14 ordres de grandeur entre ζ et χ₃ à µ = 5.5) se raffine : s croît avec la largeur γ₁ du désert infrarouge sans zéros — l'abîme se creuse là où une fonction test peut concentrer son spectre sans contrainte, et le pôle de ζ agit en repoussant γ₁ à 14.13. Le candidat numérologique s = γ₁²/(2πe), qui clouait ζ, χ₃ et χ₈, est **falsifié** par le troisième µ de χ₄ (2.94 mesuré contre 2.12 prédit, écart robuste) : la vraie structure est à deux variables, désert *et* parité, les impairs plongeant plus vite que les pairs à γ₁ comparable (χ₄ > χ₅ et χ₇ > χ₈, deux inversions concordantes). La forme exacte de s(γ₁, parité) est la question ouverte du scan ; la peupler (χ₁₁, χ₁₂, χ₁₃, χ₁₅...) est la suite naturelle.

### 13.4 Durcissement

Trois vérifications ont consolidé la moisson. **Formes fermées** : pour χ primitif réel, Φ_χ(u) = 2e^(u/2)·Σχ(n)e^(−πn²e^(2u)/q) (pair) et 2e^(3u/2)·Σχ(n)·n·e^(−πn²e^(2u)/q) (impair) vérifient ∫Φ_χ·e^(izu)du = Λ(½+iz, χ) avec rapport 1.0 plat en z — les normes passent à douze chiffres : ‖Φ₃‖ = 0.515314044, ‖Φ₄‖ = 0.815799088, ‖Φ₅‖ = 0.786984626, ‖Φ₇‖ = 1.875696997, ‖Φ₈‖ = 1.282526197, ‖Φ_S‖ = 1.130932026. La convergence quadratique de c_proj vers ces valeurs exactes est vérifiée (χ₄ : déficits 4.05×10⁻⁴ puis 1.78×10⁻⁴ de µ = 11 à 16, rapport 2.28 contre (16/11)² = 2.12). **Robustesse en base** : à NB apparié (46), les λ_min de Dirichlet bougent de ≤ 2.4% — échelles déjà convergées, pentes χ inchangées (χ₄ : 2.93 ± 0.04 ; χ₈ : 1.47 ± 0.05). **Correction ζ** : à bases appariées, les segments de ζ donnent 11.7 puis 9.1 — l'échelle de ζ n'est pas linéaire sur notre plage et oscille autour du ~10µ asymptotique de Connes-Consani ; la valeur « 11.8 » de la première moisson mélangeait des tailles de base. Les constantes C sont stables en base à ce niveau, avec une dérive en µ de ~5% (valeurs citées à µ = 16 ± 5%).

**Le principe du sismographe est établi.** Un zéro de Landau-Siegel injecterait dans la formule explicite un terme réel de type pôle ; l'observable est désormais concrète : un caractère réel pair dont l'échelle serait anormalement profonde *pour son γ₁ et sa parité* serait le drapeau rouge. La loi s(γ₁, parité) mesurée fournit la ligne de base dont un détecteur a besoin.

### 13.5 Extension du scan : dix fonctions L, un plancher, une anomalie féconde

La famille a été doublée (χ₁₁, χ₁₂, χ₁₃, χ₁₅ ; tables validées par la réalité de Λ sur la droite critique à 10⁻²⁶). Carte complète des pentes, trois µ par caractère (quatre pour χ₁₅ et χ₁₁, jusqu'à µ = 22) :

| χ | q | parité | γ₁ | s(χ) |
|---|---|---|---|---|
| χ₁₅ | 15 | impair | 3.06 | **≈ 0.70** (0.43/0.73/0.69) |
| χ₁₃ | 13 | pair | 3.12 | 0.88 ± 0.06 |
| χ₁₁ | 11 | impair | 2.48 | 0.91 ± 0.08 |
| χ₁₂ | 12 | pair | 3.81 | 0.94 ± 0.05 |
| χ₈ | 8 | pair | 4.90 | 1.47 ± 0.05 |
| χ₇ | 7 | impair | 4.48 | 1.58 ± 0.05 |
| χ₅ | 5 | pair | 6.65 | 2.41 ± 0.04 |
| χ₄ | 4 | impair | 6.02 | 2.93 ± 0.04 |
| χ₃ | 3 | impair | 8.04 | 4.00 ± 0.07 |
| ζ | 1 | (pôle) | 14.13 | ≈ 10, non linéaire |

Trois faits nouveaux. **Le plancher** : aux petits déserts (γ₁ de 2.5 à 3.8), les pentes se tassent vers s ≈ 0.9 indépendamment de la parité ; la croissance nette ne démarre qu'au-delà de γ₁ ≈ 4. **L'anomalie χ₁₅** : sa pente, stabilisée à ≈ 0.70 sur trois segments, viole l'ordre (γ₁, parité) — premier conducteur composé de la famille, il perd les premiers 3 et 5 (et leurs puissances) de la somme arithmétique, précisément les termes de plus fort poids Λ(n)/√n. Hypothèse de troisième variable : la densité de contenu arithmétique effectif dans la fenêtre ; prédiction falsifiable : χ₂₄ (qui élimine 2 et 3) devrait être encore plus plat que sa position (γ₁, parité) ne le suggère. **Le critère de fenêtre** : le noyau thêta de conducteur q a une demi-largeur ≈ ½·ln(3q/π) ; l'identification c = ‖Φ_χ‖ exige L/2 au-delà, ce qui explique la convergence retardée de χ₁₁ et χ₁₃ (écarts de quelques 10⁻³, en décroissance conforme) là où χ₁₂ et χ₁₅ (fenêtre suffisante) tombent à ~5×10⁻⁴ relatif. Bilan identification : **dix fonctions L, normes de 0.515 à 4.592, zéro exception** — pour χ₁₅ à µ = 22, accord à 3.1×10⁻⁴. Le déficit de recouvrement suit (résidu global)²/2, où « global » cesse d'être l'infrarouge quand le désert devient étroit (χ₁₁).

### 13.6 Verdict de l'hypothèse de densité arithmétique : la paire mod 24

Mod 24 vivent deux caractères réels primitifs — χ₂₄ᵒ (impair, discriminant −24) et χ₂₄ᵉ (pair, discriminant +24) — qui tuent tous deux les premiers 2 et 3 : même appauvrissement arithmétique, parités opposées. Mesures sur quatre µ (5.5 à 22, tables validées à 10⁻²⁶) : χ₂₄ᵒ, γ₁ = 1.98, segments de pente 0.17/0.30/0.39 (encore transitoire, s ≲ 0.5) ; χ₂₄ᵉ, γ₁ = 2.69, segments 0.38/0.44/0.49, s ≈ 0.5.

**Le verdict tient en une paire : χ₁₁ contre χ₂₄ᵉ.** Déserts quasi identiques (γ₁ = 2.48 contre 2.69), pentes du simple au double (0.91 contre ≈ 0.49) — la seule différence est le contenu arithmétique de la fenêtre (q = 11 ne retire presque rien ; q = 24 retire 2, 3, 4, 8, 9, 16, les termes de plus fort poids Λ(n)/√n). Le « plancher » du §13.5 était un artefact d'échantillon : s continue de chuter quand la fenêtre s'appauvrit. Mais la paire de contrôle inverse — χ₁₂ contre χ₂₄ᵉ, mêmes premiers tués {2, 3}, γ₁ = 3.81 contre 2.69 — donne 0.94 contre 0.49 : à appauvrissement fixé, γ₁ agit encore, fortement. **Les deux variables sont réelles et irréductibles l'une à l'autre** ; la parité, elle, devient secondaire aux petits déserts (les jumeaux mod 24 sont à ~0.05 l'un de l'autre). L'ordre complet par appauvrissement à petit γ₁ : conducteur premier (s ≈ 0.9) → q = 15, primes 3 et 5 retirés (0.70) → q = 24, primes 2 et 3 retirés (≈ 0.5). Nuance de rigueur : γ₁ n'est pas un bouton indépendant — retirer des premiers déplace aussi les zéros — donc la « loi » finale est vraisemblablement une fonctionnelle unique du contenu de la fenêtre (zéros et premiers ensemble) dont γ₁ et la densité sont deux ombres. Identifications : normes exactes ‖Φ₂₄ᵒ‖ et ‖Φ₂₄ᵉ‖ calculées ; recouvrements 0.998-0.999 en montée, convergence limitée par la largeur de noyau ½ln(3q/π) = 1.57 ≈ L/2 à µ = 22 (il faudra µ ≳ 30 pour l'accord fin).

### 13.7 Session de régression : la loi à une variable et son test hors échantillon

Sur les onze caractères, régressions emboîtées (cible ln s) : γ₁ seul laisse 20% de dispersion ; ajouter la masse arithmétique retirée D = Σ_{p|q} log p/(√p−1) la ramène à 15% (coefficient −0.17, réel) ; ajouter la parité la divise encore (9.4%, bonus impair +23%). Le collapse à une variable X = γ₁·e^(−0.125·D) donne ln s = 1.36·ln X − 1.34 (dispersion 15%, LOO médiane 19%, pire cas χ₁₁ à +36%). Trois prédictions préenregistrées pour χ₁₉ (conducteur premier, D = 0.876, impair) avant sa mesure : collapse ≈ 0.39-0.44 à γ₁ ∈ [1.5, 1.6] ; γ₁ seul ≈ 0.28 ; hypothèse verbale « fenêtre riche » ≈ 0.9.

**Mesure : γ₁(χ₁₉) = 1.516 (record de désert étroit) et s ≈ 0.55-0.6** (segments 0.31/0.50/0.54, encore en montée à µ = 22). Verdict : l'hypothèse « conducteur premier reste à 0.9 » est morte — le désert écrase la pente quelle que soit la richesse de la fenêtre ; γ₁ seul est mort aussi (facteur 2 d'erreur) ; le collapse est directionnellement validé mais sous-prédit de ~40% au plus petit γ₁ jamais mesuré — avec le modèle M2 complet (parité incluse) qui prédit 0.42, encore ~30% sous la mesure. Refit à douze points : θ glisse à 0.175 et l'exposant à 1.24 — le nouveau point tire les paramètres, signe d'une loi non stabilisée.

Caveat structurel découvert en chemin : **le temps de linéarisation croît quand le désert se rétrécit** — toutes les échelles à γ₁ < 3 sont encore transitoires à µ = 22 (pentes croissantes), donc leurs s mesurés sont des bornes inférieures ; le biais tire le bas de la carte vers le bas et pourrait expliquer la sous-prédiction du collapse. Trancher demande des µ ≳ 30-40 sur les petits déserts. Identification au passage : ‖Φ₁₉‖ exact = 2.88964, c_proj(µ=22) = 2.89674 (2.5×10⁻³, fenêtre juste suffisante, en convergence) — **treize fonctions L, zéro exception**.

État de la loi : s = f(γ₁, D, parité) avec f ≈ 0.21·γ₁^1.40·e^(−0.15D)·1.26^[impair] à ~10-15% près, transitoires non corrigés. C'est une loi phénoménologique honnête, pas encore une loi propre — la variable unique reste à trouver, et le premier suspect est maintenant le biais transitoire.

### 13.8 Campagne anti-transitoire : la carte corrigée change de visage

Cinq caractères à petit désert poussés à µ = 30 et 38 (bases 57 et 63, factorisation étendue aux premiers ≤ 37 — la liste codée en dur s'arrêtait à 23 et aurait silencieusement omis 29, 31, 37 : artefact de troncature attrapé avant de mordre). Pentes asymptotiques :

| χ | γ₁ | D | s avant (µ≤22) | s corrigé (µ=38) | état |
|---|---|---|---|---|---|
| χ₁₉ | 1.52 | 0.88 | ~0.55 | **0.58 ± 0.03** | convergé (0.60/0.57) |
| χ₂₄ᵒ | 1.98 | 3.17 | ~0.45 | **0.46 ± 0.02** | convergé (0.47/0.46) |
| χ₂₄ᵉ | 2.69 | 3.17 | ~0.50 | **0.50 ± 0.03** | convergé (0.47/0.52) |
| χ₁₅ | 3.06 | 2.80 | 0.70 | **≥ 0.80, croît** (0.76/0.80) | non convergé |
| χ₁₁ | 2.48 | 1.03 | 0.91 | **≈ 1.07** (1.05/1.09) | quasi convergé |

Deux découvertes structurelles. **Un** : les corrections transitoires ne sont pas uniformes — les points à fort appauvrissement (mod 24) avaient déjà convergé et restent bas, tandis que les points à fenêtre riche grimpent longtemps et haut (χ₁₁ : +18%). Résultat net : le contraste de densité **s'accentue** après correction — la paire décisive χ₁₁/χ₂₄ᵉ passe d'un rapport 1.8 à un rapport 2.1 à γ₁ quasi égal. L'hypothèse de densité arithmétique sort renforcée de la campagne qui devait la mettre à l'épreuve. **Deux** : le biais frappe toute la carte — la plupart des neuf premiers caractères ont été mesurés à µ ≤ 16-22 avec des segments encore croissants (χ₁₂ : 0.89/0.99 ; χ₁₃ : 0.83/0.94 ; χ₄ : 2.89/2.98...) ; leurs s sont donc aussi des bornes inférieures, de +5 à +18%. Le refit de la loi est **suspendu** jusqu'à l'uniformisation de la carte à µ = 38 (sept caractères restants), sous peine de mélanger valeurs corrigées et biaisées.

Sous-produit : les identifications se resserrent partout avec la fenêtre — χ₁₅ à **1.2×10⁻⁴** de sa norme exacte, χ₂₄ᵉ à 2.8×10⁻⁴, χ₂₄ᵒ à 1.1×10⁻³, χ₁₁ à 6.9×10⁻⁴, χ₁₉ à 2.1×10⁻³ (record de famille : 1.2×10⁻⁴).

### 13.9 Carte uniformisée et loi consolidée

L'uniformisation des sept caractères restants à µ = 30-38 a livré la carte finale, avec au passage un **septième artefact** pour la taxonomie : la demande en base croît avec la profondeur de l'échelle — à µ = 38, χ₃ en base 63 rendait λ_min 200 fois trop grand (1.8×10⁻⁶⁰ contre 8.8×10⁻⁶³ en base 75), créant une fausse courbure descendante (segment 3.35 → 4.02 une fois la base élargie). Ceci jette rétroactivement le doute sur la « non-linéarité » de ζ (11.7/9.1), mesurée aux mêmes tailles de base : à retester en base ~75 avant de la citer.

Pentes asymptotiques finales (corrections de +2.5% à +18% sur les valeurs µ ≤ 22) : χ₂₄ᵒ 0.46, χ₂₄ᵉ 0.50, χ₁₉ 0.58, χ₁₅ ≥ 0.82 (seul non convergé), χ₁₃ 0.95, χ₁₂ 1.01, χ₁₁ 1.07, χ₈ 1.53, χ₇ 1.70, χ₅ 2.47, χ₄ 3.04, χ₃ 4.00 ± 0.10.

Refit sur la carte propre : γ₁ seul laisse 26% de dispersion ; les trois variables la ramènent à **9.7%** (LOO médiane 12.4%) :

**s ≈ 0.29 · γ₁^1.28 · e^(−0.20·D) · 1.31^[impair]**

Les deux effets que la campagne devait éprouver en sortent **renforcés** : le coefficient de densité passe de −0.17 à −0.20, le bonus de parité de +23% à +31%. Structure résiduelle restante (χ₁₂ +20%, χ₇ −16%, χ₄ +14%) : soit une quatrième variable, soit la définition trop fruste de D (masse retirée totale, aveugle à la position des premiers retirés). Sous-produit : l'identification c = ‖Φ‖ atteint des accords de quelques 10⁻⁵ sur la moitié de la famille (χ₄ : 3.4×10⁻⁵ ; χ₇ : 4.3×10⁻⁵ ; χ₈ : 5.8×10⁻⁵ ; χ₁₂ : 8×10⁻⁵ ; χ₃ : 3.7×10⁻⁵) — treize fonctions L, et l'accord se resserre avec chaque agrandissement de fenêtre, comme une identification vraie le doit.

## Références

Sur les gouttelettes marcheuses : Y. Couder, S. Protière, E. Fort, A. Boudaoud, *Nature* 437, 208 (2005) ; E. Fort et al., *PNAS* 107, 17515 (2010) ; J. W. M. Bush, « Pilot-wave hydrodynamics », *Annu. Rev. Fluid Mech.* 47, 269 (2015) ; A. Andersen, J. Madsen, C. Reichelt, S. Rosenlund Ahl, B. Lautrup, C. Ellegaard, M. T. Levinsen, T. Bohr, « Double-slit experiment with single wave-driven particles », *Phys. Rev. E* 92, 013006 (2015).

Sur les zéros de zêta et les matrices aléatoires : H. L. Montgomery, « The pair correlation of zeros of the zeta function », *Proc. Symp. Pure Math.* 24 (1973) ; A. M. Odlyzko, « The 10²⁰-th zero of the Riemann zeta function and 175 million of its neighbors » (1992) ; M. V. Berry, J. P. Keating, « H = xp and the Riemann zeros », et « The Riemann zeros and eigenvalue asymptotics », *SIAM Review* 41, 236 (1999) ; M. C. Gutzwiller, « Periodic orbits and classical quantization conditions », *J. Math. Phys.* 12, 343 (1971).

Sur la positivité et la formule explicite : A. Weil, « Sur les "formules explicites" de la théorie des nombres premiers », *Comm. Sém. Math. Lund* (1952) ; H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloquium Publ. 53 (2004), théorème 5.12.

Sur les programmes géométriques : A. Connes, « Trace formula in noncommutative geometry and the zeros of the Riemann zeta function », *Selecta Math.* 5, 29 (1999) ; A. Connes, C. Consani, « The Arithmetic Site », *C. R. Acad. Sci.* (2014) et travaux ultérieurs ; C. Deninger, « Some analogies between number theory and dynamical systems on foliated spaces », *Doc. Math.* ICM (1998) ; C. Soulé, « Les variétés sur le corps à un élément », *Mosc. Math. J.* 4 (2004) ; J. Borger, « Λ-rings and the field with one element » (2009) ; O. Lorscheid, « F₁ for everyone », *Jahresber. Dtsch. Math.-Ver.* (2018) ; P. Deligne, « La conjecture de Weil. I », *Publ. Math. IHÉS* 43 (1974).

Sur le gaz de Riemann et Bost-Connes : B. Julia, « Statistical theory of numbers », in *Number Theory and Physics* (1990) ; J.-B. Bost, A. Connes, « Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory », *Selecta Math.* 1, 411 (1995).

Sur les sommes partielles de zêta : H. L. Montgomery, « Zeros of approximations to the zeta function », in *Studies in Pure Mathematics: To the Memory of Paul Turán* (1983) ; H. L. Montgomery, S. M. Gonek sur les sommes partielles ; P. Turán, « On some approximative Dirichlet-polynomials in the theory of the zeta-function of Riemann » (1948).

Classiques : B. Riemann, « Über die Anzahl der Primzahlen unter einer gegebenen Grösse » (1859) ; F. Mertens (1874) ; théorème des restes chinois et factorisation par roue : voir Crandall & Pomerance, *Prime Numbers: A Computational Perspective*, Springer (2005).

Ajouts v2 (vérifiés en ligne pendant l'exploration) : A. Connes, C. Consani, « Spectral triples and ζ-cycles », *L'Enseignement Mathématique* 69 (2023), arXiv:2106.01715 ; A. Connes, C. Consani, « Weil positivity and trace formula, the archimedean place », *Selecta Math.* 27 (2021), arXiv:2006.13771 ; A. Connes, C. Consani, H. Moscovici, « Zeta spectral triples », arXiv:2511.22755 (2025) ; A. Connes, W. van Suijlekom, « Quadratic forms, real zeros and echoes of the spectral action », arXiv:2511.23257 (2025) ; A. Connes, « The Riemann hypothesis: Past, present and a letter through time », arXiv:2602.04022 (2026) ; M. Suzuki, « Weil's quadratic form via the screw function », arXiv:2606.09096 (2026) ; A. Groskin, « High-Precision Approximation of Riemann Zeros via the Truncated Weil Form », arXiv:2605.20224 (2026) ; D. Slepian, H. Pollak, *Bell Syst. Tech. J.* (1961).

*Note : les références de la v1 sont citées de mémoire dans le cadre d'une exploration ; vérifier les détails bibliographiques avant tout usage formel.*

---

## Annexe A — Code complet

Quatre scripts autonomes (Python 3, NumPy, mpmath). Reproduction : exécuter dans l'ordre ; durées indicatives sur machine standard : ~1 min, ~2 min, ~1 min, ~3 min.

### A.1 Campagne 1 — champ de mémoire, émergence des zéros, GUE, convergence (`pipeline.py`)
```python
import numpy as np

# ---------- Etape 1 : crible ----------
def sieve(N):
    s = np.ones(N+1, dtype=bool); s[:2] = False
    for i in range(2, int(N**0.5)+1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]

NMAX = 10**6
primes = sieve(NMAX)
print(f"pi({NMAX}) = {len(primes)}")

# ---------- Etape 2 : le gaz = modes Lambda(n), energies log n ----------
# n = p^k <= NMAX, poids von Mangoldt Lambda = log p
logn_list, lam_list = [], []
for p in primes:
    lp = np.log(p); pk = p
    while pk <= NMAX:
        logn_list.append(np.log(pk)); lam_list.append(lp); pk *= p
logn = np.array(logn_list); lam = np.array(lam_list)
order = np.argsort(logn); logn, lam = logn[order], lam[order]
print(f"modes (p^k) = {len(logn)}")

# ---------- Etape 3 : champ de memoire spectral ----------
# S_N(t) = -sum Lambda(n) w(n) n^{-1/2} cos(t log n),  fenetre Cesaro w = 1 - log n/log N
def field(tgrid, logN):
    m = logn <= logN
    w = lam[m] * (1 - logn[m]/logN) * np.exp(-0.5*logn[m])
    S = np.empty_like(tgrid)
    B = 400
    for i in range(0, len(tgrid), B):
        tc = tgrid[i:i+B]
        S[i:i+B] = -(np.cos(np.outer(tc, logn[m])) @ w)
    return S

# ---------- Etape 4a : le spectre effectif emerge-t-il ? ----------
t = np.arange(0.0, 310.0, 0.02)
S = field(t, np.log(NMAX))

# detection de pics (maxima locaux au-dessus d'un seuil)
def peaks(t, S, tmin=10.0, thr_frac=0.25):
    thr = thr_frac * S[t>tmin].max()
    idx = np.nonzero((S[1:-1] > S[:-2]) & (S[1:-1] > S[2:]) & (S[1:-1] > thr))[0] + 1
    return t[idx][t[idx] > tmin]

pk = peaks(t, S)
true_zeros = np.array([14.134725,21.022040,25.010858,30.424876,32.935062,
                       37.586178,40.918719,43.327073,48.005151,49.773832,
                       52.970321,56.446248,59.347044,60.831779,65.112544])
print("\n15 premiers pics detectes vs zeros de zeta connus :")
for i in range(min(15,len(pk))):
    tz = true_zeros[i] if i < len(true_zeros) else float('nan')
    print(f"  pic {i+1:2d}: {pk[i]:9.4f}   zero: {tz:9.4f}   ecart: {pk[i]-tz:+.4f}")
print(f"\nNombre de pics detectes jusqu'a t=310 : {len(pk)}")
print("Nombre de zeros reels sous 310 (theorie ~ (t/2pi)log(t/2pi e)) :",
      int(310/(2*np.pi)*np.log(310/(2*np.pi*np.e)) + 7/8 + 0.5))

# ---------- Etape 4b : statistique GUE des espacements ----------
# depliage : densite locale (1/2pi) log(gamma/2pi)
g = pk
unf = np.diff(g) * np.log(g[:-1]/(2*np.pi)) / (2*np.pi)
unf = unf[(unf>0)&(unf<3.5)]
hist, edges = np.histogram(unf, bins=np.arange(0,3.2,0.32), density=True)
ctr = 0.5*(edges[:-1]+edges[1:])
wigner_gue = (32/np.pi**2)*ctr**2*np.exp(-4*ctr**2/np.pi)
poisson = np.exp(-ctr)
print("\nEspacements deplies (histogramme) vs GUE vs Poisson :")
for c,h,wg,po in zip(ctr,hist,wigner_gue,poisson):
    print(f"  s={c:.2f}  empirique={h:.3f}  GUE={wg:.3f}  Poisson={po:.3f}")
mse_gue = np.mean((hist-wigner_gue)**2); mse_poi = np.mean((hist-poisson)**2)
print(f"  MSE vs GUE = {mse_gue:.4f} ; MSE vs Poisson = {mse_poi:.4f}")

# ---------- Etape 4c : vitesse de convergence (le mur en 1/log N) ----------
print("\nConvergence du 1er zero avec N :")
tt = np.arange(12.0, 16.0, 0.002)
conv = []
for N in [10**3, 10**4, 10**5, 10**6]:
    SS = field(tt, np.log(N))
    t1 = tt[np.argmax(SS)]
    err = abs(t1 - 14.134725)
    # largeur du pic a mi-hauteur
    half = SS.max()/2
    above = tt[SS > half]
    width = above.max()-above.min() if len(above)>1 else float('nan')
    conv.append((N, t1, err, width))
    print(f"  N=10^{int(np.log10(N))}: pic a {t1:.4f}, erreur {err:.4f}, largeur {width:.3f}, 2pi/logN = {2*np.pi/np.log(N):.3f}")

# ---------- Etape 4d : positivite etage par etage (cote premiers = matrice de Gram) ----------
ts = np.linspace(5, 60, 24)
m = logn <= np.log(NMAX)
w = lam[m]*(1-logn[m]/np.log(NMAX))*np.exp(-0.5*logn[m])
K = np.zeros((len(ts), len(ts)))
for a in range(len(ts)):
    K[a,:] = np.sum(w*np.cos((ts[a]-ts[:,None])*logn[m]), axis=1)
ev = np.linalg.eigvalsh(K)
print(f"\nNoyau cote premiers K(t_j - t_k) : val. propre min = {ev.min():.3e}, max = {ev.max():.3e}")
print("(PSD attendu : c'est une matrice de Gram — le 'carre' existe a chaque etage fini, cote premiers)")

np.save('/home/claude/gas/t.npy', t); np.save('/home/claude/gas/S.npy', S)
np.save('/home/claude/gas/hist.npy', np.vstack([ctr,hist,wigner_gue,poisson]))
np.save('/home/claude/gas/conv.npy', np.array([(np.log(N),err) for N,_,err,_ in conv]))
```

### A.2 Campagne 2 — diagnostic d'aliasing, scan de blancheur, spectre des orbites (`push.py`)
```python
import numpy as np

# recharge des modes
def sieve(N):
    s = np.ones(N+1, dtype=bool); s[:2] = False
    for i in range(2, int(N**0.5)+1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]

NMAX = 10**6
primes = sieve(NMAX)
logn_l, lam_l = [], []
for p in primes:
    lp = np.log(p); pk = p
    while pk <= NMAX:
        logn_l.append(np.log(pk)); lam_l.append(lp); pk *= p
logn = np.array(logn_l); lam = np.array(lam_l)
L = np.log(NMAX)

# ============================================================
# A. Le noyau vu de pres : Toeplitz dense, scan de l'exposant beta
#    c_n = Lambda(n) * n^{-beta}.  Densite spectrale attendue ~ e^{(1-beta)w}
#    -> blancheur (spectre plat) ssi beta = 1  <=>  amplitude de champ n^{-1/2}
# ============================================================
dt = 0.2
tau = np.arange(0, 60.0001, dt)          # 301 valeurs
M = len(tau)
freqs = 2*np.pi*np.fft.rfftfreq(M, d=dt) # frequences des modes propres

print("=== A. Scan de l'exposant : pente de log(lambda) vs omega ===")
print("    (attendu : pente = 1 - beta ; plat <=> beta = 1)")
results_scan = {}
for beta in [0.6, 0.8, 1.0, 1.2]:
    c = lam * np.exp(-beta*logn)          # pas de fenetre : troncature nette
    k = np.array([np.sum(c*np.cos(t*logn)) for t in tau])
    T = k[np.abs(np.subtract.outer(np.arange(M), np.arange(M)))]
    ev, V = np.linalg.eigh(T)
    # frequence dominante de chaque vecteur propre
    om = np.array([freqs[np.argmax(np.abs(np.fft.rfft(V[:,i])))] for i in range(M)])
    ok = (ev > 1e-10) & (om > 1.0) & (om < 10.0)
    A = np.vstack([om[ok], np.ones(ok.sum())]).T
    slope, b0 = np.linalg.lstsq(A, np.log(ev[ok]), rcond=None)[0]
    ipr = np.mean(np.sum(V[:,ok]**4, axis=0))
    results_scan[beta] = (om[ok], np.log(ev[ok]))
    print(f"  beta={beta:.1f} : pente mesuree = {slope:+.3f}  (theorie {1-beta:+.1f})   IPR moyen = {ipr:.4f} (onde plane ~ {1.5/M:.4f})")

# ============================================================
# B. Verdict sur la "platitude" observee hier soir (grille grossiere, pas 2.4)
# ============================================================
print("\n=== B. Diagnostic de la platitude initiale ===")
c = lam * (1-logn/L) * np.exp(-0.5*logn)   # le noyau d'origine (beta=1/2, fenetre Cesaro)
k = np.array([np.sum(c*np.cos(t*logn)) for t in tau])
T = k[np.abs(np.subtract.outer(np.arange(M), np.arange(M)))]
ev, V = np.linalg.eigh(T)
om = np.array([freqs[np.argmax(np.abs(np.fft.rfft(V[:,i])))] for i in range(M)])
lo, hi = ev[om<5], ev[(om>7)&(om<12)]
print(f"  beta=1/2 sur grille DENSE (pas 0.2) : lambda moyen basses freq (w<5) = {lo.mean():.1f}, hautes freq (7<w<12) = {hi.mean():.1f}")
print(f"  ratio hautes/basses = {hi.mean()/lo.mean():.2f}  -> le spectre N'EST PAS plat en realite (croissance ~ e^(w/2))")
print(f"  La platitude d'hier (274-304) venait du pas grossier 2.4 : Nyquist = {np.pi/2.4:.2f} << log N = {L:.1f} -> repliement total")

# ============================================================
# C. Le milieu chante : spectre de puissance du champ S(t) sur t in [0,1200]
#    -> les modes propres du milieu doivent etre les orbites log p
# ============================================================
print("\n=== C. Spectre de puissance du champ de memoire ===")
N2 = 10**5
m = logn <= np.log(N2)
a = lam[m]*(1-logn[m]/np.log(N2))*np.exp(-0.5*logn[m])
w2 = logn[m]
t = np.arange(0, 1200, 0.05)
S = np.empty_like(t)
B = 2000
for i in range(0, len(t), B):
    S[i:i+B] = -(np.cos(np.outer(t[i:i+B], w2)) @ a)
S = S - S.mean()
S = S*np.hanning(len(S))
P = np.abs(np.fft.rfft(S))**2
om2 = 2*np.pi*np.fft.rfftfreq(len(S), d=0.05)
sel = (om2>0.4)&(om2<2.6)
oms, Ps = om2[sel], P[sel]
Ps = Ps/Ps.max()
orb = {'log2':np.log(2),'log3':np.log(3),'log4':np.log(4),'log5':np.log(5),
       'log7':np.log(7),'log8':np.log(8),'log9':np.log(9),'log11':np.log(11),'log13':np.log(13)}
print("  pics attendus aux orbites :")
for name,o in orb.items():
    j = np.argmin(np.abs(oms-o))
    jj = j-40+np.argmax(Ps[max(0,j-40):j+40])
    print(f"   {name} = {o:.4f} : pic mesure a {oms[jj]:.4f}, puissance rel. {Ps[jj]:.3f}")

np.save('scanA.npy', np.array([np.concatenate([results_scan[b][0] for b in [0.6,1.0,1.2]]),
                                np.concatenate([results_scan[b][1] for b in [0.6,1.0,1.2]])]))
ds = slice(None, None, 3)
np.save('powspec.npy', np.vstack([oms[ds], Ps[ds]]))
# series du scan pour graphe
for b in [0.6, 1.0, 1.2]:
    o,lv = results_scan[b]
    idx = np.argsort(o)
    np.save(f'scan_{b}.npy', np.vstack([o[idx], lv[idx]]))
```

### A.3 Campagne 3 — forme de Weil, validation, mode dangereux (`weil.py`)
```python
import numpy as np, mpmath as mp

# ---------- modes du gaz ----------
def sieve(N):
    s = np.ones(N+1, dtype=bool); s[:2] = False
    for i in range(2, int(N**0.5)+1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]
NMAX = 10**6
primes = sieve(NMAX)
logn_l, lam_l = [], []
for p in primes:
    lp = np.log(p); pk = p
    while pk <= NMAX:
        logn_l.append(np.log(pk)); lam_l.append(lp); pk *= p
logn = np.array(logn_l); lam = np.array(lam_l)

# ---------- fonctions test : peignes gaussiens ----------
# f_j(u) = gaussienne centree u_j, largeur s ; g_jk = f_j * f~_k = N(u_j-u_k, 2s^2)
# h_jk(r) = e^{i r (u_j-u_k)} e^{-s^2 r^2}
J, delta, s = 20, 0.5, 0.05
u = np.arange(J)*delta            # u_j dans [0, 9.5]  (< log N = 13.8)
D = np.subtract.outer(u, u)       # Delta_jk

# ---------- cote zeros (verite terrain pour validation) ----------
NZ = 40
zeros = np.array([float(mp.im(mp.zetazero(k))) for k in range(1, NZ+1)])
Wz = np.zeros((J,J))
for g in zeros:
    Wz += 2*np.cos(g*D)*np.exp(-s*s*g*g)

# ---------- cote premiers (formule explicite, AUCUN zero utilise) ----------
# terme du pole : h(i/2)+h(-i/2) = 2 cosh(D/2) e^{s^2/4}
Pole = 2*np.cosh(D/2)*np.exp(s*s/4)
# cote premiers : sum Lambda(n) n^{-1/2} [ g(log n) + g(-log n) ]
sg2 = 2*s*s
def gauss(v): return np.exp(-v*v/(2*sg2))/np.sqrt(2*np.pi*sg2)
w = lam*np.exp(-0.5*logn)
Pr = np.zeros((J,J))
for a in range(J):
    for b in range(J):
        d = D[a,b]
        Pr[a,b] = np.sum(w*(gauss(logn-d)+gauss(logn+d)))
# terme archimedien : (1/2pi) int h(r) Omega(r) dr — variantes calibrees sur Wz
rg = np.arange(0, 80, 0.01)
psi_q = np.array([complex(mp.digamma(0.25+0.5j*r)) for r in rg[::10]])
psi_qr = np.interp(rg, rg[::10], psi_q.real)
psi_h = np.array([complex(mp.digamma(0.5+1j*r)) for r in rg[::10]])
psi_hr = np.interp(rg, rg[::10], psi_h.real)
env = np.exp(-s*s*rg*rg)
variants = {
 'V1: Re psi(1/4+ir/2) - log pi'      : psi_qr - np.log(np.pi),
 'V2: (1/2)Re psi(1/4+ir/2) - (1/2)log pi' : 0.5*psi_qr - 0.5*np.log(np.pi),
 'V3: Re psi(1/2+ir) - log pi'        : psi_hr - np.log(np.pi),
}
print("Calibration du terme archimedien contre le cote zeros :")
best = None
for name, Om in variants.items():
    Ar = np.zeros((J,J))
    integ = env*Om
    for a in range(J):
        for b in range(J):
            Ar[a,b] = (1/np.pi)*np.trapezoid(np.cos(rg*D[a,b])*integ, rg)  # 2x demi-axe /2pi
    Wp = Pole + Ar - Pr
    res = np.linalg.norm(Wp-Wz)/np.linalg.norm(Wz)
    print(f"  {name}: residu relatif ||Wp-Wz||/||Wz|| = {res:.4f}")
    if best is None or res < best[1]: best = (name, res, Wp)

name, res, Wp = best
print(f"\nVariante retenue : {name} (residu {res:.4f})")
print("Controle entree par entree (diag et coin) :")
print("  Wp[0,0]={:.4f}  Wz[0,0]={:.4f}".format(Wp[0,0], Wz[0,0]))
print("  Wp[0,10]={:.4f} Wz[0,10]={:.4f}".format(Wp[0,10], Wz[0,10]))
print("  Wp[5,15]={:.4f} Wz[5,15]={:.4f}".format(Wp[5,15], Wz[5,15]))

# ---------- le mode dangereux ----------
Wp = 0.5*(Wp+Wp.T)
ev, V = np.linalg.eigh(Wp)
print(f"\nSpectre de la forme de Weil (cote premiers) : min = {ev[0]:.5f}, 2e = {ev[1]:.5f}, max = {ev[-1]:.2f}")
evz, Vz = np.linalg.eigh(0.5*(Wz+Wz.T))
print(f"Spectre cote zeros (reference)              : min = {evz[0]:.5f}, 2e = {evz[1]:.5f}, max = {evz[-1]:.2f}")
c = V[:,0]; c = c/np.max(np.abs(c))
print("\nMode dangereux (coefficients c_j sur les positions u_j) :")
print('  u_j :', ' '.join(f'{x:5.2f}' for x in u))
print('  c_j :', ' '.join(f'{x:+5.2f}' for x in c))

# profil spectral du mode : F(gamma) = |sum c_j e^{i gamma u_j}|^2 e^{-s^2 g^2}
gg = np.arange(0, 62, 0.05)
F = np.abs(np.exp(1j*np.outer(gg,u)) @ V[:,0])**2 * np.exp(-s*s*gg*gg)
F = F/F.max()
# et pour comparaison le profil d'un mode "moyen" (mediane du spectre)
Fm = np.abs(np.exp(1j*np.outer(gg,u)) @ V[:,J//2])**2 * np.exp(-s*s*gg*gg)
Fm = Fm/Fm.max()
np.save('mode.npy', np.vstack([gg, F, Fm]))
np.save('modecoef.npy', np.vstack([u, c]))
print("\nValeur de F(gamma) du mode dangereux aux 10 premiers zeros :")
for g in zeros[:10]:
    print(f"  gamma={g:8.4f}  F={F[np.argmin(np.abs(gg-g))]:.4f}")
print(f"Moyenne de F sur tout [10,60] : {F[(gg>10)&(gg<60)].mean():.4f}")
```

### A.4 Campagne 4 — fermeture de la marge, frontière de certification (`margin.py`)
```python
import numpy as np, mpmath as mp

# ---------- gaz pousse a N=10^7 pour abaisser le plancher de bruit ----------
def sieve(N):
    s = np.ones(N+1, dtype=bool); s[:2] = False
    for i in range(2, int(N**0.5)+1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]
NMAX = 10**7
primes = sieve(NMAX)
logn_l, lam_l = [], []
for p in primes:
    lp = np.log(p); pk = p
    while pk <= NMAX:
        logn_l.append(np.log(pk)); lam_l.append(lp); pk *= p
logn = np.array(logn_l); lam = np.array(lam_l)
o = np.argsort(logn); logn, lam = logn[o], lam[o]
wgt = lam*np.exp(-0.5*logn)
print(f"N = 10^7, pi(N) = {len(primes)}, modes = {len(logn)}, log N = {np.log(NMAX):.2f}")

s = 0.05
sg2 = 2*s*s
# ---------- table des ingredients sur Delta = 0 .. 13 pas 0.5 ----------
Dg = np.arange(0, 13.01, 0.5)
Prt = np.zeros(len(Dg))
for i,d in enumerate(Dg):
    a,b = np.searchsorted(logn, [d-0.45, d+0.45])
    v = logn[a:b]-d
    Prt[i] = np.sum(wgt[a:b]*np.exp(-v*v/(2*sg2)))/np.sqrt(2*np.pi*sg2)
Polet = 2*np.cosh(Dg/2)*np.exp(s*s/4)
rg = np.arange(0, 80, 0.01)
ps = np.array([complex(mp.digamma(0.25+0.5j*r)) for r in rg[::10]])
Om = np.interp(rg, rg[::10], ps.real) - np.log(np.pi)
env = np.exp(-s*s*rg*rg)*Om
Archt = np.array([(1/np.pi)*np.trapezoid(np.cos(rg*d)*env, rg) for d in Dg])
Wfun_p = Polet + Archt - Prt        # cote premiers
NZ = 40
zeros = np.array([float(mp.im(mp.zetazero(k))) for k in range(1, NZ+1)])
Wfun_z = np.array([np.sum(2*np.cos(zeros*d)*np.exp(-s*s*zeros*zeros)) for d in Dg])
print("Ecart premiers/zeros sur la table :", np.max(np.abs(Wfun_p-Wfun_z)))

# ---------- marge en fonction de la fenetre U ----------
print("\n   J     U     marge (zeros exacts)   marge (premiers 10^7)")
res = []
for J in range(6, 27, 2):
    idx = np.abs(np.subtract.outer(np.arange(J), np.arange(J)))
    Wz = Wfun_z[idx]; Wp = Wfun_p[idx]
    ez = np.linalg.eigvalsh(0.5*(Wz+Wz.T))[0]
    ep = np.linalg.eigvalsh(0.5*(Wp+Wp.T))[0]
    U = (J-1)*0.5
    res.append((U, ez, ep))
    print(f"  {J:3d}  {U:5.1f}   {ez:.6e}          {ep:.6e}")

res = np.array(res)
# ajustement exponentiel sur la partie propre (marge zeros > 1e-12)
m = res[:,1] > 1e-12
A = np.vstack([res[m,0], np.ones(m.sum())]).T
sl, b0 = np.linalg.lstsq(A, np.log(res[m,1]), rcond=None)[0]
print(f"\nAjustement marge_zeros ~ e^(-alpha U) : alpha = {-sl:.3f}  (r = {np.corrcoef(res[m,0], np.log(res[m,1]))[0,1]:.4f})")
print(f"Reperes : gamma_1/(2pi) = {zeros[0]/(2*np.pi):.3f} ; gamma_1/2pi*ln(..)?  slope/gamma1 = {-sl/zeros[0]:.4f}")
np.save('margin.npy', res)
```

### A.5 Test de robustesse — dépendance de α à la densité du peigne
```python
import numpy as np, mpmath as mp
zeros = np.array([float(mp.im(mp.zetazero(k))) for k in range(1, 41)])
s = 0.05
for delta, Jmax in [(0.25, 42), (0.5, 26), (0.75, 18)]:
    out = []
    for J in range(6, Jmax+1, 2):
        Dg = np.abs(np.subtract.outer(np.arange(J), np.arange(J)))*delta
        Wz = np.sum(2*np.cos(np.multiply.outer(zeros, Dg))
                    *np.exp(-s*s*zeros*zeros)[:,None,None], axis=0)
        e = np.linalg.eigvalsh(0.5*(Wz+Wz.T))[0]
        if e > 1e-12: out.append(((J-1)*delta, e))
    out = np.array(out); m = out[:,0] > 2.0
    A = np.vstack([out[m,0], np.ones(m.sum())]).T
    sl, b0 = np.linalg.lstsq(A, np.log(out[m,1]), rcond=None)[0]
    print(f'delta={delta:.2f} : alpha = {-sl:.3f}')
# Sortie : delta=0.25 -> alpha=1.688 ; delta=0.50 -> 0.834 ; delta=0.75 -> 0.633
# alpha*delta ~ 0.42-0.47 : la marge se ferme en e^(-0.43 J), par degré de liberté.
```

---

## Annexe B — Journal des étapes de l'exploration

L'ordre réel du raisonnement, tel qu'il s'est déroulé, chaque étape motivant la suivante : (1) intuition du crible comme empilement de dimensions, formalisée par les restes chinois et corrigée quantitativement (π(√p_n) dimensions et non n−1) ; (2) croissance calculable à l'avance du nombre de dimensions ; (3) question des dimensions sous-jacentes → zéros de zêta comme fréquences duales, Montgomery-Dyson, Hilbert-Pólya ; (4) analogie des gouttelettes marcheuses, avec la réserve d'honnêteté sur les fentes de Young ; (5) clarification projection/hologramme : oscillation lisse en haute dimension, ombre imprévisible en basse dimension ; (6) question du milieu vibrant, et critère de l'éther — un milieu n'apporte quelque chose que s'il a une dynamique propre ; (7) portrait-robot : flot de dilatations, GUE, orbites log p, confinement manquant ; (8) le tore modulaire comme paroi candidate ; (9) objection du bain — l'espace ne grandit pas, il se remplit — et distinction entre mémoire qui influence et mémoire qui dicte ; (10) le spectre n'existe qu'à la limite : émergence forte, analogie avec les transitions de phase ; (11) l'univers Weil-Deligne où tout est démontré, F₁, Deninger ; (12) transposition de la positivité : énergie du bain ↔ Castelnuovo ↔ forme de Weil — trouver le milieu et prouver la positivité sont le même acte ; (13) trois stratégies « à la Couder » : gaz critique, simulation phénoménologique, milieux ratés instructifs ; (14) analyse de complexité : calcul linéaire, mur en 1/log N, coût dominant = le temps d'avoir la bonne idée d'observable ; (15) à (18) : les quatre campagnes numériques du §4, chacune décidée au vu des résultats de la précédente — y compris une erreur d'échantillonnage détectée et corrigée en cours de route (aliasing, §4.2).

## Annexe C — Statut épistémique des affirmations

Trois registres à ne pas confondre. **Établi (littérature)** : formule explicite, critère de positivité de Weil, statistique GUE des zéros (vérifications numériques massives d'Odlyzko), théorème de Mertens, RH sur corps finis (Weil, Deligne), zéros hors-ligne des sommes partielles de zêta (Turán, Montgomery), système de Bost-Connes. **Mesuré ici (reproductible, code en annexe A)** : les nombres des tableaux du §4 — émergence des ombres des zéros (143/144, ±0.01), MSE GUE 0.0017 contre 0.154 pour Poisson, largeurs de pics en 2π/log N, sélection de β = 1 par blancheur spectrale, validation à 0.12% de la formule explicite côté premiers, structure du mode dangereux (impair, anti-accordé, réfugié sous γ₁), taux de fermeture α·δ ≈ 0.43 par degré de liberté, violation effective de la positivité par le milieu tronqué au-delà de U ≈ 0.65·log N. **Spéculatif (heuristique de recherche)** : l'existence même d'un milieu, l'identification du tore adélique comme paroi, la lecture de « blancheur ⟺ droite critique » comme mécanisme plutôt que reformulation, et l'ensemble de l'analogie hydrodynamique. Ce document n'établit aucun résultat nouveau en théorie des nombres ; il documente une démarche d'exploration et les observables qui pourraient la prolonger.

## Annexe D — Code de la phase 2 (v2)

### D.1 Cache des zéros de zêta (`zeros_cache.py`)
```python
import mpmath as mp, pickle, time
K = 280
t0 = time.time()
zeros = []
for k in range(1, K+1):
    zeros.append(float(mp.im(mp.zetazero(k))))
    if k % 40 == 0:
        print(f"  {k}/{K} zeros, gamma_{k} = {zeros[-1]:.2f}, t = {time.time()-t0:.0f}s", flush=True)
pickle.dump(zeros, open('zeros280.pkl','wb'))
print(f"OK: {K} zeros jusqu'a gamma = {zeros[-1]:.2f} en {time.time()-t0:.0f}s")
```

### D.2 Raccordement : pente α(s) et plongeon à support fixé (`raccord.py`)
```python
import numpy as np, pickle
zeros = np.array(pickle.load(open('zeros280.pkl','rb')))

def kernel_vals(Deltas, s):
    w = np.exp(-s*s*zeros*zeros)
    m = w > 1e-18
    return np.array([np.sum(2*np.cos(zeros[m]*d)*w[m]) for d in Deltas]), int(m.sum())

def margin(J, delta, s):
    Dg = np.arange(J)*delta
    kv, neff = kernel_vals(Dg, s)
    W = kv[np.abs(np.subtract.outer(np.arange(J), np.arange(J)))]
    ev = np.linalg.eigvalsh(0.5*(W+W.T))
    return ev[0], ev[-1], kv[0], neff   # marge, max, diagonale, zeros effectifs

# ============================================================
# A. Pente alpha(s) : la fermeture s'accelere-t-elle quand la bande s'ouvre ?
# ============================================================
print("=== A. Pente de fermeture alpha(s), peigne delta = 0.5 ===")
for s in [0.05, 0.025, 0.0125]:
    pts = []
    for J in range(6, 27, 2):
        e0, emax, diag, neff = margin(J, 0.5, s)
        U = (J-1)*0.5
        if e0 > 1e-12*emax:            # au-dessus du plancher float64
            pts.append((U, e0/diag))    # marge normalisee par la diagonale
    pts = np.array(pts)
    A = np.vstack([pts[:,0], np.ones(len(pts))]).T
    sl, b0 = np.linalg.lstsq(A, np.log(pts[:,1]), rcond=None)[0]
    print(f"  s = {s:7.4f} : bande utile gamma < {np.sqrt(np.log(1e18))/s:6.0f} ({neff:3d} zeros), "
          f"alpha = {-sl:.3f}, points propres = {len(pts)}, marge norm. finale = {pts[-1,1]:.3e} a U = {pts[-1,0]}")

# ============================================================
# B. Le plongeon a support fixe U = 2.5 : (s, delta) -> 0
#    Reference CC (base complete, pas de bande) : ~2.4e-48 a U = log 11 = 2.40
# ============================================================
print("\n=== B. Plongeon a U = 2.5 fixe : marge normalisee (marge brute) ===")
print("      float64 ; * = sous le plancher 1e-13*max (non fiable)")
hdr = "  s \\ delta |" + "".join(f"   {d:7.4f}   " for d in [0.5, 0.25, 0.125, 0.0625])
print(hdr)
results = {}
for s in [0.05, 0.025, 0.0125]:
    row = f"  {s:8.4f} |"
    for delta in [0.5, 0.25, 0.125, 0.0625]:
        J = int(round(2.5/delta)) + 1
        e0, emax, diag, neff = margin(J, delta, s)
        flag = "*" if e0 < 1e-13*emax else " "
        results[(s,delta)] = (e0, diag)
        row += f" {e0/diag:9.2e}{flag}  "
    print(row)
print(f"\n  (JJ aux quatre deltas : {[int(round(2.5/d))+1 for d in [0.5,0.25,0.125,0.0625]]})")
print("  Reference Connes-Consani, meme support, base complete, sans bande : ~2.4e-48")
```

### D.3 Plongeon jusqu'au mur de rang et vérification multiprécision (`plunge.py`)
```python
import numpy as np, pickle, mpmath as mp, time
zeros = np.array(pickle.load(open('zeros280.pkl','rb')))
s = 0.05
w = np.exp(-s*s*zeros*zeros); m = w > 1e-18
zz, ww = zeros[m], w[m]
print(f"Bande s=0.05 : {m.sum()} zeros effectifs -> rang max du noyau = {2*m.sum()} (cos+sin par zero)")

# ---- taux par degre de liberte a U=2.5 fixe, jusqu'au mur de rang ----
print("\nU = 2.5 fixe, on densifie le peigne (float64) :")
prev = None
for J in [6, 11, 21, 41, 51, 61, 71, 81, 86, 91]:
    delta = 2.5/(J-1)
    Dg = np.arange(J)*delta
    kv = np.array([np.sum(2*np.cos(zz*d)*ww) for d in Dg])
    W = kv[np.abs(np.subtract.outer(np.arange(J), np.arange(J)))]
    ev = np.linalg.eigvalsh(0.5*(W+W.T))
    e0, diag = ev[0], kv[0]
    rate = ""
    if prev is not None and e0 > 1e-16*ev[-1] and prev[1] > 0:
        rate = f"   taux/dim = {np.log(prev[1]/(e0/diag))/(J-prev[0]):.3f}"
    flag = " (plancher float64)" if e0 < 1e-13*ev[-1] else ""
    print(f"  J = {J:3d} : marge/diag = {e0/diag:10.3e}{flag}{rate}")
    prev = (J, e0/diag if e0 > 0 else prev[1] if prev else 1)

# ---- plongee multiprecision sur la cellule la plus profonde fiable+1 ----
print("\nVerification multiprecision (dps = 50), J = 61 :")
mp.mp.dps = 50
t0 = time.time()
J = 61; delta = 2.5/(J-1)
zzm = [mp.mpf(g) for g in zz]
kv = []
for j in range(J):
    d = mp.mpf(j)*mp.mpf(delta)
    kv.append(sum(2*mp.cos(g*d)*mp.exp(-mp.mpf(s)**2*g*g) for g in zzm))
M = mp.matrix(J, J)
for a in range(J):
    for b in range(J):
        M[a,b] = kv[abs(a-b)]
E = mp.eigsy(M, eigvals_only=True)
print(f"  marge mp = {mp.nstr(E[0], 6)} ; marge/diag = {mp.nstr(E[0]/kv[0], 6)}")
print(f"  (float64 au meme point : voir ci-dessus ; temps mp = {time.time()-t0:.0f}s)")
```

### D.4 Débogage de l'archimédien par identités fermées (`debug_weil.py`)
```python
import mpmath as mp, pickle
import numpy as np
mp.mp.dps = 30

mu = mp.mpf('5.5'); L = mp.log(mu); Lf = float(L)
print(f"mu=5.5, L={Lf:.6f}")

# ---------------- Entree (0,0) : F(y) = 2(L-y)/L ----------------
# 1) POLE : verif forme fermee 32 sinh^2(L/4)/L
W02_num = mp.quad(lambda y: 2*(L-y)/L*(mp.e**(y/2)+mp.e**(-y/2)), [0, L])
W02_cf  = 32*mp.sinh(L/4)**2/L
print(f"\nPOLE  : numerique = {mp.nstr(W02_num,8)}  forme fermee = {mp.nstr(W02_cf,8)}  -> {'OK' if abs(W02_num-W02_cf)<1e-10 else 'ECART'}")

# 2) ARCHIMEDIEN : (2.32) vs Q_infini de (2.11) = int |f^(t)|^2 (2 theta'(t)/2pi) dt
CR = mp.euler + mp.log(4*mp.pi*(mp.e**L-1)/(mp.e**L+1))
WR_232 = mp.mpf(2)/2*CR + mp.quad(lambda y: mp.e**(y/2)*(2*(L-y)/L-2)/(mp.e**y-mp.e**(-y)), [0, L])
# Q_infini : f^(t) = L^{-1/2} 2 sin(tL/2)/t ; 2theta'(t)/2pi = (Re psi(1/4+it/2) - log pi)/(2pi)... 
# theta(t) = -t/2 log pi + Im logGamma(1/4+it/2) ; theta'(t) = -log(pi)/2 + Re psi(1/4+it/2)/2
def integrand(t):
    fh2 = (2*mp.sin(t*L/2)/t)**2/L if abs(t)>1e-12 else L
    thp = -mp.log(mp.pi)/2 + mp.re(mp.digamma(mp.mpf('0.25')+0.5j*t))/2
    return fh2*2*thp/(2*mp.pi)
Qinf = 2*mp.quad(integrand, [0, 5, 20, 100, 500, 2000])   # pair -> 2x demi-axe
# queue analytique : theta' ~ (1/2)log(t/4pi... approx (1/2)log(t/2pi)) ; |fh|^2 moy = 2/(L t^2)
T = 2000
tail = 2*mp.quad(lambda t: (2/(L*t*t))*2*((mp.log(t/(2*mp.pi))/2))/(2*mp.pi), [T, mp.inf])
print(f"ARCH  : WR(2.32) = {mp.nstr(WR_232,8)}")
print(f"        -W_R attendu = +Q_inf   ->  Q_inf = {mp.nstr(Qinf,6)} (+ queue ~ {mp.nstr(tail,3)})")
print(f"        donc WR devrait valoir  -Q_inf = {mp.nstr(-Qinf-tail,6)}")

# 3) PREMIERS
pp = [(2,2),(3,3),(4,2),(5,5)]
Wp = mp.fsum(mp.log(p)/mp.sqrt(n)*2*(L-mp.log(n))/L for n,p in pp)
print(f"PRIME : Wp = {mp.nstr(Wp,8)}")

sigma00 = W02_cf - WR_232 - Wp
print(f"\nsigma(0,0) via (2.32) = {mp.nstr(sigma00,6)}")
sigma00b = W02_cf + Qinf + tail - Wp
print(f"sigma(0,0) via Q_inf  = {mp.nstr(sigma00b,6)}")

# 4) COTE ZEROS avec facteur correct : somme sur rho = paires +-gamma
#    Q(eta0) = sum_rho h^(gamma_rho) = sum_{gamma>0} 2 * [2 int_0^L F cos(gamma y) dy]
zeros = pickle.load(open('zeros280.pkl','rb'))
zs = 0.0
for g in zeros:
    # F^ pour F=2(L-y)/L : 2*(2/L)*(1-cos(gL))/g^2
    zs += 2*(4/Lf)*(1-np.cos(g*Lf))/g**2
# queue au-dela de gamma_280 ~ 513.7 : densite dN = log(t/2pi)/(2pi) dt, moyenne (1-cos)=1
gmax = zeros[-1]
tailz = float(2*mp.quad(lambda t: (4/L)/t**2*mp.log(t/(2*mp.pi))/(2*mp.pi), [gmax, mp.inf]))
print(f"\nZEROS : somme 280 zeros = {zs:.6f} + queue ~ {tailz:.6f}  ->  {zs+tailz:.6f}")
```

### D.5 Test de forme de Suzuki (1.2), version finale (`shape7.py`)
Usage : `python3 shape7.py <mu> <NB> <dps> <DEG>`. Exemples du §10 : `5.5 20 55 14`, `11 46 85 16`, `16 52 115 16`.
```python
import mpmath as mp, pickle, time, sys
import numpy as np


EU = mp.euler

def run(mu, NB, NPANEL, DEG):
    t0 = time.time()
    L = mp.log(mu)
    om = [2*mp.pi*n/L for n in range(NB+1)]

    # ---- quadrature composite Gauss-Legendre precalculee sur [0,L] ----
    xs, ws = mp.polyroots([mp.legendre(DEG, mp.mpf(0)).__class__ and 0] ) if False else (None,None)
    # noeuds GL de reference via mpmath
    ref = mp.taylor(lambda x: mp.legendre(DEG, x), 0, DEG)
    import numpy.polynomial.legendre as NL
    xr0, _ = NL.leggauss(DEG)
    xr, wr = [], []
    for x0 in xr0:                                # raffinage Newton en mp
        x = mp.mpf(float(x0))
        for _ in range(6):
            P  = mp.legendre(DEG, x); Pm = mp.legendre(DEG-1, x)
            dP = DEG*(x*P - Pm)/(x*x - 1)
            x  = x - P/dP
        P  = mp.legendre(DEG, x); Pm = mp.legendre(DEG-1, x)
        dP = DEG*(x*P - Pm)/(x*x - 1)
        xr.append(x); wr.append(2/((1 - x*x)*dP*dP))
    nodes, wts = [], []
    for p in range(NPANEL):
        a = L*p/NPANEL; b = L*(p+1)/NPANEL; h = (b-a)/2
        for x, w in zip(xr, wr):
            nodes.append(a + h*(x+1)); wts.append(w*h)
    K = len(nodes)

    # ---- tables trig ----
    SIN = [[mp.sin(om[n]*y) for y in nodes] for n in range(NB+1)]
    COS = [[mp.cos(om[n]*y) for y in nodes] for n in range(NB+1)]
    LY  = [(L - y)/L for y in nodes]
    W1  = [wts[k]*(mp.e**(nodes[k]/2) + mp.e**(-nodes[k]/2)) for k in range(K)]
    E2 = [mp.e**(nodes[k]/2) for k in range(K)]
    DD = [wts[k]/(mp.e**nodes[k] - mp.e**(-nodes[k])) for k in range(K)]
    tprep = time.time()-t0

    def theta_nodes(n, m):
        if n == 0 and m == 0:
            return [2*LY[k] for k in range(K)], mp.mpf(2)
        if n == 0 or m == 0:
            j = max(n,m); a = -2/(mp.sqrt(2)*mp.pi*j)
            return [a*SIN[j][k] for k in range(K)], mp.mpf(0)
        if n == m:
            a = 1/(mp.pi*n)
            return [2*(LY[k]*COS[n][k] - SIN[n][k]/(2*mp.pi*n)) for k in range(K)], mp.mpf(2)
        a = 2/(mp.pi*(m*m-n*n))
        return [a*(n*SIN[n][k] - m*SIN[m][k]) for k in range(K)], mp.mpf(0)

    CR = EU + mp.log(4*mp.pi*(mp.e**L-1)/(mp.e**L+1))
    ppts = []
    x = 2
    while x <= int(mp.e**L + 1e-9):
        y = x; p = None
        for q in [2,3,5,7,11,13,17,19,23]:
            if y % q == 0:
                p = q
                while y % q == 0: y //= q
                break
        if p and y == 1: ppts.append((mp.log(x), mp.log(p)/mp.sqrt(x)))
        x += 1

    def theta_at(n, m, y):
        if n == 0 and m == 0: return 2*(L-y)/L
        if n == 0 or m == 0:
            j = max(n,m); return -2*mp.sin(om[j]*y)/(mp.sqrt(2)*mp.pi*j)
        if n == m: return 2*((L-y)*mp.cos(om[n]*y)/L - mp.sin(om[n]*y)/(2*mp.pi*n))
        return 2*(n*mp.sin(om[n]*y) - m*mp.sin(om[m]*y))/(mp.pi*(m*m-n*n))

    S = mp.matrix(NB+1, NB+1)
    for n in range(NB+1):
        for m in range(n, NB+1):
            th, F0 = theta_nodes(n, m)
            W02 = mp.fsum(th[k]*W1[k] for k in range(K))
            WRi = mp.fsum((E2[k]*th[k] - F0)*DD[k] for k in range(K))
            Wp  = mp.fsum(w*theta_at(n,m,lg) for lg,w in ppts)
            v = W02 - (F0/2*CR + WRi) - Wp
            S[n,m] = v; S[m,n] = v
    tmat = time.time()-t0

    # ---- validation cote zeros (float64) ----
    zeros = pickle.load(open('zeros280.pkl','rb'))
    Lf = float(L); omf = [2*np.pi*n/Lf for n in range(NB+1)]
    def theta_np(n, m, y):
        if n==0 and m==0: return 2*(Lf-y)/Lf
        if n==0 or m==0:
            j=max(n,m); return -2*np.sin(omf[j]*y)/(np.sqrt(2)*np.pi*j)
        if n==m: return 2*((Lf-y)*np.cos(omf[n]*y)/Lf - np.sin(omf[n]*y)/(2*np.pi*n))
        return 2*(n*np.sin(omf[n]*y)-m*np.sin(omf[m]*y))/(np.pi*(m*m-n*n))
    yg = np.linspace(0, Lf, 6000)
    rats = []
    for a,b in [(0,0),(1,2),(3,3)]:
        th = theta_np(a,b,yg)
        zs = sum(2*np.trapezoid(th*np.cos(g*yg), yg) for g in zeros)
        rats.append(float(S[a,b])/zs)

    E, V = mp.eigsy(S)
    lam = [E[i] for i in range(NB+1)]
    c = [V[i,0] for i in range(NB+1)]
    if c[0] < 0: c = [-x for x in c]

    def vhat(z):
        s = c[0]*(2*mp.sin(z*L/2)/z/mp.sqrt(L) if abs(z) > mp.mpf('1e-20') else mp.sqrt(L))
        for n in range(1, NB+1):
            s += c[n]*2*mp.sqrt(2/L)*z*mp.sin(z*L/2)/(z*z-om[n]*om[n])
        return s
    def Xi(z):
        s = mp.mpf(0.5)+1j*z
        return mp.re(s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s))

    ca = Xi(0)/vhat(mp.mpf('1e-25'))
    zg = [mp.mpf(k)/10 + mp.mpf('0.037') for k in range(0, 301)]
    xg = [Xi(z) for z in zg]; vg = [ca*vhat(z) for z in zg]
    res = [v-x for v,x in zip(vg,xg)]
    Xmax = max(abs(x) for x in xg)
    infra  = [abs(r) for z,r in zip(zg,res) if z < 13]
    milieu = [abs(r) for z,r in zip(zg,res) if 15 < z < 30 and min(abs(float(z)-g) for g in [21.0220,25.0109]) > 1.0]
    i1 = min(range(len(zg)), key=lambda i: abs(float(zg[i])-14.1347))
    print(f"=== mu={float(mu)}, L={float(L):.4f}, N={NB+1} fcts paires, {K} noeuds, dps={mp.mp.dps} ===")
    print(f"  prep {tprep:.0f}s, matrice {tmat:.0f}s")
    print(f"  ratios premiers/zeros (3 entrees) : {[f'{r:.4f}' for r in rats]}")
    print(f"  vp les plus basses : {[mp.nstr(l,3) for l in lam[:6]]}")
    print(f"  c_a = {mp.nstr(ca,5)}")
    print(f"  |c_a v^ - Xi| / max|Xi| : infrarouge[0,13) max={float(max(infra)/Xmax):.2e} ; entre-zeros(15,30) max={float(max(milieu)/Xmax):.2e}")
    print(f"  au zero gamma_1=14.13 : c_a v^ = {mp.nstr(vg[i1],3)}   Xi = {mp.nstr(xg[i1],3)}")
    print(f"  total {time.time()-t0:.0f}s\n")
    return zg, vg, xg

if __name__ == '__main__':
    mu = mp.mpf(sys.argv[1]); NB = int(sys.argv[2])
    mp.mp.dps = int(sys.argv[3]); DEG = int(sys.argv[4])
    run(mu, NB, NPANEL=5*NB+20, DEG=DEG)
```

### D.6 Dénouage des conventions et identification de c_∞ (`denouage_A.py`)
```python
import mpmath as mp
import numpy as np
mp.mp.dps = 30

# ============ A. Audit des conventions + cote theorique ============
# 1) Phi_c : noyau theta classique, Xi_classique(t) = int_R Phi_c(u) e^{itu} du ?
def Phi_c(u):
    u = abs(u)   # fonction paire (equation fonctionnelle de theta)
    s = mp.mpf(0)
    for n in range(1, 9):
        s += (2*mp.pi**2*n**4*mp.e**(mp.mpf(9)*u/2) - 3*mp.pi*n**2*mp.e**(mp.mpf(5)*u/2))*mp.e**(-mp.pi*n*n*mp.e**(2*u))
    return s

def xi_classique(t):
    s = mp.mpf('0.5') + 1j*t
    return mp.re(mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s))

def xi_suzuki(t):
    return 2*xi_classique(t)

print("Verification de l'identite de Fourier (facteur exact) :")
for t in [0, 3, 7, 12]:
    I = 2*mp.quad(lambda u: Phi_c(u)*mp.cos(t*u), [0, 0.5, 1, 1.6])
    xc = xi_classique(t)
    print(f"  t={t:2d} : int Phi_c e^(itu) du = {mp.nstr(I,8)}   xi_cl(1/2+it) = {mp.nstr(xc,8)}   ratio = {mp.nstr(I/xc,6)}")

# 2) norme L2 du noyau correspondant a la convention Suzuki (Xi_S = 2 Xi_cl -> Phi_S = 2 Phi_c)
n2 = 2*mp.quad(lambda u: (2*Phi_c(u))**2, [0, 0.5, 1, 1.6])
print(f"\n||Phi_S||_L2(R) = {mp.nstr(mp.sqrt(n2),8)}    (prediction naive pour c_infini si v_a -> Phi/||Phi|| en L2)")

# 3) ajustement empirique c_a = c_inf + k/mu sur les points convergés en base
data = [(3.5,1.2173),(5.5,1.180),(7.5,1.1648),(9.5,1.1553),(11,1.1537),(16,1.1475)]
X = np.array([[1/m, 1] for m,_ in data]); y = np.array([c for _,c in data])
k, cinf = np.linalg.lstsq(X, y, rcond=None)[0]
pred = X@[k,cinf]
print(f"\nAjustement c_a = c_inf + k/mu : c_inf = {cinf:.4f}, k = {k:.4f}")
for (m,c),p in zip(data,pred):
    print(f"  mu={m:5.1f} : mesure {c:.4f}  ajuste {p:.4f}  ecart {c-p:+.4f}")
print(f"\nCandidats : ||Phi_S|| = {float(mp.sqrt(n2)):.4f} ;  2/sqrt(pi) = {float(2/mp.sqrt(mp.pi)):.4f} ;  c_inf mesure = {cinf:.4f}")
print(f"Rapport c_inf / ||Phi_S|| = {cinf/float(mp.sqrt(n2)):.4f}  (= 1/alpha si une fraction alpha de la masse L2 est dans la forme)")
```

### D.7 Recouvrement avec le noyau thêta
Variante `shape8.py` : identique à `shape7.py`, avec calcul final du recouvrement ⟨v, Φ_S⟩/‖Φ_S‖ par quadrature de Gauss-Legendre à 60 nœuds sur [0, L/2], Φ_S = 4Φ_c en série thêta (8 termes). Sortie à µ=11, base 47 : ‖Φ_S|fenêtre‖ = 1.130932, recouvrement = 0.99964071, c_pred = 1.1313385.

### D.8 Fondations Dirichlet : Frullani validé sur ζ, évaluateur Λ(s,χ₃), récolte de zéros (`dirichlet_step1.py`)
```python
import mpmath as mp, pickle, time
mp.mp.dps = 30

# ============ 1. Route archimedienne de Frullani, validee sur zeta ============
# W_psi(F; s0) = -gamma*F(0) - F(0)*log(1-e^(-2L)) + int_0^L [2F(0)e^(-2y) - 2F(y)e^(-2*s0*y)]/(1-e^(-2y)) dy
# Pour zeta : W_arch = -F(0)*log(pi)/?? ... convention CC (2.32) = (F0/2)(gamma+log(4pi tanh')) + int (e^(y/2)F - F0)/(e^y-e^-y)
# Test sur F(y) = 2(L-y)/L (entree (0,0), mu=5.5), ou (2.32) est certifie contre Q_infini.
L = mp.log(mp.mpf('5.5'))
F  = lambda y: 2*(L-y)/L
F0 = mp.mpf(2)

CR = mp.euler + mp.log(4*mp.pi*(mp.e**L-1)/(mp.e**L+1))
WR_232 = F0/2*CR + mp.quad(lambda y: (mp.e**(y/2)*F(y)-F0)/(mp.e**y-mp.e**(-y)), [0, L])

def W_psi(Ffun, F0v, s0, Lv):
    tail = -F0v*mp.log(1-mp.e**(-2*Lv))
    I = mp.quad(lambda y: (2*F0v*mp.e**(-2*y) - 2*Ffun(y)*mp.e**(-2*s0*y))/(1-mp.e**(-2*y)), [0, Lv])
    return -mp.euler*F0v + tail + I
# arch zeta (convention demi, comme psi#) : (1/2)*[ -F0 log pi + W_psi(s0=1/4) ] * (-1)^? 
# On determine la normalisation empiriquement contre WR_232 :
cand = -(F0*(-mp.log(mp.pi)) + W_psi(F, F0, mp.mpf('0.25'), L))/2
print("Validation Frullani sur zeta (entree (0,0), mu=5.5) :")
print(f"  WR (2.32) certifie      = {mp.nstr(WR_232, 10)}")
print(f"  -(1/2)[-F0 log pi + W_psi(1/4)] = {mp.nstr(cand, 10)}")
print(f"  rapport = {mp.nstr(cand/WR_232, 8)}")

# ============ 2. Evaluateur de Lambda(s, chi_3) et premiers zeros ============
# chi_3 : caractere reel impair mod 3 ; L(s,chi3) = 3^(-s) (zeta(s,1/3) - zeta(s,2/3)) ; a=1
def Lchi3(s):
    return 3**(-s)*(mp.zeta(s, mp.mpf(1)/3) - mp.zeta(s, mp.mpf(2)/3))
def Lam3(t):
    s = mp.mpf('0.5') + 1j*t
    v = (mp.mpf(3)/mp.pi)**((s+1)/2)*mp.gamma((s+1)/2)*Lchi3(s)
    return v
# realite sur la droite critique ?
for t in [0, 2, 5]:
    v = Lam3(t)
    print(f"  Lambda(1/2+{t}i, chi3) = {mp.nstr(v, 6)}  (Im/Re = {mp.nstr(abs(mp.im(v))/abs(mp.re(v)),3)})")

# scan de zeros par changements de signe de Re Lambda
t0 = time.time()
zs, step = [], mp.mpf('0.02')
prev = mp.re(Lam3(mp.mpf('0.01')))
t = mp.mpf('0.01')
while t < 140 and len(zs) < 70:
    t2 = t + step
    cur = mp.re(Lam3(t2))
    if prev*cur < 0:
        r = mp.findroot(lambda x: mp.re(Lam3(x)), (t, t2), solver='bisect')
        zs.append(float(r))
    prev, t = cur, t2
pickle.dump(zs, open('zeros_chi3.pkl','wb'))
print(f"\n{len(zs)} zeros de L(s,chi3) jusqu'a t = {zs[-1]:.2f} en {time.time()-t0:.0f}s")
print("premiers :", [f"{z:.4f}" for z in zs[:6]])
```

### D.9 Scan Dirichlet généralisé (`dscan.py`)
Usage : `python3 dscan.py chi4` (µ = 5.5 et 11) ; troisième point via `dscan.run('chi4', mp.mpf('16'), 46, 60)`. Caractères définis dans `CHARS` (table des valeurs, parité). Contient la grille en z partagée entre résidu et transformée de Φ_χ.
```python
import mpmath as mp, pickle, time, sys, os
import numpy as np
import numpy.polynomial.legendre as NL

CHARS = {
 'chi3': dict(q=3, tab=[0,1,-1], a=1),
 'chi4': dict(q=4, tab=[0,1,0,-1], a=1),
 'chi5': dict(q=5, tab=[0,1,-1,-1,1], a=0),
 'chi7': dict(q=7, tab=[0,1,1,-1,1,-1,-1], a=1),
 'chi8': dict(q=8, tab=[0,1,0,-1,0,-1,0,1], a=0),
}

def Lchi(s, q, tab):
    return q**(-s)*mp.fsum(tab[r]*mp.zeta(s, mp.mpf(r)/q) for r in range(1, q) if tab[r])

def Lam(t, q, tab, a):
    s = mp.mpf('0.5') + 1j*t
    return mp.re((mp.mpf(q)/mp.pi)**((s+a)/2)*mp.gamma((s+a)/2)*Lchi(s, q, tab))

def harvest_zeros(name, q, tab, a, tmax=85):
    fn = f'zeros_{name}.pkl'
    if os.path.exists(fn): return pickle.load(open(fn,'rb'))
    mp.mp.dps = 22
    zs, step = [], mp.mpf('0.04')
    t = mp.mpf('0.01'); prev = Lam(t, q, tab, a)
    while t < tmax:
        t2 = t + step; cur = Lam(t2, q, tab, a)
        if prev*cur < 0:
            zs.append(float(mp.findroot(lambda x: Lam(x, q, tab, a), (t, t2), solver='bisect')))
        prev, t = cur, t2
    pickle.dump(zs, open(fn,'wb'))
    return zs

def run(name, mu, NB, dps, DEG=14):
    cf = CHARS[name]; q, tab, a = cf['q'], cf['tab'], cf['a']
    zs = harvest_zeros(name, q, tab, a)
    mp.mp.dps = dps
    t0 = time.time()
    L = mp.log(mu); s0 = mp.mpf(1)/4 + mp.mpf(a)/2
    om = [2*mp.pi*n/L for n in range(NB+1)]
    xr0, _ = NL.leggauss(DEG)
    xr, wr = [], []
    for x0 in xr0:
        x = mp.mpf(float(x0))
        for _ in range(6):
            P = mp.legendre(DEG, x); Pm = mp.legendre(DEG-1, x)
            dP = DEG*(x*P - Pm)/(x*x - 1); x = x - P/dP
        P = mp.legendre(DEG, x); Pm = mp.legendre(DEG-1, x)
        dP = DEG*(x*P - Pm)/(x*x - 1)
        xr.append(x); wr.append(2/((1-x*x)*dP*dP))
    NPANEL = 4*NB + 16
    nodes, wts = [], []
    for p in range(NPANEL):
        aa, bb = L*p/NPANEL, L*(p+1)/NPANEL; h = (bb-aa)/2
        for x, w in zip(xr, wr):
            nodes.append(aa + h*(x+1)); wts.append(w*h)
    K = len(nodes)
    SIN = [[mp.sin(om[n]*y) for y in nodes] for n in range(NB+1)]
    COS = [[mp.cos(om[n]*y) for y in nodes] for n in range(NB+1)]
    LY  = [(L-y)/L for y in nodes]
    D2 = [wts[k]*2*mp.e**(-2*s0*nodes[k])/(1-mp.e**(-2*nodes[k])) for k in range(K)]
    EC = [mp.e**(-(2-2*s0)*nodes[k]) for k in range(K)]
    CST = mp.log(mp.mpf(q)/mp.pi) - mp.euler - mp.log(1-mp.e**(-2*L))

    def th_nodes(n, m):
        if n==0 and m==0: return [2*LY[k] for k in range(K)], mp.mpf(2)
        if n==0 or m==0:
            j=max(n,m); a2=-2/(mp.sqrt(2)*mp.pi*j)
            return [a2*SIN[j][k] for k in range(K)], mp.mpf(0)
        if n==m: return [2*(LY[k]*COS[n][k]-SIN[n][k]/(2*mp.pi*n)) for k in range(K)], mp.mpf(2)
        a2=2/(mp.pi*(m*m-n*n))
        return [a2*(n*SIN[n][k]-m*SIN[m][k]) for k in range(K)], mp.mpf(0)
    def th_at(n, m, y):
        if n==0 and m==0: return 2*(L-y)/L
        if n==0 or m==0:
            j=max(n,m); return -2*mp.sin(om[j]*y)/(mp.sqrt(2)*mp.pi*j)
        if n==m: return 2*((L-y)*mp.cos(om[n]*y)/L-mp.sin(om[n]*y)/(2*mp.pi*n))
        return 2*(n*mp.sin(om[n]*y)-m*mp.sin(om[m]*y))/(mp.pi*(m*m-n*n))

    ppts = []
    x = 2
    while x <= int(mp.e**L+1e-9):
        y2, p = x, None
        for qq in [2,3,5,7,11,13,17,19,23]:
            if y2 % qq == 0:
                p = qq
                while y2 % qq == 0: y2 //= qq
                break
        if p and y2 == 1 and tab[x % q] != 0:
            ppts.append((mp.log(x), tab[x % q]*mp.log(p)/mp.sqrt(x)))
        x += 1

    S = mp.matrix(NB+1, NB+1)
    for n in range(NB+1):
        for m in range(n, NB+1):
            th, F0 = th_nodes(n, m)
            arch = F0/2*CST + mp.mpf('0.5')*mp.fsum(D2[k]*(F0*EC[k]-th[k]) for k in range(K))
            v = arch - mp.fsum(w*th_at(n,m,lg) for lg,w in ppts)
            S[n,m] = v; S[m,n] = v

    # validation legere cote zeros
    Lf = float(L); omf = [2*np.pi*n/Lf for n in range(NB+1)]
    yg = np.linspace(0, Lf, 5000)
    def th_np(n, m, y):
        if n==0 and m==0: return 2*(Lf-y)/Lf
        return 2*(n*np.sin(omf[n]*y)-m*np.sin(omf[m]*y))/(np.pi*(m*m-n*n))
    rats = []
    for a2, b2 in [(0,0),(2,3)]:
        th = th_np(a2,b2,yg)
        rats.append(float(S[a2,b2])/sum(np.trapezoid(th*np.cos(g*yg), yg) for g in zs))

    E, V = mp.eigsy(S)
    lam = [E[i] for i in range(min(5, NB+1))]
    c = [V[i,0] for i in range(NB+1)]
    if c[0] < 0: c = [-u for u in c]
    def vhat(z):
        s = c[0]*(2*mp.sin(z*L/2)/z/mp.sqrt(L) if abs(z)>mp.mpf('1e-20') else mp.sqrt(L))
        for n in range(1, NB+1):
            s += c[n]*2*mp.sqrt(2/L)*z*mp.sin(z*L/2)/(z*z-om[n]*om[n])
        return s
    mp.mp.dps = 28
    def Xic(z): return Lam(z, q, tab, a)
    ca = Xic(0)/vhat(mp.mpf('1e-20'))
    g1 = zs[0]
    zgrid = [mp.mpf(k)*3/20 + mp.mpf('0.041') for k in range(0, 200)]
    xg = [Xic(z) for z in zgrid]; Xmax = max(abs(u) for u in xg)
    res = [abs(ca*vhat(z)-x2) for z, x2 in zip(zgrid, xg)]
    infra = max(r for z, r in zip(zgrid, res) if float(z) < g1-0.5)
    mil = max(r for z, r in zip(zgrid, res) if g1+0.8 < float(z) < 30 and min(abs(float(z)-g) for g in zs[:12]) > 0.8)
    # Phi_chi et recouvrement
    zq0, zw0 = NL.leggauss(60)
    zn, zw = [], []
    for (za, zb) in [(0,8),(8,25),(25,70)]:
        h = (zb-za)/2.0
        for t2, w2 in zip(zq0, zw0):
            zn.append(mp.mpf(za + h*(float(t2)+1))); zw.append(mp.mpf(h*float(w2)))
    XiZ = [Xic(u) for u in zn]
    def Phi(x2): return mp.fsum(zw[k]*XiZ[k]*mp.cos(zn[k]*x2) for k in range(len(zn)))/mp.pi
    xq0, wq0 = NL.leggauss(36)
    half = L/2
    xq = [half*(mp.mpf(float(t2))+1)/2 for t2 in xq0]; wq = [half*mp.mpf(float(w))/2 for w in wq0]
    P3 = [Phi(u) for u in xq]
    def vx(x2):
        s = c[0]/mp.sqrt(L)
        for nn in range(1, NB+1):
            s += c[nn]*(-1)**nn*mp.sqrt(2/L)*mp.cos(om[nn]*x2)
        return s
    ovl = 2*mp.fsum(wq[k]*vx(xq[k])*P3[k] for k in range(len(xq)))
    nPhi = mp.sqrt(2*mp.fsum(wq[k]*P3[k]**2 for k in range(len(xq))))
    par = 'pair' if a==0 else 'impair'
    print(f"[{name} q={q} {par}] mu={float(mu)} : gamma_1={g1:.3f} | ratios {rats[0]:.3f},{rats[1]:.3f} | "
          f"lam_min={mp.nstr(lam[0],3)} (echelle {[mp.nstr(l,2) for l in lam[1:4]]})")
    print(f"    residu infra={float(infra/Xmax):.3f} mid={float(mil/Xmax):.4f} | c_z0={mp.nstr(ca,5)} "
          f"c_proj={mp.nstr(nPhi*nPhi/ovl,6)} ||Phi||={mp.nstr(nPhi,6)} ovl={mp.nstr(ovl/nPhi,6)} | {time.time()-t0:.0f}s", flush=True)

if __name__ == '__main__':
    name = sys.argv[1]
    for mu, NB, dps in [(mp.mpf('5.5'), 24, 45), (mp.mpf('11'), 40, 52)]:
        run(name, mu, NB, dps)
```

### D.10 Normes exactes des noyaux thêta (`phi_exact.py`)
```python
import mpmath as mp
mp.mp.dps = 40

# Formes fermees : pour chi primitif reel,
#   pair  (a=0) : Phi(u) = 2 e^(u/2)  * sum chi(n)   exp(-pi n^2 e^(2u)/q),  Lambda(1/2+iz) = int Phi e^(izu) du
#   impair(a=1) : Phi(u) = 2 e^(3u/2) * sum chi(n) n exp(-pi n^2 e^(2u)/q)
# Validation : rapport int/Lambda a plusieurs z (doit etre 1 plat), puis ||Phi||_L2 en serie.
CH = {
 'chi3': (3, [0,1,-1], 1), 'chi4': (4, [0,1,0,-1], 1), 'chi5': (5, [0,1,-1,-1,1], 0),
 'chi7': (7, [0,1,1,-1,1,-1,-1], 1), 'chi8': (8, [0,1,0,-1,0,-1,0,1], 0),
}
def Lam(z, q, tab, a):
    s = mp.mpf('0.5') + 1j*z
    L = q**(-s)*mp.fsum(tab[r]*mp.zeta(s, mp.mpf(r)/q) for r in range(1, q) if tab[r])
    return mp.re((mp.mpf(q)/mp.pi)**((s+a)/2)*mp.gamma((s+a)/2)*L)

print(f"{'':7s} {'ratio z=0':>12s} {'z=4':>12s} {'z=9':>12s} {'||Phi|| ferme':>16s} {'numerique (avant)':>18s}")
prev = {'chi3':0.51531,'chi4':0.81580,'chi5':0.78699,'chi7':1.87569,'chi8':1.28252}
for name,(q, tab, a) in CH.items():
    def Phi(u):
        # serie sur n>=1, symetrisee par parite de u via l'equation fonctionnelle (Phi paire)
        uu = abs(u)
        w = mp.e**(2*uu)
        s = mp.fsum(tab[n % q]*(n if a else 1)*mp.e**(-mp.pi*n*n*w/q) for n in range(1, 40) if tab[n % q])
        return 2*mp.e**((mp.mpf(3)/2 if a else mp.mpf('0.5'))*uu)*s
    rats = []
    for z in [0, 4, 9]:
        I = mp.quad(lambda u: Phi(u)*mp.cos(z*u), [-2.5, -1, 0, 1, 2.5])
        rats.append(I/Lam(z, q, tab, a))
    n2 = mp.sqrt(mp.quad(lambda u: Phi(u)**2, [-2.5, -1, 0, 1, 2.5]))
    print(f"{name:7s} {mp.nstr(rats[0],8):>12s} {mp.nstr(rats[1],8):>12s} {mp.nstr(rats[2],8):>12s} {mp.nstr(n2,12):>16s} {prev[name]:>18.5f}")

# zeta, rappel avec la meme machinerie (Phi_S = 4 Phi_c)
def PhiS(u):
    uu = abs(u)
    return 4*mp.fsum((2*mp.pi**2*n**4*mp.e**(mp.mpf(9)*uu/2) - 3*mp.pi*n**2*mp.e**(mp.mpf(5)*uu/2))*mp.e**(-mp.pi*n*n*mp.e**(2*uu)) for n in range(1, 12))
n2z = mp.sqrt(mp.quad(lambda u: PhiS(u)**2, [-2, -0.8, 0, 0.8, 2]))
print(f"{'zeta':7s} {'':>12s} {'':>12s} {'':>12s} {mp.nstr(n2z,12):>16s} {1.13093:>18.5f}")
```

## Annexe E — Journal de la phase 2

Suite du journal de l'annexe B, dans l'ordre réel : (19) recherche web — découverte que le terrain prolates/Toeplitz/petites valeurs propres est la frontière active (Connes-Consani 2021/2023, Suzuki 2026) ; (20) lecture intégrale de « ζ-cycles » : correspondances point par point avec nos campagnes, théorème 6.4 = portrait-robot réalisé, désaccord doublement-exponentiel identifié ; (21) lecture de Suzuki : fonction vis, A_a = Friedrichs de D*G_aD, conjecture (1.2), relecture rétroactive de notre mode dangereux comme ombre de ξ ; (22) décision de méthode : raccordement avant test de forme (calibration du conditionnement) ; (23) raccordement : effondrement de α(s), invariant 0.41/dimension, plongeon de Slepian mesuré jusqu'à 2.2×10⁻³⁶ (mp, 1 s), faux négatifs float64, lecture « blancheur protectrice » ; (24) lecture de Groskin : criticité = théorème / convergence ouverte, terrain « positions » occupé à 329 chiffres, artefact T, créneaux restants (forme de la fonction, Dirichlet) ; (25) construction du test de forme, échec de performance puis optimisation (quadrature partagée, tables trig) ; (26) bug archimédien attrapé par confrontation à Q∞ et à la figure 4 de CC ; (27) bug de séparation d'intégrande ; (28) bug des nœuds float64 ; (29) série µ = 3.5 → 16, validation λ_min contre le 2.389×10⁻⁴⁸ publié ; (30) découverte du protocole à double limite (l'« accélération » était un artefact) et loi finale R ≈ e^(−L)/3 ; (31) audit des conventions, facteur ½ épinglé numériquement dans l'identité de Fourier de Φ_c ; (32) ajustement c_a = c_∞ + 0.32/µ sur six points (même coefficient que la loi de forme) ; (33) recouvrement L² de 0.99964 à µ=11 → identification c_∞ = ‖Φ_S‖ = 1.130932, scission L²/uniforme de la conjecture (1.2) ; (34) route archimédienne de Frullani validée à 10 chiffres sur ζ, évaluateur Λ(s,χ₃) réel sur la droite critique, 70 zéros récoltés ; (35) pipeline χ₃ : identification c_∞(χ₃) = ‖Φ₃‖ confirmée du premier coup, λ_min quatorze ordres au-dessus de ζ à µ = 5.5 ; (36) échelle χ₃ sur trois µ : pente 4.0, première lecture « l'abîme est une affaire de pôle » ; (37) généralisation à χ₄, χ₅, χ₇, χ₈ après optimisation de la grille en z (runs de >17 min à ~20 s) ; (38) moisson : identification 6/6, signature de parité sur C, pente croissante avec γ₁, candidat γ₁²/(2πe) ; (39) troisième µ sur quatre caractères : linéarité des échelles confirmée, γ₁²/(2πe) falsifié par χ₄, structure à deux variables (désert, parité), principe du sismographe établi ; (40) durcissement : formes fermées Φ_χ validées (rapport 1.0 plat), normes à douze chiffres, robustesse en base des échelles Dirichlet (≤2.4%), correction de la pente ζ (11.8 → ≈10 non linéaire, bases appariées), convergence quadratique vérifiée contre les normes exactes ; (41) extension à χ₁₁, χ₁₂, χ₁₃, χ₁₅ (tables validées à 10⁻²⁶) : plancher s ≈ 0.9 aux petits déserts, critère de largeur de fenêtre ½ln(3q/π) ; (42) point décisif µ = 22 : pente de χ₁₅ stabilisée à ≈ 0.70 — troisième variable confirmée, hypothèse de densité arithmétique (conducteur composé), prédiction χ₂₄ ; (43) identification portée à dix fonctions L (normes 0.515 → 4.592), χ₁₅ à 3.1×10⁻⁴ ; (44) verdict mod 24 : la paire jumelle confirme la densité arithmétique comme variable réelle (χ₁₁ vs χ₂₄ᵉ : γ₁ quasi égaux, pentes 0.91 vs ≈0.49), le plancher du §13.5 tombe, γ₁ agit encore à appauvrissement fixé (χ₁₂ vs χ₂₄ᵉ : 0.94 vs 0.49), parité secondaire aux petits déserts ; (45) session de régression : modèles emboîtés (γ₁ / +D / +parité : 20→15→9.4% de dispersion), collapse X = γ₁·e^(−0.125D), prédictions préenregistrées pour χ₁₉ ; (46) verdict hors échantillon : γ₁(χ₁₉) = 1.516, s ≈ 0.55-0.6 — deux hypothèses éliminées, collapse sous-prédisant, M2 à 15% ; découverte du biais transitoire des petits déserts ; identification portée à treize fonctions L ; (47) campagne anti-transitoire (µ = 30 et 38, factorisation étendue ≤ 37) : χ₁₉ = 0.58, χ₂₄ᵒ = 0.46, χ₂₄ᵉ = 0.50 convergés, χ₁₁ ≈ 1.07 et χ₁₅ ≥ 0.80 relevés — contraste de densité accentué (paire décisive à rapport 2.1), biais généralisé identifié sur toute la carte, refit suspendu jusqu'à uniformisation ; (48) uniformisation des sept caractères restants à µ = 30-38 ; septième artefact : demande en base croissant avec la profondeur (χ₃ : fausse courbure 3.35 → 4.02 en base 75), doute rétroactif sur la non-linéarité de ζ ; (49) refit final : s ≈ 0.29·γ₁^1.28·e^(−0.20D)·1.31^[impair] à 9.7% (LOO 12.4%), densité et parité renforcées, identifications à quelques 10⁻⁵.

## Annexe F — Tableau récapitulatif des constantes mesurées

| Constante | Valeur | Statut |
|---|---|---|
| Taux de fermeture générique de la marge de Weil | ≈ 0.41 par degré de liberté (facteur ≈ 0.66/dim) | mesuré, robuste en δ et en U ; explication théorique ouverte (prolates) |
| Taux dans le plongeon de Slepian | jusqu'à ≈ 3.0 par dimension près du mur de rang | mesuré à U = 2.5, bande 42 zéros |
| Frontière de certification du crible | U_max ≈ 0.65·log N ; bruit ~ ×8 par décade de N | mesuré (campagne 4), axe non couvert par la littérature lue |
| Décroissance CC de λ_min | −ln λ_min ≈ 10·µ (leur régime, base complète) | littérature, raccordé par nos mesures |
| Loi de forme (Suzuki 1.2) | résidu infrarouge ≈ (1/3)·e^(−L) = 0.33/µ | mesuré (v2), premier test connu de la version fonctionnelle |
| Rapport infrarouge/entre-zéros du résidu | ≈ 30-40× à tout µ | mesuré : le goulot est le bombement en Γ sous γ₁ |
| Constante de normalisation c_a | c_∞ = ‖Φ_S‖_L² = 1.130932 (norme du noyau thêta) | **identifiée** (§12) : recouvrement 0.99964 à µ=11, estimateur par projection à 4×10⁻⁴ |
| Validation externe | λ_min(µ=11) = 3.6×10⁻⁴⁸ vs 2.389×10⁻⁴⁸ (CC) | chaîne complète certifiée à l'ordre de grandeur |
| Identification en famille (§13) | c_∞(χ) = ‖Φ_χ‖ à ≤ 4×10⁻⁴, six caractères | **confirmée 6/6**, prédiction sans paramètre |
| Constante de forme C(χ) | ζ : 0.33 ; impairs : 0.39-0.43 ; pairs : 0.50-0.53 | mesurée : signature de parité |
| Loi d'échelle Dirichlet | −ln λ_min = s(χ)·µ, douze caractères uniformisés à µ = 38 : s de 0.46 (χ₂₄ᵒ) à 4.00 (χ₃) ; loi s ≈ 0.29·γ₁^1.28·e^(−0.20D)·1.31^[impair] à 9.7% | mesurée ±0.02-0.10 ; ζ ≈ 10 (non-linéarité suspecte : artefact de base probable) ; structure résiduelle ~15-20% ouverte |

## Annexe G — Statut épistémique, mise à jour v2

Aux trois registres de l'annexe C s'ajoutent, côté **mesuré ici (v2)** : les trois régimes de positivité et leurs taux, la protection par blancheur (lecture de mesures, pas théorème), les artefacts documentés (nœuds float64, séparation d'intégrande, regroupement archimédien), la loi de forme R ≈ e^(−L)/3 avec son protocole à double limite, et la validation croisée contre la valeur publiée de Connes-Consani. Côté **littérature (v2)** : théorème des ζ-cycles, criticité de Connes-van Suijlekom, fonction vis et conjecture (1.2) de Suzuki, résultats de Groskin. Passe au registre **mesuré** (v2, §12-13) : l'identification c_∞ = ‖Φ_S‖ et la vérification L² de (1.2) à 4×10⁻⁴, puis leur extension six sur six à la famille de Dirichlet, la signature de parité de C, et la loi d'échelle linéaire −ln λ_min = s(χ)·µ (pentes sur trois points par caractère, sauf ζ sur deux régimes de méthode différents). La lecture « sismographe de Siegel » est un principe d'observable, pas encore un détecteur opéré. Restent **spéculatifs** : toute lecture du milieu comme objet physique et l'interprétation de la blancheur comme mécanisme plutôt que description. La loi de forme repose sur six points en µ dont deux extrapolés en base : elle est falsifiable par extension de la série et doit être traitée comme provisoire.
