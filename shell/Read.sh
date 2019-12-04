#!/bin/bash
UBOOT_TARGET_MAP="BL31=cache/sources/arm-trusted-firmware/v2.2/build/rk3399/release/bl31/bl31.elf idbloader.img u-boot.itb;;idbloader.img u-boot.itb"

while read -r target; do
	echo "target: ${target}"
	target_make=$(cut -d';' -f1 <<< $target)
	target_patchdir=$(cut -d';' -f2 <<< $target)
	target_files=$(cut -d';' -f3 <<< $target)
	echo "make: $target_make"
	echo "patchdir: $target_patchdir"
	echo "files: $target_files"
done <<< "$UBOOT_TARGET_MAP"
