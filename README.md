pyVistA
=======

A Python package for invoking VistA RPCs through the new style RPC Broker and RPMS RPCs through the CIA Broker. Invocation can be from self-contained Python clients or web-hosted (WSGI) services. 

By way of comparison, this provides for Python some of what MDWS provides for C#, Vistalink/OVID provides for Java and EWD provides for MUMPS.

FYI: the other way to access VistA remotely from Python is using the (ill-named?) <a href="https://github.com/OSEHRA/OSEHRA-Automated-Testing/blob/master/lib/vista/OSEHRAHelper.py">OSEHRAHelper.py</a>, now in the bowels of the VistA testing framework. This module let's you login and invoke VistA options only available through its roll and scroll - remember, RPCs only take you so far with VistA.
