```sh
#!/bin/bash
set -e

# Build the game site
sh build.sh

# Serve themes and particles
sh serve_theme_particles.sh &

# Start the ultraviolet proxy
run_proxy.sh &

# Start the game site
sh start_proc.sh
```