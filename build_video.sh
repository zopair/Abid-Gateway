#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
mkdir -p media
cat > slides.txt <<'EOF'
file 'frames/scene_00.png'
duration 3
file 'frames/scene_01.png'
duration 3
file 'frames/scene_02.png'
duration 3
file 'frames/scene_03.png'
duration 3
file 'frames/scene_04.png'
duration 3
file 'frames/scene_04.png'
EOF
ffmpeg -hide_banner -loglevel error -y -f concat -safe 0 -i slides.txt \
  -vf "scale=640:360,fps=12,format=yuv420p,fade=t=in:st=0:d=0.35,fade=t=out:st=14.4:d=0.55" \
  -c:v libx264 -preset ultrafast -crf 33 -movflags +faststart -an \
  media/insta-freelancer-demo.mp4
