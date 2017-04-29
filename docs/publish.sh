#!/bin/sh

GIT="/usr/bin/env git"
CURRENT=`$GIT symbolic-ref --short -q HEAD`
PAGES="gh-pages"
HTML="_build/html"
FORMATS="html"

make $FORMATS && \
    $GIT checkout $PAGES && \
    cp -r $HTML/* . && \
    find . -type f -exec sed -i 's/_static/static/g' {} \; && \
    find . -type f -exec sed -i 's/_source/source/g' {} \; && \
    find . -type f -exec sed -i 's/_images/images/g' {} \; && \
    rm -rf static && mv _static static && \
    rm -rf sources && mv _sources sources && \
    rm -rf images && mv _images images && \
    rm -rf _* && \
    $GIT add . --all && \
    $GIT commit -a -m "Update content for GH pages." && \
    $GIT push origin +$PAGES;

$GIT checkout $CURRENT
