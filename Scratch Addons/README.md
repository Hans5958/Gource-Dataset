# Scratch Addons

## Links

- Video: 
	- Complete: [Evolution of Scratch Addons (July 2020–August 2023)](https://www.youtube.com/watch?v=Z6OxaLsCesM)
	- No localization files: [Evolution of Scratch Addons (no localization files) (July 2020–August 2023)](https://www.youtube.com/watch?v=5Zzfs0tQgfQ)
	- `addons/` only: [Evolution of Scratch Addons (addons/ only) (July 2020—July 2023)](https://www.youtube.com/watch?v=MwodbjCxPYc)
- Sources: 
	- https://github.com/ScratchAddons/ScratchAddons

## Command

```bash
/usr/bin/gource --load-config ./config/ScratchAddons__ScratchAddons.txt -3840x2160 -o - | ffmpeg -y -r 60 -f image2pipe -c:v ppm -i - -c:v libx264 -crf 18 -preset slow result.mp4
```