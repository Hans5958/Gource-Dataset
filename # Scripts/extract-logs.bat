git pull
for %%I in (.) do set name=%%~nxI
gource --output-custom-log "../../%name%.txt"