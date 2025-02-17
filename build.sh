```
#!/bin/bash

set -e

# Install Python dependencies
pip3 install -r python_requirements.txt

# Install Node.js dependencies
npm install kahoot.js-latest
npm install ultraviolet
npm install --save-dev gulp
npm install --save-dev gulp-sass
npm install --save-dev gulp-autoprefixer
npm install --save-dev gulp-minify-css
npm install --save-dev gulp-uglify
npm install --save-dev gulp-imagemin
npm install --save-dev gulp-rename
npm install --save-dev gulp-concat
npm install --save-dev gulp-sourcemaps

# Build the game site
gulp build
```