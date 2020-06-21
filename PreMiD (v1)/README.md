# PreMiD (v1)

## Links

- Video: https://www.youtube.com/watch?v=O1cRPI_hqug
- Sources: 
	- https://github.com/PreMiD/PreMiD
	- https://github.com/PreMiD/Presences
	- https://github.com/PreMiD/Discord-Bot
	- https://github.com/PreMiD/Extension
	- https://github.com/PreMiD/Website
	- https://github.com/PreMiD/Localization
	- https://github.com/PreMiD/Linux
	- https://github.com/PreMiD/API
	- https://github.com/PreMiD/Updaters
	- https://github.com/PreMiD/Docs (now defunct, present at the time of data collection)
	- https://github.com/PreMiD/Wiki (now defunct, present at the time of data collection)
	- https://github.com/doomlerd/PreMiD-Linux (now redirected, replacing PreMiD/Linux at the time of data collection)

## Command

```batch
gource "Log/Processed.txt" ^
	-s 0.5 ^
	--caption-file "Log/Captions.txt" ^
	--user-image-dir Avatar ^
	--hide filenames,mouse,progress ^
	--auto-skip-seconds .001 ^
	--bloom-multiplier 0.75 ^
	--bloom-intensity 0.5 ^
	-2560x1440 ^
	--background-colour 000000 ^
	--title "PreMiD (all repository)" ^
	--font-size 30 ^
	-r 60 ^
	-o ^
	- ^
| "%programfiles%/Shotcut/ffmpeg.exe" ^
	-y ^
	-r 60 ^
	-f image2pipe ^
	-vcodec ppm ^
	-i ^
	- ^
	-vcodec libx264 ^
	-preset faster ^
	-pix_fmt yuv420p ^
	-crf 1 ^
	-threads 0 ^
	-bf 0 gource.mp4
```