# pythonmap
> web pentesting tool, easy to use for port scanning, ideal for CTF or quick use /// herramienta para pentesting web, de facil uso para el escaneo de puertos, ideal > para CTF o uso rapido

> Before starting you have to have nmap installed on your Windows operating system or on your Linux distribution or derivative

##  Nmap installation on Linux

to install nmap on linux run the following command at sudo level:

<code>sudo apt install nmap</code>

## Nmap installation on Windows
To install on windows mac or other operating system, go to the official nmap page and download the binaries corresponding to your system

https://nmap.org/download.html

## Setup

Before you start, install the requirements for the scanner.

<code>python -m pip install requirements.txt</code>

## Examples

To do a simple scan it is necessary to enter at least one port and one target IP address as in the following example:

<code>python .\pythonmap.py -p 22 43 80 8080 -t 127.0.0.1 -v</code>

Example for an exhaustive scan to all ports that are in open state

<code>python .\pythonmap.py --superscan --allports -t 127.0.0.1 -v --open</code>

**NOTE:** *In windows operating systems it is possible to delimit the port arguments with commas ',' however, in Unix-based systems the comma delimiters are taken as a string, which would cause an argument data type error, it is recommended to specify the arguments with spaces*

## Parameters

<code>-h --help</code> Help panel

<code>-v</code>Show Additional data in the output

<code>-p --port</code> Parameter to specify ports

<code>-t --targeted</code> Target ip address argument

<code>--allports</code> Scan all ports of the target machine from 0 to 65535

<code>--superscan</code> Super exhaustive port scan, very fast [ ! ] requires sudo permissions on linux

<code>--open</code> Only for scans of all ports, show only ports with open status
