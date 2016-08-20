#!/bin/sh
path=${PWD}
export PROMPT_COMMAND="echo -ne \"\033]0;${path##*/}\007\""
