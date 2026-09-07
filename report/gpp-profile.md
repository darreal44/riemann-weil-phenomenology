# Profile of g'' on the well

Same witness, [0, y_min=0.410]. Elementary `g_pp`, `g_ppp`.

    y      g''      g'''
    0.000   9.636    −7.22
    0.041   9.306    −8.86
    0.082   8.910   −10.42
    0.123   8.453   −11.85
    0.164   7.941   −13.11
    0.205   7.381   −14.16
    0.246   6.783   −14.97
    0.287   6.157   −15.53
    0.328   5.513   −15.83
    0.369   4.862   −15.86
    0.410   4.216   −15.63

g'' falls almost linearly from 9.64 to 4.22 (slope ∼ −13, consistent
with g''' around −8 to −16). #83 must use m=4.22 on the whole well. A
two-piece mesh at y=0.20 would get m≈7.4 then m≈4.2 and keep g''(0) on
the first interval.

inf |g'''| is about 7.2 at 0; sup |g'''| about 15.9 near 0.37. A cubic
that uses m₃=−15.9 on the whole well pays a steep y³ and may lose to
#83. Local m₃ on [0,0.12] (∼ −12) is the useful one.
