from tkinter import *
from tkinter import ttk
from tkinter import Canvas
from tkinter import PhotoImage
import os


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
        self.clicked = False
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
        self.bind("<ButtonRelease-1>", self._on_click)
        self.tag_bind(self.btn_id, "<ButtonRelease-1>", self._on_click)
        self.tag_bind(self.text_id, "<ButtonRelease-1>", self._on_click)

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
        if self.command and not self.clicked:
            self.clicked = True
            self.command()
            return
        if self.clicked:
            self.clicked = False

    def _animate_color(self, from_color, to_color, steps=8, step=0):
        def hex_to_rgb(h):
            if not isinstance(h, str) or not h.startswith("#") or len(h) != 7:
                # Si no es un color hex válido, regresa color blanco o el bg
                return (255, 255, 255)
            try:
                return tuple(int(h[i : i + 2], 16) for i in (1, 3, 5))
            except Exception:
                return (255, 255, 255)

        def rgb_to_hex(rgb):
            return "#%02x%02x%02x" % rgb

        # Si el color no es válido, no animar
        if not (
            isinstance(from_color, str)
            and from_color.startswith("#")
            and len(from_color) == 7
        ):
            self.itemconfig(self.btn_id, fill=self.bg)
            return
        if not (
            isinstance(to_color, str)
            and to_color.startswith("#")
            and len(to_color) == 7
        ):
            self.itemconfig(self.btn_id, fill=self.bg)
            return
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

    def set_text(self, text):
        self.itemconfig(self.text_id, text=text)

    def set_colors(self, bg=None, fg=None, hover_bg=None):
        if bg:
            self.bg = bg
            self.itemconfig(self.btn_id, fill=bg)
        if fg:
            self.fg = fg
            self.itemconfig(self.text_id, fill=fg)
        if hover_bg:
            self.hover_bg = hover_bg


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
        self.clicked = False
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
        if self.command and not self.clicked:
            self.clicked = True
            self.command()
            return
        if self.clicked:
            self.clicked = False


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


class StyledEntry(Frame):
    def __init__(
        self,
        parent,
        textvariable=None,
        width=400,
        font=("Consolas", 13),
        placeholder="",
        border_radius=12,
        **kwargs,
    ):
        super().__init__(parent, bg="white")
        self.border_radius = border_radius
        self.canvas = Canvas(
            self, bg="white", highlightthickness=0, width=width, height=48
        )
        self.canvas.pack(fill="x", expand=True)
        self._draw_rounded_rect(
            6, 6, width-6, 42, border_radius, fill="#F6F6F6", outline="#D5D4DC"
        )
        self.entry = Entry(
            self,
            textvariable=textvariable,
            font=font,
            bd=0,
            relief="flat",
            highlightthickness=0,
            bg="#F6F6F6",
            fg="#222",
            **kwargs,
        )
        self.entry.place(x=18, y=14, width=width - 40, height=26)
        self.config(
            highlightbackground="#D5D4DC",
            highlightcolor="#688CCA",
            highlightthickness=0,
            bd=0,
        )
        self.entry.bind("<FocusIn>", self._on_focus_in)
        self.entry.bind("<FocusOut>", self._on_focus_out)
        self.placeholder = placeholder
        self.textvariable = textvariable
        if placeholder and (not textvariable or not textvariable.get()):
            self._set_placeholder()
        self.entry.bind("<FocusIn>", self._clear_placeholder)
        self.entry.bind("<FocusOut>", self._restore_placeholder)

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
        return self.canvas.create_polygon(points, smooth=True, **kwargs)

    def _on_focus_in(self, event):
        self.canvas.itemconfig(1, outline="#688CCA")

    def _on_focus_out(self, event):
        self.canvas.itemconfig(1, outline="#D5D4DC")

    def _set_placeholder(self, event=None):
        self.entry.delete(0, "end")
        self.entry.insert(0, self.placeholder)
        self.entry.config(fg="#888")

    def _clear_placeholder(self, event=None):
        if self.entry.get() == self.placeholder:
            self.entry.delete(0, "end")
            self.entry.config(fg="#222")

    def _restore_placeholder(self, event=None):
        if not self.entry.get():
            self._set_placeholder()

    def get(self):
        val = self.entry.get()
        if val == self.placeholder:
            return ""
        return val

    def set(self, value):
        self.entry.delete(0, "end")
        self.entry.insert(0, value)


