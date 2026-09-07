# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Wrap the two pre-campaign stdlib scripts so pytest runs them too.
import os, runpy

HERE = os.path.dirname(os.path.abspath(__file__))


def test_cert_mu11_script():
    runpy.run_path(os.path.join(HERE, 'test_cert_mu11.py'), run_name='__not_main__')


def test_theta_endpoints_script():
    runpy.run_path(os.path.join(HERE, 'test_theta_endpoints.py'), run_name='__not_main__')
