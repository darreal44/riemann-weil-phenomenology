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

### 13.10 Veillée : ζ blanchi, D raffiné (négatif), ζ hors famille

**ζ est linéaire.** Retest à µ = 16 en base 71 (dps 108, échelle seule) : λ_min = 1.93×10⁻⁷³, soit 5.6 ordres sous la valeur en base 53 — segments corrigés 11.8 puis 11.6 : **s_ζ = 11.7 ± 0.2, linéaire**, la « non-linéarité » était le septième artefact. Réconciliation avec l'heuristique ~10µ de Connes-Consani par l'ordonnée à l'origine : −ln λ_min ≈ 11.7·µ − 20 donne un ratio de 9.9 à µ = 11, exactement leur valeur. Toute la famille, ζ compris, obéit donc à la même forme affine.

**Le raffinement de D échoue proprement.** Scan de D(β) = Σ log p/(p^β − 1) sur les premiers retirés : β* = 0.20 en butée de plage, gain de 4% seulement (RMS 0.0932 contre 0.0972), χ₁₂ inchangé à +21%. La quatrième variable est ailleurs — et elle a été trouvée dans la foulée : **l'écart γ₂−γ₁**. Le modèle M3, ln s = 1.32·ln γ₁ + 0.45·ln(γ₂−γ₁) − 0.13·D + 0.28·[impair] − 1.95, tombe à 6.1% de dispersion et surtout à **4.8% de médiane en validation croisée** (contre 12.4%), ce qui exclut le sur-ajustement : la profondeur lit le paysage des zéros bas — le désert ET la raréfaction immédiatement après — pas seulement γ₁. χ₄ et χ₇ rentrent dans le rang (±1%) ; ne résistent que χ₁₂ (+14%) et χ₁₃ (−10%), les deux pairs de conducteur moyen, en signes opposés. (Aveu de méthode : la première version de ce paragraphe qualifiait la sonde γ₂−γ₁ de « marginale », écrite avant le calcul — corrigée sur pièce ; troisième occurrence du même péché, désormais érigé en artefact zéro de la taxonomie : ne jamais rédiger le résultat avant de l'avoir lu.)

**ζ en prédiction hors famille.** La loi Dirichlet (ajustée sans ζ) prédit à γ₁ = 14.135, D = 0 : s ∈ [8.7 (pair), 11.4 (impair)] ; mesure : 11.7. Le pôle place ζ au sommet de la fourchette, légèrement au-dessus du bonus d'impair — la contribution +|f̂(±i/2)|² agit sur la profondeur comme une parité renforcée. C'est la première prédiction quantitative inter-familles du programme, et elle tombe à 3% du bord supérieur.

### 13.11 Deux pairs de plus : la variable d'écart éprouvée

Ciblage du mystère χ₁₂/χ₁₃ (les deux résistants, pairs de conducteur moyen) par deux nouveaux pairs à prédictions préenregistrées : χ₁₇ (premier, γ₁ = 3.728, écart γ₂−γ₁ = 1.907 — le plus petit de la famille) et χ₂₁ (composé {3,7}, γ₁ = 2.315, écart 3.465). Verdicts : **χ₂₁ mesuré 0.58 contre 0.534 prédit (+9%, dans la bande ✓) ; χ₁₇ mesuré 0.71 contre 0.958 prédit (−26%, hors bande ✗)**. La variable d'écart, validée en interne (LOO 4.8%), extrapole mal vers les petits écarts : l'exposant 0.45 sur (γ₂−γ₁), ajusté sur des écarts de 2.3 à 4.3, casse sous ~2. Nouveauté systématique : χ₁₇ et χ₂₁ montrent des segments légèrement *décroissants* (0.75/0.67 et 0.60/0.56) — premier transitoire par au-dessus de la famille, non élucidé.

