"""验证远程环境与本地工具库一致。"""
import sys

import numpy
import scipy
import matplotlib

print("python     ", sys.version.split()[0])
print("numpy      ", numpy.__version__)
print("scipy      ", scipy.__version__)
print("matplotlib ", matplotlib.__version__)
print("TOOLENV_OK")
