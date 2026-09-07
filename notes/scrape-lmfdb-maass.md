<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# LMFDB Maass zeros, user at the wheel

The lab browser hits a Google
interstitial. Yours can pass it.

    pip install playwright
    playwright install chromium
    python code/scrape_lmfdb_maass.py 1.0.1.1.1 11.0.1.1.1

A Chromium window opens. Solve
the captcha, press Enter in the
terminal. The script does not
bypass anything. It dumps floats
from the page body into
`code/zeros_<label>.txt`.

Then:

    python code/import_maass_zeros.py 11.0.1.1.1 code/zeros_11.0.1.1.1.txt

The regex will pick up extra
decimals (R, conductor). Trim
if n looks insane. Not Weil.
