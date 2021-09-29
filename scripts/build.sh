#!/usr/bin/env bash
set -e

SRCS="simpleaccess"

[ -d $SRCS ] || (echo "Run this script from project root"; exit 1)

set -x

python -m build .