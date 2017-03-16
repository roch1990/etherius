# etherius
A small packet for some GNSS calculation and automatisation.

To start - run "__init__.py"

./cfg      - path for configurations file and get/set configuration script
./sh       - path for initial bash scripts
./src/deph - path for ephemeris downloading

h3.Command line specification

All commands consist of prefix, command type, method, value and key

List of prefix:
- config

List of command types:
- etherius
- glonass
- gps

List of methods:
- get
- set (available only for configuration files)
 
List of value:
- cfg file sections

List of key:
- cfg file keys