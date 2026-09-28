#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <errno.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <sys/ioctl.h>
struct ksu_get_info_cmd {
    uint32_t version;
    uint32_t flags;
    uint32_t features;
    uint32_t uapi_version;
};
int main(void) {
    int fd = -1;
    long rc = syscall(SYS_reboot, 0xDEADBEEF, 0xCAFEBABE, 0, &fd);
    printf("reboot-syscall rc=%ld fd=%d errno=%d\n", rc, fd, errno);
    if (fd < 0) return 13;
    struct ksu_get_info_cmd info;
    memset(&info, 0, sizeof(info));
    int ret = ioctl(fd, _IOR('K', 2, struct ksu_get_info_cmd), &info);
    int e = errno;
    printf("ioctl ret=%d errno=%d version=%u flags=0x%x features=0x%x uapi=%u\n",
           ret, e, info.version, info.flags, info.features, info.uapi_version);
    printf("su_compat=%s\n", (info.features & 1U) ? "ENABLED" : "MISSING");
    close(fd);
    return (ret == 0 && info.version && (info.flags & 1U) && (info.flags & 4U)) ? 0 : 14;
}
