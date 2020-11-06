from .rendering.render_config import RenderConfig


# 16K, 60fps with supersampled framerate
BONKERS_RENDER_CONFIG = RenderConfig(
    fps=240,
    only_write_every=4,
    width=15360,
    height=8640,
)

# 4K, 60fps with supersampled framerate
UHD_RENDER_CONFIG = RenderConfig(
    fps=120,
    only_write_every=2,
    width=3840,
    height=2160,
)

# 1440p, 60fps
QHD_RENDER_CONFIG = RenderConfig(
    fps=60,
    width=2560,
    height=1440
)

# 1080p, 60fps
FULL_HD_RENDER_CONFIG = RenderConfig(
    fps=60,
    width=1920,
    height=1080
)

# 720p, 60fps
HD_RENDER_CONFIG = RenderConfig(
    fps=60,
    width=1280,
    height=720
)

# 720p, 30fps
HD_RENDER_CONFIG_HALF_FPS = RenderConfig(
    fps=30,
    width=1280,
    height=720
)

# 360p, 15fps
TOASTER_RENDER_CONFIG = RenderConfig(
    fps=15,
    width=640,
    height=360
)

DEFAULT_RENDER_CONFIG = HD_RENDER_CONFIG

FFMPEG_BINARY = "ffmpeg"
