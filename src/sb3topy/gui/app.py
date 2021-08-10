"""
app.py

Contains the gui app
"""

import logging
import multiprocessing
import tkinter as tk
# from ctypes import windll
from tkinter import ttk

from .convert import ConvertFrame
from .examples import ExamplesFrame
from .output import OutputFrame
from .settings import SettingsFrame
from .sidebar import Sidebar
from .. import main, config

# windll.shcore.SetProcessDpiAwareness(True)


def run_app():
    """Runs the GUI App"""
    App().mainloop()


class App(tk.Tk):
    """Main App class"""

    def __init__(self):
        super().__init__()
        self.title("sb3topy")

        self.mode = tk.StringVar(self)
        self.mode.trace_add('write', self.cb_mode)

        sidebar = Sidebar(self, self.mode)
        self.convert = ConvertFrame(self, padding="5 0 5 5")
        self.examples = ExamplesFrame(self, padding="5 0 5 5")
        self.output = OutputFrame(self, padding="5 0 5 5")
        self.settings = SettingsFrame(self, padding="5 0 5 5")

        sidebar.grid(column=0, row=0, sticky="NSEW")
        self.convert.grid(column=1, row=0, sticky="NSWE")
        self.examples.grid(column=1, row=0, sticky="NSEW")
        self.output.grid(column=1, row=0, sticky="NSWE")
        self.settings.grid(column=1, row=0, sticky="NSWE")

        self.columnconfigure(0, minsize=100)
        self.columnconfigure(1, minsize=300, weight=1)
        self.rowconfigure(0, minsize=300, weight=1)

        self.mode.set(config.DEFAULT_GUI_TAB)

        self.geometry("720x480")
        self.resizable(0, 0)

        self.read_config()

    def cb_mode(self, *_):
        """Called when the mode switches"""
        self.convert.grid_remove()
        self.examples.grid_remove()
        self.output.grid_remove()
        self.settings.grid_remove()

        mode = self.mode.get()
        if mode == "convert":
            self.convert.grid()
        elif mode == "examples":
            self.examples.grid()
            self.examples.switch_to()
        elif mode == "output":
            self.output.grid()
        elif mode == "settings":
            self.settings.grid()

    def run_main(self):
        """Runs the converter with the current config"""
        self.save_config()
        main.main()

    def download_project(self, autorun):
        """Downloads the project and converts it"""
        self.save_config()
        config.PROJECT_PATH = None
        config.PROJECT_URL = self.examples.download_link.get()
        config.AUTORUN = autorun

        self.mode.set("output")

        process, queue = main.run_mp()
        self.output.start_watching(process, queue)

    def read_config(self):
        """
        Reads values from config and saves them in components
        """
        self.convert.project_path.set(config.PROJECT_PATH)
        self.convert.folder_path.set(config.OUTPUT_PATH)

    def save_config(self):
        """
        Saves valus from components into config
        """
        config.USE_GUI = False
        config.PROJECT_PATH = self.convert.project_path.get()
        config.OUTPUT_PATH = self.convert.folder_path.get()
