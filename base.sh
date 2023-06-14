#!/bin/bash
echo "Read file path"
echo $file
read file
key=$file
shasum -a 256 $file | cut -f1 -d\ | xxd -r -p | base64
python CheckSumvalue.py

