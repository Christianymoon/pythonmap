# pythonmap
web pentesting tool, easy to use for port scanning, ideal for CTF or quick use /// herramienta para pentesting web, de facil uso para el escaneo de puertos, ideal para CTF o uso rapido

Before you start, install the requirements for the scanner.

<code>python -m pip install requirements.txt</code>


## Examples

To do a simple scan it is necessary to enter at least one port and one target IP address as in the following example:

<code>python .\pythonmap.py -p 22, 43, 80, 8080 -t 127.0.0.1 -v</code>

Example for an exhaustive scan to all ports that are in open state

<code>python .\pythonmap.py --superscan --allports -t 127.0.0.1 -v --open</code>

## Parameters

<code>-h --help</code> Help panel

<code>-v</code>Show Additional data in the output

<code>-p --port</code> Parameter to specify ports

<code>-t --targeted</code> Target ip address argument

<code>--allports</code> Scan all ports of the target machine from 0 to 65535

<code>--superscan</code> Super exhaustive port scan, very fast [ ! ] requires sudo permissions on linux

<code>--open</code> Only for scans of all ports, show only ports with open status