class AlertDialog(Frame):
    _instance = None  # Singleton para evitar múltiples diálogos

    def __init__(self, parent, message, success=True, on_close=None):
        from ui.elements import RoundedButton

        if AlertDialog._instance is not None:
            try:
                AlertDialog._instance.destroy()
            except Exception:
                pass
        AlertDialog._instance = self

        super().__init__(parent, bg="#000000")
        self.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.lift()

        # Fondo semitransparente
        self.overlay = Canvas(self, bg="#000000", highlightthickness=0)
        self.overlay.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        self.overlay.create_rectangle(0, 0, w, h, fill="#E0E0E0")

        # Card centrada
        card_w, card_h, card_r = 600, 400, 24
        card = Frame(self, bg="white", width=card_w, height=card_h)
        card.place(relx=0.5, rely=0.5, anchor="center")
        card.pack_propagate(False)

        # Icono
        assets_path = os.path.join(os.path.dirname(__file__), "..", "assets", "images")
        icon_path = os.path.join(assets_path, "success.png" if success else "error.png")
        icon_img = PhotoImage(file=icon_path, format="png")
        Label(card, image=icon_img, bg="white").pack(pady=(40, 0))
        self.icon_img = icon_img

        # Mensaje
        msg_lbl = Label(
            card,
            text=message,
            font=("Consolas", 22, "bold"),
            fg="#222",
            bg="white",
            wraplength=520,
            justify="center",
        )
        msg_lbl.pack(pady=(18, 0), padx=24)

        def accept():
            AlertDialog._instance = None
            self.destroy()
            if on_close:
                on_close()

        # Botón de aceptar
        btn_frame = Frame(card, bg="white")
        btn_frame.pack(pady=(32, 0))
        RoundedButton(
            btn_frame,
            text="Aceptar",
            width=220,
            height=56,
            radius=22,
            font=("Consolas", 16, "bold"),
            bg="#688CCA" if success else "#E57373",
            fg="white",
            hover_bg="#4B6EA8" if success else "#C62828",
            command=accept,
        ).pack(side="left", padx=12)

        self.focus_set()
        self.bind("<Button-1>", lambda e: None)  # Captura clicks para evitar que pasen atrás


class ConfirmDialog(Frame):
    def __init__(
        self, parent, message, on_confirm=None, on_cancel=None, card_height=None
    ):
        from ui.elements import RoundedButton

        super().__init__(parent, bg="#000000")
        self.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.lift()

        # Fondo semitransparente
        self.overlay = Canvas(self, bg="#000000", highlightthickness=0)
        self.overlay.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        self.overlay.create_rectangle(0, 0, w, h, fill="#E0E0E0")

        # Card centrada
        card_w, card_r = 800, 32
        card_h = card_height if card_height is not None else 400
        card = Frame(self, bg="white", width=card_w, height=card_h)
        card.place(relx=0.5, rely=0.5, anchor="center")
        card.pack_propagate(False)

        # Icono
        assets_path = os.path.join(os.path.dirname(__file__), "..", "assets", "images")
        icon_path = os.path.join(assets_path, "error.png")
        icon_img = PhotoImage(file=icon_path, format="png")
        Label(card, image=icon_img, bg="white").pack(pady=(40, 0))
        self.icon_img = icon_img

        # Mensaje
        msg_lbl = Label(
            card,
            text=message,
            font=("Consolas", 26, "bold"),
            fg="#222",
            bg="white",
            wraplength=700,
            justify="center",
        )
        msg_lbl.pack(pady=(24, 0), padx=32)
        btn_frame = Frame(card, bg="white")
        btn_frame.pack(pady=(48, 0))

        def confirm():
            self.destroy()
            if on_confirm:
                on_confirm()

        def cancel():
            self.destroy()
            if on_cancel:
                on_cancel()

        RoundedButton(
            btn_frame,
            text="Cancelar",
            width=220,
            height=56,
            radius=22,
            font=("Consolas", 16, "bold"),
            bg="#EEE",
            fg="#222",
            hover_bg="#DDD",
            command=cancel,
        ).pack(side="left", padx=36)
        RoundedButton(
            btn_frame,
            text="Eliminar",
            width=220,
            height=56,
            radius=22,
            font=("Consolas", 16, "bold"),
            bg="#E57373",
            fg="white",
            hover_bg="#C62828",
            command=confirm,
        ).pack(side="left", padx=36)

        self.focus_set()
        self.bind("<Button-1>", lambda e: None)  # Captura clicks para evitar que pasen atrás
