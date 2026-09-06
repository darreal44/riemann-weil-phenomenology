#!/usr/bin/env python3
"""Run the heavy test files in parallel, one pytest process per file (Windows/Linux).

    python tests/run_heavy.py            # all heavy files, workers = min(#files, cpu_count)
    python tests/run_heavy.py -j 8       # explicit worker count
    python tests/run_heavy.py --light    # the light suite, split by file across workers

mpmath is single-threaded: parallelism is per file. Each file's output goes to tests/logs/<file>.log;
a summary is printed at the end and the exit code is non-zero if any file failed.
"""
import os, sys, subprocess, time, glob
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
HEAVY = ['test_cert_mu3.py', 'test_orphans_wrapped.py', 'test_chi5_mu62.py', 'test_chi3_mu80_assembly.py',
         'test_gl2_conventions.py', 'test_gl2_eight_curves.py', 'test_gl2_quorum_laws.py', 'test_depth_law.py',
         'test_gl2_37a1_drop3.py', 'test_gl2_67a1_mu74.py']

def run_file(f):
    os.makedirs(os.path.join(HERE, 'logs'), exist_ok=True)
    log = os.path.join(HERE, 'logs', f.replace('.py', '.log')); t0 = time.time()
    with open(log, 'w') as out:
        r = subprocess.run([sys.executable, '-m', 'pytest', os.path.join(HERE, f), '-q', '--tb=short', '-p', 'no:cacheprovider'],
                           stdout=out, stderr=subprocess.STDOUT, cwd=ROOT)
    return f, r.returncode, round(time.time() - t0), log

if __name__ == '__main__':
    args = sys.argv[1:]
    jobs = int(args[args.index('-j') + 1]) if '-j' in args else None
    if '--light' in args:
        files = sorted(os.path.basename(p) for p in glob.glob(os.path.join(HERE, 'test_*.py')) if os.path.basename(p) not in HEAVY)
    else:
        files = HEAVY
    jobs = jobs or min(len(files), os.cpu_count() or 4)
    print(f"{len(files)} files, {jobs} workers")
    t0 = time.time(); failed = 0
    with ThreadPoolExecutor(max_workers=jobs) as ex:
        for f, rc, dt, log in ex.map(run_file, files):
            tail = open(log).read().strip().splitlines()[-1] if os.path.getsize(log) else ''
            print(f"  {'PASS' if rc == 0 else 'FAIL'}  {f:34s} {dt:5d}s   {tail[:90]}")
            failed += (rc != 0)
    print(f"done in {round(time.time()-t0)}s ; {failed} file(s) failed ; logs in tests/logs/")
    sys.exit(1 if failed else 0)
