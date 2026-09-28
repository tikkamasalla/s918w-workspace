import tempfile
import zipfile
import glob as g
import logging
import os
logging.disable(logging.CRITICAL)

src = g.glob(r'C:\Users\Aows\Downloads\*maps_26.36*')[0]
z = zipfile.ZipFile(src)
blob = z.read('classes5.dex')
# find field ids: search raw for 'Lavmi;->A(' etc, plus interface-style calls
for nd in [b'Lavmi;->A(', b'Lavmi;->B(', b'Lahiw;->n ', b'Lahiw;->o ',
           b'Lahiw;->p ', b'Lahiw;->b(']:
    idxs = []
    i = 0
    while True:
        i = blob.find(nd, i)
        if i < 0:
            break
        idxs.append(hex(i))
        i += 1
    print(nd.decode(), '->', len(idxs), idxs[:4])
