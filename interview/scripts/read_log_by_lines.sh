
echo "method 1 \n"
cat ./data/test.log | while read line
do
    echo "File: ${line}"
done

echo "\n method 2 \n"
while read line
do
    echo "File: ${line}"
done < ./data/test.log

echo "\n method 3　user awk read lines \n"
cat ./data/test.log | awk '{print $0}'


