#!/bin/sh
set -u
pahole -C page /root/gate/gate-dwarf.o 2>/dev/null | grep -n "compound_head\|slab_cache\|page_type"
