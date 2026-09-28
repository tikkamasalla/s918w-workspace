import logging
logging.disable(logging.CRITICAL)
from androguard.misc import AnalyzeAPK

a, d, dx = AnalyzeAPK(r'E:\phone-pending\lsp-manager-7854.apk')
dexes = d if isinstance(d, list) else [d]
want = {'Lvw0;': ('n', 't'), 'Lk92;': (), 'Lrf;': ('e',), 'Lg71;': ()}
for dex in dexes:
    for cls in dex.get_classes():
        cn = cls.get_name()
        if cn in want:
            print('#' * 20, cn, 'super:', cls.get_superclassname())
            try:
                print('   source:', cls.get_source())
            except Exception:
                pass
            for m in cls.get_methods():
                if not want[cn] or m.get_name() in want[cn]:
                    print('=' * 10, m.get_name(), m.get_descriptor())
                    code = m.get_code()
                    if code is None:
                        print('   NO CODE'); continue
                    for ins in code.get_bc().get_instructions():
                        print('   ', ins.get_name(), '|', ins.get_output())
            # fields of Lk92
            if cn == 'Lk92;':
                for f in cls.get_fields():
                    print('   FIELD:', f.get_name(), f.get_descriptor())
