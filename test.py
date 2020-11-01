
from pypic import *


def main():
    my_render_config = RenderConfig()
    duration = 7 * 1000

    timeline = Timeline(duration=duration)

    renderer = CairoRenderer(my_render_config, timeline)
    renderer.render()


if __name__ == "__main__":
    main()
