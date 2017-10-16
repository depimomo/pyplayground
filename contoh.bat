start=$PWD
for directory in *; do
  cd "$directory"
  for filename in *; do
    echo "$filename" ../1_1017_full/"$directory_$filename"
  done
  cd "$start"
done

#!/bin/bash
for num in 0???; do
  pushd "$num"
  for file in *; do
    mv "$file" "${num}_${file:5:9}"
  done
  popd
done

find 501-750 -type f -name "*[3-4].jpg" | xargs -i cp {} 1_1017_full

find 1_475_new -type f -name "*[1-2].jpg" #-delete

zip -F "Handwriting Dataset_pages_train_test_color.zip" --out "hopely_fixed.zip"

DATANYA:
CEWEK 530
COWOK 487
