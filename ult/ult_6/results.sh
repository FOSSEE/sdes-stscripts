#!/bin/bash
mkdir ~/marks
cut -d " " -f 2- marks1.txt | paste -d " " students.txt - | sort > ~/marks/results.txt
