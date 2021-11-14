#!/bin/bash

for f in `find docs -name '*.drawio'`; do
    pushd `dirname $f`
    b=`basename $f`
    drawio -x -o ${b%.drawio}.svg -t -b 0 $b
    popd
done
