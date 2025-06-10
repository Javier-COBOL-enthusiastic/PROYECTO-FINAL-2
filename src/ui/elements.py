from tkinter import *
from tkinter import ttk
from tkinter import Canvas


#         self.vars = []
#         self.widgets = []
#         self.text = []

#         color = root.cget("background")

#         for name, type in self.data.items():
#             self.vars.append(StringVar())
#             match type:
#                 case "ENTRY":
#                     wid = Entry(
#                         self.root,
#                         textvariable=self.vars[-1],
#                         background=color,
#                         font=self.font,
#                     )
#                 case "OPTIONMENU":
#                     wid = OptionMenu(self.root, variable=self.vars[-1], value="")
#                     wid.configure(font=self.font)
#                     self.vars[-1].set("(...)")
#             texto = Label(self.root, text=name, background=color, font=self.font)
#             self.widgets.append(wid)
#             self.text.append(texto)

#     def show(self):
#         for x in range(len(self.widgets)):
#             self.text[x].grid(column=0, row=self.row_pad)
#             if type(self.widgets[x]) == tuple:
#                 self.widgets[x][0].grid(column=1, row=self.row_pad)
#             else:
#                 self.widgets[x].grid(column=1, row=self.row_pad)
#             self.row_pad += 1

#     def hide(self):
#         for x in range(len(self.widgets)):
#             self.text[x].grid_remove()
#             if type(self.widgets[x]) == tuple:
#                 self.widgets[x][0].grid_remove()
#             else:
#                 self.widgets[x].grid_remove()
#             self.row_pad -= 1

#     def load_option_menu(self, name, data):
#         n = 0
#         for x in self.data.keys():
#             if x == name and self.data[x] == "OPTIONMENU":
#                 self.vars[n].set("(...)")
#                 self.widgets[n][0]["menu"].delete(0, "end")
#                 for y in data:
#                     self.widgets[n][0]["menu"].add_command(
#                         label=y, command=lambda v=y: self.vars[n].set(v)
#                     )
#                 break
#             n += 1

#     def clear(self):
#         for var in self.vars:
#             var.set("")

#     def get(self) -> list:
#         n = []
#         for x in self.vars:
#             n.append(x.get())

#         return n

#     def get_current_row_pad(self):
#         return self.row_pad


# class GUITable:
#     def __handle_click__(self, event):
#         if self.table.identify_region(event.x, event.y) == "separator":
#             return "break"

#     def __init__(self, root, font, keys: tuple):
#         self.root = root
#         self.keys = keys
#         self.font = font

#         self.table = ttk.Treeview(
#             self.root, selectmode="none", columns=self.keys[0], show="headings"
#         )
#         self.table.configure(selectmode="browse")
#         self.table.bind("<Button-1>", self.__handle_click__)

#         for c in range(len(self.keys[0])):
#             self.table.heading(self.keys[0][c], text=self.keys[1][c], anchor="center")
#             self.table.column(self.keys[0][c], anchor="center", stretch=False)

#         self.shown = False

#     def insert_item(self, *info):
#         self.table.insert(parent="", index="end", values=info)

#     def configure_width_columns(self, *config):
#         for c in range(len(self.keys[0])):
#             self.table.column(self.keys[0][c], width=config[c])

#     def show(self):
#         if not self.shown:
#             self.shown = True
#             self.table.pack(anchor="s", expand=False)

#     def hide(self):
#         if self.shown:
#             self.table.pack_forget()

#     def add_elements(self, *elements):
#         for elem in elements:
#             pass


# class GUITableCustom:
#     def __init__(self, root, font, **keys_type):
#         self.root = root
#         self.font = font

#         self.bg = "white"
#         self.table = Frame(
#             self.root, bg=self.bg, bd=1, relief="solid", highlightcolor="gray"
#         )

#         self.keys_type = keys_type

#         self.widgets = []
#         n = 0
#         for key, type in self.keys_type.items():
#             sep = ttk.Separator(self.table, orient="vertical")

#             match type:
#                 case "LABEL":
#                     wid = Label(
#                         self.table,
#                         text=key,
#                         bg=self.bg,
#                         font=self.font,
#                         justify="center",
#                     )
#                 case "BUTTON":
#                     wid = Button(
#                         self.table,
#                         text=key,
#                         bg=self.bg,
#                         relief="sunken",
#                         font=self.font,
#                     )

