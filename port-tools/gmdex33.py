import tempfile
import zipfile
import glob as g
import logging
import os
logging.disable(logging.CRITICAL)

src = g.glob(r'C:\Users\Aows\Downloads\*maps_26.36*')[0]
z = zipfile.ZipFile(src)
blob = z.read('classes5.dex')
# brute force: every occurrence of the ASCII method names of interest,
# print the closest Lrdu method signature above it (class refs are elsewhere,
# so instead scan for 'Lrdu;->' refs)
needles = [b'Lrdu;->', b'Lahiw;->b(', b'setIsCompassNeedleOnly',
           b'CompassButtonView']
for nd in needles:
    idxs = []
    i = 0
    while True:
        i = blob.find(nd, i)
        if i < 0:
            break
        idxs.append(i)
        i += 1
    print(nd.decode(), '->', len(idxs), 'refs; first at', [hex(x) for x in idxs[:5]])
