"""
############################################################
Pyndorama - Principal
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: 2013/07/16
:Status: This is a "work in progress"
:Revision: 0.1.3
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
from visual import Visual
from visual import Gui


class Main:
    """Game base with board and pieces."""
    def __init__(self, visual, gui):
        """Constroi a casa que indica a peca que foi selecionada. """
        self.visual, self.gui = visual, gui

    def build_book(self, visual):
        """Constroi as partes do Jogo. """
        visual.build_book(self.gui)


def main(doc, svg, html, ajax, win):
    print('Pyndorama 0.1.0')
    visual = Visual(doc, svg, html, ajax, win)
    gui = Gui(doc, svg, html, ajax, win)
    app = Main(visual, gui)
    app.build_book(visual)
