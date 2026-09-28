#!/bin/sh
set -u
echo "===== rt_mutex_waiter"
pahole -C rt_mutex_waiter /root/gate/gate-dwarf.o 2>/dev/null
echo "===== file_operations (head -30)"
pahole -C file_operations /root/gate/gate-dwarf.o 2>/dev/null | head -30
echo "===== mm_struct (head -12 + tail -6)"
pahole -C mm_struct /root/gate/gate-dwarf.o 2>/dev/null | head -12
pahole -C mm_struct /root/gate/gate-dwarf.o 2>/dev/null | tail -6
