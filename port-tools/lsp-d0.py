import logging
logging.disable(logging.CRITICAL)
from androguard.misc import AnalyzeAPK

a, d, dx = AnalyzeAPK(r'E:\phone-pending\lsp-manager-7854.apk')
dexes = d if isinstance(d, list) else [d]
for dex in dexes:
    for cls in dex.get_classes():
        if cls.get_name() == 'Lur3;':
            for m in cls.get_methods():
                if m.get_name() in ('d0', 'm0'):
                    print('=' * 20, m.get_name(), m.get_descriptor())
                    code = m.get_code()
                    if code is None:
                        print('   NO CODE'); continue
                    for ins in code.get_bc().get_instructions():
                        print('   ', ins.get_name(), '|', ins.get_output())
