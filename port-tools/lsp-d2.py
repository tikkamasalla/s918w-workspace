import logging
logging.disable(logging.CRITICAL)
from androguard.misc import AnalyzeAPK

a, d, dx = AnalyzeAPK(r'E:\phone-pending\lsp-manager-7854.apk')
dexes = d if isinstance(d, list) else [d]
want = {'Lvw0;': ('n', 't'), 'Lrf;': ('e', 'd')}
out = []
for dex in dexes:
    for cls in dex.get_classes():
        cn = cls.get_name()
        if cn in want:
            out.append('#' * 20 + ' ' + cn)
            for m in cls.get_methods():
                if m.get_name() in want[cn]:
                    out.append('=' * 10 + ' ' + m.get_name() + ' ' + m.get_descriptor())
                    code = m.get_code()
                    if code is None:
                        out.append('   NO CODE'); continue
                    for ins in code.get_bc().get_instructions():
                        out.append('    ' + ins.get_name() + ' | ' + ins.get_output())
open(r'E:\s918w-port\lsp-n.txt', 'w').write('\n'.join(out))
print('wrote', len(out), 'lines')
