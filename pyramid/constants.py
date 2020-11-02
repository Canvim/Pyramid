from .rendering.render_config import RenderConfig


UHD_RENDER_CONFIG = RenderConfig(
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
