#!/bin/bash

while true;
do
 case "$1"
 in
 mp.input) shift;INPUT=$1;;
 mp.output) shift;OUTPUT=$1;;
 vnf) shift;VNF=$1;;
 esac
 shift;
 if [ "$1" = "" ]; then
  break
 fi
done

echo "Input:"$INPUT
echo "Output:"$OUTPUT
echo "vnf:"$VNF
