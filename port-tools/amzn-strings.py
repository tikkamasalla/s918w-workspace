data = open(r'E:\morphe\amazon-32.13.2.100-patched.apk', 'rb').read()
print('size:', len(data))
for needle in [b'SortByRatings', b'Most rated', b'PriceHistory', b'pricehistory', b'Rufus', b'rufus', b'DarkMode', b'darkmode']:
    print(needle.decode(), '->', data.count(needle))
