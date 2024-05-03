import PyInstaller.__main__

#/usr/bin/python3.9

PyInstaller.__main__.run([
    'frontend.py',  # Your main Python application file
    '--onefile',       # Bundles everything in a single executable
    '--windowed',      # Prevents a command prompt window from appearing (optional)
    '--icon=icon.ico', # Path to an icon file (optional)
    '--name=D2_WebScrapingApp' # Name of the generated executable
])