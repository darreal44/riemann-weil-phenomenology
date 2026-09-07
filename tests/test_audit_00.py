# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# (0,0) audit at mu=11 (notebook 42).
QPR_00 = 0.05233872425
QZ_RHO_00 = 0.05210465942
REL = (QPR_00 - QZ_RHO_00) / QPR_00


def test_gap_is_half_a_percent():
    assert 0.003 < REL < 0.006


def test_script_exists():
    import os
    src = open(os.path.join(os.path.dirname(__file__), '..', 'code', 'audit_00.py')).read()
    assert 'tail_rho' in src and 'qpr_pieces' in src
