import zipfile
import glob as g
import logging
logging.disable(logging.CRITICAL)
from androguard.core.dex import DEX

src = g.glob(r'C:\Users\Aows\Downloads\*maps_26.36*')[0]
z = zipfile.ZipFile(src)
dx = DEX(z.read('classes5.dex'))
targets = {
    'displayConfig.isSpeedometerClickable: ',
    'displayConfig.isSpeedometerMphLabelEnabled: ',
    'isSpeedometerEligible: ',
    'allowShowSpeedLimitAndWatermark',
    'speedLimitAndWatermarkMode: ',
    'speedLimitSettingEnabled: ',
}
for s in dx.get_strings():
    v = s.get_value() if hasattr(s, 'get_value') else str(s)
    if v in targets:
        print('STRING:', repr(v))
        for m in dx.get_methods():
            try:
                code = m.get_code()
                if code is None:
                    continue
                bc = code.get_bc()
                insns = list(bc.get_instructions())
            except Exception:
                continue
            for ins in insns:
                try:
                    op = str(ins.get_op_value())
                    out = ins.get_output()
                except Exception:
                    continue
                if v in out:
                    print(f'  used by {m.get_class_name()} -> {m.get_name()} {m.get_descriptor()}')
                    break
