# Mininet Setup

The experiments were reproduced using [Mininet 2.2.2 on Ubuntu 14.04 LTS - 64bit edition](https://github.com/mininet/mininet/releases/download/2.2.2/mininet-2.2.2-170321-ubuntu-14.04.4-server-amd64.zip). This was the [latest stable version](https://github.com/mininet/mininet/wiki/Mininet-VM-Images) on 8/17/2019.

## Converting to vhd format

This image comes in VMWare format and does not work with my Hyper-V environment. This [blog post](https://blogs.msdn.microsoft.com/timomta/2015/06/11/how-to-convert-a-vmware-vmdk-to-hyper-v-vhd/) points to an official tool for translating the disk format.

```powershell
Import-Module S:\tools\vmdk-to-vhd\MvmcCmdlet.psd1
ConvertTo-MvmcVirtualHardDisk -SourceLiteralPath S:\vhd\mininet-vm\mininet-vm-x86_64.vmdk -VhdType DynamicHardDisk -VhdFormat Vhdx -DestinationLiteralPath S:\vhd\mininet-vm\mininet-vm-x86_64.vhdx
```

## Login to image

The vhdx imported into Hyper-V (Windows 10 Version 1709 Build 16299.967) [using the default settings](https://blog.couchbase.com/hyper-v-run-ubuntu-linux-windows/).

Using 1 core and 2gb memory was slow on my laptop; this was increased to 8 cores and 4gb of memory.

```credentials
user: mininet
pass: mininet
```

## Start graphical display

```bash
sudo apt-get -y update
sudo apt-get -y install xinit lxde
startx
```

## Using MiniNet

The [WalkThrough](http://mininet.org/walkthrough/#part-1-everyday-mininet-usage) was followed step by step to understand the functionality.

## Installing VS Code

Using this [tutorial](https://linuxize.com/post/how-to-install-visual-studio-code-on-ubuntu-18-04/) installed vscode on the machine.
