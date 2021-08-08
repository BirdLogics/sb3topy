"""
toolbox.py

Contains miscellaneous custom components used by the gui app
"""

# pylint: disable=too-many-ancestors

from tkinter import ttk


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
        examples_button = FlatRadio(self, "Examples", variable=variable)
        output_button = FlatRadio(self, "Output", variable=variable)
        settings_button = FlatRadio(self, "Settings", variable=variable)

        convert_button.grid(column=0, row=0, sticky="NSEW")
        examples_button.grid(column=0, row=1, sticky="NSEW")
        output_button.grid(column=0, row=2, sticky="NSEW")
        settings_button.grid(column=0, row=3, sticky="NSEW")

        self.columnconfigure(0, weight=1)
