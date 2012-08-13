Description
===========

Infrastructure for building higher-performance (yes, hardware float, among other things) Fedora on Raspberry Pi hardware.

Very RedHat-land specific, so don't bother looking into here if you want help porting OpenDebuntuArchMediaCenter applications.

Ultimately this project will create a high performance raspberry-pi Fedora remix, but I use 'remix' lightly; idealogically, the only changes against Fedora ARM will be changes very specifically for the Raspberry pi architecture (i.e. binary blobs, extra modules, compile options); package requests will be directed upstream for all other needs.

Instructions
============

Not really, here are some example commands you'll want to use:

    git submodule init / git submodule update

    ./yum-packagelist.py base core