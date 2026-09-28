import logging
logging.disable(logging.CRITICAL)
from androguard.misc import AnalyzeAPK
import re

a, d, dx = AnalyzeAPK(r'E:\phone-pending\lsp-manager-7854.apk')
dexes = d if isinstance(d, list) else [d]
strs = set()
for dex in dexes:
    for s in dex.get_strings():
        if re.search(r'(?i)(getService|addService|checkService|listServices|lspd|lsposed|IXposed|manager.*service|service.*manager)', s):
            strs.add(s)
for s in sorted(strs):
    print(repr(s))
