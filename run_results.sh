#!/bin/bash

declare -a StringArray=(
'config_files/visual_clothing'
'config_files/visual_sports'
'config_files/visual_toys'
'config_files/visual_office'
'config_files/visual_beauty'
'config_files/textual_clothing'
'config_files/textual_sports'
'config_files/textual_toys'
'config_files/textual_office'
'config_files/textual_beauty'
'config_files/visual_textual_clothing'
'config_files/visual_textual_sports'
'config_files/visual_textual_toys'
'config_files/visual_textual_office'
'config_files/visual_textual_beauty'
)

for conf in "${StringArray[@]}"; do
  echo ${conf}
  python3.8 -u start_experiments.py --config ${conf}
done