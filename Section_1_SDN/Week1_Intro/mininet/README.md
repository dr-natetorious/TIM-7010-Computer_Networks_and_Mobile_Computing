# Mininet Virtual Networking Utility

The mininet, or mn, is a utility for creating software defined networks. It does not require any fancy hardware and can run on a laptop.

The authors of the tool created a [walkthrough](http://mininet.org/walkthrough/#part-1-everyday-mininet-usage) to cover common scenarios.

For convienence a cached copy of the walkthrough can be found under this weeks [reading section](../Readings/Mininet_Walkthrough.pdf).

## Configuring the environment

To complete the walkthrough requires a GUI and [setting up vnc](https://linoxide.com/debian/configure-vnc-server-debian-9-stretch/) exceeded my patience.

The VNC guide is fairly straight forward but its becoming tedious to [automate within docker image](Dockerfile) (another day perhaps).

Instead a virtual machine was created using [debian-9.9.0 netinst](https://saimei.ftp.acc.umu.se/debian-cd/current/amd64/iso-cd/debian-9.9.0-amd64-netinst.iso); the latest stable build.

