import logging
logging.disable(logging.CRITICAL)
from androguard.core.apk import APK
import os
d = r'E:\phone-pending'
for f in sorted(os.listdir(d)):
    if any(k in f for k in ['Downgrade', 'disabletarget', 'mobile-arm64', 'corepatch']):
        a = APK(os.path.join(d, f))
        print(f, '->', a.get_package(), a.get_androidversion_name())
