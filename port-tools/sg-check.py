import logging
logging.disable(logging.CRITICAL)
from androguard.core.apk import APK
for f in [r'E:\SeriesGuide-classic\app\build\outputs\apk\pure\release\app-pure-release.apk',
          r'E:\SeriesGuide-classic-input\SeriesGuide-installed-2026.1.5.apk']:
    a = APK(f)
    certs = a.get_certificates()
    print(f.split('\\')[-1])
    print('  pkg:', a.get_package(), a.get_androidversion_name(), a.get_androidversion_code())
    for c in certs:
        print('  cert sha256:', c.sha256_fingerprint.replace(' ', '')[:32], '...')
