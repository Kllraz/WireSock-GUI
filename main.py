import flet
from flet_core import TemplateRoute

from views.edit import EditView
from views.main import MainView


def main(page: flet.Page):
    page.title = "WireSock"

    def route_change(route):
        template_route = TemplateRoute(route.route)

        page.views.clear()
        page.views.append(
            flet.View(
                "/",
                [
                    MainView()
                ],
                padding=flet.padding.all(0)
            )
        )
        if template_route.match("/edit/:config_name"):
            page.views.append(
                flet.View(
                    "/edit",
                    [
                        EditView(template_route.config_name)
                    ],
                    scroll=flet.ScrollMode.AUTO
                )
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)


flet.app(main)
