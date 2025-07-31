import os
import subprocess

input_folder = "videos"
output_folder = "webp"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".mp4"):
        input_path = os.path.join(input_folder, filename)

        base_name = os.path.splitext(filename)[0]
        short_name = base_name[:3]
        output_name = f"{short_name}.webp"
        output_path = os.path.join(output_folder, output_name)

        cmd = [
            "ffmpeg",
            "-i", input_path,
            "-vf", "setpts=0.5*PTS,fps=10,scale=480:-1",
            "-loop", "0",
            "-an",
            "-vsync", "0",
            output_path
        ]

        print(f"⚡ Converting {filename} → {output_name} (2.5× speed)...")
        subprocess.run(cmd, check=True)

print("✅ All MP4s converted to WebP at 2.5× speed.")
