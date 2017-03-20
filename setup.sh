#!/bin/bash
# setup.sh
# aoneill - 03/20/17

REPOS="repos"
RAFTOS="raftos"

function tell() { echo "$@"; $@; }

! [[ -d "$REPOS" ]] && tell mkdir $REPOS
! [[ -d "$REPOS/$RAFTOS" ]] \
  && tell git clone "https://github.com/zhebrak/raftos" "$REPOS/$RAFTOS"
! [[ -d "$RAFTOS" ]] \
  && tell cp -r "$REPOS/$RAFTOS/$RAFTOS" "$RAFTOS"