#             wid.grid(column=n, row=0)
#             sep.grid(padx=10, column=n + 1, row=0, sticky="NSEW")
#             n += 2
#             self.widgets.append(wid)
#             self.widgets.append(sep)

#         self.widgets[-1].grid_remove()
#         self.widgets.pop()
#         self.shown = False

#     def insert_elements(self, *elements):
#         for c in range(len(elements)):
#             if self.widgets[c].winfo_class() != "Button":
#                 n = self.widgets[c].cget("text") + elements[c]
#                 self.widgets[c].configure(text=n)
#             else:
#                 pass

#     def insert_elemnt(self, key, element):
#         pass

#     def show(self):
#         if not self.shown:
#             self.shown = True
#             self.table.pack(anchor="s", expand=False)

#     def hide(self):
#         if self.shown:
#             self.table.pack_forget()


class MenuButton(Button):
    def __init__(self, master, text, command=None, font=None, **kwargs):
        super().__init__(
            master,
            text=text,
            font=font if font else ("Nirmala UI", 12),
            relief="groove",
            bg="#688CCA",
            fg="white",
            activebackground="#5A7BB8",
            activeforeground="white",
            cursor="hand2",
            command=command,
            **kwargs,
        )

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self["background"] = "#5A7BB8"

    def on_leave(self, e):
        self["background"] = "#688CCA"


