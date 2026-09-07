# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Raccourci mono-echelle : le theoreme du quorum a mu=11 (zeta), via le moteur de reference.
# Usage : python3 theoreme_quorum.py [verify]   — verify rejoue les temoins geles witnesses_zeta_mu11.json
import sys
from quorum_general import run
run(11, 46, 22, 'zeta', 'verify' if 'verify' in sys.argv[1:] else 'freeze')
