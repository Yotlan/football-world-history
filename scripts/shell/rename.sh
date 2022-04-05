#! /bin/bash

shopt -s globstar

for d in *;do
rename 's/&/and/g' ../../csv/*/*/*/equipes/**/*
done
