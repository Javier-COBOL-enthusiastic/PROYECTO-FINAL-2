"""
Elementos de interfaz de usuario personalizados
Este módulo contiene componentes de UI reutilizables como botones redondeados,
tablas, campos de entrada estilizados y diálogos personalizados.
"""

from tkinter import *
from tkinter import ttk
from tkinter import Canvas
from tkinter import PhotoImage
import os


def draw_rounded_rect(canvas, x1, y1, x2, y2, r, fill, outline, width=1):
    """
    Función auxiliar para dibujar rectángulos con esquinas redondeadas en un canvas
    
    Args:
        canvas: Canvas donde dibujar
        x1, y1: Coordenadas de la esquina superior izquierda
        x2, y2: Coordenadas de la esquina inferior derecha
        r: Radio de las esquinas redondeadas
        fill: Color de relleno
        outline: Color del borde
        width: Grosor del borde
    """
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
    """
    Botón personalizado para menús con efectos hover
    """
    def __init__(self, master, text, command=None, font=None, **kwargs):
        """
        Constructor del botón de menú
        
        Args:
            master: Widget padre
            text: Texto del botón
            command: Función a ejecutar al hacer clic
            font: Fuente del texto
            **kwargs: Argumentos adicionales para el botón
        """
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

        # Vincular eventos de hover
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        """Cambia el color de fondo al pasar el mouse"""
        self["background"] = "#5A7BB8"

    def on_leave(self, e):
        """Restaura el color de fondo al salir el mouse"""
        self["background"] = "#688CCA"


class RoundedButton(Canvas):
    """
    Botón personalizado con esquinas redondeadas y efectos de hover
    """
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
        """
        Constructor del botón redondeado
        
        Args:
            parent: Widget padre
            text: Texto del botón
            width: Ancho del botón
            height: Alto del botón
            radius: Radio de las esquinas redondeadas
            bg: Color de fondo
            fg: Color del texto
            font: Fuente del texto
            hover_bg: Color de fondo al hacer hover
            command: Función a ejecutar al hacer clic
            **kwargs: Argumentos adicionales
        """
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
        
        # Dibujar el botón redondeado
        self.btn_id = self._draw_rounded_rect(
            5, 5, width - 5, height - 5, radius, fill=bg, outline=""
        )
        self.text_id = self.create_text(
            width // 2, height // 2, text=text, fill=fg, font=font
        )
        
        # Vincular eventos
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
        """
        Dibuja un rectángulo redondeado en el canvas
        
        Args:
            x1, y1: Coordenadas de la esquina superior izquierda
            x2, y2: Coordenadas de la esquina inferior derecha
            r: Radio de las esquinas
            **kwargs: Propiedades adicionales del polígono
            
        Returns:
            ID del polígono creado
        """
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
        """Efecto al entrar el mouse"""
        self._animate_color(self.bg, self.hover_bg)

    def _on_leave(self, e):
        """Efecto al salir el mouse"""
        self._animate_color(self.itemcget(self.btn_id, "fill"), self.bg)

    def _on_click(self, e):
        """Maneja el evento de clic"""
        if self.command and not self.clicked:
            self.clicked = True
            self.command()
            return
        if self.clicked:
            self.clicked = False

    def _animate_color(self, from_color, to_color, steps=8, step=0):
        """
        Anima la transición de color del botón
        
        Args:
            from_color: Color inicial
            to_color: Color final
            steps: Número de pasos para la animación
            step: Paso actual de la animación
        """
        def hex_to_rgb(h):
            """Convierte color hexadecimal a RGB"""
            if not isinstance(h, str) or not h.startswith("#") or len(h) != 7:
                # Si no es un color hex válido, regresa color blanco o el bg
                return (255, 255, 255)
            try:
                return tuple(int(h[i : i + 2], 16) for i in (1, 3, 5))
            except Exception:
                return (255, 255, 255)

        def rgb_to_hex(rgb):
            """Convierte color RGB a hexadecimal"""
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
        """Cambia el texto del botón"""
        self.itemconfig(self.text_id, text=text)

    def set_colors(self, bg=None, fg=None, hover_bg=None):
        """
        Cambia los colores del botón
        
        Args:
            bg: Color de fondo
            fg: Color del texto
            hover_bg: Color de fondo al hacer hover
        """
        if bg:
            self.bg = bg
            self.itemconfig(self.btn_id, fill=bg)
        if fg:
            self.fg = fg
            self.itemconfig(self.text_id, fill=fg)
        if hover_bg:
            self.hover_bg = hover_bg


