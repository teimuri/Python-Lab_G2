# **Lab1**

## 1-1

- NAT:

  With NAT, **a virtual machine does not have its own IP address on the external network**. Instead, **a separate private network** is set up **on the host system**. In the **default** configuration, a virtual machine **gets an address on this private network from the virtual DHCP server**. The **virtual machine and the host system share a single network identity that is not visible on the external network**.

  When you install Workstation on a Windows or Linux host system, a NAT network (**VMnet8**) is set up for you. When you use the New Virtual Machine wizard to create a new virtual machine and select the typical configuration type, the wizard configures the virtual machine to use the default NAT network. You can have **only one NAT network**.

- Bridged:
  
  Bridged networking connects a virtual machine to a network **by using the network adapter on the host system**. If the **host system is on a network**, bridged networking is often the **easiest way to give the virtual machine access to that network**. When you install Workstation on a Windows or Linux host system, a bridged network (**VMnet0**) is set up for you.

- Host-Only
  
  Host-only networking **creates a network that is completely contained within the host computer**. Host-only networking provides **a network connection between the virtual machine and the host system** by using a **virtual network adapter** that is **visible on the host operating system**. When you install Workstation on a Windows or Linux host system, a host-only network (**VMnet1**) is set up for you.

## 3-1

Install `fortune`: `sudo apt install fortune`

Check if `fortune` is installed: `apt list --installed` or `fortune --version`

Run fortune: `fortune -a` or `fortune -c`

Remove `fortune`: `sudo apt remove fortune`

## 3-2

Create folders named A and B in home directory: `mkdir A && mkdir B`

Change directory to `~/A`: `cd A`

Change directory to `~/B`: `cd ../B`

Create a file named 'test.txt' in directory A: `touch ../A/test.txt && cp ../A/test.txt .`

Move 'test.txt' from B/ to Desktop: `mv ../A/test.txt ../Desktop`

Remove `~/B` directory and all of its subfolders and files: `cd ~ && rm -r B`

## 3-3

Change directory to `/etc/`: `cd /etc/`

Show full-detailed list of directories and files: `ls -la`

Most used flags for `ls` cmd: `-l -la -a -A --author`

## 3-4

Install `tree`: `sudo apt install tree`

Command: `tree -d -L 2 /etc`

## 3-5: main

Copy and rename `sqspell.php` to `sqspell.jpg`: `cp sqspell.php sqspell.jpg`

Check both for real type: `file sqspell.php sqspell.jpg`

## 3-5: extra

Just use it.

## 4-1

Create new user with `user96103722` as username: `sudo adduser user96103722`

Give permission to `user96103722`: `sudo EDITOR=nano visudo` and fill all three sections as sample

Kill all `user`'s processes: `sudo killall -u user`

Remove `user`: `sudo userdel -r user`

## 5-1

Get the `firefox`' version: `dpkg -l | grep "firefox"`

## 5-2

`find *.c *.py`

## 5-3

1. If whitespace matters: `cat GPL-1 | grep "^GNU"`

   else: `cat GPL-1 | tr -d " " | grep "^GNU"`
2. `cat GPL-1 | grep "cept"`
3. ???

## 5-4

`cat GPL-1 | grep -v "###"`

## 6-1

`top -o VIRT`

## 6-2

`kill $(ps aux | grep "firefox -new-window$" | cut -d " " -f 5)`

## 6-3

`cat /proc/devices > out.txt 2>> out.txt && cat /proc/cpuinfo > out.txt 2>> out.txt`

## 6-4

Run in background: `ping sharif.ir > log.txt 2>> log.txt &`

See what's running in background: `jobs`

Get the pid: `ps aux | grep "ping"`

stop pinging: `kill <pid>`

## 7-1

`set number` & 'set autoindent'

## 7-2

1. `:set number`, press ENTER, `/GNU`. Press N to goto the next match, press ESCAPE to end.
2. `:set number`, press ENTER, `/cept`. Press N to goto the next match, press ESCAPE to end.
3. `/(`, press ENTER. Use `%` to find the end ). Press N to goto the next match, press ESCAPE to end.

## 7-3

Use `q` to save a bunch of commands by running them. assign `@W` to them at the end. Reuse by `@W`.

## 7-3 tmux

`CTRL-B-%`: Add vertical pane

`CTRL-B-"`: Add horizental pane

`CTRL-B-t`: Show time in pane