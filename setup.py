
##IN caz  de eoare nu uita la  compilare sa copii manual  failu CONFIG.INI
##IN caz  de eoare nu uita la  compilare sa copii manual  failu CONFIG.INI
##IN caz  de eoare nu uita la  compilare sa copii manual  failu CONFIG.INI
##IN caz  de eoare nu uita la  compilare sa copii manual  failu CONFIG.INI
##IN caz  de eoare nu uita la  compilare sa copii manual  failu CONFIG.INI

####iCONCILE  MAPA INAGES,  TOT  COPIO


from cx_Freeze import setup, Executable


# import PySide.QtWebKit


GUI2Exe_Target_1 = Executable(
    # what to build

    script = "start.pyw",
    # script = "main_window.py",
    # script = "classes_becash.py",

    initScript = None,
    base = 'Win32GUI',  # <-- add this
#    targetDir = "compiled",
    targetName = "Red Ball.exe",
    compress = True,
    copyDependentFiles = False,
    appendScriptToExe = True,
    appendScriptToLibrary = False,
    icon = r"images\circle_red_big.ico"
    )


# Dependencies are automatically detected, but it might need fine tuning.
#build_exe_options = {"packages": [], "excludes": ["_bz2","_decimal","_lzma","_ssl","_hashlib"]}


setup(
    name = "Trio Ball",
    version = "2.0",
 #   options = {"build_exe": build_exe_options},
    description = "www.suav.biz",
    include_files = r"config.ini",
    executables = [GUI2Exe_Target_1])
