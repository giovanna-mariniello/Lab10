import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._stato = None


    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()

        anno = self._view._txtAnno.value
        try:
            int(anno)
        except ValueError:
            self._view.create_alert("Per favore inserire un anno.")
            self._view.update_page()
            return

        if int(anno) not in range(1816, 2017):
            self._view.create_alert("L'anno inserito non è valido, per favore inserisci un valore compreso tra 1816 e 2016.")
            self._view.update_page()
            return

        self._model.costruisci_grafo(int(anno))
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.get_num_comp_conn()} componenti connesse."))
        self._view._txt_result.controls.append(ft.Text("Di seguito il dettaglio sui nodi:"))

        for s in self._model.get_nodi():
            self._view._txt_result.controls.append(ft.Text(f"{s} -- {self._model.get_num_confinanti(s)} vicini"))

        self._view._dd_stato.disabled = False
        self._view._btn_stati_ragg.disabled = False
        self.riempi_dd_stati()

        self._view.update_page()

    def handleStatiRaggiungibili(self, e):
        raggiungibili = self._model.get_raggiungibili_DFS(self._stato)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Da {self._stato} è possibile raggiungere a piedi {len(raggiungibili)} stati:"))

        for r in raggiungibili:
            self._view._txt_result.controls.append(ft.Text(f"{r}"))

        self._view.update_page()



    def riempi_dd_stati(self):

        stati = self._model.get_nodi()

        for s in stati:
            self._view._dd_stato.options.append(ft.dropdown.Option(text=s.StateNme, data=s, on_click=self.leggi_dd_stato))

    def leggi_dd_stato(self, e):

        if e.control.data is None:
            self._stato = None
        else:
            self._stato = e.control.data

        return self._stato

