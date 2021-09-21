inputfile="char_freq_merged.txt"
dictfile="source_data/moetaigi-raw.dict.yaml"
new_dictfile="moetaigi.dict.yaml"

cut -d $'\t' -f 1,2 $dictfile > $new_dictfile
while IFS= read -r line
do
    c=$(echo $line | cut -d " " -f 2)
    n=$(echo $line | cut -d " " -f 4)
    # echo $c
    d=$(grep -P "^$c\t" $new_dictfile | head -n 1)
    # echo $d # | sed 's/^.//g'
    # echo $d
    # echo "----"
    if [ ! -z "$d" ]
    then
        d1=$(echo $d | cut -d " " -f 1)
        d2=$(echo $d | cut -d " " -f 2)
        dnew=$(echo -e "$d1\t$d2\t$n")
        sed -i "s/$d/$dnew/g" $new_dictfile
        # while IFS= read -r line2
        # do
            # d1=$(echo $line2 | cut -d " " -f 1)
            # d2=$(echo $line2 | cut -d " " -f 2)
            # dnew=$(echo -e "$d1\t$d2\t$n")
            # echo $line2
            # echo $dnew
            # sed -i "s/$line2/$dnew/g" $new_dictfile
            # echo '##########'
            # echo $dnew
            # echo "\$d is NOT empty"
        # done < <(echo $d)
    fi
    # take some action on $line
    # echo "$c $n"
done < <(tac $inputfile)