#!/bin/bash

KEY='s3k@1_v3ry_w0w'
TESTSTRING='20762001782445454615001000284b41193243004e41000b2d0542052c0b1932432d0441000b2d05422852124a1f096b4e000f'

Asc() { printf '%d' "'$1"; }
HexToDec() { printf '%d' "0x$1"; }

XORDecrypt() {

    local key="$1" DataIn="$2"
    local ptr DataOut val1 val2 val3

    local ptrs
    ptrs=0

    for (( ptr=0; ptr < ${#DataIn}/2; ptr++ )); do

        val1="$( HexToDec "${DataIn:$ptrs:2}" )"
        val2=$( Asc "${key:$(( ptr % ${#key} )):1}" )

        val3=$(( val1 ^ val2 ))

        ptrs=$((ptrs+2))

        DataOut+=$( printf \\$(printf "%o" "$val3") )

    done
    printf '%s' "$DataOut"
}

XORDecrypt $KEY $TESTSTRING #| base64 -D

