#!/bin/bash

# Store current directory being run in
curdir="$@"
pushd `pwd` > /dev/null
cd $curdir

# Create temporary file later to be overwritten to index.md
tempfile=/tmp/gen_index.md

cat << EOF > $tempfile
---
title: Index of /notes/$curdir
---

## Collections

EOF

setopt null_glob
# Find all directories in the current folder
# Sort them alphabetically
# and append into 'index.md'
for d in */ ; do
    dname=`basename $d`
    if [[ $dname == 'res' ]]; then
        continue
    fi
    echo "* [$dname]($dname)" >> $tempfile
done

cat << EOF >> $tempfile

## Posts

EOF

# Find all .md files in the the current folder
# Sort them based on modification time
# and append into 'index.md'
for f in *.md ; do
    if [[ $f == "index.md" ]]; then
        continue
    fi
    fname=${f%.md}
    echo "* [$fname]($fname.html)" >> $tempfile
done

cat $tempfile > index.md
echo "Index written to `pwd`/index.md"

# Pop out back to original directory
popd > /dev/null
