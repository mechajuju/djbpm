# DJBPM

DJBPM is a tool for DJs - it simplifies 3/4 loop transitions from a slower bpm to a faster bpm.  
This can be useful if you are transitioning from one genre to another (*e.g. from House to Drum and Bass*)

If you'd like to know how to perform the 3/4 loop transition technique, please reference this [Youtube video by DJ Carlo.](https://youtu.be/UUyqNDDdNn0)

## Installation

DJBPM is a portable application, meaning you do not need to install anything. 

Simply transfer the DJBPM.exe file to any Windows PC and run it to access the tool. 

If you'd prefer not to run an EXE file (or if you are not on Windows),  
install Python on your machine and run DJBPM.py instead.  
(I plan to make an executable for OS X available in the future, but currently I do not have access to a Mac.)
##
**Python 3 installation guide - only needed if you are not on Windows or prefer not to run the EXE file**

Links:

- [Python](https://python.org/) homepage
- [Python docs](https://docs.python.org/)


How to install:

- Debian/Ubuntu (for other Linux distros, see this [Gist](https://gist.github.com/MichaelCurrin/57d70f6aaba1b2b9f8a834ca5dd19a59)).
    1. Install using [apt-get](https://linux.die.net/man/8/apt-get).
        ```sh
        $ sudo apt-get update
        $ sudo apt-get install python3  # OR python3.12
        ```
    1. Recommended - install development extensions (C headers necessary for some packages) and `pip` (for installing packages globally).
        ```sh
        $ sudo apt-get install python3-dev python3-pip
        ```
- macOS
    1. Install [Brew](https://brew.sh). 
    1. Install Python using Brew:
        ```sh
        $ brew install python@3  # OR python@3.12
        ```
    1. Make your the Brew executables `bin` directory is in your `PATH` variable.
- Windows
    1. Download Python from the [Windows Download](https://www.python.org/downloads/windows/) page.
    1. Run the installer. Make sure to _check_ the box to have Python added to your `PATH` if the installer offers such an option (it's normally off by default).

For managing multiple versions of Python, you can use [pyenv](https://github.com/pyenv/pyenv) to install and switch between versions.

For more details and best practices, see this Gist - [Set up a Python 3 virtual environment](https://gist.github.com/MichaelCurrin/3a4d14ba1763b4d6a1884f56a01412b7).


## Usage
![Screenshot of DJBPM tool](https://i.imgur.com/zsa02l8.png)
Referencing the screenshot above, you will enter your current BPM in the 'Known BPM' box.   
You will get two outputs: a Start/Loop BPM and an End BPM.

**'Start/Loop' Example**   
*You want to transition to 168 BPM, but don't know what the starting BPM should be.*
1. You enter '168' into the Known BPM field.
2. Look only at Start/Loop BPM - the result is 126.0
3. In this case, you will set your starting track to 126BPM, create a 3/4 loop, and end up at 168 BPM.

**'End' Example** (pictured in the screenshot above)   
*You're starting at 130 BPM. You need to know what the resulting BPM will be after your 3/4 loop has been made.* 
1. You enter '130' into the Known BPM field
3. Look only at End BPM - the result is 173.33
4. In this case, you are transitioning from a track at 130 BPM to another track at 173.33 BPM. 

I opted to display two decimal places for those that prefer to be hyper-precise, but feel free to round (*i.e. 173 BPM instead of 173.33 BPM*)


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)
