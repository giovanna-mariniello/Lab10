import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handleCalcola(self, e):
        anno = self._view._txtAnno.value
        if anno is None or anno == "":
            self._view.create_alert("Per favore inserire un anno.")

        if int(anno) not in range(1816, 2017):
            self._view.create_alert("L'anno inserito non è valido.")


        grafo = self._model.costruisci_grafo(anno)
        self._view.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.controls.append(ft.Text(f"Il grafo ha {self._model.get_num_comp_conn()} componenti connesse."))
        self._view.controls.append(ft.Text("Di seguito il dettaglio sui nodi:"))

        for s in grafo.get_nodi():
            self._view.controls.append(ft.Text(f"{s} -- {self._model.get_num_confinanti(s)} vicini"))

        self._view.update_page()



