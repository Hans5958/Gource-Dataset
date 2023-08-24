# PreMiD (v1)

## Links

- Video: https://www.youtube.com/watch?v=Z6OxaLsCesM
- Sources: 
	- https://github.com/ScratchAddons/ScratchAddons

## Command

```bash
/usr/bin/gource --load-config ./config/ScratchAddons__ScratchAddons.txt -3840x2160 -o - | ffmpeg -y -r 60 -f image2pipe -c:v ppm -i - -c:v libx264 -crf 18 -preset slow result.mp4
```