import logging
logging.disable(logging.CRITICAL)
from androguard.core.apk import APK
a = APK(r'E:\rmg-app-fork\app\build\outputs\apk\release\app-release.apk')
print('pkg:', a.get_package(), a.get_androidversion_name(), a.get_androidversion_code())
for c in a.get_certificates():
    print('cert:', c.sha256_fingerprint.replace(' ', ''))
print('valid sig:', a.is_signed())
