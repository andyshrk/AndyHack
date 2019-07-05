#!/bin/sh
name=$1
export PROMPT_COMMAND="echo -ne \"\033]0;${name##*/}\007\""
PS1=$
