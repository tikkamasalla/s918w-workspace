#!/bin/sh
set -u
grep -n "kdp_usecount_dec_and_test_t)(struct cred\|KERNEL_VERSION(5, 11\|inc_rlimit_ucounts_t\|dec_rlimit_ucounts_t\|samsung_kdp_commit_work {" /root/KernelSU-dm3q/kernel/compat/samsung_kdp.c | head -12
