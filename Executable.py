from cx_Freeze import setup, Executable
base = None
executables = [Executable("Main.py", base=base)]
packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },
}
setup(
    name = "MasterPass",
    options = options,
    version = "1.0",
    description = 'Programme de gestion de mot passe',
    executables = executables
)