Refit à quatorze points : la dispersion se tient à 7.6% mais la validation croisée se dégrade à 12.8%, et surtout les paramètres sautent (exposant d'écart 0.45 → 0.68, coefficient de densité divisé par deux) — la loi M3 est réelle mais sa forme en loi de puissance sur l'écart est trop rigide, et son instabilité paramétrique le signe. Lecture consolidée : la profondeur lit le paysage des zéros bas par une fonctionnelle plus riche que (γ₁, γ₂−γ₁) — vraisemblablement une intégrale du comptage N_χ(t) à petit t — dont nos quatre variables sont des projections. Identifications au passage : χ₁₇ à 1.1×10⁻⁴, χ₂₁ à ~10⁻³ en convergence — **quinze fonctions L, zéro exception**.

### 13.12 La chasse à la fonctionnelle : deux rejets propres et une cible affinée

Deux fonctionnelles du paysage des zéros bas ont été testées contre M3. **S₂ = Σ 1/γₖ²** (la courbure du noyau côté zéros en z = 0, sans paramètre libre) : RMS 12.9%, LOO 13.2% — rejetée ; dominée à ~94% par γ₁ seul aux petits déserts, elle dilue l'information d'écart que M3 capture. **L(τ) = Σ e^(−γₖ/τ)** (Laplace du comptage, listes plafonnées uniformément à t < 50 après détection d'une contamination par fenêtres de récolte inégales) : τ file en butée de scan, RMS 10.2%, LOO 14.4% — rejetée aussi, avec un échec spectaculaire d'extrapolation : ζ prédit à 39.6 contre 11.7 mesuré, car le comptage brut confond la *densité* (∝ log q, forte pour les grands conducteurs) et la *forme* du paysage — ζ, pauvre en zéros bas, sort du domaine.

Deux vrais enseignements dans ces rejets. D'abord, **l'absorption partielle de D est réelle** : sous L(τ), le coefficient de densité arithmétique tombe de −0.13 à −0.05 — le comptage spectral encode bien le conducteur (la formule explicite oblige), mais au prix de la qualité globale : l'information arithmétique et l'information de paysage ne se substituent pas proprement l'une à l'autre dans ces formes simples. Ensuite, la cible s'affine : la bonne fonctionnelle est vraisemblablement une **vacance** — le déficit ∫(N̄_χ(t) − N_χ(t))·w(t)dt contre la densité attendue (t/2π)·log(qt/2πe), qui sépare précisément forme et densité. Sa construction exige les bonnes constantes de N̄_χ : chantier propre pour une session dédiée. En attendant, M3 (γ₁, écart, D, parité) reste la meilleure loi de travail, avec ses limites cartographiées (χ₁₇, instabilité paramétrique).

### 13.13 Les deux traces, élucidées et exécutées

**Les transitoires décroissants de χ₁₇/χ₂₁ sont réels mais pas inédits.** Test de base à µ = 38 (NB 63 → 75) : λ_min ne bouge que de 5% — ce n'est pas le septième artefact. Relecture des séries complètes : le motif existe en version douce ailleurs (χ₁₉ : 0.597 → 0.571 ; χ₂₄ᵒ : 0.467 → 0.462). C'est un **dépassement-puis-tassement** : les échelles surtirent légèrement avant de se poser sur leur asymptote, et χ₁₇/χ₂₁, mesurés seulement à µ ≥ 22, n'exhibent que la phase de tassement. Contribution systématique : ±0.05 sur les s asymptotiques, désormais budgétée.

**Les quatre résistants gardent leur secret.** L'hypothèse χ(2) — les quatre sont pairs, ceux à conducteur pair (2 retiré) au-dessus du modèle, ceux à 2 présent en dessous — est **falsifiée** par la quantification : corrélation résidus/χ(2) = −0.07, coefficient nul en régression, χ(3) à peine mieux (−0.31) avec une validation croisée qui explose (LOO max 59%). Septième hypothèse exécutée en vingt-quatre heures (après γ₁²/2πe, « conducteur premier reste haut », γ₁ seul, D(β), S₂, L(τ)). Les résistants χ₈/χ₁₂ (+11%) et χ₁₃/χ₁₇ (−9/−10%) attendent la fonctionnelle de vacance ou une variable encore invisible — question ouverte, proprement bornée.

### 13.14 La vacance échoue — et son échec renverse la lecture

Construction propre : N̄_χ = θ_χ/π + c avec la phase Γ exacte (pas d'asymptotique), c calibré sur la queue t ∈ [25, 50]. La calibration elle-même valide la machinerie : **c ≈ 0 ± 0.03 pour les quatorze caractères** (la constante théorique des χ réels primitifs à ε = +1) et **c = 1.006 pour ζ** — le « +1 » classique de N = θ/π + 1 retrouvé à 0.6%. Puis V(τ) = ∫(N̄−N)·e^(−t/τ)dt, quantité signée, testée dans l'exposant : ln s = α·V + ...

**Échec décisif : RMS 21% au mieux (contre 7.6% pour M3), validation croisée 23-66%, ζ prédit à ~0 contre 11.7.** Et la raison de l'échec est la trouvaille : les vacances mesurées tiennent dans V ∈ [−0.10, +0.05] sur une famille dont s varie d'un facteur 9 — **en unités de comptage, tous les déserts se ressemblent** (~½ zéro manquant : le premier zéro arrive par construction vers N̄ ≈ ½, Riemann-von Mangoldt oblige). Le déficit de comptage est quasi-universel, donc muet.

**Reformulation : la profondeur est un phénomène de bande passante, pas de comptage.** Trois fonctionnelles de type comptage sont mortes (désert normalisé par l'espacement, L(τ), V(τ)) pendant que les variables en fréquence *absolue* (γ₁, γ₂−γ₁ en unités de t) tiennent : ce que l'échelle mesure, c'est la bande [0, ~γ₂) où une fonction test peut cacher son spectre — le produit temps×bande de Slepian, en hertz et pas en zéros. Le mécanisme prolate ne compte pas les zéros manquants ; il mesure la place. Cohérence rétroactive : ζ porte la seule vacance non triviale de la famille (V = +0.40, presque un zéro entier manquant — la poussée du pôle, visible dans V mais inutilisable par le modèle). Huitième hypothèse exécutée ; la cible théorique se déplace : dériver s(γ₁, écart) de la théorie des prolates en fréquences absolues, chantier théorique et non plus statistique.

## 14. Théorie du régime générique : le front de moisson

La constante 0.41/dimension — la plus ancienne question ouverte du fil — a une explication, testée en quatre expériences de falsification.

**Cadre.** La matrice à J points est de Toeplitz à symbole atomique : T_J = Σ_γ w(γ)·v(γδ)v(γδ)*, atomes aux angles γδ mod 2π, poids w(γ) = e^(−s²γ²). Trois régimes en découlent. (i) Atomes équidistribués à poids égaux → T ∝ identité : la « blancheur protectrice » de la campagne 2 est un fait de séries de Fourier. (ii) Un vecteur à J dimensions annule exactement J−1 atomes (polynôme de degré J−1 sur le cercle) ; l'optimum moissonne les plus lourds — les zéros les plus bas — et la marge résiduelle est le poids du premier atome épargné : **marge(J) ≈ e^(−s²·γ²_(⌈J/2⌉))** (deux atomes par zéro), d'où le taux par dimension **s²·γ_front/ρ(γ_front)** avec ρ la densité des zéros. À notre fenêtre de mesure (s = 0.05, front γ ≈ 40-50) : 0.34-0.40 — le « 0.41 » expliqué, ainsi que son accélération observée (0.37 → 0.73) quand le front avance en territoire clairsemé. (iii) Le plongeon de Slepian s'allume quand la bande cesse d'envelopper le cercle de Nyquist : **J* = U·γ_max/2π + 1**.

**Falsifications (toutes passées).** Confrontation directe : le modèle sans paramètre colle aux marges mesurées sur quatre décades (J = 21 : 8.44×10⁻⁴ mesuré vs 8.99×10⁻⁴ prédit ; J = 31 : 1.31×10⁻⁵ vs 1.30×10⁻⁵), décrochant seulement au pré-plongeon. Grille uniforme de même densité : indiscernable des vrais zéros (4.38×10⁻¹⁰ vs 3.94×10⁻¹⁰ à J = 41) — le régime générique est aveugle à l'arithmétique. Enveloppe plate : marge stagnante à O(1) (pas d'échelle de poids à moissonner) puis effondrement brutal à J = 26, contre J* = 24.9 prédit par le critère de Nyquist ✓. Fréquences poissoniennes : marges erratiquement plus profondes (10⁻⁵ dès J = 11) — l'agglutination crée des directions quasi-dégénérées à bas prix ; **la rigidité GUE maintient la marge au maximum du modèle de front : des zéros poissoniens seraient plus dangereux pour la positivité**. Énoncé comparatif qui donne enfin son contenu précis à la protection par blancheur.

**Prédiction préenregistrée** pour un test futur : à s = 0.025 (front γ ≈ 40), le taux générique par dimension doit tomber à ≈ 0.085. Et la jonction avec la loi d'échelle Dirichlet (§13) se dessine : le mécanisme du plongeon en fréquences absolues (arcs de Nyquist, produit temps×bande) est exactement ce que la mort des fonctionnelles de comptage (§13.14) exigeait — la profondeur est une affaire de bande passante, et le front de moisson en est la première pièce théorique.

### 14.2 L'architecture universelle des barreaux

Analyse d'ensemble des échelles quasi-nulles stockées (33 barreaux, quinze fonctions L à µ = 38, ζ à µ = 16 en base 71) : l'espacement d'un barreau, en unités de −ln λ, ne dépend que du **niveau de profondeur** ℓ où il se trouve — pas du caractère. Par bandes de niveau : ℓ ∈ [0,15) : 10.9 ± 1.5 (huit barreaux, huit caractères différents) ; [15,40) : 13.5 ± 1.5 ; [40,80) : 16.0 ± 1.6 ; [80,150) : 16.0 ± 2.1 — où les barreaux de ζ (13.4 à 17.7) s'intercalent indistinctement entre ceux de χ₃ et χ₄ aux mêmes niveaux. Profil ajusté : **Δ(ℓ) ≈ 9.8 + 0.65·√ℓ** (RMS 1.8, dispersion inter-caractères ~12%), avec saturation apparente vers Δ ≈ 16 en profondeur.

Conséquence structurelle majeure : **le problème se factorise**. L'architecture de l'échelle — le profil Δ(ℓ) — est universelle, pure analyse harmonique de la fenêtre (vraisemblablement l'asymptotique des valeurs propres de Slepian, indépendante de l'arithmétique) ; toute la dépendance en χ de la saga du §13 — γ₁, écart, densité, parité — vit dans **un seul nombre, la vitesse de forage s(χ) = dℓ/dµ**. La question théorique se scinde donc proprement : (a) dériver Δ(ℓ) de la théorie des prolates (cible harmonique, χ-aveugle) ; (b) dériver s(χ) du couplage entre le contenu spectral-arithmétique de la fenêtre et le foret (cible arithmétique). Le §14 a résolu l'analogue de (a) pour le régime bandé ; le pont vers (a) profond passe par le critère de Nyquist appliqué aux modes de l'application E.

### 14.3 L'architecture identifiée : du Slepian à la puissance κ

Test frontal du candidat « prolate classique » : les petites valeurs propres de l'opérateur de concentration pur (complémentaire I − sinc, Nyström multiprécision, validé contre l'asymptotique de Fuchs ln(8c/(k+1))) donnent des espacements de 3 à 5 là où les échelles de Weil en montrent 11 à 19 — **le Slepian classique est rejeté tel quel**. Mais la comparaison des formes, barreau par barreau (33 barreaux, chaque échelle contre son classique au c effectif = ℓ_max/2), révèle une dilatation pure :

**Δ_Weil(k) = κ · ln(8c/(k+1)), avec κ = 2.85 ± 0.26** (médiane 2.82), sans corrélation avec c (+0.08) ni avec le caractère — équivalent : **λ_Weil,k ≈ (1 − λ_k^Slepian)^κ**. L'architecture universelle du §14.2 est donc l'échelle de Slepian élevée à une puissance universelle. Les candidats e = 2.718 et 3 sont tous deux à moins d'un écart-type ; les départager exige κ à ±0.05 (barreaux plus nombreux et plus propres — faisable). Hypothèse de mécanisme pour κ = 3, à traiter avec la prudence due (cf. les numérologies exécutées) : la construction semi-locale enchaîne trois filtrages — limitation temporelle, application E, évaluation sur les zéros — et trois projections composées cubent les fuites. Le seul barreau déviant (χ₁₇, k = 1, rapport 1.89) siège au sommet non-asymptotique de son échelle.

La cible d'analyse harmonique pure du programme est ainsi transformée : il ne s'agit plus de deviner un profil, mais de **démontrer l'exposant κ** pour l'opérateur de Connes-Consani — un énoncé précis, falsifiable à ±0.05, et vraisemblablement accessible aux techniques de composition de projections.

### 14.4 La vitesse de forage : un théorème-esquisse, une rétrogradation, un ordre zéro

**Le théorème-esquisse de linéarité.** Via §14.3, s·µ = 2κ·c_eff, donc c_eff ∝ µ. Or tout mécanisme porté par la fenêtre continue — prolates sur [−L/2, L/2] contre une bande fixe — plafonne à c ∝ γ·L = γ·ln µ, logarithmique. Le comptage de Landau du désert sur le réseau multiplicatif {log n} donne lui aussi du ln µ. La croissance linéaire de la profondeur exige donc que chaque *entier* de la fenêtre contribue un incrément O(1) : **la linéarité de −ln λ_min en µ est la signature du réseau des entiers** — le forage est un phénomène de réseau discret (l'application E de Connes-Consani en est l'incarnation), inaccessible à toute analyse du continuum seul. C'est, en creux, une explication de plus de l'échec des approches génériques.

**Rétrogradation du §14.3.** Test de cohérence interne du modèle Slepian^κ : les deux estimateurs de c — par la profondeur (ℓ_max/2κ) et par l'espacement du bas (e^(Δ₀/κ)/8) — divergent d'un facteur 2.1 à 5.5 selon le caractère. Le *profil* des espacements est bien Slepian-morphe à dilatation κ ≈ 2.85 près (§14.3 tient sur la forme), mais l'identification littérale λ_Weil,k = (1−λ_k^Slepian(c))^κ à c unique **échoue sur la normalisation absolue**. L'architecture reste à construire ; l'exposant κ reste sa meilleure empreinte mesurée.

**L'ordre zéro de s(χ).** Le candidat de Landau discret c_eff ≈ γ₁·N_χ(µ)/(2π) — bande du désert × nombre d'entiers χ-supportés — tient à un facteur 1.86 ± 0.91 sur une famille où s varie d'un facteur 25 : l'échelle du réseau est la bonne, mais la dispersion (χ₁₇ à 4.5×, la structure résiduelle de M3) montre que la bande effective n'est pas γ₁ seul — l'écart γ₂−γ₁ et le contenu arithmétique fin manquent, comme au §13. État de la cible « prouver s(χ) » : un squelette (réseau discret, échelle γ₁N/2π, exposant κ), trois chaînons manquants bien identifiés (la normalisation de l'architecture, la bande effective, le couplage arithmétique). Dur, comme annoncé — mais désormais dur *avec un cahier des charges*.

**Chaînon 2, test exécuté (négatif).** La bande effective inversée du modèle de Landau, W_eff = 2π·c_eff/N_supporté = π·s·q/(κ·φ(q)), ne s'accroche à aucun repère spectral : W/γ₁ = 0.63 ± 0.23 (36% de dispersion, le meilleur), W/γ₂ et W/(γ₁+0.45·écart) pires, χ₁₇ toujours en queue extrême (0.22). Le comptage Λ-pondéré ne fait pas mieux. Enseignement : **la factorisation c = W×N/2π est elle-même trop naïve** — la bande et le comptage ne se séparent pas, le couplage (dont χ₁₇ est le marqueur récurrent) est irréductible. Le cahier des charges du chaînon 2 se précise en s'assombrissant : la bande du foret n'est pas un repère fixe du paysage mais une fonctionnelle couplée bande-réseau, et son identification passe probablement par le chaînon 1 (construire l'opérateur) plutôt que par l'inversion phénoménologique. Dixième exécution d'hypothèse du fil.

### 14.5 Chaînon 3 : la chirurgie du foret — obstruction et spectroscopie

L'expérience causale du chaînon 3 — éclaircir artificiellement le réseau d'un ζ jouet, tout le reste fixé — a été exécutée avec prédictions préenregistrées (profondeurs ≈ 130 / 104 / 122 pour sans-2 / sans-{2,3} / sans-pôle, contre 167.4 pour ζ complet, via la loi Dirichlet transposée). **Les prédictions sont spectaculairement fausses, et leur mode d'échec est le résultat.**

**Retirer le premier 2 n'atténue pas le forage : il effondre la positivité** — six valeurs propres négatives d'ordre 1 (−0.554 à −0.213) à µ = 16. Mécanisme : le quasi-radical de ζ (douze directions sous 10⁻⁴⁰) est accordé au produit d'Euler complet ; la tour du 2, réinjectée, agit comme perturbation indéfinie O(1) sur ce sous-espace, et le spectre négatif observé est son ombre sur le radical. C'est la sensibilité arithmétique de Connes-Consani (p = 2 épinglé à 10⁻³) vue en coupe. **Retirer le pôle effondre exactement une direction** (−6.49) en laissant le reste de l'échelle quasi intact (barreaux k ≥ 1 inchangés à quelques pourcents) — et la chute est identifiée : le pôle est quasi rang-un de valeur diagonale 32·sinh²(L/4)/L = 6.51 à µ = 16, accord à 0.3%.

**Leçon d'obstruction (onzième exécution).** L'arithmétique n'est pas un cadran qu'on tourne : la cohérence de la formule explicite est *porteuse* — on ne peut pas varier le contenu du réseau indépendamment du côté spectral, car chaque composante (chaque tour de premier, le pôle) soutient des directions précises du quasi-radical. Les variables de la loi du §13 (γ₁, écart, D, parité) sont les ombres corrélées d'une cohérence unique, pas des boutons indépendants — d'où l'irréductibilité constatée au chaînon 2. **Le programme qui en sort : la spectroscopie du radical** — mesurer la matrice de couplage ⟨v_k | Q_composante | v_l⟩ des formes composantes (tours de premiers, pôle, archimédien) sur la base des états quasi-nuls : c'est le couplage arithmétique lui-même, directement observable, et le chemin restant vers s(χ).

### 14.6 Spectroscopie du radical : la loi de recrutement des premiers

L'instrument : matrices composantes séparées (pôle P, archimédien A, une tour T_p par premier), diagonalisation de la somme, projection de chaque composante sur les huit états du bas — le bilan de chaque barreau, avec l'identité Σ = λ_k en contrôle de ligne. (Un masquage de variable dans la branche χ — le paramètre de parité écrasé par une borne de panneau de quadrature — a d'abord produit un faux spectre, attrapé parce que λ_min ne reproduisait pas l'échelle connue : le contrôle interne Σ/λ = 1 valide les projections mais pas l'assemblage ; seule la confrontation externe protège. Consigné en pratique de laboratoire.)

**Le spectrogramme de ζ (µ = 11)** : le fondamental est un interféromètre pôle/archimédien (+1.502/−1.443) ajusté par la seule tour du 2 (−0.058), les autres premiers morts à trois décimales. Chaque barreau suivant recrute exactement un premier de plus — 3, puis 5, puis 7 — le suivant apparaissant en murmure un barreau avant son tour ; l'archimédien change de camp en route (−1.44 → +1.19). **Le spectrogramme de χ₃ (µ = 38, λ_min = 1.83×10⁻⁶⁰ retrouvé)** : même diagonale, le 3 sauté (χ₃(3) = 0), recrutements 2, 5, 7, 11, 13, 17, 19, 23 dans l'ordre, avec les signes des tours modulés par χ(p) — chez χ₃, où χ(2) = −1, la tour du 2 *soutient* le fondamental (+0.345 contre arch −0.347) : les rôles de ζ inversés.

**La loi de recrutement : le barreau k de l'échelle recrute le (k+1)-ième premier χ-supporté.** Elle explique rétroactivement, d'un coup : l'effondrement en six directions du retrait du 2 (§14.5 — la colonne T₂ est d'ordre 1 sur *tous* les barreaux, chez ζ comme chez χ₃ : le 2 est porteur partout) ; le comptage des états quasi-nuls ; et elle recadre la linéarité en µ — chaque puissance de premier nouvelle (p^k ≤ µ) renforce les barreaux qui ont recruté p, et le compte Λ-pondéré des puissances est ψ(µ) ≈ µ : **la linéarité du forage est le théorème des nombres premiers vu du radical.** L'intégration quantitative (comment la profondeur par recrue produit s(χ)) est la prochaine session de théorie — mais elle se fera au microscope, plus à l'aveugle.

### 14.7 Le microscope : la positivité est un quorum

Expérience cumulative à µ = 11 (composantes construites une fois, échelles des sommes partielles), avec deux scénarios préenregistrés — la loi de recrutement littérale (λ_min(P+A+T₂) ≈ 3.6×10⁻⁴⁸) contre l'effondrement vers l'échelle du barreau 1. **Les deux sont faux (treizième exécution)** : P+A est négatif (−0.775), et le reste chaque fois qu'on ajoute une tour — +2 : −0.771 ; +3 : −0.654 (dernière vp à −3.3×10⁻⁵) ; +5 : −0.517 (−1.7×10⁻⁵) — jusqu'au **dernier premier intérieur à la fenêtre** : +7, et la forme saute d'un coup sur l'échelle complète exacte (3.58×10⁻⁴⁸, 5.67×10⁻⁴¹, 2.03×10⁻³⁴, 1.73×10⁻²⁸, aux trois chiffres près) ; la tour du 11, assise au bord de fenêtre où θ s'annule, ne change rien.

**Trois lectures.** Un : *la positivité est un quorum* — un produit d'Euler incomplet dans la fenêtre viole la positivité (les valeurs propres négatives résiduelles sont l'écho exact des pseudo-zéros hors-ligne de la campagne 4 : même phénomène, vu du radical), et la profondeur n'est pas décomposable en contributions par premier : c'est une propriété collective du consensus complet, ce qui explique en dernière instance l'obstruction du §14.5 et l'irréductibilité du chaînon 2. Deux : *l'atterrissage sur le rasoir* — le quorum atteint, la forme ne devient pas robustement positive mais se pose à 10⁻⁴⁸ du zéro : la criticité de l'hypothèse de Riemann n'est pas approchée par la troncature, elle y est déjà, à chaque µ, dès que la fenêtre est arithmétiquement complète. Trois : la loi de recrutement du §14.6 garde son sens comme *organisation interne* de la forme complète (qui siège sur quel barreau), mais l'existence de l'échelle est un fait de quorum — architecture et existence sont deux questions distinctes, et c'est la seconde qui porte le contenu de RH.

### 14.8 Les deux lemmes à l'épreuve : κ se dissout, le profil survit

Campagne de précision sur les lemmes candidats : échelles étendues à dix barreaux (ζ à µ = 16 base 71 ; χ₃ à µ = 38 base 75 ; χ₄ base 69), ajustements à trois paramètres (κ, c, constante) par échelle contre la référence de Fuchs — validée au préalable contre notre Nyström à 1%. En chemin, réplication accidentelle du quorum : le pipeline ζ lancé à µ = 38 avec sa liste de factorisation s'arrêtant à 23 (premiers 29, 31, 37 manquants) donne λ_min = −0.575 — un produit d'Euler incomplet viole, comme le §14.7 l'exige.

**Verdict : le lemme κ se dissout (quatorzième exécution).** Les ajustements sont excellents (RMS ≈ 0.3 sur des niveaux jusqu'à 167, résidus ± 0.4 sur neuf à dix barreaux) mais les κ ajustés ne se transfèrent pas : 3.46 (ζ), 4.48 (χ₃), 5.37 (χ₄) à c libre, contre 2.85 à c contraint (§14.3) — trois paramètres suffisent à épouser toute suite lisse, la qualité du fit ne prouvait rien, et « e ou 3 ? » était une question mal posée : **le modèle Slepian-puissance n'a pas d'exposant bien défini**. Le §14.3 est rétrogradé une seconde fois, définitivement.

**Ce qui survit, et devient l'unique lemme candidat : le profil Δ(ℓ) sans modèle** du §14.2 — l'effondrement des 33 barreaux de quinze fonctions L sur une courbe espacement-niveau unique (± 12%), fait empirique indépendant de toute paramétrisation, ζ indistinguable des χ à niveau égal. C'est lui qu'une preuve d'analyse harmonique doit viser : non pas « l'échelle est un Slepian à la puissance κ », mais « l'espacement des barreaux est une fonction universelle du niveau, indépendante du caractère » — énoncé plus faible, mieux mesuré, et vrai autant que nos données portent.

## 15. Formalisation du quorum

**Cadre.** Fenêtre W_L = fonctions test paires à support dans [−L/2, L/2], µ = e^L. Composantes de la forme de Weil semi-locale : P (pôle), A (archimédien), et pour chaque premier p ≤ µ la forme de tour T̂_p(f) = Σ_k Λ(p^k) p^(−k/2) · (f⋆f)_sym(k log p). Forme partielle Q_S = P + A − Σ_{p∈S} T̂_p ; forme complète Q = Q_{P(µ)}.

**Conjecture du quorum (forme nette, vérifiée à µ = 11).** Pour tout sous-ensemble propre S des premiers intérieurs à la fenêtre, Q_S a une valeur propre négative d'ordre 1. Vérification complète des quatre délétions simples, dans un tableau unique pour lever toute ambiguïté entre la mesure spectrale et la borne certifiée du théorème (S désigne l'ensemble *conservé*) :

| p retiré | S conservé | λ_min(Q_S) mesuré | borne certifiée Q_S(w_S) ≤ |
|---|---|---|---|
| 2 | {3,5,7} | −0.542 | −0.5421 |
| 3 | {2,5,7} | −0.68 | −0.6804 |
| 5 | {2,3,7} | −0.71 | −0.7101 |
| 7 | {2,3,5} | −0.517 | −0.5168 |

(le 11, au bord de fenêtre où θ s'annule identiquement, est extérieur de fait).

**Lemme A (élémentaire, prouvé).** Chaque forme de tour est indéfinie sur W_L dès que p a une puissance intérieure : pour x = k log p ∈ (0, L), prendre f = bosse en u₀ + bosse en u₀+x donne (f⋆f)(x) > 0 ; changer le signe de la seconde bosse donne (f⋆f)(x) < 0. Deux lignes, aucun contenu arithmétique — l'indéfini est gratuit ; tout le contenu est dans *où* vivent les directions négatives.

**Réduction au radical (mesurée exacte, quinzième exécution en passant).** La direction violatrice w de Q_∖2 vit à 99.4% dans le quasi-radical de Q (masses 0.541/0.143/0.156/0.097/0.051/0.006 sur les six barreaux, bulk 0.006), avec Q(w) = 7.7×10⁻⁵ et T̂_2(w) = −0.5422 = λ_min à quatre chiffres : la perturbation au premier ordre est exacte, car Q|_radical ≈ 0. La prédiction « négativité assistée par le bulk » est morte : **λ_min(Q_∖p) = λ_min(M_p) + O(10⁻⁴), où M_p est la matrice (dim ~6) de la tour de p restreinte au radical** — diagonale positive (les barreaux recrutent p en soutien), hors-diagonales gagnantes (les recouvrements oscillants entre barreaux).

**L'objet formel.** Sur le radical, Σ_p M_p + M_pôle + M_arch = diag(λ) ≈ 0 : **une résolution de zéro en matrices toutes indéfinies, telle que toute somme partielle garde une valeur propre négative**. Le quorum, formalisé : aucune sous-collection de la résolution n'atteint la positivité. Ce qui reste pour une preuve : le lemme B — pour tout premier intérieur p, M_p a une valeur propre négative — énoncé de dimension finie, mesurable pour chaque p (fait ci-dessus), et vraisemblablement attaquable par la structure de recrutement (les hors-diagonales ⟨v_j|T̂_p|v_k⟩ sont des recouvrements oscillants calculables). La positivité de Weil apparaît ainsi, à chaque échelle, comme un équilibre de termes tous individuellement violents — et RH comme l'affirmation que cet équilibre ne penche jamais du mauvais côté.

### 15.2 Le lemme B : preuve certifiée à µ = 11 et mécanisme du silence

Les quatre matrices M_p (tours restreintes au radical à huit états) sont calculées exactement. Valeurs propres minimales : −0.541 (p = 2, contre −0.542 pour Q_∖2 : la réduction revérifiée), −0.634, −0.594, −0.322. **Chaque négativité est certifiée par un seul mineur 2×2**, avec des marges de 0.10 à 0.19 contre des erreurs de quadrature < 10⁻⁸ : le lemme B est prouvé à µ = 11 au sens assisté par ordinateur.

Le motif des certificats est la découverte : chaque paire certifiante apparie un **barreau silencieux** (diagonale ≈ 0 : le barreau n'a pas encore recruté p — tour_3 sur le barreau 0 : +0.000 ; tour_5 sur les barreaux 0-2 ; tour_7 sur 0-4) et un **barreau parlant**, avec un couplage hors-diagonal d'ordre 0.4 (recouvrement oscillant, aucune symétrie ne l'annule). Or [[ε, b],[b, a]] a une valeur propre négative dès que b² > ε·a — automatique quand ε ≈ 0. D'où la stratégie du cas général, en deux énoncés d'analyse harmonique : (B1) *silence diagonal pré-recrutement* — pour j < k(p), (v_j ⋆ v_j)(log p) ≈ 0, ce qui est la teneur microscopique de la loi de recrutement ; (B2) *le couplage survit au silence* — (v_j ⋆ v_k)(log p) ≠ 0 pour un barreau parlant k. Le silence est diagonal seulement : un premier muet sur un barreau mais qui lui parle depuis un autre crée une direction négative. Le quorum général suivrait de B1 + B2 + la réduction au radical (§15) — trois énoncés dont aucun ne mentionne RH.

**Vérification exhaustive et statut épistémique.** Les 16 sous-ensembles de {2,3,5,7} sont mesurés : tout sous-ensemble propre est négatif (λ_min de −0.52 à −1.15 — non monotone : {5,7} = −1.15 fait pire que l'ensemble vide, un premier sans ses prédécesseurs aggrave), le complet atterrit à +3.58×10⁻⁴⁸. La logique de réduction est par ailleurs rigoureuse dans le sens utile : par restriction de Rayleigh, λ_min(Q_S) ≤ λ_min(M_S|radical) + λ_max(Q|radical) ≤ λ_min(M_S) + 10⁻¹³ — donc un M_p certifié négatif entraîne rigoureusement la violation. **Ce qui manque pour un théorème** : (a) l'arithmétique d'intervalles — nos erreurs sont contrôlées empiriquement (validations croisées, reproductions à 10⁻⁴⁸), pas par des bornes prouvées ; les entrées étant des sommes finies et des intégrales 1D de fonctions explicites, la certification par intervalles est un projet fini et faisable ; (b) la portée — µ = 11 et ζ seulement, la conjecture étant universelle ; (c) B1/B2. Statut honnête : lemme A = théorème (trivial) ; quorum à µ = 11 = fait numérique exhaustivement vérifié, promouvable en théorème assisté par ordinateur au prix de (a) ; quorum général = conjecture munie d'une stratégie. Dans toute communication : « vérifié », jamais « démontré ».

### 15.3 Phases 1-2 exécutées : le quorum certifié

Le moteur (`theoreme_quorum.py`, 7 secondes) : les sept matrices composantes en arithmétique de boules Arb — tours et pôle par formes closes et intégrales entières, archimédien par quadrature rigoureuse sur [10⁻¹⁵, L] plus queue bornée (|θ'| ≤ élémentaire) — rayon maximal 9.4×10⁻¹¹ sur 1128 paires. Témoins : vecteurs propres float64 gelés (leur précision est indifférente, le quotient certifié arbitre). **Résultat : les quinze quotients de Rayleigh des sous-ensembles propres sont certifiés négatifs**, marges de 0.52 à 1.15 contre des enclos de ~10⁻⁹ — et le contraste de contrôle est parfait : le quotient du produit complet ressort non certifiable à +0.0000, le rasoir à 10⁻⁴⁸ étant invisible à cette précision, comme il se doit (notre énoncé ne revendique pas, et ne peut pas revendiquer, le côté positif).

**Statut honnête : le théorème est calculé, pas encore écrit.** *[Mise à jour du 31.08 au soir : dépassé — la phase 3 est écrite (appendices A et B dérivés en entier), relue par l'auteur et corrigée (v2) ; voir les étapes (70) à (76) du journal. Le paragraphe est conservé tel quel, principe du carnet.]* Ce qui existe : une preuve certifiée de « pour les formes bilinéaires Q_S définies par la table d'appariement θ, tout sous-produit d'Euler propre de la fenêtre µ = 11 admet un témoin explicite négatif ». Ce qui manque (phase 3, travail humain) : la dérivation manuelle autonome de la table θ (convolutions de cosinus, élémentaire, validée à 10⁻²⁶ mais une preuve l'exige en appendice) — qui identifie Q_S à la forme de Weil partielle et donne à l'énoncé son sens arithmétique — plus le lemme de queue en deux lignes et la rédaction. Après quoi : « Proper sub-Euler products violate Weil positivity on the window [−½log 11, ½log 11]: certified witnesses » sera, sauf erreur de rédaction, le premier théorème né de ce fil.

### 15.5 Le théorème généralisé : trois échelles, deux fonctions L, 340 certificats

Le moteur paramétré (`quorum_general.py` : µ, base, ζ ou χ₃ — pôle débrayé, tours signées, archimédien Frullani pour χ) a étendu la certification en trois tirs de 8 à 14 secondes chacun. **χ₃ à µ = 11** (premiers supportés {2,5,7}, la tour du 3 nulle par caractère et celle du 11 par bord) : 7/7 propres certifiés négatifs (pire −0.107, plus violent −0.917) — **le quorum tient sans pôle** : ce n'est pas un phénomène du pôle de ζ mais du produit d'Euler. **ζ à µ = 16** : 63/63 (pire −0.360, plus violent −1.424). **ζ à µ = 22** : 255/255 (pire −0.331, plus violent −1.864). Dans les trois cas, le complet reste non certifiable à +0.000000, comme il se doit.

Structure quantitative émergente, cohérente avec la loi de recrutement : la violation la plus douce est systématiquement la délétion du **dernier premier recruté** (sans 7 / sans 13 / sans 19 : −0.52 / −0.36 / −0.33 — le nouveau venu porte de moins en moins), la plus violente est toujours un paquet de **tardifs privés de leurs précoces** ({5,7} à µ=11, {3,11,13} à µ=16, {11,13,17,19} à µ=22). Total cumulé du théorème : **340 sous-produits propres, 340 certificats de violation, zéro exception** — tables complètes dans `quorum_cert_*.txt`, note #3 mise à jour en conséquence.

### 15.6 Le crochetage commence : la moitié positive, certifiée

Le théorème du quorum certifiait la violation de tout sous-produit ; la positivité du produit complet restait un nombre flottant. Elle est maintenant un fait démontré. La Cholesky directe en boules meurt au pivot 14 (le conditionnement ~10⁴⁸ dévore les rayons — échec instructif, consigné) ; la serrure latérale passe : **congruence + Gershgorin + Sylvester** — V = vecteurs propres *flottants* (dps 100, précision indifférente à la rigueur), M = VᵀQV certifiée en boules (entrées de Q à rayons ≤ 10⁻⁵⁵, dps 90, queue ε = 10⁻⁶⁰), M strictement diagonale-dominante positive sur les 47 lignes ⇒ M ≻ 0 ⇒ V inversible ⇒ Q ≻ 0. La ligne critique est le rasoir lui-même : M₀₀ = 3.58317×10⁻⁴⁸ ± 3×10⁻⁵⁴ contre une somme hors-diagonale ≤ 8.5×10⁻⁵⁴. 152 secondes (`positivite_certifiee.py`).

**Ce que c'est** : à notre connaissance la première vérification *certifiée* du critère de positivité de Weil sur une fenêtre — le théorème du quorum acquiert ses deux moitiés à µ = 11 (tout sous-produit propre viole ; le produit complet est défini positif, posé à 3.58×10⁻⁴⁸ du zéro avec barres d'erreur à 10⁻⁵⁴) — et la preuve que la machinerie traverse un conditionnement de 10⁴⁸. **Ce que ce n'est pas** : un progrès sur RH en soi (positivité à fenêtre fixe = vérification finie d'une condition nécessaire). **Ce que ça ouvre** : la décomposition certifiée exhibe Q comme somme de 47 carrés explicites — l'objet « identité ou rien » du graal, tenu en main à échelle fixe. Prochain coup de crochet : la structure de ces carrés — les directions du haut convergent-elles vers les évaluateurs de zéros f̂(γ_k) ? Regarder les zéros de ζ émerger d'une factorisation purement arithmétique, la convergence de Groskin vue du côté somme-de-carrés.

## 16. Le crochetage : MUSIC sur la forme de Weil, ou les zéros émergent du radical

Deux prédictions préenregistrées sur l'identité Q = Σ_γ 2ĉ(γ)ĉ(γ)ᵀ, où ĉ(γ) est l'évaluateur de zéro en forme close (η̂_n(γ) = √(2/L)·sin(γL/2)·2γ/(γ²−ω_n²) — un noyau de Dirichlet).

**P1, confirmée : la formule explicite comme identité matricielle, avec son horizon.** La reconstruction Q_K = Σ_{k≤K} 2ĉ(γ_k)ĉ(γ_k)ᵀ contre notre Q *construit par les premiers* : résidu 31% à K=35 (γ=112), **8.9% à K=40 (γ=123)** — la chute encadre exactement le bord de bande ω_max = 120.53 — puis queue algébrique lente (5.1% à K=60, γ=163 : les lobes en 1/(γ²−ω²) des zéros hors-bande). La matrice des premiers est la matrice de Gram des zéros, vérifiée en norme de Frobenius, horizon mesuré.

**P2, confirmée au-delà de l'espéré : le radical est un sous-espace de bruit MUSIC.** Rigoureusement, Q(v) = λ force |v̂(γ_k)| ≤ √(λ/2) pour tout zéro : chaque vecteur quasi-nul s'annule en Fourier sur *tous* les zéros à portée — chaque barreau est un détecteur de zéros de précision √λ. Le spectre MUSIC ‖ĉ(γ)‖²/‖P_rad ĉ(γ)‖² (radical à 6 états) donne 38 pics ; le raffinement en section dorée sur les trois barreaux les plus profonds (λ ≤ 2×10⁻³⁴) retrouve **les douze premiers zéros à 10⁻¹⁹-10⁻²⁰ près** (γ₁ = 14.1347251417 à 9×10⁻²⁰), et 30 des 40 zéros en bande (les derniers, près du bord, passent sous le seuil). Une matrice 47×47 bâtie de cinq premiers, d'un pôle et d'un terme archimédien contient les zéros de Riemann à vingt décimales.

**Lecture.** La récupération des zéros depuis la forme tronquée est le phénomène de Groskin (convergence superexponentielle) — notre apport est la lentille : (i) la borne-mécanisme |v̂(γ)| ≤ √(λ/2), qui transforme la profondeur de l'échelle en précision de localisation, exponentielle contre exponentielle ; (ii) la formulation sous-espace (MUSIC), qui fait du radical l'objet dual des zéros ; (iii) la jonction avec la loi de recrutement : chaque barreau recrute un premier *et* annule sa transformée sur tous les zéros — la dualité premiers↔zéros comme fait de sous-espaces, un premier par barreau, un détecteur par premier. Le prochain cran de la serrure : la version Dirichlet (le radical de χ₃ doit détecter les zéros de L(s,χ₃)) et la question structurelle — les carrés du haut de la décomposition certifiée sont-ils *individuellement* proches des ĉ(γ_k), ou seulement leur enveloppe ?

### 16.2 Les deux crans suivants : l'individualité vit dans le bruit, et s(χ) est un exposant de lisibilité

**B — les carrés du haut : enveloppe exacte, individus inexistants (préenregistrement confirmé).** La masse des évaluateurs de zéros dans l'espace du haut vaut 1.000000 pour tout zéro en bande (conséquence de la borne |v̂_rad(γ)| ≤ √(λ/2) : le radical n'en retient rien), mais aucun vecteur propre du haut n'est un zéro individuel : recouvrements maximaux 0.50-0.93 avec des seconds presque égaux (0.932 contre 0.899 pour le premier), mélanges pilotés par la cohérence du cadre des noyaux de Dirichlet (voisins à 0.19 médian, pics à 0.84 — espacement ~2.3 contre largeur ~2.6). **L'asymétrie structurelle : l'information de sous-espace vit dans le signal, l'individualité des zéros vit dans le bruit** — c'est chaque barreau du radical qui s'annule sur chaque zéro, pas chaque carré du haut qui en épouse un.

**A — le détecteur Dirichlet, avec sa leçon de méthode.** Premier tir raté instructif : en admettant dans le « bruit » un quatrième vecteur à λ = 0.12 (|v̂| ≤ 0.25 — qui ne s'annule sur rien), le spectre MUSIC de χ₃ se décale de +8 à +10 et engloutit les premiers zéros : la borne √(λ/2) est le *critère d'admission* au sous-espace de bruit, pas une décoration. Restreint aux deux barreaux légitimes (λ ≤ 5.6×10⁻¹⁰) : **γ₁(χ₃) = 8.039737156 retrouvé à 2.5×10⁻⁹**, γ₂ à 1.1×10⁻⁸, puis dégradation en échelle — 2.7×10⁻⁷, 3.3×10⁻⁶, 1.0×10⁻⁵, 10⁻⁴, 10⁻³... — qui reflète l'échelle des valeurs propres elle-même : la masse résiduelle des barreaux profonds se concentre sur les zéros hauts, la couverture s'amincit avec k.

**Le recadrage qui en sort.** ζ à µ = 11 (échelle à 48 chiffres) donne les zéros à 10⁻¹⁹ ; χ₃ à µ = 11 (échelle à 16 chiffres) les donne à 10⁻⁹ : la précision de localisation est ~e^(−sµ/2). **La vitesse de forage s(χ) est l'exposant de lisibilité des zéros de L(s,χ) par la fenêtre arithmétique** — toute la phénoménologie de profondeur (la carte, γ₁, l'écart, la parité) se relit comme la théorie de « quelles fonctions L sont faciles à lire depuis les premiers ». Prochain cran naturel : la loi précision-µ (χ₃ à µ = 38 devrait donner ~30 chiffres), et le pont avec Groskin rendu quantitatif.

### 16.3 La loi de précision fermée : erreur ≈ e^(−sµ), et l'hyper-nullité du radical

Étalon indépendant γ₁(χ₃) à 60 chiffres (Hurwitz, dps 130 : 8.0397371556814666817136232141729658027930102673860614272709...), puis localisation MUSIC à d=1 sur la forme µ=38 (base 65, dps 94, barreau du fond λ = 7.3×10⁻⁶¹). **Erreur vraie : 4.16×10⁻⁵⁸** — cinquante-sept décimales du premier zéro de L(s,χ₃) depuis quatorze premiers et un terme archimédien. La préenregistration (10⁻³³ à 10⁻²³) est pulvérisée par le haut, et le mécanisme se referme exactement : erreur = |v̂₀(γ₁)|/|dv̂₀/dγ| = 6.4×10⁻⁶⁰/0.0154 = 4.16×10⁻⁵⁸, prédiction = mesure à trois chiffres.

**L'hyper-nullité, fait structurel neuf.** |v̂₀(γ₁)| = 6.4×10⁻⁶⁰ contre la borne totale √(λ/2) = 6×10⁻³¹ : la transformée du barreau à γ₁ est 10²⁹ fois sous sa borne de masse. La masse λ = Σ 2v̂(γ_k)² ne vit donc pas sur les zéros intérieurs — elle est refoulée aux zéros de la frontière de bande (ω_max = 110.5) : **l'annulation du radical est hyper-efficace à basse fréquence et décharge son résidu au bord** — le front de moisson (§14) vu du côté des zéros, et la raison pour laquelle λ mesure la fuite frontalière, pas la qualité intérieure.

**La loi de précision, corrigée et mesurée.** Entre µ = 11 (erreur 2.5×10⁻⁹) et µ = 38 (4.16×10⁻⁵⁸) : −ln(erreur) passe de 19.8 à 132.1, pente **4.16 ≈ s(χ₃) = 4.00** — pas e^(−sµ/2) mais **e^(−sµ), la pleine profondeur** : v̂(γ₁) suit λ lui-même (hyper-nullité), pas √λ. La vitesse de forage s(χ) est le coût par décimale du premier zéro : la carte de profondeur du §13 est, mot pour mot, la table des taux de lecture des zéros depuis l'arithmétique.

### 16.4 Le spectre de fuite du radical : une loi exponentielle en distance au bord

Mesure directe de |v̂₀(γ_k)| sur 55 zéros de ζ à 55 chiffres (zetazero, dps 60 — le cache 16 chiffres de χ₃ rendait le profil illisible, d'où le retour à ζ), forme µ = 11 à dps 50. **Trois faits.** (i) *Le profil est exponentiel dans la distance au bord* : ln|v̂₀(γ)| croît linéairement de γ₁ (7.8×10⁻⁴⁷ — 10²² sous la borne de masse) au bord de bande (1.4×10⁻²⁶ à γ = 112), taux mesuré **τ ≈ 0.48 par unité de fréquence** — l'hyper-nullité du §16.3 n'est pas un accident de γ₁, c'est la loi |v̂₀(γ)| ≈ e^(−τ(ω_max−γ)+const) évaluée en profondeur ; l'identification de τ (0.48 pour ζ à µ=11 ; contre L/2 = 1.20, s/µ = 1.06...) reste ouverte. (ii) *Le pic est frontalier* : maximum du profil à γ = 124.3, juste au-delà du bord ω_max = 120.5 — prédiction préenregistrée confirmée. (iii) *Le budget ne se referme pas dans la bande* : Σ 2v̂₀² sur 55 zéros = 42% de λ₀ seulement ; le reste vit dans la traîne algébrique hors-bande (plateau oscillant ~10⁻²⁵ jusqu'à γ = 153 et au-delà) — **λ mesure la fuite frontalière plus sa traîne, jamais la qualité intérieure**. Bonus d'universalité : les barreaux 1 et 2 suivent des profils parallèles (même τ), décalés de l'échelle — un seul spectre de fuite pour tout le radical, scalé par la profondeur du barreau.

Lecture pour la serrure : la difficulté de la positivité tronquée vit *au bord de bande* — l'intérieur est arbitrairement propre (exponentiellement), et tout le prix se paie à la frontière où la fenêtre cesse de résoudre. Une preuve de positivité devrait donc contrôler exactement un voisinage de ω_max — le front de moisson, une fois de plus, mais cette fois comme *localisation du problème* : le rempart de RH, vu de cette fenêtre, est une bande de largeur O(1/τ) autour du bord.

### 16.5 La campagne τ : intrinsèque, arithmétique, et approximativement γ₁/30

D'abord un artefact des familles nouvelles, attrapé par violation de borne : les trois premiers profils de contrôle étaient de la bouillie (RMS 4-6, « pentes » négatives, et |v̂₀(γ₁)| = 2.92×10⁻¹⁸ *identique sur trois bases* — au-dessus de la borne rigoureuse √(λ/2) = 9.6×10⁻²⁵, ce qui condamnait la mesure, pas le monde). Diagnostic : le résidu ‖Sv−λv‖ = 10⁻⁶¹ innocentait le vecteur ; le coupable était le **chargement des zéros avant le réglage de précision** (mp.mpf tronque à 15 chiffres ; 2.92×10⁻¹⁸ = pente × 10⁻¹⁶ exactement). Neuvième famille d'artefacts : *précision au chargement* — la constante suspecte à travers les configurations est sa signature.

Zéros rechargés proprement (et ceux de χ₃/χ₄ raffinés par Hurwitz à 35+ chiffres), les trois discriminants préenregistrés répondent : **D1** — τ insensible à la base (0.477 → 0.504 quand ω_max croît de 22% : la pente est intrinsèque, seul le pic suit le bord) ; **D2** — τ insensible à µ (0.471 à µ=8 : l'échelle en L exclue) ; **D3** — τ(χ₃) = 0.269 ≠ τ(ζ) = 0.48 : **la mise « grandeur de fenêtre » est morte (seizième exécution)** — τ dépend de l'arithmétique. Le ratio suggérait τ = γ₁/29.8 (0.0337 et 0.0335 aux deux premiers points) ; le test décisif χ₄ (prédiction 0.202) mesure 0.167 : **la proportionnalité pure meurt à 17% (dix-septième exécution)**. Statut : τ croît avec γ₁ (ordre respecté sur trois fonctions L), loi approchée τ ≈ γ₁/30 à ±20% ; les profils des caractères à µ = 11 sont trop courts pour trancher (échelles peu profondes, RMS 1.7 contre 0.5 pour ζ, courbure visible — la pente locale de ζ décroît de 0.55 à 0.19 le long de la bande, suggérant un profil sous-exponentiel, peut-être quadratique en distance au bord comme le front de moisson le voudrait). Remède chiffré pour la session suivante : profils à µ = 20-38 où les échelles des caractères sont profondes.

### 16.6 Le profil long de µ=16 : courbure réelle, plancher à 56 chiffres, verdict suspendu

Le juge ζ à µ=16 (échelle 1.9×10⁻⁷³, base 71, dps 100) livre trois morceaux. **(i)** L'hyper-nullité y dépasse la précision des zéros : les premières lectures collent au plancher (pente × 10⁻⁵⁵ du cache à 55 chiffres) — |v̂₀(γ₁)| < 10⁻⁵⁶, et le vrai fond est invisible même à cette précision : mesurer le profil intérieur de µ=16 exige des zéros à 90+ chiffres (liste de courses de la prochaine session ; zetazero les fournit, ~5-8 min pour 40). **(ii)** Sur le segment propre (γ ∈ [85, 155], ~16 décennies), les pentes locales décroissent vers le bord (0.55 → 0.43) — même dérive qu'à µ=11 (0.55 → 0.19 sur sa bande) : la **signature qualitative d'un profil quadratique-de-front** (pente ∝ distance au bord, comme la moisson le voudrait), mais l'accord quantitatif échoue (le point d'annulation extrapolé déborde le bord d'un tiers dans les deux cas) : ni l'exponentielle pure ni la quadratique pure ne gagnent — verdict suspendu aux zéros profonds. **(iii)** La pente de mi-bande ~0.5 coïncide entre µ=11 et µ=16 : le taux local est **universel en µ** sur profil long, confirmant D2 dans un régime bien plus exigeant.

### 16.7 Les zéros profonds tranchent : la loi d'extrémité |v̂₀(γ₁)| ≈ C·λ₀

Quarante-cinq zéros de ζ à 85 chiffres (zetazero, 2 secondes — la liste de courses coûtait moins cher que prévu), et le profil de µ=16 se lit jusqu'au fond : **|v̂₀(γ₁)| = 4.7×10⁻⁷²**, entre les deux prédictions préenregistrées (10⁻⁷⁰ exponentiel, 10⁻⁷⁵ quadratique). Sur la forme : le quadratique gagne statistiquement (RMS 0.325 contre 0.693) mais la courbure est douce (pentes 0.64 → 0.49) et aucun modèle pur ne colle ; en route, la « µ-indépendance » de τ (D2, §16.5) meurt — τ_eff(µ=16) = 0.56 contre 0.48 à µ=11, et les pentes locales diffèrent à γ égal : l'indépendance apparente était un artefact de gammes plafonnées (**dix-huitième exécution**).

**La vraie loi, lue en recoupant tout le §16 : |v̂₀(γ₁)| ≈ C·λ₀ — proportionnel à λ, pas à √λ.** Quatre configurations, soixante ordres de grandeur : µ=16 ratio 24 ; µ=11 ratio 22 ; χ₃ µ=38 ratio 8.8 ; χ₃ µ=11 ratio 7 — C ∈ [7, 25] partout. C'est la racine unique du chapitre : l'hyper-nullité (la part de masse de γ₁ vaut ~λ² : rien), la loi de précision e^(−sµ) pleine profondeur (erreur = |v̂|/pente ~ λ), et le profil de fuite lui-même, qui interpole de ~λ à γ₁ vers ~√λ au pic frontalier — d'où **τ ≈ sµ/(2ω_max)**, vérifié à 6% sur les deux ζ propres (0.45/0.477 à µ=11 ; 0.53/0.56 à µ=16 ; les caractères, aux profils courts et bruités, restent à revisiter avec cette grille). La question théorique qui reste est donc unique et nette : *pourquoi la transformée au premier zéro est-elle d'ordre λ ?* — une relation d'auto-cohérence du vecteur fondamental (sa valeur en γ₁ pèse dans λ qui pèse dans sa valeur...) qui sent le point fixe, et qui est le prochain énoncé à formaliser.

## 17. Formalisation du point fixe : la dualité de Gram

**Proposition A (démontrée).** Soit v₀ le vecteur fondamental de Q = Σ_k 2ĉ(γ_k)ĉ(γ_k)ᵀ, λ₀ sa valeur propre, et v̂ = (v̂₀(γ_k))_k la suite de ses transformées aux zéros. Alors v̂ est vecteur propre du Gram (infini) des évaluateurs, G_{jk} = ⟨ĉ(γ_j), ĉ(γ_k)⟩, avec la même valeur propre : **G·v̂ = (λ₀/2)·v̂**. *Preuve* : de Qv₀ = λ₀v₀ vient v₀ = (2/λ₀)Σ_k v̂_k ĉ_k ; apparier avec ĉ_j donne v̂_j = (2/λ₀)[Gv̂]_j. ∎ — Le radical en espace de fonctions et le quasi-noyau du Gram des zéros sont *le même objet* ; la loi d'extrémité devient : pourquoi la composante γ₁ du vecteur fondamental de G est-elle d'ordre √λ₀ relatif (soit λ₀ absolu) ?

**La conspiration de la queue (mesurée).** La vérification tronquée de l'identité est impossible par construction, et cette impossibilité est un fait : sur 45 zéros, [Gv̂]₁ ≈ 10⁻²⁸ contre une cible (λ/2)v̂₁ ≈ 10⁻⁹⁴ — **les zéros au-delà du 45ᵉ annulent l'action du Gram en bande sur 66 chiffres** (98 chiffres à µ = 16). La suite v̂, calculable depuis les premiers seuls, encode donc une dépendance linéaire quasi-exacte entre les évaluateurs de zéros s'étendant loin hors bande. L'identité elle-même est acquise indirectement par le résidu propre (‖Sv−λv‖ = 10⁻⁶¹).

**Le genou de Nyquist : mort (dix-neuvième exécution).** Le seuil calculable γ* = 2πµ (où la densité des zéros N′(γ) = log(γ/2π)/2π atteint le taux de Nyquist L/2π de la fenêtre — dérivation d'une ligne) prédisait des ruptures de pente à 69.1 (µ=11) et 100.5 (µ=16) ; les ajustements à deux segments mesurent 94.7 et 87.4 — ni les positions ni même l'ordre en µ. Le mécanisme de clairsemage sous-Nyquist reste une heuristique séduisante et fausse comme prédicteur du genou. **État du problème ouvert** : la loi d'extrémité |v̂₀(γ₁)| ≈ C·λ₀ (C ∈ [7,25], quatre configurations, soixante ordres) est désormais posée dans le bon cadre — une propriété du vecteur fondamental du Gram des zéros — avec sa question nette : d'où vient le second ordre de petitesse en γ₁ ? C'est le lemme candidat le plus jeune et le mieux mesuré du programme, aux côtés de Δ(ℓ) et B1/B2.

## 18. La campagne des lemmes en pull requests : les trois caractères manquants, et la mort de la carte

L'auteur a empaqueté la campagne en six PR (couture, quatre notes de lemmes — Δ(ℓ) relu en rampe-plateau, s = κ_win·Λ(χ), B1/B2 toute-échelle, les 47 carrés — et l'instanciation des trois caractères retenus hors carte). Revue : noyau Kronecker vérifié cas par cas (règle mod 8, flip négatif, auto-tests), scanner conforme au pipeline dscan, zéros moissonnés **contre-vérifiés indépendamment par Hurwitz à 7 chiffres** (γ₁(χ₋₈) = 3.576154837, γ₁(χ₋₂₃) = 2.871339849). Les six PR sont mergées.

**Le verdict out-of-sample, aux fenêtres d'uniformisation (µ jusqu'à 38).** χ₋₈, contrôle interne : 1.30 en deux fenêtres basses, cohérent transitoire avec le 1.47 du jumeau pair — PASS. χ₋₂₀ : sécantes 0.26 → 0.40 → 0.54 → 0.68 *encore montantes* à µ=38 (transitoire de type χ₁₅) — déjà +19% au-dessus de sa prédiction 0.57 : kill probable par le haut, stationnarité à exiger vers µ ≥ 50. **χ₋₂₃, le vrai out-of-sample : sécantes 0.49 → 0.53 (+8%, quasi stationnaires), s ≈ 0.54 contre 0.76 prédit — −29% : le critère préenregistré (>20%) s'applique, LA CARTE TELLE QU'ÉCRITE EST MORTE (vingtième exécution).**

La structure des deux échecs est le vrai enseignement : ils tombent exactement sur les deux axes que la note de profondeur publiée cartographiait comme fragiles — le petit écart (γ₂−γ₁(χ₋₂₃) = 1.34, le plus petit de la famille : l'axe de χ₁₇) et le coin D-fort/γ₁-petit (l'axe de χ₁₂). La carte meurt où sa documentation l'annonçait fragile : la *carte des modes d'échec* était, elle, correcte — et c'est elle qui survit. Statut final de la loi de profondeur : une carte à ~10% dans son régime d'entraînement, systématiquement fausse hors régime, avec trois modes d'échec documentés et désormais confirmés out-of-sample.

## 19. Le bloc 5×5 en Arb : une enclosure, pas une égalité

Suite naturelle des 47 carrés après le merge. `code/squares47_arb.py` : mêmes boules que `positivite_certifiee.py` pour le côté premiers (rayons 10⁻²⁴ sur le bloc N₀=4), zéros hp à 85 chiffres plus la queue float64 jusqu'à γ=811, enveloppe non signée 3.18×10⁻² ajoutée en rayon. **Quinze boules sur quinze contiennent 0.** Borne supérieure certifiée par entrée : 3.61×10⁻², dont 3.18×10⁻² d'enveloppe. Le côté premiers n'est plus le goulot ; la queue non oscillante l'est. L'identité sur V est un enclosure Arb du bloc 5×5, pas encore le rasoir 10⁻⁴⁸.

## 20. B1/B2 pour ζ à µ=16 : six mineurs sur six, dès que R suit le recrutement

Le lock laissé ouvert après χ₋₈ : assembler Q(ζ, µ=16) et restreindre chaque T_p au bas du spectre. `code/lemma_B_mu16.py`. À N=37, R=8 : 4/6 (11 et 13 muets). À N=29, R=12 : **6/6**, les deux premiers du bord parlent sur les barreaux 7-11. Le quorum à cette échelle n'est pas un échec de B1/B2, c'est un R trop court pour k(p) des bords. Même motif qu'à µ=11, fenêtre suivante, à condition d'emmener le radical assez loin.

## 21. La carte à deux variables meurt plus fort : χ₋₂₃ est impair et forage comme pair

Candidat restant après le kill §18 : s = c γ₁^α ρ^[impair]. Ajusté sur les 13 lignes stationnaires de la note de profondeur : s = 0.171 γ₁^1.327 · 1.54^[impair], rms d'entraînement 21%. Hold-out : χ₋₈ +10%, χ₋₂₀ +21%, **χ₋₂₃ +97% (1.06 contre 0.54)**. La carte à deux variables meurt plus fort que la carte à quatre. Diagnostic : χ₋₂₃ (γ₁=2.87, impair, s=0.54) est sur le lieu des *pairs* (χ₂₄ᵉ 2.69→0.50, χ₂₁ 2.32→0.58), pas sur χ₁₁ (2.48→1.07). Le facteur de parité est l'axe coupable. Un réajustement γ₁+écart+D sans parité donne 0.45 contre 0.54 (−16%) : diagnostic, pas carte successeur — lu sur le même hold-out. `code/map2.py`.

## 22. Le plateau contre 2πe : χ₃ grimpe 15.88 → 16.92 → 17.07

Lock laissé sur Δ_∞. 2πe ≈ 17.079 est dans les bandes publiées 16.0±1.6 / 16.0±2.1. Échelles χ₃ nouvelles (`scan_s.py`) : µ=16 Δ=15.88 au niveau 40 ; µ=22 Δ=16.92 au niveau 62 ; µ=30 Δ=17.07 au niveau 105. Le barreau le plus profond colle à 2πe à 0.01 nat. Le lock « ça reste à 16 » est mort. 2πe survit ; une base N=45 et un caractère ne le sélectionnent pas. Cran suivant, crible réparé (premiers 37+ manquants = quorum accidentel) : χ₃ µ=38 Δ=16.82 (niveau 129, +0.26 de 2πe) ; χ₄ µ=30/38 Δ=17.65 / 18.16. χ₃ stagne 16.8–17.1 ; χ₄ est au-dessus. Le plateau est l'intervalle [16.8, 18.2], 2πe n'en est plus l'unique occupant.

## 23. χ₋₂₀ à µ=50 : la montée ne déclenche pas le kill

Cinq fenêtres `scan_s.py` : sécantes 0.534 → 0.547 → 0.564 → 0.590 (µ=16,22,32,38,50). Dernière sécante +4% au-dessus de ŝ₄=0.57. La montée est réelle et lente. Le kill à 20% n'est pas tiré. χ₋₂₃ reste la seule mort out-of-sample nette. Le « kill probable par le haut » du §18 se rétracte.


## 24. Le cran Dirichlet de la serrure : le radical de χ₃ détecte les zéros de L(s,χ₃)

Prochain coup de crochet annoncé au §16 : MUSIC sur χ₃. `music_zeros.py chi3 16 36 48 3` (17 s). Trois barreaux de bruit λ = 8.9×10⁻²⁵, 7.0×10⁻¹⁸, 5.7×10⁻¹². Douze pics raffinés contre `zeros_chi3.pkl` (70 zéros, γ₁ Hurwitz) :

γ₁ MUSIC = 8.039737155683 contre 8.039737155681, écart 1.3×10⁻¹². Les six premiers à mieux que 10⁻⁸ ; la précision se dégrade vers le bord (γ₁₂ à 1.3×10⁻⁴), comme pour ζ. Une matrice 37×37 bâtie des premiers de χ₃, d'un pôle et d'un terme archimédien rend les zéros de L(s,χ₃). Le radical n'est pas un artefact de ζ. La serrure s'ouvre du même côté en Dirichlet.


## 25. Les directions du haut : span des évaluateurs en bande, pas un dictionnaire γ₁ ↔ λ_max

Le crochet annoncé après MUSIC-par-le-bas. `code/high_directions.py`, Q côté premiers à µ=11. Cosinus entre vecteurs propres et ĉ(γ_k) normalisés.

À N=13 (ω_max≈31, quatre zéros bien en bande) : le radical est orthogonal à tous les ĉ (cos < 10⁻³). Les trois plus grandes directions collent à γ₁, γ₂, γ₄ avec cos 0.90, 0.84, 0.84. À N=21 (ω_max≈52) : même orthogonalité du radical ; le top-6 vit dans le span des évaluateurs en bande (cos 0.65–0.85), mais λ_max vise γ₁₀ (cos 0.84), pas γ₁. Les carrés du haut *sont* des évaluateurs de zéros. Ils ne sont pas rangés par γ croissant. La serrure s'ouvre sur la structure, pas sur un dictionnaire.


## 26. Le second ordre en γ₁ : |v̂(γ₁)| = C λ, pas √λ

Le bound MUSIC dit |v̂(γ)| ≤ √(λ/2) pour tout zéro. La loi d'extrémité dit |v̂(γ₁)| ≈ C λ avec C ∈ [7,25]. Un ordre de plus.

`code/endpoint_order.py`. ζ à µ=11, N=21 : λ₀ = 1.65×10⁻³⁶, |v̂(γ₁)| = 4.59×10⁻³⁵, **C = 27.8** — au bord haut de la fenêtre publiée. Rapport au bound : |v̂(γ₁)| / √(λ/2) ≈ 5×10⁻¹⁷. χ₃ à µ=16 donne un plancher à 10⁻¹⁸ (base courte) et ne contraint pas C.

Le premier ordre est le bound, saturé là où la masse vit (la frontière). Le second est la fuite jusqu'à γ₁. τ ≈ sµ/(2ω_max) convertit cette fuite en un facteur √λ supplémentaire, d'où λ. La constante C reste un nombre mesuré, pas dérivé.


## 27. Queue signée : l'enveloppe 3×10⁻² était le 1−cos oublié

C(χ₃) reste illisible (cond Q ~ 10⁴⁶, plancher |v̂| ~ 10⁻¹⁸). Le rasoir des 47 carrés, lui, se serre. `squares_tail.py` : hat ~ (2√(2/L)/γ) sin(γL/2), d'où 2 hat hat ~ (4/L)(1−cos(γL))/γ². La queue non signée intégrait la densité × 1/γ² et donnait 3.18×10⁻² à G=811. La queue signée est 1/G + O(sin(LG)/(LG)) : **2.49×10⁻³**, douze fois plus serrée, au niveau du résidu mesuré 2–4×10⁻³. L'enclosure Arb 5×5 passe d'une borne 3.6×10⁻² à une borne ~5×10⁻³. Le rasoir n'est pas 10⁻⁴⁸ ; il n'est plus 3 %.


## 28. Quatre crans en parallèle

**C = κ, conditionnel.** Si le fondamental sature le bound au bord (|v̂|=κ√λ) et si la fuite est τ=sµ/(2ω_max) avec γ₁≪ω_max, alors C=κ. Mesure : C(ζ)=27.8, κ(χ₃)=0.097. Pas le même nombre — aucune fenêtre ne sature le bord *et* résout γ₁ (cond Q ~ 10⁴⁶). La forme est dérivée ; la valeur reste mesurée.

**Enclosure Arb signée.** Queue = décalage 1/G plus rayon 1.5×enveloppe signée. 15/15 boules contiennent 0. Borne certifiée **6.0×10⁻³** (contre 3.6×10⁻² non signée).

**Δ_∞ n'est pas un nombre.** χ₃, ℓ>60 : moyenne 16.94 (2πe−0.14). χ₄ : 17.90 (2πe+0.82). Deux amas, un nat d'écart. 2πe attire χ₃, pas la famille.

**Appariement 1-1.** Greedy sans réemploi, ζ µ=11 N=13, K=4 zéros en bande : (eig 11→γ₁, 0.90), (10→γ₄, 0.84), (12→γ₂, 0.84), (9→γ₃, 0.65). Cos moyen 0.81, min 0.65. Les quatre directions du haut se partagent les quatre évaluateurs, sans collision.


## 29. Δ_∞ n'est pas coupé par la parité

Hypothèse : les deux amas du §28 sont pair / impair. Test : χ₅ pair et χ₈ pair à la fenêtre plateau µ=30, plus χ₅ à µ=38.

χ₅ µ=30, ℓ=68, Δ=17.27 (2πe+0.19). χ₅ µ=38, ℓ=88, Δ=17.99 (2πe+0.92). χ₈ µ=30, ℓ=41, Δ=15.99 — trop peu profond pour le plateau (sµ≈46). χ₅ pair grimpe vers l'amas haut de χ₄, pas vers χ₃. χ₃ impair reste seul à 16.9. La parité n'est pas l'axe. Δ_∞ n'a plus de candidat de coupure dans {parité, 2πe}.


## 30. χ₇ : encore une montée, pas un second χ₃

χ₇ impair, d=−7. Sécante 30→38 : s≈1.67. Plus profond atteint : ℓ=58, Δ=17.34 (2πe−0.26). À µ=30, ℓ=44, Δ=16.23. Même geste que χ₅ : ça traverse 2πe par le bas et ça continue. χ₃ à ℓ comparable (62) était à 16.92 ; χ₇ est déjà à 17.34. Pas un jumeau. Le plateau n'est visible que pour les χ à grand s (χ₃ s=4, χ₄ s≈3) — les autres n'ont pas encore le niveau.


## 31. Appariement 1-1 à N=21 : tient pour K=6, casse à K=8

`match_squares.py 20`. Huit zéros en bande (ω_max=52). Cos moyen 0.60, min 0.14. Les six premiers appariements restent au-dessus de 0.61 (γ₈, γ₂, γ₁, γ₆, γ₃, γ₅). Les deux derniers (γ₄ à 0.30, γ₇ à 0.14) sont du bruit de bord. Le dictionnaire 1-1 n'est pas une base complète : il l'est sur le cœur de bande.

ζ à µ=11, mêmes valeurs propres : Δ du bas = 12.1–12.5 à ℓ=62–69. Encore la rampe 9–13, pas le plateau. Le plateau demande ℓ₀≳80, donc N≳47 ici, l'assemblage certifié — pas cette base.


## 32. Queue synthétique : le biais 4×10⁻³ tombe à 1.5×10⁻³

Peigne de 2975 zéros placés par l'espacement 2π/log(γ/2π) de G=811 à 4000. Contribution 2 ĉĉᵀ : 1.42×10⁻³ sur (0,0), 2.01×10⁻³ sur (0,m), 2.84×10⁻³ sur le bloc n,m≥1. Retranchée aux diffs mesurées (2.15 / 3.04 / 4.30)×10⁻³, il reste (0.73 / 1.03 / 1.46)×10⁻³. Le goulot n'est plus l'enveloppe : c'est G>4000 plus la corrélation des zéros absente du peigne. ζ à µ=16, N=29 sort deux λ négatifs (base trop large à dps 42) ; les barreaux propres donnent encore Δ≈11.7 à ℓ≈88 — rampe, pas plateau.


## 33. Peigne jusqu'à 20 000 : le reste tombe en 1/G, la corrélation ne fait rien

Même peigne, Gmax=4 000 / 10 000 / 20 000. Résidu sur le bloc n,m≥1 : 1.46 / 0.91 / 0.71 ×10⁻³. Jitter type GUE à Gmax=20 000 : 0.72×10⁻³ — identique. La corrélation des paires n'est pas le goulot. Le reste suit 1/G. Un facteur ~1.2 sur le peigne annulerait le biais : 20 % de masse manquent, pas la statistique locale. Prochaine coupe utile : soit G→∞ analytique (Ci, Si), soit le préfacteur des hats hors bande.


## 34. Ce qu'on loupe

Deux faits déjà sous les yeux, jamais posés comme crans.

**La carte sans parité sauve le hold-out.** `map2.py`, modèle γ₁+gap+D : χ₋₂₃ hat=0.45 contre s=0.47 (−4 %), χ₋₈ −7 %, χ₋₂₀ −19 %. Le seuil 20 % n'est pas franchi. La 4-var meurt sur la parité ; la 3-var sans parité passe les trois caractères. On l'avait écrite en passant (« pas une nouvelle carte entraînée »). C'est le successeur empirique.

**Le profil universel Δ(ℓ) survit à mi-échelle et meurt au sommet.** Les rungs 3+ tombent encore dans 9–14 pour χ₃, χ₄, χ₅, χ₇. Les plus profonds, au même ℓ, non : 16.8 / 18.2 / 18.0 / 17.3. « Fifteen L-functions, one ladder » est vrai sur la rampe, faux sur le plateau.

Le 20 % de masse de queue n'est pas une troisième omission : jitter GUE l'a déjà tué comme statistique locale. C'est un préfacteur ou un biais de Qpr.


## 35. La 3-var est un successeur mou

`code/map3.py`. Fit log-log sur les 13 lignes TRAIN :

ŝ = 0.082 · γ₁^{1.342} · gap^{0.880} · D^{-0.180}

Train RMS 17.5 %. LOO RMS 29 % — χ₁₇ +64 %, χ₁₃ +52 %. Hold-out figé : χ₋₈ −7.5 %, χ₋₂₀ −19.1 %, χ₋₂₃ −3.9 %. La variante D-linéaire (e^{−0.106 D}) ne change rien. χ₋₂₃ est sauvé. χ₋₂₀ est sur la ligne de kill. Ce n'est pas une loi serrée. C'est une carte qui ne meurt pas tout de suite.


## 36. χ₋₂₀ se stationnarise à s≈0.58 : la 3-var meurt

Sécantes : 0.534 → 0.547 → 0.564 → 0.590 → **0.582** (50→62, crible jusqu'à 71). Première descente. s se fige vers 0.58. La 4-var prédisait 0.57 (+2 %). La 3-var prédisait 0.44 : 0.44/0.58 − 1 = **−24 %**, au-delà du kill 20 %. Le hold-out « sauvé » du §35 utilisait s=0.55, une sécante trop courte. Une fois s stationnaire, il ne reste plus que χ₋₈ comme succès. La carte successeur meurt sur χ₋₂₀.


## 37. Convergence de la sécante χ₋₂₀ : un revirement, pas un plateau

Points (μ, ℓ₀) : (16, 3.44), (22, 6.65), (32, 12.12), (38, 15.50), (50, 22.59), (62, 29.57).

Sécantes : 0.535, 0.547, 0.563, 0.591, 0.582. Le dernier pas descend de 0.008 ; les montées précédentes étaient 0.013, 0.017, 0.026. C'est un premier revirement, pas une stationnarité.

Modèles :
- ℓ = 0.569 μ − 5.90 (global)
- ℓ = 0.595 μ − 7.77 + 27.5/μ
- s(μ_mid) = 0.614 − 1.58/μ_mid
- Aitken sur les trois dernières sécantes : 0.584

s_∞ habite [0.57, 0.62]. La 3-var à 0.44 est hors de l'intervalle, kill inchangé. La 4-var à 0.57 est *dans* l'intervalle — coïncidence, déjà tuée par χ₋₂₃. Contrôles : χ₋₂₃ déjà plat (0.469→0.473), χ₋₈ encore montant (1.358→1.462).


## 38. Newton–Raphson sur la sécante

Newton : \(x_{n+1}=x_n-f(x_n)/f'(x_n)\). Sans \(f'\), Steffensen = Aitken, déjà calculé.

Sur les triplets de sécantes :
- (0.535, 0.547, 0.563) → 0.499 (encore dans la montée, extrapole trop bas)
- (0.547, 0.563, 0.591) → 0.526
- (0.563, 0.591, 0.582) → **0.584**

Newton à deux points sous le modèle \(s=s_\infty+A/\mu\) :
- paires montantes : \(s_\infty=0.576, 0.617, 0.700\)
- paire du revirement : \(A\) change de signe, \(s_\infty=0.549\)

Le dernier pas casse l'hypothèse monotone. Newton le dit tout de suite : la dérivée empirique n'est plus celle du modèle. Un itéré de plus exige la sécante 62→74. En attendant, le seul Newton stable après le revirement est Steffensen 0.584, déjà dans [0.57, 0.62].

(Les nœuds de Legendre de `scan_s.py` sont déjà Newton ; ce cran porte sur \(s\), pas sur la quadrature.)


## 39. Sécante 62→74 : le 0.582 était un creux

ℓ₀(74)=37.02, λ=8.3×10⁻¹⁷. Sécante 62→74 = **0.622**. Suite : 0.535, 0.547, 0.563, 0.591, 0.582, 0.622. Le 0.582 rebondit. Ce n'était pas le début d'un plateau.

Steffensen (0.591, 0.582, 0.622) = 0.589. Régression linéaire à 7 points : s=0.579. Newton 1/μ sur la dernière paire : s_∞=0.809 (A=-12.7, sans valeur — le rebond est trop raide pour le modèle). s_∞ reste dans [0.58, 0.62] si on écarte le 0.809. La 3-var à 0.44 est toujours hors jeu.


## 40. Le 20 % était 4/L collé sur tout le bloc

Les hats hors bande n'ont pas le même préfacteur :
2 ĉ₀ĉ₀ ∼ (4/L)(1−cos)/γ², 2 ĉ₀ĉₙ ∼ (4√2/L)(1−cos)/γ², 2 ĉₙĉₘ ∼ (8/L)(1−cos)/γ².
À G=811, 1/G donne 2.056 / 2.908 / 4.113 ×10⁻³ contre mesuré 2.15 / 3.04 / 4.30 ×10⁻³. Rapport **1.045** partout. Le 20 % n'existait que parce que 4/L était mis sur les entrées 8/L. Il reste 4.5 % contre le 1/G à densité 1. **Corrigé en §41–§49** : ce n'est pas une oscillation ; après densité ρ et bord C/G l'identité (0,0) est close à O(1/G²). Ne pas lire « à 5 % » comme une enclosure.


## 41. Les 4.5 % ne sont pas une oscillation

Trois candidats, trois rejets.

- Oscillation. ∫ cos(Lγ)/γ² dγ = O(sin(LG)/(L G²)) : 3×10⁻⁷, soit 0.03 % de 1/G. Sur un peigne à l'espacement 2π/log, Σ(1−cos)/γ² = Σ 1/γ² à 0.06 %. L'oscillation s'annule. Elle n'est pas 4.5 %.
- Terme ω²/γ² dans g/(g²−ω²). Sur le 5×5, < 0.03 %. Non.
- Densité. 1/G suppose ρ=1. ρ réelle ≈ log(γ/2π)/2π ≈ 0.77 à G=811. Le peigne discret donne 0.873 × 1/G. Ça va dans l'autre sens : le 4.5 % au-dessus de 1/G devient **20 % au-dessus du peigne correct** — le même 20 % qu'avant le 4/L.

Le 1.045 uniforme est une compensation : 1/G trop grand (ρ=1) contre Q_pr encore trop grand d'environ 20 % par rapport à une queue à la bonne densité. Les 4.5 % ne se décomposent pas. Le reste est dans Q_pr (CR, quadrature) ou dans un facteur global du 2ĉĉ discret.


## 42. Audit (0,0) : l'identité tient à 4.5 ‰

`code/audit_00.py`, μ=11, 500 zéros jusqu'à G=811, queue à la densité \(\log(t/2\pi)/2\pi\).

(0,0) : pôle = 5.39852145601 = \(32\sinh^2(L/4)/L\) exact. Arch = −2.79251513121. Tours = 2.55366760055.
\(Q_{\mathrm{pr}}=0.05233872425\). \(Q_z^{\mathrm{cut}}=0.05018654823\). Queue ρ = 0.00191811119.
\(Q_{\mathrm{pr}}-(Q_z+
ho)=2.34	imes10^{-4}\) soit **0.45 % de \(Q_{\mathrm{pr}}\)**.

| entrée | \(Q_{\mathrm{pr}}\) | \(Q_z+
ho\) | écart | écart / \(Q_{\mathrm{pr}}\) |
|---|---|---|---|---|
| (0,0) | 0.052339 | 0.052105 | \(2.34	imes10^{-4}\) | 0.45 % |
| (0,1) | 0.074968 | 0.074637 | \(3.31	imes10^{-4}\) | 0.44 % |
| (1,1) | 0.107404 | 0.106936 | \(4.68	imes10^{-4}\) | 0.44 % |

Le 20 % était 20 % de la queue, pas de \(Q\). Sur la forme, l'identité est tenue au demi-pourcent. Le facteur 2 de `debug_weil.py` ((8/L) au lieu de (4/L) sur (0,0)) est la mauvaise convention : celle de `squares47` (2 η̂η̂) est celle qui colle. Il reste un biais positif uniforme ~0.44 %, même signe, même ordre relatif — quadrature / \(S(T)\) / constante de von Mangoldt, plus un terme neuf.


## 43. Le 0.44 % tombe en 1/G : ce n'est pas Q_pr

Six cuts sur (0,0) :

| n zéros | G | \(Q_{\mathrm{pr}}-(Q_z+\rho)\) | relatif |
|---|---|---|---|
| 50 | 143 | 1.31×10⁻³ | 2.50 % |
| 100 | 237 | 7.90×10⁻⁴ | 1.51 % |
| 200 | 396 | 4.82×10⁻⁴ | 0.92 % |
| 300 | 542 | 3.45×10⁻⁴ | 0.66 % |
| 400 | 680 | 2.78×10⁻⁴ | 0.53 % |
| 500 | 811 | 2.34×10⁻⁴ | 0.45 % |

Écart ≈ 0.190 / G à tous les cuts. Si c'était un biais d'assemblage de \(Q_{\mathrm{pr}}\), il serait indépendant de G. Il suit la queue.

Contrôles qui ne font pas 2×10⁻⁴ :
- arch vs ∫ ψ : 3×10⁻⁶ à T=400, 2×10⁻⁸ à T=4000
- Euler–Maclaurin ½ f(G) : 1×10⁻⁶
- |S(G)| f(G) : ≲ 2×10⁻⁵

Le 0.44 % est un O(1/G) manquant dans la queue, équivalent à une densité constante α ≈ 0.114 ajoutée à \(\log(t/2\pi)/2\pi\). Ce n'est pas 1/(2π)≈0.159 (ça surestimerait de 40 %) ni 7/8 (saut, pas une densité). Plus de zéros après 811 le fera tomber ; ce n'est pas un terme neuf dans Q.


## 44. 0.190/G tenu jusqu'à G=1001

60 zéros de plus (mpmath, n=501–560, G=888) puis 90 encore (n=561–650, G=1001).

| n | G | écart | 0.190/G |
|---|---|---|---|
| 500 | 811 | 2.341×10⁻⁴ | 2.342×10⁻⁴ |
| 560 | 888 | 2.166×10⁻⁴ | 2.138×10⁻⁴ |
| 650 | 1001 | 1.925×10⁻⁴ | 1.897×10⁻⁴ |

Produit écart × G = 0.190, 0.192, 0.193. La loi tient hors de l'échantillon qui l'a produite. C ≈ 0.191, α = C L/4 ≈ 0.115. Toujours pas 1/(2π). Identifier α reste ouvert ; fermer l'écart demande des zéros, pas un autre terme dans Q.


## 45. C=0.190 jusqu'à G=1244 ; la phase voit le premier 11

n=750, G=1123, écart=1.710×10⁻⁴, C=0.192. n=850, G=1244, écart=1.524×10⁻⁴, C=0.1895.

L=log 11, et 11 est premier. Σ cos(Lγ)/γ² n'est pas une oscillation nulle : sur les zéros 651–850 elle vaut −2.4×10⁻⁵, ce qui *augmente* 1−cos et donc la vraie queue. Le signe est celui du biais (Qz+ρ trop petit). α n'est toujours pas nommé, mais ce n'est plus une densité abstraite : c'est la modulation du peigne par le premier posé au bord de la fenêtre. C reste 0.190 ± 0.003 sur neuf cuts, G=143→1244.


## 46. C = Λ(μ)/(4√μ)

Le 0.190 n'est pas universel. Il dépend de μ, et de ce que μ est comme entier.

| μ | C mesuré | Λ(μ)/(4√μ) | rapport |
|---|---|---|---|
| 11 (premier) | 0.190 | 0.181 | 1.05 |
| 13 (premier) | 0.177 | 0.178 | 0.99 |
| 9 = 3² | 0.104 | 0.092 | 1.13 |
| 16 = 2⁴ | 0.042 | 0.043 | 0.97 |

C'est le poids de tour au bord y=L, là où Θ(L)=0 donc le terme n'entre pas dans Q_pr, mais où la phase e^{iγL} = n^{iγ} à n=μ voit encore l'entier. La queue hérite du premier (ou de la puissance) posé sur le cadre. α a un nom. L'écart (0,0) est Λ(μ)/(4√μ G) plus les 3 % de bruit de cut.


## 47. Convergence de C : déjà finie en G, pas vers la même cible

C(G)=écart×G, huit cuts, G=143→811.

μ=11 : C=0.187 dès n=50, Steffensen (300,400,500)=0.191. **Plat.** Cible Λ/(4√μ)=0.181. Écart +0.009 figé, pas un 1/G.
μ=13 : 0.164→0.177, pred=0.178. **Monte vers la cible.** À n=500 : −0.0009.
μ=16 : bruité (écart petit), 0.028→0.042, pred=0.043. Steffensen 0.043. **Monte vers la cible.**
μ=9 : C=0.103–0.107 dès n=50, Steffensen 0.105, pred=0.092. **Plat**, +0.013 figé.

La convergence en G est faite vers G≈200. Deux familles : {13,16} tombent sur Λ/(4√μ) à 2 % ; {9,11} restent 5–13 % au-dessus et n'en bougent plus. Ce qui reste n'est plus un cut de queue. C'est un second terme, ou Q_pr à ces μ.


## 48. Le 4 était un fit : \(C=2\Lambda(\mu)/(\pi L\sqrt{\mu})\)

\(\hat h_L(\gamma)=4(1-\cos(\gamma L))/(L\gamma^2)\). La queue modèle garde \(\sum 1/\gamma^2\) et jette \(\sum\cos(\gamma L)/\gamma^2\). L'écart est
\[
\Delta(G)=\frac4L\sum_{\gamma>G}\frac{\cos(\gamma L)}{\gamma^2}+O(G^{-2}).
\]
La formule explicite couple \(\sum_\gamma\cos(\gamma x)\) au peigne \(\sum_n\Lambda(n)n^{-1/2}\delta(x-\log n)\). La convention de Fourier \(\hat h=\int h\,e^{i\gamma x}\,dx\), inversion \(1/2\pi\), donne au bord \(x=L=\log\mu\) le noyau tronqué \(K_G(0)=\int_G^\infty t^{-2}\,dt=1/G\). D'où
\[
\Delta(G)=\frac4L\cdot\frac{\Lambda(\mu)}{2\pi\sqrt{\mu}}\cdot\frac1G+O(G^{-2}),
\qquad
C=\frac{2\Lambda(\mu)}{\pi L\sqrt{\mu}}.
\]
L'ancienne \(\Lambda/(4\sqrt{\mu})\) coïncide quand \(4/L=\pi/2\), i.e. \(L=8/\pi\approx2.55\), pile μ=13. Ce n'était pas une constante universelle.

| μ | C mesuré | \(2\Lambda/(\pi L\sqrt{\mu})\) | ancien \(\Lambda/(4\sqrt{\mu})\) |
|---|---|---|---|
| 11 | 0.190 | 0.192 | 0.181 |
| 13 | 0.177 | 0.177 | 0.178 |
| 9 | 0.104 | 0.106 | 0.092 |
| 16 | 0.042 | 0.040 | 0.043 |

{9,11} se ferment. Le plat du §47 n'était pas un second terme : c'était \(L\) oublié.


## 49. \(Q_{\mathrm{pr}}-(Q_z+\rho+C/G)=O(1/G^2)\)

μ=11, n=500 : écart brut \(2.34\times10^{-4}\), \(C/G=2.37\times10^{-4}\), reste \(-2.6\times10^{-6}\). μ=13 : reste \(+4.7\times10^{-7}\). Les quatre fenêtres : reste \(\sim10^{-6}\), produit par \(G^2\) borné. L'identité (0,0) est close à l'ordre suivant. Le cran du bord était le dernier terme en \(1/G\).


## 50. Le 5×5 ferme avec les mêmes C scalés

Préfacteurs §40 : C_{00}, C_{0n}=√2 C_{00}, C_{nm}=2 C_{00}. μ=11, n=500 :

| entrée | écart | C/G | reste | G² reste |
|---|---|---|---|---|
| (0,0) | 2.341×10⁻⁴ | 2.366×10⁻⁴ | −2.6×10⁻⁶ | −1.7 |
| (0,1) | 3.310×10⁻⁴ | 3.346×10⁻⁴ | −3.6×10⁻⁶ | −2.4 |
| (1,1) | 4.682×10⁻⁴ | 4.733×10⁻⁴ | −5.1×10⁻⁶ | −3.4 |

Même O(1/G²). Le 4 du Fourier n'est pas spécial à η₀.


## 51. C=κ : C est lisible, κ ne l'est pas sur la même Q

ζ, μ=11, dps=50. C = |v̂(γ₁)|/λ. κ = |v̂(bord)|/√λ.

| N | ℓ | C | κ | C/κ |
|---|---|---|---|---|
| 5 | 32.5 | 7.1×10³ | (bruit) | — |
| 7 | 40.3 | 402 | (bruit) | — |
| 9 | 48.5 | 120 | (bruit) | — |
| 11 | 55.9 | 66.8 | (bruit) | — |
| 13 | 62.2 | 48.1 | (bruit) | — |

C descend vers la valeur publiée 27.8 à N=21. κ est sous le plancher : |v̂(bord)| ~ e^{−ℓ/2} une fois que γ₁ est résolu. cond(Q)~e^ℓ. RQI à 80 chiffres n'y change rien — le vecteur propre vrai est déjà orthogonal au bord à 10⁻²⁰. C=κ reste une identité de forme (le leak fournit le second √λ). Les deux nombres ne sont pas co-mesurables sur une même fenêtre.


## 52. RH : ce que Weil donne, ce qu'on a, ce qui manque

Critère de Weil (1952). L'hypothèse de Riemann est équivalente à la positivité de la forme
\[
Q(h)=\sum_{\gamma}\hat h(\gamma)
\]
pour toute fonction test \(h\) paire, à décroissance convenable. Équivalence : toutes les \(h\), pas une fenêtre.

Ce qu'on a.
- \(Q_{\mathrm{pr}}\) sur \(V_N\) à \(L=\log\mu\) fixé est PSD dès que le quorum de tours est complet (certifié : tout sous-produit propre viole). C'est une conséquence attendue de RH, pas une preuve : une famille finie de \(h\) positives n'implique pas toutes les \(h\).
- \(Q_{\mathrm{pr}}=Q_z\) à \(O(1/G^2)\) sur le 5×5. Ça vérifie la formule explicite sur cette base. La formule explicite est inconditionnelle. Elle n'est pas RH.
- MUSIC retrouve les zéros déjà calculés. Cohérence, pas existence.
- \(Q_z\) est assemblé avec des zéros sur la droite. S'en servir pour « voir » RH est circulaire.

Ce qui manquerait pour une preuve.
- Positivité pour une classe dense de tests, ou un passage à la limite \(N,L	o\infty\) contrôlé sans les zéros.
- Ou un argument spectral (trou, factorisation) qui force tous les \(\gamma\) réels. On n'en a pas.

Le quorum isole le caractère collectif de la positivité. L'identité de Gram ferme la formule explicite sur une fenêtre. Ni l'un ni l'autre ne déplace RH.


## 53. Ce qui manquait

**K=7.** N=17, ω_max=41.9, sept zéros en bande. Cosinus greedy : 0.83, 0.81, 0.80, 0.75, 0.61, 0.50, **0.27**. Le septième est γ₇=40.92, collé au bord. K=6 tenait parce qu'on s'arrêtait avant la plongée. K=8 (min 0.14) n'était pas un saut magique : la casse commence au dernier zéro en bande.

**47×47 Arb.** `squares47_arb.py` importe `flint`. Pas de python-flint ici (miroir PyPI en 502). Le 5×5 est déjà enclosure + bord C/G. Le 47-dim certifié reste bloqué par l'outil, pas par une idée.

**C=κ et RH** déjà tranchés (§51–§52). Plus rien d'ouvert qui soit un cran de calcul dans cet environnement.


## 54. Les trois routes vers RH : deux sont fermées, une est un certificat infini

**Classe dense à L fixé.** Q_pr seul, μ=11, pas de zéros :

| N | λ_min | ℓ | signe |
|---|---|---|---|
| 5 | 7.8×10⁻¹⁵ | 32.5 | + |
| 9 | 8.9×10⁻²² | 48.5 | + |
| 13 | 9.4×10⁻²⁸ | 62.2 | + |
| 17 | 3.7×10⁻³³ | 74.7 | + |

La base cosinus se densifie, la forme reste PSD. ℓ croît avec N : on ne tend pas vers un λ_∞>0, on creuse le quasi-noyau. Positivité sur V_N pour tout N à L fixé est le bon énoncé de fenêtre. On en a des échantillons, pas une preuve pour tout N.

**N,L→∞ sans les zéros.** Déjà mesuré : −ln λ_min = sμ+b, s>0. Donc λ_min(L)→0 quand L→∞. Un minorant uniforme en L est faux même sous RH. La limite contrôlée ne peut pas être « λ≥c>0 ». Elle devrait être « λ(L)>0 pour chaque L ». C'est un certificat infini, un L à la fois. scan_s le sonde. Il ne le clôt pas.

**Trou spectral.** Le trou au-dessus de 0 *est* λ_min ~ e^{−sμ}. Il rétrécit. Il n'existe pas de gap uniforme qui forcerait tous les γ réels. Cette route est fermée par la phénoménologie même du forage.

Reste une seule formulation non vide : pour tout L, Q_L>0 sur tout le window space. Équivalent à Weil restreint aux supports ≤L, puis L→∞. On n'a pas cet énoncé. On a des (L,N) positifs et le quorum qui dit que le produit d'Euler y est nécessaire.


## 55. Positivité de Weil

Deux directions, pas la même force.

**RH ⇒ Q≥0.** Si tout zéro non trivial est 1/2+iγ, γ réel, et si h est la transformée d'un η de fenêtre,
\[
Q(h)=\sum_{\gamma}\hat\eta(\gamma)^2
\]
(paire ±γ déjà dans la convention du dépôt). Somme de carrés. Positive. Inconditionnelle dès que les γ sont réels. C'est Q_z.

**Q≥0 pour toute h ⇒ RH.** Contraposée : un zéro à 1/2+σ+iγ, σ≠0, produit un terme \(\hat h(1/2+\sigma+i\gamma)+\hat h(1/2-\sigma-i\gamma)\) qui n'est plus un carré. On choisit h concentré sur cette fréquence complexe ; Q(h)<0. Donc la positivité *sur toute la classe de Weil* force σ=0. C'est le critère.

La classe de Weil n'est pas V_N. Ce sont les h paires à support compact (ou décroissance) sur la variable additive y=log n, toutes les longueurs de support. V_N à L=log μ est une sous-classe.

**Ce que Q_pr mesure.** La formule explicite identifie Q_z et
\[
Q_{\mathrm{pr}}(h)=P(h)+A(h)-\sum_{n\le e^L}\frac{\Lambda(n)}{\sqrt n}h(\log n)
\]
sans hypothèse sur les zéros. Positivité de Q_pr sur V_N est un test fini, *équivalent* à Q_z≥0 sur V_N seulement après l'identité de Gram. L'identité est tenue à O(1/G²) sur le 5×5. Elle ne s'étend pas toute seule à toute h.

**Quorum.** Q_S pour S⊂neq{p : p≤μ} n'est pas la forme de Weil. C'est un produit d'Euler amputé. Sa négativité certifiée ne dit rien sur RH. Elle dit que la compensation pôle + arch contre les tours est collective. Weil demande le produit entier sur la fenêtre.

**Signe et forage.** λ_min(Q_pr)>0 observé, de taille e^{−sμ}. Sous RH c'est le coût du mode le plus profond, pas un trou stable. Un λ_min<0 sur un V_N complet (tours pleines) serait un contre-exemple numérique à RH. On n'en a pas. Un λ_min>0 sur un V_N n'est pas un théorème.

**Bilan.** La positivité de Weil est une équivalence avec RH *sur la classe entière*. Sur une fenêtre, elle est une somme de carrés d'un côté et un quorum de l'autre. Les deux coïncident où on a vérifié le Gram. Aucun des deux ne ferme la classe.


## 56. Fonctions de test « optimales »

Trois optima, trois objets.

**Rayleigh : l'état fondamental.** Dans V_N, min Q(η)/‖η‖² est λ_min, atteint au vecteur propre v. À μ=11, N=9 : v = (0.60, −0.69, 0.38, −0.13, 0.02, …), 98 % de la masse sur n=0,1,2. Alternance. Cosinus avec l'évaluateur γ₁ : 10⁻¹⁹. Ce n'est pas un peigne sur γ₁. C'est le quasi-noyau : v̂ s'annule sur les zéros en bande (MUSIC). Optimale pour mesurer la rive de positivité, nulle pour lire un zéro.

**Lecture d'un zéro : l'évaluateur ĉ(γ_k).** C'est la fonction de V_N qui maximise |η̂(γ_k)|. Appariement 1-1 jusqu'à la plongée. Optimale pour MUSIC, pas pour Q.

**Critère de Weil (hors fenêtre).** Si un zéro quitte la droite, Q(h) peut devenir <0 pour une h dont ĥ est porté près de σ+iγ. Les candidates classiques — gaussiennes (§9), majorantes de Beurling–Selberg, coefficients de Li — ne vivent pas dans un V_N à support L fixé. Les tester ici serait changer de classe, pas optimiser V_N.

η₀ (triangle) n'est optimale pour aucun des trois : Q(η₀) est O(1), loin de λ_min, et η̂₀(γ₁) n'est pas maximal. Le « meilleur test » dépend de la question. Pour la positivité tronquée, c'est v. Pour RH, ce n'est pas v : v est déjà orthogonal aux zéros réels.


## 57. Polynômes de Riemann–Siegel

Deux objets portent ce nom. Ni l'un ni l'autre n'est $V_N$.

**1. Formule de Riemann–Siegel.** $Z(t)=e^{i\theta(t)}\zeta(1/2+it)$ est réelle. Avec $m=\lfloor\sqrt{t/2\pi}\rfloor$,
\[
Z(t)=2\sum_{n\le m}n^{-1/2}\cos\bigl(\theta(t)-t\log n\bigr)+R(t).
\]
$R(t)$ est un développement en puissances de $(t/2\pi)^{-1/2}$ dont les coefficients sont des polynômes en la partie fractionnaire $z=\sqrt{t/2\pi}-m$ (polynômes de Siegel, issus du Nachlass). C'est une *formule de calcul* de $Z$ sur la droite. Les zéros de $Z$ sont les zéros de $\zeta$ sur la droite, pas une approximation polynomiale de $\xi$.

**2. Polynôme de l'équation fonctionnelle approchée.**
\[
\zeta(s,X)=\sum_{n\le X}n^{-s}+\chi(s)\sum_{n\le t/(2\pi X)}n^{s-1}.
\]
Dirichlet polynomial de longueur $\sim\sqrt{t/2\pi}$. Ses zéros ne sont pas ceux de $\zeta$ (Turán : les sommes partielles ont des zéros hors droite). Ce n'est pas un contre-exemple à RH.

**Lien avec la fenêtre.** Le cut RS est $n\le\sqrt{t/2\pi}$, à $t$ fixé, pour évaluer $\zeta$ *en un point*. Le cut Weil est $n\le e^L=\mu$, pour une forme quadratique *sur un espace de tests*. $\sqrt{\mu}$ n'est pas $m$. Le quorum (2,3,5,7 à μ=11) n'est pas la somme $n\le m$. Confondre les deux troncatures mélange un point et une forme.

**Lien avec $v$.** L'état fondamental de $Q$ est un vecteur de $V_N$, support $L$, orthogonal aux $\gamma_k$ en bande. Un polynôme RS est une fonction de $t$, support spectral $\log n$ pour $n\le m$. Même variable additive $\log n$, autre usage : l'un minimise $Q$, l'autre approxime $Z(t)$.

**Sismographe.** L'annexe G parlait d'un « sismographe de Siegel » : lire les zéros sur $Z(t)$ ou $\theta'(t)$. MUSIC le fait déjà depuis $Q$, sans passer par $Z$. Recalculer des polynômes RS ne ferme ni Gram ni RH.


## 58. Polynômes de Weil

Le nom désigne, en arithmétique, le polynôme caractéristique de Frobenius, pas un polynôme attaché à $Q$.

**Sur un corps fini.** Pour $X/\mathbb{F}_q$ lisse projective, le facteur
\[
P_i(T)=\det\bigl(1-T\,\mathrm{Frob}\big| H^i_{\mathrm{ét}}(X_{\bar{\mathbb F}},\mathbb Q_\ell)\bigr)
\]
est le polynôme de Weil de poids $i$. Théorème de Weil (courbes) puis Deligne (conjectures de Weil) : toutes les racines ont module $q^{i/2}$. C'est RH pour les corps finis. Preuve géométrique (correspondances, positivité de l'intersection, ou faisceaux $\ell$-adiques). Pas une fenêtre de tests sur $\zeta$.

**Nombres de Weil.** $\alpha$ est un $q$-nombre de Weil de poids $k$ si $\alpha$ et $q^k/\alpha$ sont des entiers algébriques conjugués de module $q^{k/2}$. Les racines de $P_i$ en sont.

**Ce que ce n'est pas.** $\det(zI-Q)$ sur $V_N$ n'est pas un polynôme de Weil. Ses racines sont les $\lambda_j$ de la forme tronquée, réelles (Q symétrique), une négative si le quorum manque. Aucune action de Frobenius, aucun $q$.

**Le pont, et sa limite.** Weil a tiré le critère de positivité *pour $\zeta$* de la même intuition que la positivité qui prouve RH sur $\mathbb F_q$. Sur $\mathbb F_q$ l'espace est de dimension finie (cohomologie) et Frobenius le range. Sur $\mathbb Q$ l'espace des tests est infini et il n'y a pas de Frobenius. Le quorum dit que le produit d'Euler joue, dans $V_N$, le rôle d'un « ensemble de correspondances » nécessaire à la positivité — analogie, pas dictionnaire. Les $P_i$ ne se calculent pas à partir de $Q$, et $Q$ ne se factorise pas en $P_i$.


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

Suite du journal de l'annexe B, dans l'ordre réel : (19) recherche web — découverte que le terrain prolates/Toeplitz/petites valeurs propres est la frontière active (Connes-Consani 2021/2023, Suzuki 2026) ; (20) lecture intégrale de « ζ-cycles » : correspondances point par point avec nos campagnes, théorème 6.4 = portrait-robot réalisé, désaccord doublement-exponentiel identifié ; (21) lecture de Suzuki : fonction vis, A_a = Friedrichs de D*G_aD, conjecture (1.2), relecture rétroactive de notre mode dangereux comme ombre de ξ ; (22) décision de méthode : raccordement avant test de forme (calibration du conditionnement) ; (23) raccordement : effondrement de α(s), invariant 0.41/dimension, plongeon de Slepian mesuré jusqu'à 2.2×10⁻³⁶ (mp, 1 s), faux négatifs float64, lecture « blancheur protectrice » ; (24) lecture de Groskin : criticité = théorème / convergence ouverte, terrain « positions » occupé à 329 chiffres, artefact T, créneaux restants (forme de la fonction, Dirichlet) ; (25) construction du test de forme, échec de performance puis optimisation (quadrature partagée, tables trig) ; (26) bug archimédien attrapé par confrontation à Q∞ et à la figure 4 de CC ; (27) bug de séparation d'intégrande ; (28) bug des nœuds float64 ; (29) série µ = 3.5 → 16, validation λ_min contre le 2.389×10⁻⁴⁸ publié ; (30) découverte du protocole à double limite (l'« accélération » était un artefact) et loi finale R ≈ e^(−L)/3 ; (31) audit des conventions, facteur ½ épinglé numériquement dans l'identité de Fourier de Φ_c ; (32) ajustement c_a = c_∞ + 0.32/µ sur six points (même coefficient que la loi de forme) ; (33) recouvrement L² de 0.99964 à µ=11 → identification c_∞ = ‖Φ_S‖ = 1.130932, scission L²/uniforme de la conjecture (1.2) ; (34) route archimédienne de Frullani validée à 10 chiffres sur ζ, évaluateur Λ(s,χ₃) réel sur la droite critique, 70 zéros récoltés ; (35) pipeline χ₃ : identification c_∞(χ₃) = ‖Φ₃‖ confirmée du premier coup, λ_min quatorze ordres au-dessus de ζ à µ = 5.5 ; (36) échelle χ₃ sur trois µ : pente 4.0, première lecture « l'abîme est une affaire de pôle » ; (37) généralisation à χ₄, χ₅, χ₇, χ₈ après optimisation de la grille en z (runs de >17 min à ~20 s) ; (38) moisson : identification 6/6, signature de parité sur C, pente croissante avec γ₁, candidat γ₁²/(2πe) ; (39) troisième µ sur quatre caractères : linéarité des échelles confirmée, γ₁²/(2πe) falsifié par χ₄, structure à deux variables (désert, parité), principe du sismographe établi ; (40) durcissement : formes fermées Φ_χ validées (rapport 1.0 plat), normes à douze chiffres, robustesse en base des échelles Dirichlet (≤2.4%), correction de la pente ζ (11.8 → ≈10 non linéaire, bases appariées), convergence quadratique vérifiée contre les normes exactes ; (41) extension à χ₁₁, χ₁₂, χ₁₃, χ₁₅ (tables validées à 10⁻²⁶) : plancher s ≈ 0.9 aux petits déserts, critère de largeur de fenêtre ½ln(3q/π) ; (42) point décisif µ = 22 : pente de χ₁₅ stabilisée à ≈ 0.70 — troisième variable confirmée, hypothèse de densité arithmétique (conducteur composé), prédiction χ₂₄ ; (43) identification portée à dix fonctions L (normes 0.515 → 4.592), χ₁₅ à 3.1×10⁻⁴ ; (44) verdict mod 24 : la paire jumelle confirme la densité arithmétique comme variable réelle (χ₁₁ vs χ₂₄ᵉ : γ₁ quasi égaux, pentes 0.91 vs ≈0.49), le plancher du §13.5 tombe, γ₁ agit encore à appauvrissement fixé (χ₁₂ vs χ₂₄ᵉ : 0.94 vs 0.49), parité secondaire aux petits déserts ; (45) session de régression : modèles emboîtés (γ₁ / +D / +parité : 20→15→9.4% de dispersion), collapse X = γ₁·e^(−0.125D), prédictions préenregistrées pour χ₁₉ ; (46) verdict hors échantillon : γ₁(χ₁₉) = 1.516, s ≈ 0.55-0.6 — deux hypothèses éliminées, collapse sous-prédisant, M2 à 15% ; découverte du biais transitoire des petits déserts ; identification portée à treize fonctions L ; (47) campagne anti-transitoire (µ = 30 et 38, factorisation étendue ≤ 37) : χ₁₉ = 0.58, χ₂₄ᵒ = 0.46, χ₂₄ᵉ = 0.50 convergés, χ₁₁ ≈ 1.07 et χ₁₅ ≥ 0.80 relevés — contraste de densité accentué (paire décisive à rapport 2.1), biais généralisé identifié sur toute la carte, refit suspendu jusqu'à uniformisation ; (48) uniformisation des sept caractères restants à µ = 30-38 ; septième artefact : demande en base croissant avec la profondeur (χ₃ : fausse courbure 3.35 → 4.02 en base 75), doute rétroactif sur la non-linéarité de ζ ; (49) refit final : s ≈ 0.29·γ₁^1.28·e^(−0.20D)·1.31^[impair] à 9.7% (LOO 12.4%), densité et parité renforcées, identifications à quelques 10⁻⁵ ; (50) veillée : ζ blanchi (base 71 : s_ζ = 11.7 ± 0.2 linéaire, réconciliation avec le ~10µ de CC par l'ordonnée −20), scan D(β) négatif (β* en butée, +4%), ζ hors famille à 3% du bord supérieur de la loi ; (51) quatrième variable trouvée : γ₂−γ₁ (M3 à 6.1%, LOO 4.8% — réel, pas du sur-ajustement), il ne résiste que χ₁₂/χ₁₃ ; artefact zéro ajouté à la taxonomie : rédiger avant de calculer ; (52) deux pairs préenregistrés : χ₂₁ à +9% ✓, χ₁₇ à −26% ✗ (petit écart hors du domaine d'ajustement), transitoires décroissants inédits, refit 14 points : RMS 7.6% mais LOO 12.8% et paramètres instables — la loi de puissance sur l'écart est trop rigide, cible suivante : fonctionnelle du comptage N_χ(t) ; identification portée à quinze fonctions L ; (53) chasse à la fonctionnelle : S₂ et L(τ) testées et rejetées (LOO 13-14%, ζ à 39.6 contre 11.7 — le comptage brut confond densité et forme), absorption partielle de D constatée (−0.13 → −0.05), cible affinée : la fonctionnelle de vacance ∫(N̄−N)·w ; (54) traces élucidées : transitoires décroissants = dépassement-tassement réel (±0.05 budgété, base contrôlée), hypothèse χ(2) sur les quatre résistants falsifiée (corrélation −0.07) — septième exécution d'hypothèse de la journée ; (55) fonctionnelle de vacance : construction validée (c ≈ 0 pour les χ, c = 1.006 pour ζ — le +1 classique) mais échec décisif (RMS 21%, ζ à ~0) pour cause de quasi-universalité du déficit de comptage (~½ zéro par désert) — reformulation : la profondeur est un phénomène de bande passante (fréquences absolues), pas de comptage ; huitième exécution, cible déplacée vers la théorie des prolates ; (56) théorie du front de moisson (§14) : marge ≈ e^(−s²γ²_front) confirmée sans paramètre sur quatre décades, taux 0.41 = s²γ/ρ au front, plongeon à J* = Uγ_max/2π + 1 (prédit 24.9, mesuré 26), grille ≡ zéros (généricité), Poisson plus dangereux (la rigidité GUE maximise la marge) — la plus ancienne question du fil est fermée ; (57) architecture universelle des barreaux : 33 barreaux de 15 fonctions L sur un seul profil Δ(ℓ) ≈ 9.8 + 0.65√ℓ (dispersion ~12%, ζ indistinguable de χ₃/χ₄ à niveau égal) — le problème se factorise : architecture universelle × vitesse de forage s(χ) ; (58) architecture identifiée : Slepian classique rejeté tel quel (espacements 3-5 contre 11-19, Fuchs validé) mais dilatation pure découverte — λ_Weil,k ≈ (1−λ_k^Slepian)^κ, κ = 2.85 ± 0.26 sans dépendance en c ni en χ ; candidats e et 3 indépartageables ; hypothèse des trois projections composées ; cible théorique : démontrer κ ; (59) vitesse de forage : théorème-esquisse de linéarité (−ln λ_min ∝ µ ⇔ mécanisme de réseau discret, le continuum plafonne à ln µ), rétrogradation du Slepian^κ littéral (estimateurs de c incohérents ×2-5.5, seul le profil tient), ordre zéro c ≈ γ₁·N_χ/2π à un facteur 1.9 ± 0.9 — cahier des charges de la preuve établi ; (60) test du chaînon 2 : W_eff = πsq/(κφ) n'accroche aucun repère spectral (W/γ₁ = 0.63 ± 0.23 au mieux) — la factorisation bande×comptage est trop naïve, le couplage est irréductible, dixième exécution ; l'identification de la bande passe par la construction de l'opérateur (chaînon 1) ; (61) chirurgie du foret (chaînon 3) : prédictions préenregistrées spectaculairement fausses — retirer le 2 effondre la positivité (six vp négatives O(1), ombre de la tour sur le radical), retirer le pôle effondre exactement une direction (−6.49 ≈ 32sinh²(L/4)/L = 6.51, accord 0.3%) ; onzième exécution, leçon d'obstruction (la cohérence de la formule explicite est porteuse), programme de spectroscopie du radical ouvert ; (62) spectroscopie exécutée (ζ µ=11, χ₃ µ=38 après correction d'un masquage de variable attrapé par confrontation externe) : LOI DE RECRUTEMENT — le barreau k recrute le (k+1)-ième premier supporté, murmure annonciateur un barreau avant, signes modulés par χ(p), tour du 2 porteuse sur tous les barreaux (explique §14.5), linéarité en µ recadrée comme théorème des nombres premiers vu du radical ; (63) le microscope cumulatif : deux scénarios préenregistrés faux (treizième exécution) — la positivité est un QUORUM (toute somme partielle de tours est négative, écho des pseudo-zéros de la campagne 4), le dernier premier intérieur fait atterrir la forme sur l'échelle complète exacte à 10⁻⁴⁸ du zéro ; profondeur non décomposable, criticité présente à chaque µ dès complétude arithmétique ; (64) campagne des lemmes : échelles à dix barreaux, ajustements Fuchs excellents mais κ non transférable (3.46/4.48/5.37 à c libre) — le lemme κ se dissout (quatorzième exécution), « e ou 3 » était mal posé ; survit le profil Δ(ℓ) sans modèle du §14.2, unique lemme candidat ; quorum répliqué par accident (ζ à µ=38, premiers >23 manquants : λ_min = −0.575) ; (65) formalisation du quorum (§15) : conjecture nette vérifiée (quatre délétions simples toutes négatives), lemme A prouvé (indéfini des tours, deux bosses), réduction au radical exacte (w à 99.4% radical, λ_min(Q_∖p) = λ_min(M_p) à 10⁻⁴ — prédiction bulk morte, quinzième exécution), objet formel : résolution de zéro en matrices indéfinies dont toute somme partielle est négative ; reste le lemme B, fini et mesurable ; (66) lemme B prouvé à µ = 11 par certificats 2×2 (marges 0.10-0.19 contre erreurs < 10⁻⁸) — motif universel : chaque certificat apparie un barreau silencieux (pré-recrutement, diagonale nulle) et un barreau parlant (couplage 0.4) ; stratégie générale en deux énoncés d'analyse harmonique (B1 silence diagonal, B2 le couplage survit), aucun ne mentionnant RH ; (67) vérification exhaustive : 16/16 sous-ensembles (tout propre négatif, −0.52 à −1.15, non monotone), réduction de Rayleigh rigoureuse — statut : fait vérifié promouvable en théorème assisté par intervalle, pas encore un théorème ; (68) voie du théorème ouverte et testée : par Rayleigh il suffit de témoins explicites (Q_S(w) < 0 certifié, pas de valeurs propres), tours et pôle en formes closes certifiables en intervalles (fait : enclos à 30 chiffres via mpmath.iv), archimédien par quadrature rigoureuse (fait : python-flint/Arb installé, entrée (0,0) certifiée à ±2×10⁻³⁸) — le théorème du quorum à µ = 11 est un projet fini en trois phases ; (69) phases 1-2 EXÉCUTÉES (`theoreme_quorum.py`, 7 s) : 1128 paires certifiées (rayon max 9.4×10⁻¹¹), quinze quotients de Rayleigh certifiés < 0 (marges 0.52-1.15), le complet non certifiable à +0.0000 comme il se doit — le théorème est calculé ; reste la phase 3 (rédaction, dérivation de la table θ) ; (70) phase 3 rédigée : convention de la table tranchée à 10⁻³⁰ (autocorrélation symétrisée en base cosinus décalée ; la base centrée diffère du signe (−1)^(n+m)), T₁₁ ≡ 0 identiquement (log 11 = L, recouvrement vide — les intérieurs sont {2,3,5,7} sans convention), note-théorème DRAFT de 4 pages compilée — au tiroir, en attente de vérification manuelle ; (71) théorème généralisé : moteur paramétré, χ₃ µ=11 (7/7 — le quorum tient SANS pôle), ζ µ=16 (63/63), ζ µ=22 (255/255), complet non certifiable partout — 340 certificats, zéro exception ; loi émergente : la délétion du dernier recruté est la plus douce et s'adoucit avec µ, les tardifs sans les précoces sont les plus violents ; (72) checklist 1-2 de la note #3 : appendice A dérivé en entier (quatre cas, base décalée, aucun signe parasite) et appendice B écrit — l'identité de normalisation Q = Σ|f̂(γ)|² SANS facteur, par la série de ψ, la paire de Fourier a/(a²+t²/4) ↔ e^(−2a|x|), et les trois constantes exactes (log 2 du glissement e^(−2y)→e^(−y), −log tanh(L/2) de la troncature à L licite car Θ y meurt, log π absorbé) recomposant C_L = γ + log(4π·tanh(L/2)) ; pôle vérifié à 12 chiffres, archimédien à 10⁻⁴ (résidu = queue oscillante du contrôle lui-même) — le rôle de l'auteur passe de créer à vérifier ; (73) point 3 : les 340 témoins gelés en dyadiques exacts (witnesses_*.json, quatre fichiers), mode verify installé (certification depuis les fichiers gelés, sans diagonalisation) et démontré (15/15 rejoué à l'identique) — la checklist de la note #3 se réduit au point 4 (rerun tiers, prévu au push) et aux relectures d'algèbre ; (74) audit épistémique de l'auteur suivi de deux correctifs d'artefact public : les rayons Arb consignés dans les en-têtes des tables de certificats (1.1×10⁻¹⁰ entrées / 8.6×10⁻¹⁰ quotients à µ = 22, puis ligne à ligne) et l'identification Weil-Bombieri vérifiable par script autonome (weil_normalization_check.py : pôle exact à 12 chiffres, archimédien contre l'intégrale de ψ directe) — plus rien de central ne repose sur la parole de l'auteur ; (75) relecture v2 de l'auteur : témoins du dépôt distant corrompus au transfert (plists uniformes = placeholders iCloud ; les quatre JSON locaux vérifiés sains, SHA-256 consignés, rejeu verify 15/15), facteur 2 corrigé dans la phrase intermédiaire de l'appendice B (2g(0)log2 = g(0)log4 — l'identité finale était juste), moteur de référence clarifié (quorum_general.py), phrase des bases agrandies ajoutée, fossiles purgés (commentaire de theoreme_quorum.py, « pending » du README) — reste le re-transfert propre côté serveur et le rerun tiers ; (76) revue de code de l'auteur appliquée en cinq points : requirements.txt complet (python-flint, scipy) et lien README réparé, scories purgées (zombie if-False de shape8, convention fausse Φ_S=2Φ_c du commentaire de denouage_A corrigée en 4Φ_c), chemins ancrés sur __file__ (dscan, quorum_general — cwd-indépendants) avec garde µ≤22 explicite, theoreme_quorum réduit à une enveloppe du moteur (duplication éliminée, verify hérité), et tests/ créé — test_theta_endpoints (bords exacts, table=autocorrélation à 10⁻¹⁸) et test_cert_mu11 (16 lignes, 15 propres < −0.3, complet ~0, JSON↔table cohérents), les deux au vert ; (77) contre-relecture finale de l'auteur appliquée : partage measurement/theorem tranché dans le bandeau README, §15.3 daté (principe du carnet : le paragraphe dépassé reste, l'addendum date), tableau unique des délétions simples au §15 (mesure spectrale vs borne certifiée, S = ensemble conservé), test d'identité du pôle ajouté à la non-régression — restent, côté auteur : sortir le dossier d'iCloud, remplacer les 19 placeholders, vérifier sur clone vierge (file + json.load + pdftotext) ; (78) note #2 réécrite (v2, 6 pages) autour de son nouveau centre de gravité : la carte à quinze fonctions L avec son palmarès de stress-tests EN VITRINE (deux hypothèses tuées par χ₁₉, paire jumelle, χ₂₁ ✓, χ₁₇ ✗ et instabilité paramétrique — « une carte à 10%, pas une loi fermée »), bande passante vs comptage (vacance quasi-universelle ~½ zéro, V_ζ = 0.401), linéarité = réseau (PNT vu du radical), profil Δ(ℓ) survivant avec la dissolution de κ racontée honnêtement, loi de recrutement, quorum citant le théorème compagnon, et la conséquence-graal (aucune inégalité avec du jeu) — au tiroir, en attente de relecture ; (79) rapport de rapporteur de l'auteur sur la note #2 appliqué en quinze patchs : quorum recalibré (« certified computationally at fixed windows », le théorème toute-échelle reste conjecture), 14/17 caractères avec critère de sélection avoué (d = −8, −20, −23 non calculés, prochains tests), protocole du training set explicité (12 = table moins χ₂₁/χ₁₇ ; χ₁₉ absorbé après test ; χ₁₅† transitoire exclu du fit ; ζ hors carte), 10⁻⁴⁸ ancré à (ζ, µ=11), collision lexicale « fifteen » levée (2⁴−1), légende de table complétée (segments, intercepts b_ζ ≈ −20 non uniformisés), Siegel clarifié (zéro réel ≠ petit γ₁), χ₋₂₃ désigné meilleur prochain test, hash de dépôt figé dans Reproducibility — et README du dépôt aligné et POUSSÉ (commit 9785235 : carte M3 finale + palmarès, s_ζ = 11.7, ancienne loi trois-variables retirée), vérifié sur clone frais ; (80) note #2 v2 PUBLIÉE au dépôt (notes/depth-phenomenology.pdf, commit vérifié sur clone frais), dateline « draft pending » levée après application du rapport, section Documents du README complétée — le triptyque est public : note Suzuki (v2), théorème du quorum, phénoménologie de profondeur, plus le carnet ; (81) LE CROCHETAGE COMMENCE : positivité de Q(µ=11) CERTIFIÉE (congruence + Gershgorin + Sylvester : rasoir 3.58×10⁻⁴⁸ ± 3×10⁻⁵⁴ contre hors-diag ≤ 8.5×10⁻⁵⁴, 152 s) après échec instructif de la Cholesky directe (pivot 14, conditionnement 10⁴⁸) — les deux moitiés du théorème existent à µ = 11 ; prochain coup : les 47 carrés certifiés contre les évaluateurs de zéros ; (82) MUSIC exécuté : P1 confirmée (identité matricielle premiers=zéros, chute au bord de bande 120.5, queue algébrique 1/γ), P2 confirmée au-delà de l'espéré — le radical est un sous-espace de bruit rigoureux (|v̂(γ)| ≤ √(λ/2)), douze premiers zéros retrouvés à 10⁻¹⁹-10⁻²⁰ (γ₁ à 9×10⁻²⁰), 30/40 en bande, 60 s — chaque barreau est un détecteur de zéros de précision √λ, la dualité premiers↔zéros comme fait de sous-espaces ; (83) les deux crans suivants : B — enveloppe exacte (masse 1.000000) mais individus inexistants (mélanges 0.5-0.93, cohérence du cadre 0.19/0.84), l'individualité vit dans le bruit ; A — détecteur Dirichlet après leçon de méthode (le vecteur à λ=0.12 admis à tort décale tout de +8 : √(λ/2) est le critère d'admission), γ₁(χ₃) à 2.5×10⁻⁹, dégradation en échelle reflétant les valeurs propres — RECADRAGE : s(χ) est l'exposant de lisibilité des zéros, la carte de profondeur devient la théorie de quelles fonctions L sont faciles à lire depuis les premiers ; (84) loi de précision FERMÉE : étalon Hurwitz 60 chiffres, erreur vraie 4.16×10⁻⁵⁸ à µ=38 (57 décimales de γ₁(χ₃)), mécanisme exact (erreur = |v̂|/|v̂′| à 3 chiffres), HYPER-NULLITÉ (|v̂₀(γ₁)| = 6.4×10⁻⁶⁰ contre borne 6×10⁻³¹ : masse refoulée à la frontière de bande, front de moisson côté zéros), et loi corrigée erreur ≈ e^(−sµ) pleine profondeur (pente mesurée 4.16 contre s = 4.00) — s(χ) est le coût par décimale du premier zéro ; (85) spectre de fuite mesuré (55 zéros de ζ à 55 chiffres) : loi exponentielle ln|v̂₀(γ)| ≈ −τ(ω_max−γ), τ ≈ 0.48 (identification ouverte), pic frontalier à γ = 124.3 (bord 120.5, préenregistré ✓), budget 42% dans la bande — λ = fuite frontalière + traîne ; profils parallèles des barreaux 1-2 (spectre de fuite universel scalé par la profondeur) ; LECTURE : la difficulté de la positivité vit dans une bande de largeur O(1/τ) autour du bord — le problème est localisé ; (86) campagne τ : artefact « précision au chargement » attrapé par violation de borne (neuvième famille — la constante 2.92×10⁻¹⁸ trans-configurations = pente × troncature 10⁻¹⁶), puis D1 base-insensible ✓, D2 µ-insensible ✓, D3 arithmétique-dépendant (mise fenêtre morte, seizième exécution), τ = γ₁/29.8 séduisant sur deux points puis tué par χ₄ à −17% (dix-septième) — statut : τ ≈ γ₁/30 à ±20%, profils des caractères trop courts à µ=11, courbure sous-exponentielle visible (front de moisson quadratique ?), remède = µ 20-38 ; (87) profil long ζ µ=16 : hyper-nullité > 56 chiffres (le plancher des zéros à 55 chiffres est atteint — il faut des zéros à 90+ chiffres pour voir le fond), pentes locales décroissantes vers le bord dans les deux µ (signature quadratique-de-front qualitative, accord quantitatif en échec : verdict exponentiel/quadratique suspendu), pente de mi-bande ~0.5 universelle en µ ; (88) zéros profonds (45 à 85 chiffres, 2 s) : |v̂₀(γ₁)|(µ=16) = 4.7×10⁻⁷² entre les deux prédictions, quadratique statistiquement vainqueur mais courbure douce, D2 (µ-indépendance de τ) MORT — artefact de gammes plafonnées (dix-huitième exécution) — et LA LOI D'EXTRÉMITÉ : |v̂₀(γ₁)| ≈ C·λ₀ avec C ∈ [7,25] sur quatre configurations et soixante ordres — racine unique de l'hyper-nullité, de e^(−sµ) et du profil (τ ≈ sµ/2ω_max à 6% sur ζ) ; question restante : pourquoi λ et pas √λ — auto-cohérence de point fixe à formaliser ; (89) formalisation : PROPOSITION A démontrée (G·v̂ = (λ/2)·v̂ — le radical et le quasi-noyau du Gram des zéros sont le même objet, preuve en trois lignes), conspiration de la queue mesurée (les zéros >45 annulent l'action du Gram en bande sur 66-98 chiffres), genou de Nyquist γ*=2πµ MORT (94.7/87.4 mesurés contre 69/100.5 prédits, ordre inversé — dix-neuvième exécution) — la loi d'extrémité est posée dans son cadre, question ouverte : le second ordre de petitesse en γ₁ ; (90) les six PR de la campagne des lemmes revues et mergées ; zéros des trois caractères manquants contre-vérifiés (Hurwitz, 7 chiffres) ; verdict out-of-sample aux fenêtres d'uniformisation : χ₋₈ PASS (contrôle interne), χ₋₂₀ kill probable par le haut (0.68 montant contre 0.57), χ₋₂₃ KILL NET (0.54 contre 0.76, −29% — vingtième exécution) : LA CARTE EST MORTE, et elle est morte exactement sur ses deux axes de fragilité documentés — la carte des modes d'échec survit à la carte ; (91) lecture de l'état post-merge : les addenda des branches sont l'œuvre d'un second modèle (Grok) — travail vérifié sur pièces et retenu : variation de L à χ₋₈ fixé (l'espacement suit le NIVEAU, pas la fenêtre — A1 à arithmétique fixée ; le peigne 2π donne Δ≈7-9 hors profil : l'universalité appartient à la famille de Weil, A2 se scinde) et budget de queue des 47 carrés (500 zéros, résidu 4.1%, enveloppe explicite O(1/G)) ; section Documents du README complétée (8 notes, compteurs 1690/90) — le dépôt est cohérent surface par surface ; (92) bloc 5×5 en Arb : quinze boules sur quinze contiennent 0, Qpr certifié à 10⁻²⁴, goulot = enveloppe de queue 3.18×10⁻² — enclosure, pas égalité au rasoir ; (93) B1/B2 pour ζ à µ=16 : 4/6 à R=8, 6/6 à R=12 — 11 et 13 parlent tard, le recrutement fixe R. (94) carte à 2 var (γ₁, parité) : +97% sur χ₋₂₃ — elle meurt plus fort que la 4-var ; χ₋₂₃ impair forage comme pair ; la parité est l'axe coupable. (95) plateau Δ vs 2πe : χ₃ à µ=16/22/30 grimpe 15.88→16.92→17.07 (niveau 105), écart à 2πe = 0.01 — le lock « reste à 16 » est mort ; (96) χ₃ µ=38 Δ=16.82 et χ₄ µ=38 Δ=18.16 — plateau = [16.8, 18.2], 2πe à l'intérieur, plus seul. (97) χ₋₂₀ à µ=50 : sécante 0.590 contre 0.57 (+4%), montée lente, kill 20% non tiré — une seule mort nette reste χ₋₂₃ ; (98) cran Dirichlet : MUSIC χ₃ µ=16 retrouve γ₁(L(·,χ₃)) à 1.3×10⁻¹² et les six premiers à <10⁻⁸ — le radical détecte les zéros du L, pas seulement ceux de ζ ; (99) directions du haut : radical ⊥ ĉ(γ) ; top-6 dans le span des évaluateurs en bande (cos 0.65–0.90) ; λ_max n'est pas γ₁ ; (100) second ordre : ζ µ=11 N=21 donne C=|v̂(γ₁)|/λ = 27.8 (fenêtre publiée [7,25]) ; |v̂|/√λ est 10⁻¹⁶ sous le bound MUSIC ; (101) queue signée des 47 carrés : 2.49×10⁻³ contre 3.18×10⁻² non signée (facteur 13), au niveau du résidu mesuré ; (102) quatre crans : C=κ conditionnel (valeurs pas encore égales) ; Arb signé 15/15 borne 6.0×10⁻³ ; Δ_∞ = deux amas (16.94 / 17.90) ; appariement 1-1 greedy cos moyen 0.81 ; (103) Δ_∞ n'est pas coupé par la parité : χ₅ pair à µ=38 Δ=17.99, grimpe vers l'amas χ₄, χ₃ reste seul ; (104) χ₇ s≈1.67, Δ=16.23→17.34 à ℓ=44→58 : encore une montée, pas un second amas χ₃. Le plateau n'est lisible qu'à grand s ; (105) appariement N=21 : 1-1 tient à K=6 (min 0.61), casse à K=8 (min 0.14) ; ζ µ=11 encore sur la rampe Δ=12 ; (106) queue synthétique 811→4000 : biais 4.3→1.5×10⁻³ ; ζ µ=16 toujours sur la rampe Δ≈12 ; (107) peigne à 20 000 : résidu 0.71×10⁻³, jitter GUE inutile, reste en 1/G, ~20 % de masse manquante ; (108) ce qu'on loupe : 3-var (γ₁,gap,D) sauve χ₋₂₃ à −4 % ; Δ(ℓ) universel sur la rampe, pas au sommet ; (109) 3-var LOO RMS 29 % (χ₁₇ +64 %) ; hold-out −7.5/−19.1/−3.9 % — successeur mou, pas une loi ; (110) χ₋₂₀ sécante 50→62 = 0.582 (stationnaire) ; 3-var ŝ=0.44 tue à −24 %. Plus que χ₋₈ ; (111) sécante χ₋₂₀ : s_∞ ∈ [0.57, 0.62], un revirement de 0.008 n'est pas un plateau ; 3-var 0.44 hors intervalle ; (112) Newton–Raphson / Steffensen : triplet final → 0.584 ; la paire du revirement casse le modèle 1/μ (s_∞=0.549) ; (113) sécante 62→74 = 0.622 : le 0.582 était un creux ; Steffensen 0.589, linéaire 0.579 ; (114) préfacteurs 4/L, 4√2/L, 8/L : rapport mesuré/prédite = 1.045 partout — le 20 % était 4/L sur le bloc 8/L ; (115) les 4.5 % ne sont pas une oscillation (O(1/G²)=0.03 %) : compensation ρ=1 contre un biais Q_pr ~20 % ; (116) audit (0,0) : Qpr−(Qz+ρ)=2.34×10⁻⁴ = 0.45 % de Qpr, même 0.44 % sur (0,1) et (1,1). L'identité tient au demi-pourcent ; (117) le 0.44 % tombe en 0.190/G sur six cuts : queue, pas Qpr. Arch propre à 10⁻⁸ ; (118) 0.190/G tenu à G=888 et G=1001 (n=560, 650). C≈0.191, α≈0.115 ; (119) C=0.190 ± 0.003 jusqu'à G=1244 (n=850). Phase cos(Lγ) cohérente avec le premier 11, signe du biais ; (120) C=Λ(μ)/(4√μ) : 0.190/0.181/0.104/0.042 mesurés contre 0.181/0.178/0.092/0.043. Le bord de fenêtre est un entier ; (121) C(G) convergé dès G≈200 : {13,16} sur la cible, {9,11} plat 5–13 % au-dessus — plus un effet de cut ; (122) C=2Λ/(π L √μ) : {9,11} se ferment. Λ/(4√μ) était un fit à L=8/π ; (123) (0,0) close : reste O(1/G²) ~10⁻⁶ après C/G ; (124) 5×5 : (0,1) et (1,1) mêmes restes après √2 C et 2 C ; (125) C=κ : C(N)=7107→48 vers 27.8 ; κ illisible sur la même Q (e^{−ℓ/2}) ; (126) RH : Weil exige toutes les h ; une fenêtre PSD + Gram n'est pas une preuve. Circulaire si Qz ; (127) K=7 min cos=0.27 (γ₇ au bord) ; 47-dim Arb bloqué sans flint ; (128) trois routes RH : classe dense échantillonnée PSD ; L→∞ n'a pas de minorant ; pas de trou uniforme (λ~e^{−sμ}) ; (129) positivité de Weil : RH⇒Q≥0 est un carré ; la réciproque exige toute la classe, pas V_N. Quorum ≠ Weil ; (130) trois optima : v (Rayleigh), ĉ(γ) (lecture), Beurling/Li (classe de Weil). v ⟂ zéros en bande ; (131) polynômes RS : cut √(t/2π) pour Z(t), pas le quorum n≤μ. Turán ≠ RH ; (132) polynômes de Weil = det(1−T Frob) sur F_q, RH théorème (Weil–Deligne). det(zI−Q) n'en est pas un.

## Annexe F — Tableau récapitulatif des constantes mesurées

| Constante | Valeur | Statut |
|---|---|---|
| Taux de fermeture générique de la marge de Weil | s²·γ_front/ρ(γ_front) ≈ 0.34-0.40 à notre fenêtre (le « 0.41 ») | **expliqué** (§14) : front de moisson, confirmé sans paramètre sur 4 décades |
| Taux dans le plongeon de Slepian | jusqu'à ≈ 3.0 par dimension près du mur de rang | mesuré à U = 2.5, bande 42 zéros |
| Frontière de certification du crible | U_max ≈ 0.65·log N ; bruit ~ ×8 par décade de N | mesuré (campagne 4), axe non couvert par la littérature lue |
| Décroissance CC de λ_min | −ln λ_min ≈ 10·µ (leur régime, base complète) | littérature, raccordé par nos mesures |
| Loi de forme (Suzuki 1.2) | résidu infrarouge ≈ (1/3)·e^(−L) = 0.33/µ | mesuré (v2), premier test connu de la version fonctionnelle |
| Rapport infrarouge/entre-zéros du résidu | ≈ 30-40× à tout µ | mesuré : le goulot est le bombement en Γ sous γ₁ |
| Constante de normalisation c_a | c_∞ = ‖Φ_S‖_L² = 1.130932 (norme du noyau thêta) | **identifiée** (§12) : recouvrement 0.99964 à µ=11, estimateur par projection à 4×10⁻⁴ |
| Validation externe | λ_min(µ=11) = 3.6×10⁻⁴⁸ vs 2.389×10⁻⁴⁸ (CC) | chaîne complète certifiée à l'ordre de grandeur |
| Identification en famille (§13) | c_∞(χ) = ‖Φ_χ‖ à ≤ 4×10⁻⁴, six caractères | **confirmée 6/6**, prédiction sans paramètre |
| Constante de forme C(χ) | ζ : 0.33 ; impairs : 0.39-0.43 ; pairs : 0.50-0.53 | mesurée : signature de parité |
| Loi d'échelle | −ln λ_min = s·µ + b, affine pour TOUTE la famille ζ comprise : s de 0.46 (χ₂₄ᵒ) à 11.7 (ζ, base 71) ; loi Dirichlet M3 : s ≈ 0.14·γ₁^1.32·(γ₂−γ₁)^0.45·e^(−0.13D)·1.32^[impair] à 6.1% (LOO 4.8%) ; ζ hors famille à 3% du bord | mesurée ±0.02-0.2 ; résidus χ₁₂ +14% / χ₁₃ −10% ouverts |

## Annexe G — Statut épistémique, mise à jour v2

Aux trois registres de l'annexe C s'ajoutent, côté **mesuré ici (v2)** : les trois régimes de positivité et leurs taux, la protection par blancheur (lecture de mesures, pas théorème), les artefacts documentés (nœuds float64, séparation d'intégrande, regroupement archimédien), la loi de forme R ≈ e^(−L)/3 avec son protocole à double limite, et la validation croisée contre la valeur publiée de Connes-Consani. Côté **littérature (v2)** : théorème des ζ-cycles, criticité de Connes-van Suijlekom, fonction vis et conjecture (1.2) de Suzuki, résultats de Groskin. Passe au registre **mesuré** (v2, §12-13) : l'identification c_∞ = ‖Φ_S‖ et la vérification L² de (1.2) à 4×10⁻⁴, puis leur extension six sur six à la famille de Dirichlet, la signature de parité de C, et la loi d'échelle linéaire −ln λ_min = s(χ)·µ (pentes sur trois points par caractère, sauf ζ sur deux régimes de méthode différents). La lecture « sismographe de Siegel » est un principe d'observable, pas encore un détecteur opéré. Restent **spéculatifs** : toute lecture du milieu comme objet physique et l'interprétation de la blancheur comme mécanisme plutôt que description. La loi de forme repose sur six points en µ dont deux extrapolés en base : elle est falsifiable par extension de la série et doit être traitée comme provisoire.

Mise à jour 1er septembre 2026 (journal 69–88, HEAD `6048ab1`). Passe au registre **théorème, à fenêtre fixe** : le quorum sur les formes explicitement définies Q_S (340 témoins Arb) — `notes/quorum-theorem.pdf`. Passe au registre **certificat fini, pas RH** : définie-positivité de Q à µ = 11 (rasoir 3.58317×10⁻⁴⁸ ± 3×10⁻⁵⁴). Passe au registre **mesuré** : MUSIC, hyper-nullité, loi de précision e^(−sµ), spectre de fuite, et la loi d'extrémité |v̂₀(γ₁)| ≈ C·λ₀ avec C ∈ [7,25] sur soixante ordres (journal 88) — racine unique de l'hyper-nullité, de e^(−sµ) et de τ ≈ sµ/(2ω_max) à 6% sur ζ. D2 (µ-indépendance de τ) est morte. Le quorum à toute échelle et les 47 carrés certifiés restent ouverts. Neuvième famille d'artefacts : précision au chargement des zéros.


## Annexe H — Statut au 1er septembre 2026 (HEAD de ce cran)

Trois colonnes. Ne pas les mélanger.

**Tenu.**
- Quorum : un premier manquant casse la PSD.
- Pôle (0,0) = 32 sinh²(L/4)/L. Arch = ∫ψ à 10⁻⁸.
- MUSIC : les zéros de L(s,χ) sortent du radical (ζ, χ₃).
- Directions du haut = span des évaluateurs en bande. Appariement 1-1 pour K≤6, pas K=8.
- |v̂(γ₁)| = C λ, pas √λ (mesuré).
- Q_pr = Q_z sur le 5×5 à O(1/G²) après queue ρ + bord C/G, C = 2Λ(μ)/(π L √μ).

**Mort.**
- Cartes de s(χ) : 4-var tuée par χ₋₂₃, 3-var tuée par χ₋₂₀ à s≈0.58.
- Δ_∞ = 2πe universel. Deux amas. χ₃ seul vers 16.9.
- Δ_∞ coupé par la parité. χ₅ pair grimpe.
- « Fifteen L-functions, one ladder » au sommet. Vrai sur la rampe 9–14 seulement.
- « Q_pr = Q_z à 5 % » du §40 (densité 1, pas une enclosure).

**Ouvert.**
- 47×47 en Arb : script prêt, python-flint absent de l'environnement.
- RH (§52, §54) : pas de trou uniforme ; pas de minorant en L ; fenêtre PSD échantillonnée seulement. Une fenêtre n'est pas une preuve.

**Tranché depuis.**
- C=κ : forme seulement (§51).
- Appariement K>6 : casse au dernier zéro en bande, K=7 min=0.27 (§53).

