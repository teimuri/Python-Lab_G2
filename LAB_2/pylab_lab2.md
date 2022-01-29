# Pylab Lab 2 Report

## Bash Shell-Scripting

### 1-1

```bash
#! /bin/bash

filename="resolv.conf"
cd /etc
sudo sed -i "s/nameserver *.*/nameserver 185.51.200.2/" $filename
```

`chmod +x script1.sh`

### 1-2

#### 1

`@taha`

#### 2

[Code](D://education//pylab//Lab2//bfs.py)

#### 3

Script file: `script_bsscr_3.sh`

To make it more easy: `chmod +x script_bsscr_3.sh`

## SSH

### 2-1

`sudo service ssh status`

Login: `ssh mmaharebi@192.168.159.38`

Install Posh-SSH: `Instal-Module Posh-SSH -Scope CurrentUser`

As admin:

`Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted`

Import Posh-SSH: `Import-Module Posh-SSH`

Check if imported: `Get-Command -Module Posh-SSH`

Download file:

`Get-SCPItem -ComputerName 192.168.159.38 -Credential mmaharebi -Path "/home/mmaharebi/Desktop/note1.txt" -PathType File -Destination ./ -Verbose`

After changing file upload it using this command:

`Set-SCPItem -ComputerName 192.168.159.38 -Credential mmaharebi -Path "~\note1.txt" -Destination /home/mmaharebi/Desktop -Verbose`

### 2-2

Some stuff.
