```sh
#!/bin/bash
set -e

# Build the game site
sh build.sh

# Start the game site
sh start_proc.sh

# Start the ultraviolet proxy
run_proxy.sh

```