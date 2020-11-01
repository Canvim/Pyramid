from .rendering.render_config import RenderConfig

HD_RENDER_CONFIG = RenderConfig(
    fps=60,
    width=1920,
    height=1080,
    extension="mp4"
)

FFMPEG_BINARY = "ffmpeg"