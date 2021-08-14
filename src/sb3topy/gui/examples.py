"""
example.py

Contains the Examples tab of the GUI

TODO Avoid auto download when starting GUI?
Causes issues without internet
"""

import json
import tkinter as tk
import webbrowser
from os import path
from tkinter import ttk

import requests

from .. import config


class ExamplesFrame(ttk.Frame):
    """Handles the Examples tab"""

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.app = parent

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

        self.thumbnail = Thumbnail(project_frame)

        self.download_link = tk.StringVar()

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

        info_frame = ttk.Frame(project_frame)
        user_label = ttk.Label(info_frame, text="Made by")
        user_link = Hyperlink(
            info_frame, self.userlink, textvariable=self.username)
        project_link = Hyperlink(
            info_frame, self.project_link, textvariable=self.project_viewer)
        description = ttk.Label(
            info_frame, textvariable=self.project_desc)

        # instr_label = ttk.LabelFrame(right, text="Instructions")
        # instr_box = tk.Text(instr_label, width=57)

        # Grid everything
        self.listbox.grid(column=0, row=0, sticky='NSW', pady=5, padx=(0, 2))

        project_frame.grid(column=1, row=0, sticky='NSEW', pady=5)

        self.thumbnail.grid(column=0, row=0, sticky='NW')

        download_frame.grid(column=0, row=1, sticky='NEW')
        download_box.grid(column=0, row=0, sticky='WE', padx=2)
        download_button.grid(column=1, row=0, sticky='NWE', padx=2)
        download_button2.grid(
            column=2, row=0, sticky='NWE', padx=2, pady=(0, 2))
        download_frame.columnconfigure(0, weight=1)

        info_frame.grid(column=0, row=2, sticky='NEW')
        user_label.grid(column=0, row=1, sticky='NW')
        user_link.grid(column=1, row=1, sticky='NW')
        info_frame.columnconfigure(1, weight=1)

        project_link.grid(column=0, row=2, columnspan=2, sticky='NW')

        description.grid(column=0, row=3, columnspan=2, sticky='NW')

        # instr_label.grid(column=0, row=2, sticky='NSEW', padx=5)
        # instr_box.grid(sticky='NSEW')

        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=1)

        # Bind events
        self.listbox.bind("<<ListboxSelect>>", self.update_project)

        # Load examples data
        self.examples = {}
        self.read_examples()

    def read_examples(self):
        """Reads examples from a json file"""
        # Get the path to the examples file
        if config.EXAMPLES_PATH is None:
            examples_path = path.join(path.dirname(__file__), "examples.json")
        else:
            examples_path = config.EXAMPLES_PATH

        # Read the json file, if it exists
        if path.isfile(examples_path):
            with open(examples_path, 'r') as examples_file:
                self.examples = json.load(examples_file)
        else:
            self.examples = []

        # Update the listbox items
        self.examples_list.set([example['name'] for example in self.examples])

    def update_project(self, _=None):
        """Updates the project info"""
        # Can happen when not on examples tab for some reason
        if not self.listbox.curselection():
            return

        example = self.examples[self.listbox.curselection()[0]]

        self.thumbnail.set_image(example['id'])

        self.username.set("@" + example['author'])
        self.userlink.set(
            f"https://scratch.mit.edu/users/{example['author']}/")

        self.project_link.set(example['link'])
        self.project_viewer.set(example['description'].split('\n')[0])

        self.project_desc.set(
            '\n'.join(example['description'].split('\n')[1:]))

        self.download_link.set(f"https://scratch.mit.edu/{example['id']}/")

        self.app.setvar("JSON_SHA", example.get("sha256", True))

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
        self.listbox.selection_set(0)
        self.update_project()


class Thumbnail(tk.Label):
    """Handles displaying a project thumbnail"""

    def __init__(self, parent, **kwargs):
        super().__init__(parent, width=480, **kwargs)
        self.image = None

    def set_image(self, project_id):
        """Sets the image to a project's thumbnail"""
        resp = requests.get(
            f"https://cdn2.scratch.mit.edu/get_image/project/{project_id}_480x360.png")
        self.image = tk.PhotoImage(data=resp.content)
        self['image'] = self.image


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
