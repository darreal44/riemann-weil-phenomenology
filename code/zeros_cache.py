# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
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
