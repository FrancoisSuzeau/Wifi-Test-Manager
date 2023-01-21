from cx_Freeze import setup, Executable

# if your architecture is different then don't hesitate to change the relative path of your file when the main call is
executables = [
        Executable(
            script="src/main.py", 
            base="Win32GUI",
            targetName="Wifi Test Manager.exe",
            icon = None # if you want to use an icon file, specify the file name here
        )
]

packages = ["idna"]
includefiles = [] #include path of your personnal module if they are not located in the same directory of your main script
binaries = []
excludes = []
options = {
    'build_exe': {    
        'excludes':excludes,
        'packages':packages,
        'include_files':includefiles,
        'bin_includes':binaries,
        "include_msvcr": True
    },
}
# all the external module (such as matplot lib etc is copy directly in the lib directory and then transformed in a dynamic library file)

# change the name field with name of your application
setup(
    name = "Wifi Test Manager",
    options = options,
    version = "1.0",
    description = 'Juste un programme de test de wifi et d\'affichage des résultats',
    executables = executables
)