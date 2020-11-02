from .rendering.render_config import RenderConfig


BONKERS_RENDER_CONFIG = RenderConfig(
    fps=240,
    width=15360,
    height=8640,
    only_write_every=4
)

UHD_RENDER_CONFIG = RenderConfig(
    fps=120,
    width=3840,
    height=2160,
    only_write_every=2
)

QHD_RENDER_CONFIG = RenderConfig(
    fps=60,
    width=2560,
    height=1440
)

FULL_HD_RENDER_CONFIG = RenderConfig(
    fps=60,
    width=1920,
    height=1080
)

HD_RENDER_CONFIG = RenderConfig(
    fps=60,
    width=1280,
    height=720
)

HD_RENDER_CONFIG_HALF_FPS = RenderConfig(
    fps=30,
    width=1280,
    height=720
)

DEFAULT_RENDER_CONFIG = HD_RENDER_CONFIG

FFMPEG_BINARY = "ffmpeg"
