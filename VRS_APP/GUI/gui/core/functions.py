# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os
import sys


# APP FUNCTIONS
# ///////////////////////////////////////////////////////////////
def set_image(image_name):

    app_path = os.path.abspath(os.getcwd())
    folder = "GUI/gui/images/images/"
    path = os.path.join(app_path, folder)
    image = os.path.normpath(os.path.join(path, image_name))
    return image


def set_svg_image(icon_name: str):

    if getattr(sys, 'frozen', False):
        app_path = os.path.dirname(sys.executable)
        folder = f"GUI/gui/core/images/svg_images/"

        # folder = "images/svg_images/"

    elif __file__:
        app_path = os.path.dirname(__file__)
        # folder = f"GUI/gui/core/images/svg_images/"
        folder = "images/svg_images/"


    # app_path = os.path.abspath(os.getcwd())
    # folder = "GUI/gui/images/svg_images/"
    path = os.path.join(app_path, folder)
    icon = os.path.normpath(os.path.join(path, icon_name))
    return icon


def set_svg_icon(icon_name: str):
    # app_path = os.path.abspath(os.getcwd())
    # folder = "GUI/gui/images/svg_icons/"
    if getattr(sys, 'frozen', False):
        app_path = os.path.dirname(sys.executable)
        folder = f"GUI/gui/core/images/svg_icons/"

        # folder = "images/svg_icons/"

    elif __file__:
        app_path = os.path.dirname(__file__)
        folder = "images/svg_icons/"
    path = os.path.join(app_path, folder)
    icon = os.path.normpath(os.path.join(path, icon_name))
    return icon


class Functions:

    # SET SVG ICON
    # ///////////////////////////////////////////////////////////////
    pass

    # SET SVG IMAGE
    # ///////////////////////////////////////////////////////////////

    # SET IMAGE
    # ///////////////////////////////////////////////////////////////
