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

# windll.shcore.SetProcessDpiAwareness(True)


def run_app():
    """Runs the GUI App"""
    App().mainloop()


class App(tk.Tk):
    """Main App class"""

    def __init__(self):
        tk.Tk.__init__(self)
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

        self.mode.set("convert")

        self.geometry("720x480")
        self.resizable(0, 0)

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
