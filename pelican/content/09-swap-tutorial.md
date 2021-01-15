penserbjorne@painkiller-legion:~$ free -m
              total       usado       libre  compartido búfer/caché  disponible
Memoria:       31959       11234       16217         162        4507       20101
Swap:          4095           0        4095
penserbjorne@painkiller-legion:~$ dh -f
dh: error: "debian/control" not found. Are you sure you are in the correct directory?
penserbjorne@painkiller-legion:~$ dh -h
Usage: dh [options]

  dh is a part of debhelper. See debhelper(7)
  and dh(1) for complete usage instructions.
penserbjorne@painkiller-legion:~$ df -h
S.ficheros            Tamaño Usados  Disp Uso% Montado en
udev                     16G      0   16G   0% /dev
tmpfs                   3.2G   2.2M  3.2G   1% /run
/dev/mapper/data-root   930G    26G  857G   3% /
tmpfs                    16G   147M   16G   1% /dev/shm
tmpfs                   5.0M      0  5.0M   0% /run/lock
tmpfs                    16G      0   16G   0% /sys/fs/cgroup
/dev/nvme0n1p2          4.0G   2.4G  1.7G  60% /recovery
/dev/nvme0n1p1          498M   187M  311M  38% /boot/efi
tmpfs                   3.2G    20K  3.2G   1% /run/user/110
/dev/dm-3               916G   348G  523G  40% /mnt/extra
tmpfs                   3.2G    44K  3.2G   1% /run/user/1000
penserbjorne@painkiller-legion:~$ cat /sys/power/state 
freeze mem disk
penserbjorne@painkiller-legion:~$ free -h
              total       usado       libre  compartido búfer/caché  disponible
Memoria:        31Gi        10Gi        16Gi       128Mi       4.4Gi        20Gi
Swap:         4.0Gi          0B       4.0Gi
penserbjorne@painkiller-legion:~$ cat /etc/re
request-key.conf  request-key.d/    resolv.conf       resolvconf/       
penserbjorne@painkiller-legion:~$ cat /etc/os-release
os-release           os-release.diverted  
penserbjorne@painkiller-legion:~$ cat /etc/os-release
NAME="Pop!_OS"
VERSION="20.04 LTS"
ID=pop
ID_LIKE="ubuntu debian"
PRETTY_NAME="Pop!_OS 20.04 LTS"
VERSION_ID="20.04"
HOME_URL="https://pop.system76.com"
SUPPORT_URL="https://support.system76.com"
BUG_REPORT_URL="https://github.com/pop-os/pop/issues"
PRIVACY_POLICY_URL="https://system76.com/privacy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
LOGO=distributor-logo-pop-os
penserbjorne@painkiller-legion:~$ ls /
bin   dev  home  lib32  libx32      media  opt   recovery  run   srv  tmp  var
boot  etc  lib   lib64  lost+found  mnt    proc  root      sbin  sys  usr
penserbjorne@painkiller-legion:~$ cat /sys/power/state 
freeze mem disk
penserbjorne@painkiller-legion:~$ free -h
              total       usado       libre  compartido búfer/caché  disponible
