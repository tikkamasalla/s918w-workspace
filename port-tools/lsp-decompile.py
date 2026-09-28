import logging
logging.disable(logging.CRITICAL)
from androguard.misc import AnalyzeAPK

a, d, dx = AnalyzeAPK(r'E:\phone-pending\lsp-manager-7854.apk')
print('package:', a.get_package())
for cl in dx.get_classes():
    try:
        cname = cl.get_vm_class().get_name()
    except Exception:
        continue
    short = cname.strip('L;').split('/')[-1]
    if short == 'ur3':
        print('CLASS:', cname)
        for mm in cl.get_methods():
            try:
                m = mm.get_method()
                print('  ', m.get_name(), m.get_descriptor())
            except Exception as e:
                print('  ERR', e)
