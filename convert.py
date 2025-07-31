from ffmpeg import FFmpeg
ffmpeg = (
    FFmpeg()
    .input('./001.mp4')  # convert first 5 seconds
    .output('output.webp', vf='scale=480:-1', loop=0)
)
ffmpeg.execute()