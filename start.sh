```sh
#!/bin/bash
set -e

# clean up process
killall -9 python3
killall -9 node

# (re)build web application
sh build.sh

# start web application
python3 webapp.py

```