class TableActionButton(Canvas):
    """
    Botón de acción para tablas con icono y efectos hover
    Se usa para botones de editar, eliminar, ver, etc. en las tablas
    """
    def __init__(self, parent, icon_path, command=None, size=32, **kwargs):
        """
        Constructor del botón de acción
        
        Args:
            parent: Widget padre
            icon_path: Ruta al archivo de icono
            command: Función a ejecutar al hacer clic
            size: Tamaño del botón (cuadrado)
            **kwargs: Argumentos adicionales
        """
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
        
        # Vincular eventos
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<Button-1>", self._on_click)
        self.tag_bind(self.icon_id, "<Enter>", self._on_enter)
        self.tag_bind(self.icon_id, "<Leave>", self._on_leave)
        self.tag_bind(self.icon_id, "<Button-1>", self._on_click)

    def _on_enter(self, e):
        """Cambia el color de fondo al entrar el mouse"""
        self.configure(bg=self.bg_hover)

    def _on_leave(self, e):
        """Restaura el color de fondo al salir el mouse"""
        self.configure(bg=self.bg_normal)

    def _on_click(self, e):
        """Maneja el evento de clic"""
        if self.command and not self.clicked:
            self.clicked = True
            self.command()
            return
        if self.clicked:
            self.clicked = False


class TableView(Frame):
    """
    Componente de tabla personalizada con diseño moderno
    Permite mostrar datos en formato de tabla con acciones personalizables
    """
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
        """
        Constructor de la tabla
        
        Args:
            parent: Widget padre
            headers: Lista de encabezados de columnas
            data: Lista de datos a mostrar
            actions: Lista de acciones disponibles para cada fila
            title: Título de la tabla
            subtitle: Subtítulo de la tabla
            count: Número total de elementos
            col_widths: Anchos de las columnas
            action_text: Texto para el botón de acción
            anchor_cols: Alineación de las columnas
            button_text: Texto del botón principal
            button_command: Función del botón principal
            card_w: Ancho de la tarjeta
            card_h: Alto de la tarjeta
            **kwargs: Argumentos adicionales
        """
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
        """
        Construye la interfaz de la tabla
        """
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
    """
    Campo de entrada personalizado con esquinas redondeadas y placeholder
    Proporciona una interfaz moderna para la entrada de texto
    """
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
        """
        Constructor del campo de entrada estilizado
        
        Args:
            parent: Widget padre
            textvariable: Variable de texto de Tkinter
            width: Ancho del campo
            font: Fuente del texto
            placeholder: Texto de placeholder
            border_radius: Radio de las esquinas redondeadas
            **kwargs: Argumentos adicionales
        """
        super().__init__(parent, bg="white")
        self.border_radius = border_radius
        
        # Crear canvas para el fondo redondeado
        self.canvas = Canvas(
            self, bg="white", highlightthickness=0, width=width, height=48
        )
        self.canvas.pack(fill="x", expand=True)
        self._draw_rounded_rect(
            6, 6, width-6, 42, border_radius, fill="#F6F6F6", outline="#D5D4DC"
        )
        
        # Crear el campo de entrada
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
        
        # Configurar el frame
        self.config(
            highlightbackground="#D5D4DC",
            highlightcolor="#688CCA",
            highlightthickness=0,
            bd=0,
        )
        
        # Vincular eventos de focus
        self.entry.bind("<FocusIn>", self._on_focus_in)
        self.entry.bind("<FocusOut>", self._on_focus_out)
        
        # Configurar placeholder
        self.placeholder = placeholder
        self.textvariable = textvariable
        if placeholder and (not textvariable or not textvariable.get()):
            self._set_placeholder()
        self.entry.bind("<FocusIn>", self._clear_placeholder)
        self.entry.bind("<FocusOut>", self._restore_placeholder)

    def _draw_rounded_rect(self, x1, y1, x2, y2, r, **kwargs):
        """
        Dibuja un rectángulo redondeado en el canvas
        
        Args:
            x1, y1: Coordenadas de la esquina superior izquierda
            x2, y2: Coordenadas de la esquina inferior derecha
            r: Radio de las esquinas
            **kwargs: Propiedades adicionales del polígono
            
        Returns:
            ID del polígono creado
        """
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
        """Cambia el color del borde al obtener el foco"""
        self.canvas.itemconfig(1, outline="#688CCA")

    def _on_focus_out(self, event):
        """Restaura el color del borde al perder el foco"""
        self.canvas.itemconfig(1, outline="#D5D4DC")

    def _set_placeholder(self, event=None):
        """Establece el texto placeholder"""
        self.entry.delete(0, "end")
        self.entry.insert(0, self.placeholder)
        self.entry.config(fg="#888")

    def _clear_placeholder(self, event=None):
        """Limpia el placeholder al obtener el foco"""
        if self.entry.get() == self.placeholder:
            self.entry.delete(0, "end")
            self.entry.config(fg="#222")

    def _restore_placeholder(self, event=None):
        """Restaura el placeholder si el campo está vacío"""
        if not self.entry.get():
            self._set_placeholder()

    def get(self):
        """
        Obtiene el valor del campo, ignorando el placeholder
        
        Returns:
            str: Valor del campo o cadena vacía si es el placeholder
        """
        val = self.entry.get()
        if val == self.placeholder:
            return ""
        return val

    def set(self, value):
        """
        Establece el valor del campo
        
        Args:
            value: Valor a establecer
        """
        self.entry.delete(0, "end")
        self.entry.insert(0, value)

