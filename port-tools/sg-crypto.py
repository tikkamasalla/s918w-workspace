for label, path in [
    ('installed-2026.1.5', r'E:\SeriesGuide-classic-input\SeriesGuide-installed-2026.1.5.apk'),
    ('classic-build', r'E:\SeriesGuide-classic\app\build\outputs\apk\pure\release\app-pure-release.apk'),
]:
    data = open(path, 'rb').read()
    print('===', label, len(data))
    for needle in [b'EncryptedSharedPreferences', b'MasterKey', b'androidx/security/crypto', b'trakt.refresh_token', b'trakt-oauth-settings', b'Tink', b'AndroidKeyStore']:
        print('  ', needle.decode(), '->', data.count(needle))
