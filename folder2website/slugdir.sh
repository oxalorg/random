for d in **/ **/*/ .; do
    d=`echo "$d" | sed 's|[ )(]|\\\&|g'`
    echo ./$d
done;