Memoria:        31Gi       8.5Gi        15Gi       472Mi       7.3Gi        21Gi
Swap:         4.0Gi          0B       4.0Gi
penserbjorne@painkiller-legion:~$ sudo fallocate -l 32G /swapfile
[sudo] contraseña para penserbjorne: 
penserbjorne@painkiller-legion:~$ ls /
bin   dev  home  lib32  libx32      media  opt   recovery  run   srv       sys  usr
boot  etc  lib   lib64  lost+found  mnt    proc  root      sbin  swapfile  tmp  var
penserbjorne@painkiller-legion:~$ ls -lah /
total 33G
drwxr-xr-x  19 root root 4.0K sep 28 15:23 .
drwxr-xr-x  19 root root 4.0K sep 28 15:23 ..
lrwxrwxrwx   1 root root    7 abr  3 09:00 bin -> usr/bin
drwxr-xr-x   3 root root 4.0K sep 23 21:25 boot
drwxr-xr-x  23 root root 4.7K sep 28 10:21 dev
drwxr-xr-x 149 root root  12K sep 25 14:46 etc
drwxr-xr-x   3 root root 4.0K ago 28 12:21 home
lrwxrwxrwx   1 root root    7 abr  3 09:00 lib -> usr/lib
lrwxrwxrwx   1 root root    9 abr  3 09:00 lib32 -> usr/lib32
lrwxrwxrwx   1 root root    9 abr  3 09:00 lib64 -> usr/lib64
lrwxrwxrwx   1 root root   10 abr  3 09:00 libx32 -> usr/libx32
drwx------   2 root root  16K ago 28 12:13 lost+found
drwxr-xr-x   3 root root 4.0K sep 16 13:38 media
drwxr-xr-x   3 root root 4.0K ago 28 14:04 mnt
drwxr-xr-x   5 root root 4.0K ago 31 14:10 opt
dr-xr-xr-x 359 root root    0 sep 28 06:58 proc
drwx------   6 root root 4.0K dic 31  1969 recovery
drwx------   8 root root 4.0K sep  9 14:54 root
drwxr-xr-x  36 root root 1000 sep 28 12:25 run
lrwxrwxrwx   1 root root    8 abr  3 09:00 sbin -> usr/sbin
drwxr-xr-x   2 root root 4.0K abr  3 09:00 srv
-rw-r--r--   1 root root  32G sep 28 15:23 swapfile
dr-xr-xr-x  13 root root    0 sep 28 06:58 sys
drwxrwxrwt  27 root root 4.0K sep 28 15:22 tmp
drwxr-xr-x  14 root root 4.0K ago 25 08:52 usr
drwxr-xr-x  13 root root 4.0K ago 25 09:06 var
penserbjorne@painkiller-legion:~$ dh -f
dh: error: "debian/control" not found. Are you sure you are in the correct directory?
penserbjorne@painkiller-legion:~$ df -h
S.ficheros            Tamaño Usados  Disp Uso% Montado en
udev                     16G      0   16G   0% /dev
tmpfs                   3.2G   2.2M  3.2G   1% /run
/dev/mapper/data-root   930G    58G  825G   7% /
tmpfs                    16G   457M   16G   3% /dev/shm
tmpfs                   5.0M      0  5.0M   0% /run/lock
tmpfs                    16G      0   16G   0% /sys/fs/cgroup
/dev/nvme0n1p2          4.0G   2.4G  1.7G  60% /recovery
/dev/nvme0n1p1          498M   187M  311M  38% /boot/efi
tmpfs                   3.2G    20K  3.2G   1% /run/user/110
/dev/dm-3               916G   349G  521G  41% /mnt/extra
tmpfs                   3.2G    56K  3.2G   1% /run/user/1000
penserbjorne@painkiller-legion:~$ sudo chmod 600 /swapfile 
penserbjorne@painkiller-legion:~$ sudo mkswap /swapfile 
Configurando espacio de intercambio versión 1, tamaño = 32 GiB (34359734272 bytes)
sin etiqueta, UUID=483dc828-81d7-4f85-a688-830c1fb0709c
penserbjorne@painkiller-legion:~$ sudo swapo
swapoff  swapon   
penserbjorne@painkiller-legion:~$ sudo swapon /swapfile
penserbjorne@painkiller-legion:~$ echo '/swapfile none swap defaults 0 0' | sudo tee -a /etc/fstab 
/swapfile none swap defaults 0 0
penserbjorne@painkiller-legion:~$ cat /etc/fstab 
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system>  <mount point>  <type>  <options>  <dump>  <pass>
PARTUUID=df006535-2b8a-4a72-bfee-995d5bd71112  /boot/efi  vfat  umask=0077  0  0
PARTUUID=31c0f49b-a13e-49be-a80b-25f4656eab80  /recovery  vfat  umask=0077  0  0
/dev/mapper/cryptswap  none  swap  defaults  0  0
UUID=e02e2e5a-ed6b-4a98-b4db-93a5940a4a85  /  ext4  noatime,errors=remount-ro  0  0
LABEL=extra /mnt/extra auto nosuid,nodev,nofail,x-gvfs-show,x-gvfs-name=extra 0 0
/swapfile none swap defaults 0 0
penserbjorne@painkiller-legion:~$ free -m
              total       usado       libre  compartido búfer/caché  disponible
Memoria:       31959        7716       16424         159        7818       23620
Swap:         36863           0       36863
penserbjorne@painkiller-legion:~$ findmnt -no UUID -T /swapfile
e02e2e5a-ed6b-4a98-b4db-93a5940a4a85
penserbjorne@painkiller-legion:~$ sudo filefrag -v /swapfile | awk '{ if($1=="0:"){print $4} }'
57808896..
penserbjorne@painkiller-legion:~$ sudo kernelstub -a "resume=UUID=sudo filefrag -v /swapfile | awk '{ if($1=="0:"){print $4} }'
> ^C
penserbjorne@painkiller-legion:~$ sudo kernelstub -a "resume=UUID=e02e2e5a-ed6b-4a98-b4db-93a5940a4a85 resume_offset=57808896"
penserbjorne@painkiller-legion:~$ sudo nano /etc/initramfs-tools/conf.d/resume
penserbjorne@painkiller-legion:~$ sudo update-initramfs -u
update-initramfs: Generating /boot/initrd.img-5.4.0-7642-generic
cryptsetup: WARNING: Resume target cryptswap uses a key file
kernelstub.Config    : INFO     Looking for configuration...
kernelstub           : INFO     System information: 

    OS:..................Pop!_OS 20.04
    Root partition:....../dev/dm-1
    Root FS UUID:........e02e2e5a-ed6b-4a98-b4db-93a5940a4a85
    ESP Path:............/boot/efi
    ESP Partition:......./dev/nvme0n1p1
    ESP Partition #:.....1
    NVRAM entry #:.......-1
    Boot Variable #:.....0000
    Kernel Boot Options:.quiet loglevel=0 systemd.show_status=false splash resume=UUID=e02e2e5a-ed6b-4a98-b4db-93a5940a4a85 resume_offset=57808896
    Kernel Image Path:.../boot/vmlinuz-5.4.0-7642-generic
    Initrd Image Path:.../boot/initrd.img-5.4.0-7642-generic
    Force-overwrite:.....False

kernelstub.Installer : INFO     Copying Kernel into ESP
kernelstub.Installer : INFO     Copying initrd.img into ESP
kernelstub.Installer : INFO     Setting up loader.conf configuration
kernelstub.Installer : INFO     Making entry file for Pop!_OS
kernelstub.Installer : INFO     Backing up old kernel
kernelstub.Installer : INFO     No old kernel found, skipping
penserbjorne@painkiller-legion:~$ 

