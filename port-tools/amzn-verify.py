import logging
logging.disable(logging.CRITICAL)
from androguard.core.apk import APK
a = APK(r'E:\morphe\amazon-32.13.2.100-patched.apk')
print('package:', a.get_package(), a.get_androidversion_name(), a.get_androidversion_code())
dex = a.get_dex()
names = dex.get_classes_names() if hasattr(dex, 'get_classes_names') else []
hits = [c for c in dex.get_classes() for _ in [0] if False]
found = []
for c in dex.get_classes():
    n = c.get_name()
    if 'SortByRatings' in n or 'PriceHistory' in n or 'Rufus' in n:
        found.append(n)
print('hook-helper classes:', found if found else 'NONE')
