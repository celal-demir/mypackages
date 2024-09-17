from PyQt6.QtGui import QFontDatabase

import os
import pathlib



package_path = pathlib.Path(__file__).parent
font_path = package_path.joinpath('assets/fonts')

def addFonts():
    for font in os.listdir(font_path):
        font_id=QFontDatabase.addApplicationFont(f"{font_path}\\{font}")
    return True

