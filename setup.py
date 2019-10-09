from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base="Win32GUI")]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "<StockVu>",
    options = options,
    version = "<1.1>",
    description = '<Designed to perform various analysis on number of stocks every day>',
    executables = executables)