# alldirs=`find . -type d -not -path './.git*'`

for d in **/*/; do
    zsh gen_index.sh "$d"
done
