import matplotlib.pyplot as plt
import numpy as np
from shiny import App, render, ui

import title


t = np.linspace(0, 2 * np.pi, 1024)
data2d = np.sin(t)[:, np.newaxis] * np.cos(t)[np.newaxis, :]

app_ui = ui.page_fluid(
    title.ui("title", "A Title"),
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_radio_buttons("cmap", "Colormap type",
                dict(viridis="Perceptual", gist_heat="Sequential", RdYlBu="Diverging")
            ),
            ui.input_slider("range", "Color range", -1, 1, value=(-1, 1), step=0.05),
        ),
        ui.panel_main(
            ui.output_plot("plot"),
        ),
    ),
    style="padding: 0;",
)


def server(input, output, session):
    @output
    @render.plot
    def plot():
        fig, ax = plt.subplots()
        im = ax.imshow( # type: ignore
            data2d,
            cmap=input.cmap(),
            vmin=input.range()[0],
            vmax=input.range()[1],
        )
        fig.colorbar(im, ax=ax)
        return fig


app = App(app_ui, server)
