from htmltools import css

from shiny import (
    module,
    ui as sui,
)


@module.ui
def ui(page_title: str) -> sui.TagList:
    """
    Page title ui.

    :param id: ID of the module
    :param page_title: Title of the page
    :returns: Shiny Tag list of elements
    """

    nav_style = css(
        background_color="blue",
        border_radius="8px",
        color="white",
        margin_left="12px",
        padding="4px 12px",
    )

    nav = sui.row(
        sui.column(2),
        sui.column(
            3,
            sui.div("Page 1"),
            style=nav_style,
        ),
        sui.column(
            3,
            sui.div("Page 2"),
            style=nav_style,
        ),
        sui.column(
            3,
            sui.div("Page 3"),
            style=nav_style,
        ),
    )

    title_style = css(
        border_bottom="1px solid black",
        background_color="cyan",
        padding="10px 20px",
    )

    page_title_style = css(
        font_size="20px",
    )

    title = sui.row(
        sui.column(
            4,
            sui.row(
                sui.column(
                    12,
                    sui.div(page_title),
                    style=page_title_style,
                ),
            ),
        ),
        sui.column(
            8,
            nav,
        ),
        style=title_style,
    )

    return sui.panel_title(
        title,
        window_title=page_title,
    )
