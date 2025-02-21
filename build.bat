rmdir /s /q dist

python -m PyInstaller .\WheelOfStreams.py --onefile

rmdir /s /q build