class StyledCombobox(Frame):
    """
    Combobox personalizado con esquinas redondeadas y dropdown personalizado
    Proporciona una interfaz moderna para selección de opciones
    """
    def __init__(
        self,
        parent,
        values=None,
        textvariable=None,
        width=400,
        height=48,
        font=("Consolas", 13),
        placeholder="",
        border_radius=12,
        mousewheel_callback = None
    ):
        """
        Constructor del combobox estilizado
        
        Args:
            parent: Widget padre
            values: Lista de valores disponibles
            textvariable: Variable de texto de Tkinter
            width: Ancho del combobox
            height: Alto del combobox
            font: Fuente del texto
            placeholder: Texto de placeholder
            border_radius: Radio de las esquinas redondeadas
            mousewheel_callback: Función callback para el scroll del mouse
        """
        super().__init__(parent, bg="white")
        self.border_radius = border_radius
        self.width = width
        self.height = height
        self.values = values or []
        self.font = font
        self.placeholder = placeholder
        self.textvar = textvariable
        self._on_mousewheel_callback = mousewheel_callback
        self.dropdown_canvas = None
        
        # Crear canvas para el fondo redondeado
        self.canvas = Canvas(
            self, 
            width=width, 
            height=height, 
            bg="white", 
            highlightthickness=0
        )
        self.canvas.pack(fill="x", expand=True)
        
        self._draw_rounded_rect(
            0, 0, width, height, border_radius, 
            fill="#F6F6F6", outline="#D5D4DC"
        )
        
        self.text = self.canvas.create_text(
            18, 
            height//2, 
            text=placeholder, 
            font=font, 
            fill="#888", 
            anchor="w"
        )
        
        flecha_size = 8
        self.flecha = self.canvas.create_polygon(
            width - 24, height//2 - flecha_size//2,
            width - 16, height//2 - flecha_size//2,
            width - 20, height//2 + flecha_size//2,
            fill="#888"
        )
        
        self.selected_val = None
        self.dropdown = False
        
        self.canvas.bind("<Button-1>", self._on_click)
        self.canvas.bind("<Enter>", self._on_enter)
        self.canvas.bind("<Leave>", self._on_leave)
        
        self.dropdown_frame = None
        
        if placeholder and (not textvariable or not textvariable.get()):
            self._set_placeholder()
        elif(textvariable.get()):
            self._select_item(textvariable.get())
    
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
    
    def _on_enter(self, e):
        self.canvas.itemconfig(1, outline="#688CCA")
        self.canvas.itemconfig(self.flecha, fill="#688CCA")
    
    def _on_leave(self, e):
        if not self.dropdown:
            self.canvas.itemconfig(1, outline="#D5D4DC")
            self.canvas.itemconfig(self.flecha, fill="#888")
    
    def _on_click(self, e):
        if not self.dropdown:
            self._open_dropdown()
        else:
            self._close_dropdown()
    
    def _open_dropdown(self):
        self.dropdown = True
        self.canvas.itemconfig(1, outline="#688CCA")
        self.canvas.itemconfig(self.flecha, fill="#688CCA")
        if self._on_mousewheel_callback is not None:
            self._mousewheel_callback = self.winfo_toplevel().bind("<MouseWheel>")
            self.winfo_toplevel().unbind("<MouseWheel>")

        self.dropdown_frame = Frame(
            self.winfo_toplevel(),
            bg="white",
            highlightbackground="#688CCA",
            highlightthickness=1
        )
        
        x = self.winfo_rootx()
        y = self.winfo_rooty() + self.height
        
        max_h = min(150, len(self.values) * 36 + 10)
        self.dropdown_frame.place(x=x, y=y, width=self.width, height=max_h)
        
        self.dropdown_canvas = Canvas(
            self.dropdown_frame,
            bg="white",
            highlightthickness=0
        )
        self.dropdown_canvas.pack(side="left", fill="both", expand=True)
        
        scrollbar = Scrollbar(
            self.dropdown_frame,
            orient="vertical",
            command=self.dropdown_canvas.yview
        )
        scrollbar.pack(side="right", fill="y")
        
        self.dropdown_canvas.configure(yscrollcommand=scrollbar.set)

        def _on_mousewheel(event):
            if self.dropdown_canvas and self.dropdown:  # Verificar que exista y esté abierto
                self.dropdown_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        self.dropdown_canvas.bind_all("<MouseWheel>", _on_mousewheel)

        items_frame = Frame(self.dropdown_canvas, bg="white")
        self.dropdown_canvas.create_window((0, 0), window=items_frame, anchor="nw")
        
        def on_frame_configure(e):
            self.dropdown_canvas.configure(scrollregion=self.dropdown_canvas.bbox("all"))
        
        items_frame.bind("<Configure>", on_frame_configure)
        
        for i, value in enumerate(self.values):
            card_frame = Frame(items_frame, bg="white")
            card_frame.pack(fill="x", pady=(2 if i == 0 else 0, 2))
            
            card = Canvas(
                card_frame,
                width=self.width - 2,
                height=32,
                bg="white",
                highlightthickness=0
            )
            card.pack(fill="x")
            

            card.create_rectangle(
                1, 1, self.width - 3, 31,
                fill="#F6F6F6" if i % 2 == 0 else "white",
                outline="#F6F6F6" if i % 2 == 0 else "white"
            )
            
            card.create_text(
                10, 16,
                text=value,
                font=self.font,
                fill="#222",
                anchor="w"
            )
            
            card.bind("<Enter>", lambda e, c=card: self._on_item_enter(e, c))
            card.bind("<Leave>", lambda e, c=card: self._on_item_leave(e, c))
            card.bind("<Button-1>", lambda e, v=value: self._select_item(v))
                
        self.winfo_toplevel().bind("<Button-1>", self._check_click_outside, add="+")
    
    def _on_item_enter(self, e, canvas):
        canvas.itemconfig(1, fill="#E0E0E0", outline="#E0E0E0")
    
    def _on_item_leave(self, e, canvas):
        index = self.values.index(canvas.itemcget(2, "text"))
        canvas.itemconfig(1, 
            fill="#F6F6F6" if index % 2 == 0 else "white",
            outline="#F6F6F6" if index % 2 == 0 else "white"
        )
    
    def _select_item(self, value):
        self.selected_val = value
        self.canvas.itemconfig(self.text, text=value, fill="#222")
        
        if self.textvar:
            self.textvar.set(value)
        
        self._close_dropdown()
    
    def _close_dropdown(self):
        if self.dropdown_frame:
            self.dropdown_frame.destroy()
            self.dropdown_frame = None            
            self.dropdown_canvas = None
        
        self.dropdown = False
        self.canvas.itemconfig(1, outline="#D5D4DC")
        self.canvas.itemconfig(self.flecha, fill="#888")

        if self._on_mousewheel_callback is not None:
            self.winfo_toplevel().bind("<MouseWheel>", self._on_mousewheel_callback)
    
        self.winfo_toplevel().unbind("<Button-1>")
    
    def _check_click_outside(self, e):
        if not self.dropdown_frame:
            return
                    
        combobox_x = self.winfo_rootx()
        combobox_y = self.winfo_rooty()
        combobox_width = self.winfo_width()
        combobox_height = self.winfo_height()
        
        dropdown_y = combobox_y + combobox_height
        dropdown_height = self.dropdown_frame.winfo_height()
        
        if (e.x_root < combobox_x or 
            e.x_root > combobox_x + combobox_width or
            e.y_root < combobox_y or 
            (e.y_root > combobox_y + combobox_height and 
             e.y_root < dropdown_y) or
            e.y_root > dropdown_y + dropdown_height):
            
            self._close_dropdown()
    
    def _set_placeholder(self):
        self.canvas.itemconfig(self.text, text=self.placeholder, fill="#888")
    
    def get(self):
        if self.selected_val == self.placeholder:
            return ""
        return self.selected_val
    
    def set(self, value):
        if value in self.values:
            self.selected_val = value
            self.canvas.itemconfig(self.text, text=value, fill="#222")
            if self.textvar:
                self.textvar.set(value)
        elif not value:
            self._set_placeholder()
    
    def configure(self, **kwargs):
        if 'values' in kwargs:
            self.values = kwargs['values']
            if self.selected_val and self.selected_val not in self.values:
                self._set_placeholder()
                self.selected_val = None


