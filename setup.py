from cx_Freeze import setup, Executable
base = None
executables = [Executable("src/main.py", base=base)]
packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },
}
setup(
    name = "Wifi Test Manager",
    options = options,
    version = "1.0",
    description = 'Juste un programme de test de wifi et d\'affichage des résultats',
    executables = executables
)