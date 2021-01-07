"""

"""

# pylint: disable=wildcard-import, unused-wildcard-import

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


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

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="5 0 5 5")

        self.project_path = tk.StringVar()
        project_label = ttk.Label(self, text="Input Project:")
        project_box = ttk.Entry(self, textvariable=self.project_path)
        project_button = ttk.Button(
            self, text="Browse...", command=self.browse_project)

        self.folder_path = tk.StringVar()
        folder_label = ttk.Label(self, text="Output Folder:")
        folder_box = ttk.Entry(self, textvariable=self.folder_path)
        folder_button = ttk.Button(
            self, text="Browse...", command=self.browse_folder)
        # folder_button2 = ttk.Button(
        #     self, text="Create Now", command=self.delete_assets)

        convert_button = ttk.Button(
            self, text="Convert Now", command=self.convert)
        seperator = ttk.Separator(self, orient=tk.HORIZONTAL)

        self.zip_path = tk.StringVar()
        self.zip_create = tk.BooleanVar()
        self.zip_overwrite = tk.BooleanVar()
        zip_label = ttk.Label(self, text="Output zip:")
        zip_box = ttk.Entry(self, textvariable=self.zip_path)
        zip_button = ttk.Button(
            self, text="Browse...", command=self.browse_zip)
        zip_check1 = ttk.Checkbutton(
            self, text="Create zip", variable=self.zip_create)
        zip_check2 = ttk.Checkbutton(
            self, text="Allow Overwrite", variable=self.zip_overwrite)
        zip_button2 = ttk.Button(
            self, text="Export Now", command=self.create_zip)

        self.exe_path = tk.StringVar()
        self.exe_create = tk.BooleanVar()
        self.exe_overwrite = tk.BooleanVar()
        exe_label = ttk.Label(self, text="Output exe:")
        exe_box = ttk.Entry(self, textvariable=self.exe_path)
        exe_button = ttk.Button(
            self, text="Browse...", command=self.browse_exe)
        exe_check1 = ttk.Checkbutton(
            self, text="Create exe", variable=self.exe_create)
        exe_check2 = ttk.Checkbutton(
            self, text="Allow Overwrite", variable=self.exe_overwrite)
        exe_button2 = ttk.Button(
            self, text="Export Now", command=self.create_exe)

        # Grid everything
        project_label.grid(column=0, row=0, sticky="W")
        project_box.grid(column=0, row=1, columnspan=2, sticky="WE")
        project_button.grid(column=2, row=1, sticky="WE", padx=(5, 0))

        folder_label.grid(column=0, row=2, sticky="W", pady=(10, 0))
        folder_box.grid(column=0, row=3, columnspan=2, sticky="WE")
        folder_button.grid(column=2, row=3, sticky="WE", padx=(5, 0))

        convert_button.grid(column=0, row=4, columnspan=3, sticky="WE", pady=5)
        seperator.grid(column=0, row=5, columnspan=3, sticky="WE")

        zip_label.grid(column=0, row=6, sticky="W")
        zip_box.grid(column=0, row=7, columnspan=2, sticky="WE")
        zip_button.grid(column=2, row=7, sticky="WE", padx=(5, 0))
        zip_check1.grid(column=0, row=8, sticky="W")
        zip_check2.grid(column=1, row=8, sticky="W")
        zip_button2.grid(column=2, row=8, sticky="WE", padx=(5, 0))

        exe_label.grid(column=0, row=9, sticky="W", pady=(10, 0))
        exe_box.grid(column=0, row=10, columnspan=2, sticky="WE")
        exe_button.grid(column=2, row=10, sticky="WE", padx=(5, 0))
        exe_check1.grid(column=0, row=11, sticky="W")
        exe_check2.grid(column=1, row=11, sticky="W")
        exe_button2.grid(column=2, row=11, sticky="WE", padx=(5, 0))

        self.columnconfigure(1, weight=1)

    def browse_project(self):
        """Show a dialog to select the project file"""
        path = filedialog.askopenfilename(
            filetypes=[("Project Files", "*.sb3;*.zip"),
                       ("All Files", "*.*")])
        if path:
            self.project_path.set(path)

    def browse_folder(self):
        """Show a dialog to select the output folder"""
        self.project_path.set(filedialog.askdirectory())

    def convert(self):
        """Run the converter"""

    def delete_assets(self):
        """Clear the contents of the assets folder"""

    def browse_zip(self):
        """Show a dialog to select the output zip path"""
        path = filedialog.asksaveasfilename(
            defaultextension=".zip",
            filetypes=[("ZIP Files", "*.zip"),
                       ("All Files", "*.*")])
        if path:
            self.zip_path.set(path)

    def create_zip(self):
        """Create a zip from the last conversion"""

    def browse_exe(self):
        """Show a dialog to select the output exe path"""
        path = filedialog.asksaveasfilename(
            defaultextension=".exe",
            filetypes=[("EXE Files", "*.exe"),
                       ("All Files", "*.*")])
        if path:
            self.exe_path.set(path)

    def create_exe(self):
        """Create a zip from the last conversion"""


class OutputFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="5 0 5 5")

        text = tk.scrolledtext.ScrolledText(self, width=10, height=10)

        text.grid(column=0, row=0, columnspan=3, sticky="NSWE")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


class SettingsFrame(ttk.Frame):
    pass


class FlatRadio(ttk.Label):
    """A custom flat radio button"""

    def __init__(self, parent, text, variable, **args):
        ttk.Label.__init__(
            self, parent, text=text,
            style="FlatRadio.TLabel", **args)
        self.value = text.lower()
        self.variable = variable

        variable.trace_add("write", self.cb_variable)
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
        self.variable.set(self.value)

    def cb_variable(self, name, index, operation):
        """Called when the variable is updated"""
        state = self.variable.get()
        if state == self.value:
            self.state(["selected"])
        else:
            self.state(["!selected"])


class Sidebar(ttk.Frame):
    """Handles the sidebar on the left and frames put in it"""

    def __init__(self, root, variable):
        ttk.Frame.__init__(self, root)

        style = ttk.Style(self)
        style.map(
            "FlatRadio.TLabel",
            background=[('selected', 'lightgrey'),
                        ('active', '#dfdfdf')],
            font=[('', 'TkMenuFont 14')])

        convert_button = FlatRadio(self, "Convert", variable=variable)
        output_button = FlatRadio(self, "Output", variable=variable)
        settings_button = FlatRadio(self, "Settings", variable=variable)

        convert_button.grid(column=0, row=0, sticky="NSEW")
        output_button.grid(column=0, row=1, sticky="NSEW")
        settings_button.grid(column=0, row=2, sticky="NSEW")

        self.columnconfigure(0, weight=1)


class App(tk.Tk):
    """Main App class"""

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("sb3topy")

        self.mode = tk.StringVar(self)
        self.mode.trace_add('write', self.cb_mode)

        sidebar = Sidebar(self, self.mode)
        self.convert = ConvertFrame(self)
        self.output = OutputFrame(self)
        self.settings = SettingsFrame(self)

        sidebar.grid(column=0, row=0, sticky="NSEW")
        self.convert.grid(column=1, row=0, sticky="NSWE")
        self.output.grid(column=1, row=0, sticky="NSWE")
        self.settings.grid(column=1, row=0, sticky="NSWE")

        self.columnconfigure(0, minsize=100)
        self.columnconfigure(1, weight=1)

        self.mode.set("convert")

    def cb_mode(self, *_):
        """Called when the mode switches"""
        self.convert.grid_remove()
        self.output.grid_remove()
        self.settings.grid_remove()

        mode = self.mode.get()
        if mode == "convert":
            self.convert.grid()
        elif mode == "output":
            self.output.grid()
        elif mode == "settings":
            self.settings.grid()


def main():

    app = App()
    app.mainloop()

    # mainframe = ttk.Frame(root, padding="5 5 12 0")
    # mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    # root.grid_columnconfigure(0, weight=1)
    # root.grid_rowconfigure(0, weight=1)

    # mainframe = ttk.Frame(root, padding="3 3 3 3")

    # mainframe.grid(column=0, row=0, sticky="NWES")
    # root.columnconfigure(0, weight=1)
    # root.rowconfigure(0, weight=1)

    # convert_frame = ConvertFrame(root)

    # choices = ["apples", "bannanas", "oranges"]
    # choicesvar = StringVar(value=choices)
    # sidebar = Listbox(mainframe, listvariable=choicesvar)
    # sidebar.grid(column=0, row=0, sticky=(N, S))

    # outbook = ttk.Notebook(mainframe, padding="3 3 3 3")
    # outbook.grid(column=1, row=0, sticky=(N, S, W, E))

    # outframe = ttk.Frame(outbook, padding="3 3 3 3")
    # outbook.add(outframe, text="Output")
    # outframe2 = ttk.Frame(outbook, padding="3 3 3 3")
    # outbook.add(outframe2, text="Settings")

    # logbox = Text(outframe, width=40, height=10)
    # # logbox['state'] = "disabled"
    # logbox.grid(column=1, row=0, sticky=(N, S, W, E))

    # scrollbar = ttk.Scrollbar(outframe, orient=VERTICAL, command=logbox.yview)
    # scrollbar.grid(column=2, row=0, sticky=(N, S))
    # logbox['yscrollcommand'] = scrollbar.set

    # progress = ttk.Progressbar(mainframe, orient=HORIZONTAL, length=200, mode='determinate')
    # progress.grid(column = 1, row=10, sticky=(E, W), padx=5, pady=2)


if __name__ == "__main__":
    main()
