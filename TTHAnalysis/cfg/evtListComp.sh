#!/bin/bash



if [[ "$#" -eq 0 ]]; then
echo "ERROR: the script needs at least two argument. Relaunch it with one of the following options:"
exit;
fi;

fileA="$1"
fileB="$2"

labelA="$3"
labelB="$4"

outputFolder="$5"



workingDir="$PWD"


if [ -d $outputFolder ]; then
    echo "output folder " $outputFolder " already exists. Exiting.."
    exit;
else
    mkdir $outputFolder;
fi


awk '{ print $4 " " $6 " "$8 }' $fileA > $outputFolder/listA.txt
awk '{ print $4 " " $6 " "$8 }' $fileB > $outputFolder/listB.txt





#diff -EbwB  <(sort $outputFolder/listA.txt) <(sort $outputFolder/listB.txt) > $outputFolder/diff.txt
diff -EbwB -y --suppress-common-lines   <(sort $outputFolder/listA.txt) <(sort $outputFolder/listB.txt) > $outputFolder/diff.txt

var1="<"
var2=">"

sed  "\%<% !d" "$outputFolder/diff.txt" >>  $outputFolder/diff_$labelA.txt
#sed  "\%<%  !d" "$outputFolder/diff.txt" >>  $outputFolder/diff_short.txt
sed  "\%>%  !d" "$outputFolder/diff.txt" >>  $outputFolder/diff_$labelB.txt
sed  "\%|%  !d" "$outputFolder/diff.txt" >>  $outputFolder/diff_between.txt

#sed "\%<% \%>%  !d" "$outputFolder/diff.txt" >>  $outputFolder/diff_short.txt

awk '{ print $1 }' $outputFolder/diff_between.txt > $outputFolder/eventList_diff.txt
awk '{ print $1 }' $outputFolder/diff_$labelA.txt > $outputFolder/eventList_onlyIn$labelA.txt
awk '{ print $2 }' $outputFolder/diff_$labelB.txt > $outputFolder/eventList_onlyIn$labelB.txt


awk '{ print $1 }' $outputFolder/diff_between.txt > $outputFolder/eventList_Total.txt
awk '{ print $1 }' $outputFolder/diff_$labelA.txt >> $outputFolder/eventList_Total.txt
awk '{ print $2 }' $outputFolder/diff_$labelB.txt >> $outputFolder/eventList_Total.txt


