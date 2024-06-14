import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_grafo(self, e):
        grafo = self._model.creaGrafo(self._view.dd_mese.value, int(self._view.txt_min.value))
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumEdges()} archi."))
        for match in grafo.nodes:
            self._view.dd_m1.options.append(ft.dropdown.Option(
                text=match.MatchID))
            self._view.dd_m2.options.append(ft.dropdown.Option(
                text=match.MatchID))

        self._view.update_page()
    def handle_connessione(self, e):
        arco=self._model.connessione()
        self._view.txt_result.controls.append(ft.Text(f"Coppie con connessione massima pari a {arco[1]}:"))

        self._view.txt_result.controls.append(ft.Text(f"{arco[0][0]} - {arco[0][1]}"))

        self._view.update_page()

    def handle_collegamento(self, e):
        cammino, peso=self._model.getBestPath(self._view.dd_m1.value,self._view.dd_m2.value)
        self._view.txt_result.controls.append(ft.Text(f"Il cammino di peso massimo ha un peso pari a {peso} ed è composto dai seguenti nodi:"))
        for nodo in cammino:
            self._view.txt_result.controls.append(ft.Text
                                                  (f"{nodo}"))
        self._view.update_page()
    def fillDD(self):
        for mese in self._model._idMapMese.keys():
            self._view.dd_mese.options.append(ft.dropdown.Option(
                text=mese))
