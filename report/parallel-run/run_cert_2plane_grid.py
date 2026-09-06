#!/usr/bin/env python3
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "code"))
os.chdir(os.path.join(ROOT, "code"))
from cert_2plane import cert

for name in ("chi5", "chi3", "chi4", "chi8", "chi13", "chi29", "chi7"):
    for mu in (11.0, 16.0, 38.0):
        try:
            cert(name, mu, 40)
        except Exception as e:
            print(name, mu, "FAIL", e, flush=True)
