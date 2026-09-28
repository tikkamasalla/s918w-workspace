import logging
logging.disable(logging.CRITICAL)
from androguard.core.apk import APK
a = APK(r'E:\morphe\gmaps-26.36-speedo-v2.apk')
dex = a.get_dex()
names = [c.get_name() for c in dex.get_classes()]
print('total classes:', len(names))
for n in names:
    if 'ungoogled' in n.lower():
        print('  ', n)
