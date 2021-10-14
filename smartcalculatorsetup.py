from cx_Freeze import *
import sys
includafiles = ['Calculator-icon.png']
base = None
if sys.platform == "Win32":
    base = "Win32GUI"


shortcut_table = [
    ("DesktopShortcut",  #  Shortcut
     "DesktopFolder",   #  Directory_
     "My calculator",  #  Name
     "TARGETDIR",     #  component_
     "[TARGETDIR]\smartcalculator.exe",  # Target
     None,  #  Arguments
     None,  #  Description
     None,  #  Hotkey
     None,  #  Icon
     None,  #  IconIndex
     None,  #  showCmd
     "TARGETDIR",   #  WKDIR
     )
 ]
msi_data = {"Shortcut": shortcut_table}

# change some default MSI options and specify the use of the above definedtables
bdist_msi_options = {'data': msi_data}
setup(
    version ="0.1",
    description=" My calculator",
    author="vicky kartoos",
    name="My calculator",
    options={'build_exe': {'include_files': includafiles},"bdist_msi": bdist_msi_options},
    executables=[
        Executable(
            script="calculatorproject.py",
            base=base,
            icon='Calculator-icon.png',
        )
    ]
)
