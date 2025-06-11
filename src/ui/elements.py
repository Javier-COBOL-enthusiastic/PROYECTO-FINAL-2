from tkinter import *
from tkinter import ttk
from tkinter import Canvas


def draw_rounded_rect(canvas, x1, y1, x2, y2, r, fill, outline, width=1):
    # Arcos de las esquinas
    canvas.create_arc(
        x1,
        y1,
        x1 + 2 * r,
        y1 + 2 * r,
        start=90,
        extent=90,
        style="pieslice",
        fill=fill,
        outline=outline,
        width=width,
    )
    canvas.create_arc(
        x2 - 2 * r,
        y1,
        x2,
        y1 + 2 * r,
        start=0,
        extent=90,
        style="pieslice",
        fill=fill,
        outline=outline,
        width=width,
    )
    canvas.create_arc(
        x2 - 2 * r,
        y2 - 2 * r,
        x2,
        y2,
        start=270,
        extent=90,
        style="pieslice",
        fill=fill,
        outline=outline,
        width=width,
    )
    canvas.create_arc(
        x1,
        y2 - 2 * r,
        x1 + 2 * r,
        y2,
        start=180,
        extent=90,
        style="pieslice",
        fill=fill,
        outline=outline,
        width=width,
    )

    # Rectángulo central
    canvas.create_rectangle(
        x1 + r, y1, x2 - r, y2, fill=fill, outline=outline, width=width
    )
    # Rectángulos laterales
    canvas.create_rectangle(
        x1, y1 + r, x1 + r, y2 - r, fill=fill, outline=outline, width=width
    )
    canvas.create_rectangle(
        x2 - r, y1 + r, x2, y2 - r, fill=fill, outline=outline, width=width
    )


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
        anchor_cols="w",
        button_text=None,
        button_command=None,
        card_w=980,
        card_h=350,
        **kwargs,
    ):
        super().__init__(parent, bg="#EDEDED", **kwargs)
        self.headers = headers
        self.data = data
        self.actions = actions or []
        self.title = title
        self.subtitle = subtitle
        self.count = count
        self.col_widths = col_widths or [140] * len(headers)
        self.action_text = action_text
        self.anchor_cols = anchor_cols
        self.button_text = button_text
        self.button_command = button_command
        self.card_w = card_w
        self.card_h = card_h
        self._build_table()

    def _build_table(self):
        card_w, card_h = self.card_w, self.card_h
        card = Frame(self, bg="#EDEDED", width=card_w, height=card_h)
        card.pack(padx=0, pady=0, fill="both", expand=True)
        card.pack_propagate(False)
        canvas = Canvas(
            card,
            width=card_w,
            height=card_h,
            bg="#EDEDED",
            highlightthickness=0,
        )
        canvas.pack(fill="both", expand=True)
        draw_rounded_rect(
            canvas, 0, 0, card_w, card_h, 18, fill="white", outline="white"
        )
        card_content = Frame(canvas, bg="white")
        card_content.place(x=0, y=0, width=card_w, height=card_h)
        # Header con título, pill y botón
        if self.title or self.count is not None or self.button_text:
            title_row = Frame(card_content, bg="white")
            title_row.pack(fill="x", padx=32, pady=(24, 0))
            if self.title:
                Label(
                    title_row,
                    text=self.title,
                    font=("Consolas", 20, "bold"),
                    bg="white",
                    fg="#222",
                ).pack(side="left")
            if self.count is not None:
                pill_w, pill_h, radius = 110, 28, 18
                pill = Canvas(
                    title_row,
                    width=pill_w,
                    height=pill_h,
                    bg="white",
                    highlightthickness=0,
                    bd=0,
                )
                pill.pack(side="left", padx=(16, 0))

                def rounded_rect(canvas, x1, y1, x2, y2, r, **kwargs):
                    points = [
                        (x1 + r, y1),
                        (x2 - r, y1),
                        (x2, y1),
                        (x2, y1 + r),
                        (x2, y2 - r),
                        (x2, y2),
                        (x2 - r, y2),
                        (x1 + r, y2),
                        (x1, y2),
                        (x1, y2 - r),
                        (x1, y1 + r),
                        (x1, y1),
                    ]
                    return canvas.create_polygon(points, smooth=True, **kwargs)

                rounded_rect(
                    pill,
                    1,
                    1,
                    pill_w - 2,
                    pill_h - 2,
                    radius,
                    fill="#E0E0E0",
                    outline="#E0E0E0",
                )
                pill.create_text(
                    pill_w // 2,
                    pill_h // 2,
                    text=f"{self.count} Existentes",
                    font=("Consolas", 10, "bold"),
                    fill="#888",
                )
            if self.button_text:
                from ui.elements import RoundedButton

                RoundedButton(
                    title_row,
                    text=self.button_text,
                    width=180,
                    height=48,
                    radius=18,
                    font=("Consolas", 14, "bold"),
                    command=self.button_command,
                ).pack(side="right", padx=(0, 50))
        # Tabla
        table_frame = Frame(card_content, bg="white")
        table_frame.pack(padx=0, pady=(10, 0), fill="both", expand=True)
        # Header de la tabla
        header_row = Frame(table_frame, bg="white")
        header_row.pack(fill="x", padx=0, pady=(6, 0))
        for i, h in enumerate(self.headers):
            Label(
                header_row,
                text=h,
                font=("Consolas", 12, "bold"),
                bg="white",
                fg="#222",
                anchor=self.anchor_cols,
                width=int(self.col_widths[i] // 10),
                pady=12,
                padx=0,
            ).grid(
                row=0, column=i, sticky="nsew", padx=(24 if i == 0 else 8, 0), pady=0
            )
        table_canvas = Canvas(table_frame, bg="white", highlightthickness=0, height=320)
        table_canvas.pack(fill="both", expand=True, side="left")
        scrollbar = Scrollbar(
            table_frame, orient="vertical", command=table_canvas.yview
        )
        scrollbar.pack(side="right", fill="y")
        table_canvas.configure(yscrollcommand=scrollbar.set)
        rows_frame = Frame(table_canvas, bg="white")
        window_id = table_canvas.create_window((0, 0), window=rows_frame, anchor="nw")

        def on_configure(event):
            table_canvas.configure(scrollregion=table_canvas.bbox("all"))
            table_canvas.itemconfig(window_id, width=table_canvas.winfo_width())

        rows_frame.bind("<Configure>", on_configure)
        table_canvas.bind("<Configure>", on_configure)

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
