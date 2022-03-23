#! /bin/bash

shopt -s globstar

for d in *;do
rename 's/&/and/g' **/*
done