class RoundedButton(Canvas):
    def __init__(
        self,
        parent,
        text,
        width=180,
        height=60,
        radius=18,
        bg="#9FACE8",
        fg="white",
        font=None,
        hover_bg="#688CCA",
        command=None,
        **kwargs,
    ):
        super().__init__(
            parent,
            width=width,
            height=height,
            bg=parent["bg"],
            highlightthickness=0,
            **kwargs,
        )
        self.radius = radius
        self.bg = bg
        self.fg = fg
        self.hover_bg = hover_bg
        self.command = command
        self.font = font
        self.btn_id = self._draw_rounded_rect(
            5, 5, width - 5, height - 5, radius, fill=bg, outline=""
        )
        self.text_id = self.create_text(
            width // 2, height // 2, text=text, fill=fg, font=font
        )
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.tag_bind(self.btn_id, "<Enter>", self._on_enter)
        self.tag_bind(self.btn_id, "<Leave>", self._on_leave)
        self.tag_bind(self.text_id, "<Enter>", self._on_enter)
        self.tag_bind(self.text_id, "<Leave>", self._on_leave)
        self.bind("<Button-1>", self._on_click)
        self.tag_bind(self.btn_id, "<Button-1>", self._on_click)
        self.tag_bind(self.text_id, "<Button-1>", self._on_click)

    def _draw_rounded_rect(self, x1, y1, x2, y2, r, **kwargs):
        points = [
            x1 + r,
            y1,
            x2 - r,
            y1,
            x2,
            y1,
            x2,
            y1 + r,
            x2,
            y2 - r,
            x2,
            y2,
            x2 - r,
            y2,
            x1 + r,
            y2,
            x1,
            y2,
            x1,
            y2 - r,
            x1,
            y1 + r,
            x1,
            y1,
        ]
        return self.create_polygon(points, smooth=True, **kwargs)

    def _on_enter(self, e):
        self._animate_color(self.bg, self.hover_bg)

    def _on_leave(self, e):
        self._animate_color(self.itemcget(self.btn_id, "fill"), self.bg)

    def _on_click(self, e):
        if self.command:
            self.command()

    def _animate_color(self, from_color, to_color, steps=8, step=0):
        def hex_to_rgb(h):
            if h.startswith("#"):
                return tuple(int(h[i : i + 2], 16) for i in (1, 3, 5))
            # Si es un nombre de color, conviértelo usando winfo_rgb
            try:
                r, g, b = self.winfo_rgb(h)
                return (r // 256, g // 256, b // 256)
            except Exception:
                return (255, 255, 255)  # fallback blanco

        def rgb_to_hex(rgb):
            return "#%02x%02x%02x" % rgb

        start = hex_to_rgb(from_color)
        end = hex_to_rgb(to_color)
        new_rgb = tuple(
            int(start[i] + (end[i] - start[i]) * (step / steps)) for i in range(3)
        )
        self.itemconfig(self.btn_id, fill=rgb_to_hex(new_rgb))
        if step < steps:
            self.after(
                15,
                lambda: self._animate_color(
                    rgb_to_hex(new_rgb), to_color, steps, step + 1
                ),
            )


class TableActionButton(Canvas):
    def __init__(self, parent, icon_path, command=None, size=32, **kwargs):
        super().__init__(
            parent,
            width=size,
            height=size,
            bg=parent["bg"],
            highlightthickness=0,
            bd=0,
            **kwargs,
        )
        self.icon = PhotoImage(file=icon_path)
        self.icon_id = self.create_image(size // 2, size // 2, image=self.icon)
        self.command = command
        self.size = size
        self.bg_normal = parent["bg"]
        self.bg_hover = "#e0e0e0"
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<Button-1>", self._on_click)
        self.tag_bind(self.icon_id, "<Enter>", self._on_enter)
        self.tag_bind(self.icon_id, "<Leave>", self._on_leave)
        self.tag_bind(self.icon_id, "<Button-1>", self._on_click)

    def _on_enter(self, e):
        self.configure(bg=self.bg_hover)

    def _on_leave(self, e):
        self.configure(bg=self.bg_normal)

    def _on_click(self, e):
        if self.command:
            self.command()


class TableView(Frame):
    def __init__(
        self,
        parent,
        headers,
        data,
        actions=None,
        title=None,
        subtitle=None,
        count=None,
        col_widths=None,
        action_text="Ver",
        **kwargs,
    ):
        super().__init__(parent, bg="#F6F6F6", **kwargs)
        self.headers = headers
        self.data = data
        self.actions = actions or []
        self.title = title
        self.subtitle = subtitle
        self.count = count
        self.col_widths = col_widths or [140] * len(headers)
        self.action_text = action_text
        self._build_table()

    def _build_table(self):
        card = Frame(self, bg="white", bd=0, highlightthickness=0)
        card.pack(padx=0, pady=0, fill="both", expand=True)

        if self.title or self.count is not None:
            title_row = Frame(card, bg="white")
            title_row.pack(fill="x", padx=24, pady=(18, 0))
            if self.title:
                Label(
                    title_row,
                    text=self.title,
                    font=("Consolas", 16, "bold"),
                    bg="white",
                    anchor="w",
                ).pack(side="left")

        header_row = Frame(card, bg="white")
        header_row.pack(fill="x", padx=0, pady=(6, 0))
        for i, h in enumerate(self.headers):
            Label(
                header_row,
                text=h,
                font=("Consolas", 12, "bold"),
                bg="white",
                fg="#222",
                anchor="w",
                width=int(self.col_widths[i] // 10),
                pady=12,
                padx=0,
            ).grid(
                row=0, column=i, sticky="nsew", padx=(24 if i == 0 else 8, 0), pady=0
            )

        table_canvas = Canvas(card, bg="white", highlightthickness=0, height=320)
        table_canvas.pack(fill="both", expand=True, side="left")

        scrollbar = Scrollbar(card, orient="vertical", command=table_canvas.yview)
        scrollbar.pack(side="right", fill="y")

        table_canvas.configure(yscrollcommand=scrollbar.set)

        rows_frame = Frame(table_canvas, bg="white")
        window_id = table_canvas.create_window((0, 0), window=rows_frame, anchor="nw")

        def on_configure(event):
            table_canvas.configure(scrollregion=table_canvas.bbox("all"))
            table_canvas.itemconfig(window_id, width=table_canvas.winfo_width())

        rows_frame.bind("<Configure>", on_configure)
        table_canvas.bind("<Configure>", on_configure)

        # Habilitar scroll con mouse
        def _on_mousewheel(event):
            table_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        table_canvas.bind_all("<MouseWheel>", _on_mousewheel)

        for r, row in enumerate(self.data):
            row_bg = "#EEEEEE" if r % 2 == 1 else "white"
            row_frame = Frame(rows_frame, bg=row_bg)
            row_frame.pack(fill="x", padx=0, pady=0)
            for c, value in enumerate(row):
                Label(
                    row_frame,
                    text=value,
                    font=("Consolas", 11),
                    bg=row_bg,
                    fg="#444",
                    anchor="center",
                    width=int(self.col_widths[c] // 10),
                    pady=14,
                    padx=0,
                ).grid(
                    row=0,
                    column=c,
                    sticky="nsew",
                    padx=(24 if c == 0 else 8, 0),
                    pady=0,
                )
            if self.actions:
                action_frame = Frame(row_frame, bg=row_bg)
                action_frame.grid(row=0, column=len(row), sticky="e", padx=(8, 24))
                for action in self.actions:
                    btn = action(row, action_frame, self.action_text)
                    btn.pack(side="left", padx=4)
