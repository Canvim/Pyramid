
from pyramid.writing.ffmpeg_writer import FFMPEGWriter
from pyramid import *


with Timeline() as timeline:
    timeline.add(Animation(duration=7*1000))

    with CairoRenderer(timeline=timeline) as renderer:
        with FFMPEGWriter(total_frames=renderer.total_frames) as writer:
            renderer.render(writer)
