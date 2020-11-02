from .rendering.render_config import RenderConfig


UHD_RENDER_CONFIG = RenderConfig(
    fps=60,
    width=2560,
    height=1440,
    extension="mp4"
)

FULL_HD_RENDER_CONFIG = RenderConfig(
    fps=60,
    width=1920,
    height=1080,
    extension="mp4"
)

HD_RENDER_CONFIG = RenderConfig(
    fps=60,
    width=1280,
    height=720,
    extension="mp4"
)

DEFAULT_RENDER_CONFIG = HD_RENDER_CONFIG

FFMPEG_BINARY = "ffmpeg"
