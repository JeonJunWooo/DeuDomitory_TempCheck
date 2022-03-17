import sys
from distutils.core import setup
from cx_Freeze import setup, Executable
import os

buildOptions = dict(packages = ["time", "sys", "os", "chromedriver_autoinstaller", "selenium.webdriver.common.keys", "selenium"],
                   excludes = [],
                   includes = [])
                   
base = "Win32GUI" if sys.platform == "win32" else None
exe = [Executable('hyomin_temp_check.py', base=base)]

setup(
    name= 'happy_temp_check',
    version = '0.1',
    author = "Inys",
    description = "dong-eui university happy domitory auto temperature check program",
    options = dict(build_exe = buildOptions),
    executables = exe
)