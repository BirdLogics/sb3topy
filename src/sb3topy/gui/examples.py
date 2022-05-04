"""
example.py

Contains the Examples tab of the GUI

TODO Avoid auto download when starting GUI?
Causes issues without internet
"""

import json
import logging
import tkinter as tk
import webbrowser
from os import path
from tkinter import ttk

try:
    import requests
except ImportError:
    requests = None

from .. import config

logger = logging.getLogger(__name__)


class Example:
    """
    Represents an example project
    """

    def __init__(self, example):
        self.name = example['name']
        self.download_link = "https://scratch.mit.edu/projects/" + \
            str(example['id']) + "/"

        self.thumb_link = "https://cdn2.scratch.mit.edu/get_image/project/" + \
            str(example['id']) + "_480x360.png"
        self.thumb_image = None

        self.viewer = example['description'].partition('\n')[0]
        self.view_link = example['link']

        self.username = '@' + example['author']
        self.user_link = "https://scratch.mit.edu/users/" + \
            example['author'] + "/"

        self.description = example['description'].partition('\n')[2]
        self.sha256 = example['sha256']
        self.config = example['config']

    def get_image(self):
        """Gets a PhotoImage of the example thumbnail"""
        if requests is None:
            logger.warning(
                "Failed to load thumbnail; requests not installed.")
            return None

        if self.thumb_image is None:
            resp = requests.get(self.thumb_link)
            self.thumb_image = tk.PhotoImage(data=resp.content)
        return self.thumb_image


def read_examples():
    """Reads and returns the examples.json data"""
    # Get the path to the examples file
    if config.EXAMPLES_PATH is None:
        examples_path = path.join(path.dirname(__file__), "examples.json")
    else:
        examples_path = config.EXAMPLES_PATH

    # Attempt to read the json file
    try:
        with open(examples_path, 'r') as examples_file:
            return json.load(examples_file)
    except OSError:
        logger.exception(
            "Failed to load examples json '%s'", examples_path)
        return []
    except json.JSONDecodeError:
        logger.exception("Failed to parse examples json '%s'", examples_path)
        return []


