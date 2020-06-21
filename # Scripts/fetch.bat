@echo off

cd clone
pushd .
for /d %%i in (*) do call :$DoSomething "%%i"
popd

cd ..
pause
exit /B

:$DoSomething

cd %1
"../../fetch.py"
cd ..

exit /B