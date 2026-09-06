#!/usr/bin/env python3
"""Silent until SUMMARY.txt exists. Prints DONE or FAILED only."""
import os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
SUMMARY = os.path.join(HERE, "SUMMARY.txt")
# launcher stdout is also copied here if we tee; fall back to any *.log growing
while True:
    if os.path.exists(SUMMARY):
        text = open(SUMMARY, encoding="utf-8").read()
        # "done in Ns ; F failed / N"
        if "; 0 failed" in text:
            print("DONE")
            sys.exit(0)
        print("FAILED")
        sys.exit(1)
    time.sleep(30)