class AlertDialog(Frame):
    """
    Diálogo de alerta modal con diseño moderno
    Se usa para mostrar mensajes de éxito o error al usuario
    Implementa patrón singleton para evitar múltiples diálogos
    """
    _instance = None  # Singleton para evitar múltiples diálogos

    def __init__(self, parent, message, success=True, on_close=None):
        """
        Constructor del diálogo de alerta
        
        Args:
            parent: Widget padre
            message: Mensaje a mostrar
            success: Si es True muestra alerta de éxito, si es False muestra error
            on_close: Función a ejecutar al cerrar el diálogo
        """
        from ui.elements import RoundedButton

        # Implementar patrón singleton
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

        # Icono según el tipo de alerta
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
            """Función para cerrar el diálogo"""
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
    """
    Diálogo de confirmación modal con diseño moderno
    Se usa para pedir confirmación al usuario antes de realizar acciones críticas
    """
    def __init__(
        self, parent, message, on_confirm=None, on_cancel=None, card_height=None, ops = ("Cancelar", "Eliminar")
    ):
        """
        Constructor del diálogo de confirmación
        
        Args:
            parent: Widget padre
            message: Mensaje a mostrar
            on_confirm: Función a ejecutar al confirmar
            on_cancel: Función a ejecutar al cancelar
            card_height: Alto de la tarjeta
            ops: Tupla con textos de los botones (cancelar, confirmar)
        """
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

        # Icono de advertencia
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
            """Función para confirmar la acción"""
            self.destroy()
            if on_confirm:
                on_confirm()

        def cancel():
            """Función para cancelar la acción"""
            self.destroy()
            if on_cancel:
                on_cancel()

        # Botones de confirmar y cancelar
        RoundedButton(
            btn_frame,
            text=ops[0],
            width=220,
            height=56,
            radius=22,
            font=("Consolas", 16, "bold"),
            bg="#9FACE8",
            fg="white",
            hover_bg="#688CCA",
            command=cancel,
        ).pack(side="left", padx=12)
        RoundedButton(
            btn_frame,
            text=ops[1],
            width=220,
            height=56,
            radius=22,
            font=("Consolas", 16, "bold"),
            bg="#E57373",
            fg="white",
            hover_bg="#C62828",
            command=confirm,
        ).pack(side="left", padx=12)

        self.focus_set()
        self.bind("<Button-1>", lambda e: None)  # Captura clicks para evitar que pasen atrás
