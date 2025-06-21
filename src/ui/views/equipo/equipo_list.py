from tkinter import *
from ui.elements import (
    TableView,
    TableActionButton,
    RoundedButton,
    AlertDialog,
    ConfirmDialog,
)
from ui.views.equipo.equipo_form import EquipoFormView
from ui.views.equipo.equipo_ver import EquipoFormViewNoEdit
import os
from ui.mocks import (
    get_equipos,
    get_jugadores,
    create_equipo,
    update_equipo,
    delete_equipo,
)


class EquipoView:
    def __init__(self, parent):
        self.parent = parent
        self.show_list()

    def show_list(self):
        for widget in self.parent.winfo_children():
            widget.destroy()
        frame = Frame(self.parent, bg="#EDEDED")
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Encabezado grande con fondo gris claro
        header_bg = Frame(frame, bg="#F6F6F6")
        header_bg.pack(fill="x", padx=0, pady=(0, 0))
        Label(
            header_bg,
            text="Equipos",
            font=("Consolas", 28, "bold"),
            bg="#F6F6F6",
            fg="#222",
            anchor="w",
        ).pack(fill="x", padx=60, pady=(36, 18))

        # Más espacio entre el título y la tarjeta
        Frame(frame, height=18, bg="#EDEDED").pack()

        # Tarjeta de tabla de equipos
        table_card_w, table_card_h = 980, 400
        table_card_container = Frame(
            frame, bg="#EDEDED", width=table_card_w, height=table_card_h
        )
        table_card_container.pack(
            anchor="n", padx=40, pady=(0, 0), fill=None, expand=False
        )

        headers = ["ID", "Nombre", "Participantes", "Acciones", ""]
        equipos = get_equipos()
        data = [
            [f"{e['id']:02}", e["nombre"], str(len(e["jugadores"]))] for e in equipos
        ]

        def action_buttons(row, parent, text):
            btn_frame = Frame(parent, bg=parent["bg"])
            TableActionButton(
                btn_frame,
                icon_path="assets/images/delete.png",
                command=lambda: self.confirm_delete(int(row[0]), row[1]),
            ).pack(side="left", padx=(0, 8))
            TableActionButton(
                btn_frame,
                icon_path="assets/images/edit.png",
                command=lambda: self.show_edit_form(int(row[0])),
            ).pack(side="left", padx=(0, 8))
            return btn_frame

        def info_button(row, parent, text):
            btn = RoundedButton(
                parent,
                text=text,
                width=160,
                height=36,
                radius=16,
                font=("Consolas", 11, "bold"),
                bg="#9FACE8",
                fg="white",
                hover_bg="#688CCA",
                command=lambda: self.show_info_form(int(row[0]))
            )
            btn.pack()
            return btn

        col_widths = [60, 300, 160, 120, 200]

        table = TableView(
            table_card_container,
            headers,
            data,
            actions=[action_buttons, info_button],
            title="Lista de equipos",
            count=len(data),
            col_widths=col_widths,
            action_text="Ver información",
            anchor_cols="center",
            button_text="Crear equipo",
            button_command=self.show_create_form,
            card_w=table_card_w,
            card_h=table_card_h,
        )
        table.pack(padx=0, pady=(10, 0), fill="both", expand=True)

    def show_create_form(self):
        for widget in self.parent.winfo_children():
            widget.destroy()
        EquipoFormView(
            self.parent, get_jugadores(), equipo=None, on_save=self.on_save_create
        )

    def show_edit_form(self, equipo_id):
        equipos = get_equipos()
        equipo = next((e for e in equipos if e["id"] == equipo_id), None)
        if equipo:
            for widget in self.parent.winfo_children():
                widget.destroy()
            EquipoFormView(
                self.parent,
                get_jugadores(),
                equipo=equipo,
                on_save=lambda nombre, jugadores, lider: self.on_save_edit(
                    equipo_id, nombre, jugadores, lider
                ),
            )

    def show_info_form(self, equipo_id):
        equipos = get_equipos()
        equipo = next((e for e in equipos if e["id"] == equipo_id), None)
        if equipo:
            for widget in self.parent.winfo_children():
                widget.destroy()
            EquipoFormViewNoEdit(
                parent=self.parent,
                jugadores=get_jugadores(),
                equipo=equipo,               
                )            

    def on_save_create(self, nombre, jugadores, lider_id):
        equipos = get_equipos()
        if not nombre.strip():
            AlertDialog(
                self.parent.winfo_toplevel(), "El nombre del equipo no puede estar vacío.", success=False
            )
            return
        if not jugadores:
            AlertDialog(self.parent.winfo_toplevel(), "Selecciona al menos un jugador.", success=False)
            return
        if not lider_id or not any(j["id_jugador"] == lider_id for j in jugadores):
            AlertDialog(self.parent.winfo_toplevel(), "Selecciona un líder válido.", success=False)
            return

        result = create_equipo(nombre, jugadores)
        if result is None:
            AlertDialog(
                self.parent.winfo_toplevel(), "Ya existe un equipo con ese nombre.", success=False
            )
            return
        AlertDialog(
            self.parent.winfo_toplevel(),
            "Equipo creado exitosamente.",
            success=True,
            on_close=self.show_list,
        )

    def on_save_edit(self, equipo_id, nombre, jugadores, lider_id):
        equipos = get_equipos()
        if not nombre.strip():
            AlertDialog(
                self.parent.winfo_toplevel(), "El nombre del equipo no puede estar vacío.", success=False
            )
            return
        if not jugadores:
            AlertDialog(self.parent.winfo_toplevel(), "Selecciona al menos un jugador.", success=False)
            return
        if not lider_id or not any(j["id_jugador"] == lider_id for j in jugadores):
            AlertDialog(self.parent.winfo_toplevel(), "Selecciona un líder válido.", success=False)
            return
        if any(
            e["nombre"].strip().lower() == nombre.strip().lower()
            and e["id"] != equipo_id
            for e in equipos
        ):
            AlertDialog(
                self.parent.winfo_toplevel(), "Ya existe un equipo con ese nombre.", success=False
            )
            return
        update_equipo(equipo_id, nombre, jugadores)
        AlertDialog(
            self.parent.winfo_toplevel(),
            "Equipo actualizado exitosamente.",
            success=True,
            on_close=self.show_list,
        )

    def confirm_delete(self, equipo_id, equipo_nombre):
        ConfirmDialog(
            self.parent.winfo_toplevel(),
            f"¿Estás seguro de que deseas eliminar el equipo '{equipo_nombre}'? Esta acción no se puede deshacer.",
            on_confirm=lambda: self.delete_equipo(equipo_id),
            card_height=500,
        )

    def delete_equipo(self, equipo_id):
        delete_equipo(equipo_id)
        self.show_list()
