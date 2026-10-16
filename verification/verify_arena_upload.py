#!/usr/bin/env python3
"""Verify the specific Arena export using exact arithmetic, without NumPy."""
if not __debug__:
    raise SystemExit('Run without -O or -OO; proof assertions are required.')
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import resource
import signal
import sys
resource.setrlimit(resource.RLIMIT_CPU, (45,45))
resource.setrlimit(resource.RLIMIT_AS, (512*1024**2,)*2)
signal.alarm(65)
p = Path(sys.argv[1]) if len(sys.argv)>1 else Path('.')
c = json.loads((p/'certificate.json').read_text())
raw = (p/'solution.json').read_bytes()
assert hashlib.sha256(raw).hexdigest() == c['solution_sha256'], 'payload bytes'
a, D = c['height_numerators'], c['denominator']
assert len(a)==2048 and D==2**40 and all(type(x) is int for x in a)
assert all(0<=x<=D for x in a), 'height box'
assert sum(a)==1024*D, 'exact mass'
exact = [F(x) for x in json.loads(raw,parse_float=F)['values']]
assert exact==[F(x,D) for x in a], 'exact decimal interpretation'
assert [F.from_float(float(x)) for x in json.loads(raw)['values']]==exact, 'binary64 interpretation'
assert 1024*D<2**53
C={k:sum(a[i]*(D-a[i-k]) for i in range(max(0,k),min(2048,2048+k)))
   for k in range(-2048,2049)}
peak=max(C.values());cap=F(peak,1024*D*D)
assert cap==F(58934702484885152546989329,154742504910672534362390528)==F(c['exact_cap'])
assert [k for k,v in C.items() if v==peak]==[-311,311]
variation=F(sum(abs(x-y) for x,y in zip(a,a[1:])),D)
assert variation==F(8586218236003,274877906944)==F(c['exact_variation'])
print('PASS: exact mass/box; identical decimal and binary64 values;4097signed events')
print('EXACT_UPLOAD_CAP',cap,'ACTIVE_LAGS',[-311/1024,311/1024])
