#!/bin/bash

declare -a StringArray=(
'visual_clothing'
'visual_sports'
'visual_toys'
'visual_office'
'visual_beauty'
'textual_clothing'
'textual_sports'
'textual_toys'
'textual_office'
'textual_beauty'
'visual_textual_clothing'
'visual_textual_sports'
'visual_textual_toys'
'visual_textual_office'
'visual_textual_beauty'
)

for conf in "${StringArray[@]}"; do
  echo ${conf}
  python3.8 -u start_experiments.py --config ${conf}
done