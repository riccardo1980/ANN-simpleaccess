#!/usr/bin/env bash
set -e

SRCS="simpleaccess"
DATA="data"
RESOURCE=${1-""}

declare -A RESOURCE_MAP
RESOURCE_MAP["googlenews"]="https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz"

[ -d $SRCS ] || (echo "Run this script from project root"; exit 1)
[ ! -z "$RESOURCE" ] || (echo "Most specify a resource"; exit 1)
[ -v "RESOURCE_MAP[$RESOURCE]" ] || (echo "Resource $RESOURCE is not supported"; exit 1)


set -x

wget -c ${RESOURCE_MAP[$RESOURCE]} -P $DATA