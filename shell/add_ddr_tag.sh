#!/bin/sh
TAG=$1
TARGET=$2
echo "add tag "$TAG" on the head of ${TARGET}"
sed -i "/^/{1s/^/${TAG}/}" ${TARGET} 
