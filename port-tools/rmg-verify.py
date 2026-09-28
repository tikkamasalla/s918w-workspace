data = open(r'E:\rmg-app-fork\app\build\outputs\apk\release\app-release.apk', 'rb').read()
print('size:', len(data))
print('ours:', data.count(b'tikkamasalla/Root-My-Galaxy-Payloads'))
print('his:', data.count(b'HyperRamzey/Root-My-Galaxy-Payloads'))
