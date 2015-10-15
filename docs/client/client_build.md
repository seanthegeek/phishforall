# Client Build

Phish for All is designed to be cross-platform, and runs with no external dependencies. As a result, 
its build environment is somewhat complex.The system you build the client on must be the same 
platform that you are targeting. You need a separate client build for each platform that
you are targeting.

## Build environment setup

### Mac OS 10.6+

[Install MacPorts](https://www.macports.org/install.php)

    $ sudo port install py35-pip openssl
    $ cd phishforall/client
    $ sudo pip-3.5 install -r requires-py35.txt
    
### Debian/Ubuntu Linux

    $ sudo apt-get install python3-pip python3-dev libssl-dev
    $ cd phishforall/client
    $ sudo pip-3.5 install -r requires-py3.txt
    
## Other Linux/UNIX distributions
 
It might work

Ensure Python 3, the Python 3 development headers, pip, and the openssl library are installed, then:

    $ cd phishforall/client=

    $ sudo pip-3.5 install -r requires-py35.txt

If you are using Python 3.5. Or, if you are using an older version of Python 3: 

    $ sudo pip-3.5 install -r requires-py3.txt

    
### Windows

**Warning**: pyinstaller, which is used to build the client, is currently incompatible with Windows 10.
The build will still succeed, but the resulting EXE will not run an any older Windows version,
unless the 
[Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/en-us/download/details.aspx?id=48145)
has been installed on the system, which is unlikely. Clients built with older versions of Windows will run on 
Windows 10. For the latest details, see 
[pyinstaller issue # 1566](https://github.com/pyinstaller/pyinstaller/issues/1566).

Windows 7 or 8.1 is required

[Visual Studio 2015](https://www.visualstudio.com/e) is required. The free community addition will work. 
*Be sure to select custom install in the installer*

Make sure the following are checked, along with the defeats:

- Visual C++ tools
- Python tools
- Windows SDK

Install [Python 3.5](https://www.python.org/) 32-bit, **Even if you use a 64 bit OS**. This will ensure that you will 
build 32 bit EXEs, which will run on 32 bit and 64 bit Windows. 

**Again, be sure to select a custom install**

Ensure the following are set along with the defaults:

- Install for all users
- Add python to the PATH enticement variables
- Visual Studio integration
- Debugging symbols
- Change the install path to `C:\Python35` **pyinstaller will fail if you use the default because it has spaces!**

Open Power Shell as administrator. Run:
 
     cd phishforall/client
     pip install -r requires-py35.txt

## Building the client

    cd phishforall/client
    ./builder.py

Your build will be located in the `dist` directory.
