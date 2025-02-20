```sh
#!/bin/bash
set -e

# Build the game site
sh build.sh

# Serve themes and particles
sh serve_theme_particles.sh &

# Start the ultraviolet proxy with custom config
run_proxy.sh -c ultraviolet_custom_config.yml &

# Start game card service
sh start_card_service.sh &

# Start sidebar service
sh start_sidebar_service.sh &

# Start the game site
sh start_proc.sh
```