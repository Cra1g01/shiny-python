from shiny import App, render, ui

import title


app_ui = ui.page_fluid(
    title.ui("title", "A Title"),
    ui.layout_sidebar(
        ui.panel_sidebar(),
        ui.panel_main(),
    ),
    style="padding: 0;",
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*5 is {input.n() * 5}"


app = App(app_ui, server)
