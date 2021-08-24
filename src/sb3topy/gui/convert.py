"""
convert.py

Contains the Convert tab of the gui
"""

import tkinter as tk
from tkinter import filedialog, ttk


class ConvertFrame(ttk.Frame):
    """
    ConvertFrame

    project_path
    folder_path

    zip_path
    create_zip, overwrite_zip

    exe_path
    create_exe, overwrite_exe
    """

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.app = parent

        self.project_path = tk.StringVar(self.app, name="PROJECT_PATH")
        project_label = ttk.Label(self, text="Input Project:")
        project_box = ttk.Entry(self, textvariable=self.project_path)
        project_button = ttk.Button(
            self, text="Browse...", command=self.browse_project)

        self.output_path = tk.StringVar(self.app, name="OUTPUT_PATH")
        folder_label = ttk.Label(self, text="Output Folder:")
        folder_box = ttk.Entry(self, textvariable=self.output_path)
        folder_button = ttk.Button(
            self, text="Browse...", command=self.browse_folder)
        # folder_button2 = ttk.Button(
        #     self, text="Create Now", command=self.delete_assets)

        convert_button = ttk.Button(
            self, text="Convert Now", command=self.convert)
        # seperator = ttk.Separator(self, orient=tk.HORIZONTAL)

        # self.zip_path = tk.StringVar()
        # self.zip_create = tk.BooleanVar()
        # self.zip_overwrite = tk.BooleanVar()
        # zip_label = ttk.Label(self, text="Output zip:")
        # zip_box = ttk.Entry(self, textvariable=self.zip_path)
        # zip_button = ttk.Button(
        #     self, text="Browse...", command=self.browse_zip)
        # zip_check1 = ttk.Checkbutton(
        #     self, text="Create zip", variable=self.zip_create)
        # zip_check2 = ttk.Checkbutton(
        #     self, text="Allow Overwrite", variable=self.zip_overwrite)
        # zip_button2 = ttk.Button(
        #     self, text="Export Now", command=self.create_zip)

        # self.exe_path = tk.StringVar()
        # self.exe_create = tk.BooleanVar()
        # self.exe_overwrite = tk.BooleanVar()
        # exe_label = ttk.Label(self, text="Output exe:")
        # exe_box = ttk.Entry(self, textvariable=self.exe_path)
        # exe_button = ttk.Button(
        #     self, text="Browse...", command=self.browse_exe)
        # exe_check1 = ttk.Checkbutton(
        #     self, text="Create exe", variable=self.exe_create)
        # exe_check2 = ttk.Checkbutton(
        #     self, text="Allow Overwrite", variable=self.exe_overwrite)
        # exe_button2 = ttk.Button(
        #     self, text="Export Now", command=self.create_exe)

        # Grid everything
        project_label.grid(column=0, row=0, sticky="W")
        project_box.grid(column=0, row=1, columnspan=2, sticky="WE")
        project_button.grid(column=2, row=1, sticky="WE", padx=(5, 0))

        folder_label.grid(column=0, row=2, sticky="W", pady=(10, 0))
        folder_box.grid(column=0, row=3, columnspan=2, sticky="WE")
        folder_button.grid(column=2, row=3, sticky="WE", padx=(5, 0))

        convert_button.grid(column=2, row=4, columnspan=1,
                            sticky="WE", pady=(0, 5), padx=(5, 0))
        # seperator.grid(column=0, row=5, columnspan=3, sticky="WE")

        # zip_label.grid(column=0, row=6, sticky="W")
        # zip_box.grid(column=0, row=7, columnspan=2, sticky="WE")
        # zip_button.grid(column=2, row=7, sticky="WE", padx=(5, 0))
        # zip_check1.grid(column=0, row=8, sticky="W")
        # zip_check2.grid(column=1, row=8, sticky="W")
        # zip_button2.grid(column=2, row=8, sticky="WE", padx=(5, 0))

        # exe_label.grid(column=0, row=9, sticky="W", pady=(10, 0))
        # exe_box.grid(column=0, row=10, columnspan=2, sticky="WE")
        # exe_button.grid(column=2, row=10, sticky="WE", padx=(5, 0))
        # exe_check1.grid(column=0, row=11, sticky="W")
        # exe_check2.grid(column=1, row=11, sticky="W")
        # exe_button2.grid(column=2, row=11, sticky="WE", padx=(5, 0))

        self.columnconfigure(1, weight=1)

    def browse_project(self):
        """Show a dialog to select the project file"""
        path = filedialog.askopenfilename(
            filetypes=[("Project Files", "*.sb3;*.zip"),
                       ("All Files", "*.*")])
        if path:
            self.app.setvar("PROJECT_PATH", path)

    def browse_folder(self):
        """Show a dialog to select the output folder"""
        output_path = filedialog.askdirectory()
        if output_path:
            self.output_path.set(output_path)

    def convert(self):
        """Run the converter"""
        self.app.setvar("AUTORUN", True)
        self.app.setvar("PROJECT_URL", "")
        self.app.setvar("JSON_SHA", False)
        self.app.write_config()
        self.app.run_main()

    # def browse_zip(self):
    #     """Show a dialog to select the output zip path"""
    #     path = filedialog.asksaveasfilename(
    #         defaultextension=".zip",
    #         filetypes=[("ZIP Files", "*.zip"),
    #                    ("All Files", "*.*")])
    #     if path:
    #         self.zip_path.set(path)

    # def browse_exe(self):
    #     """Show a dialog to select the output exe path"""
    #     path = filedialog.asksaveasfilename(
    #         defaultextension=".exe",
    #         filetypes=[("EXE Files", "*.exe"),
    #                    ("All Files", "*.*")])
    #     if path:
    #         self.exe_path.set(path)
