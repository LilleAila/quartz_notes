for file in Notes/*
do
  birth_date=$(date -d @"$(stat -c %W "$file")" +"%Y%m%dT%H%M")
  filename=$(basename "$file")
  new_name="$birth_date-$filename"
  echo "${new_name%.*}"
done
