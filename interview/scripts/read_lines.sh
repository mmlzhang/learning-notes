

IFS=$'\n'


echo "method 1"


echo "method 2"
cat $1| while read line2
do
    echo $line2
done

echo "method 3"

for line3 in $(<$0)
do
    echo $line3
done