class ExamplesFrame(ttk.Frame):
    """
    Handles the Examples tab

    When the examples tab is switched to, if the current download link
    is blank or equal to that of the last download link, the details of
    the current example will be loaded. Otherwise, all example tabs
    will be deselected.

    Notable Attributes:
        last_download_link:
    """

    def __init__(self, app, **kwargs):
        super().__init__(app, **kwargs)
        self.app = app

        # Create styles
        style = ttk.Style(self)
        style.map(
            "Hyperlink.TLabel",
            foreground=[('', "#0000EE")],
            font=[('active', 'TkDefaultFont 9 underline'),
                  ('!active', 'TkDefaultFont 9')]

        )

        # Create components
        self.examples_list = tk.StringVar()
        self.listbox = tk.Listbox(
            self, height=25, listvariable=self.examples_list)

        project_frame = ttk.Frame(self, relief='groove',
                                  borderwidth=1, padding="0 0 2 0")

        self.thumbnail = ttk.Label(project_frame)

        self.download_link_raw = ""
        self.download_link = tk.StringVar(self.app, name="PROJECT_URL")

        download_frame = ttk.Frame(project_frame)
        download_box = ttk.Entry(
            download_frame, textvariable=self.download_link)
        download_button = ttk.Button(
            download_frame, text="Download",
            command=self.download_project)
        download_button2 = ttk.Button(
            download_frame, text="Download & Run",
            command=self.download_run_project)

        self.project_viewer = tk.StringVar()
        self.project_link = tk.StringVar()
        self.username = tk.StringVar()
        self.userlink = tk.StringVar()
        self.project_desc = tk.StringVar()
        self.json_sha = tk.Variable(self.app, name="JSON_SHA")

        info_frame = ttk.Frame(project_frame)
        user_label = ttk.Label(info_frame, text="Made by")
        user_link = Hyperlink(
            info_frame, self.userlink, textvariable=self.username)
        project_link = Hyperlink(
            info_frame, self.project_link, textvariable=self.project_viewer)
        description = ttk.Label(
            info_frame, textvariable=self.project_desc)
        copyright_label = Hyperlink(
            info_frame, tk.StringVar(
                value="https://creativecommons.org/licenses/by-sa/2.0/"),
            text="CC BY-SA-2.0")

        # Grid everything
        self.listbox.grid(column=0, row=0, sticky='NSW', pady=5, padx=(0, 2))

        project_frame.grid(column=1, row=0, sticky='NSEW', pady=5)

        self.thumbnail.grid(column=0, row=0, sticky='NS')

        download_frame.grid(column=0, row=1, sticky='NEW')
        download_box.grid(column=0, row=0, sticky='WE', padx=2)
        download_button.grid(column=1, row=0, sticky='NWE', padx=2)
        download_button2.grid(
            column=2, row=0, sticky='NWE', padx=2, pady=(0, 2))
        download_frame.columnconfigure(0, weight=1)

        info_frame.grid(column=0, row=2, sticky='NEW')
        user_label.grid(column=0, row=1, sticky='NW')
        user_link.grid(column=1, row=1, sticky='NW')
        copyright_label.grid(column=2, row=1, sticky='NE')
        info_frame.columnconfigure(1, weight=1)

        project_link.grid(column=0, row=2, columnspan=3, sticky='NW')

        description.grid(column=0, row=3, columnspan=3, sticky='NW')

        project_frame.columnconfigure(0, minsize=480*app.scale)
        project_frame.rowconfigure(0, minsize=360*app.scale)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Bind events
        self.listbox.bind("<<ListboxSelect>>", self.listbox_changed)
        self.download_link.trace_add('write', self.download_changed)

        # Load examples data
        self.examples = [Example(example) for example in read_examples()]
        self.examples_list.set([example.name for example in self.examples])
        self.example = self.examples[0] if self.examples else None
        self.listbox.select_set([0])

    def download_changed(self, *_):
        """Called when the download link is changed"""
        if self.download_link.get() != self.example.download_link:
            self.thumbnail['image'] = ""
            self.json_sha.set(False)  # TODO New bool config for json_sha

    def listbox_changed(self, _):
        """Called when the listbox selection is changed by the user"""
        # Avoid weird events when on another tab
        selected = self.listbox.curselection()
        if selected and self.app.mode.get() == 'examples':
            self.example = self.examples[selected[0]]
            self.download_link.set("")
            self.update_project()

    def update_project(self):
        """Updates the project info"""
        dw_link = self.download_link.get()
        example = self.example

        # Don't update the project if the dw link is modified
        if dw_link and dw_link != example.download_link:
            self.thumbnail['image'] = ""
            self.listbox.selection_clear(0, "end")
            return

        self.thumbnail['image'] = example.get_image()

        self.username.set(example.username)
        self.userlink.set(example.user_link)
        self.project_desc.set(example.description)

        self.project_viewer.set(example.viewer)
        self.project_link.set(example.view_link)

        self.download_link.set(example.download_link)

        self.json_sha.set(example.sha256)

    def download_project(self):
        """Downloads and converts the project"""
        self.app.setvar("AUTORUN", False)
        self.app.write_config()
        self.app.run_main()

    def download_run_project(self):
        """Downloads, converts, and runs the project"""
        self.app.setvar("AUTORUN", True)
        self.app.write_config()
        self.app.run_main()

    def switch_to(self):
        """Called when this tab is shown"""
        self.update_project()
        if self.download_link.get() != self.example.download_link:
            self.listbox.selection_clear(0, "end")


class Hyperlink(ttk.Label):
    """A label which goes to a webpage when clicked"""

    def __init__(self, parent, url, **kwargs):
        super().__init__(parent, style="Hyperlink.TLabel", **kwargs)
        self.url = url

        self.bind("<Enter>", self.mouse_enter)
        self.bind("<Leave>", self.mouse_leave)
        self.bind("<Button-1>", self.mouse_click)

    def mouse_enter(self, _):
        """Called when the mouse hovers"""
        self.state(["active"])

    def mouse_leave(self, _):
        """Called when the mouse stops hovering"""
        self.state(["!active"])

    def mouse_click(self, _):
        """Called when the mouse clicks"""
        webbrowser.open(self.url.get())
