---
title: The process of installing Arch Linux and what it taught me
html_title: Installing Arch Linux | Lmpkessels Blog
description: A summary of the process of installing Arch Linux and what it taught me
section: comp-sci
image: /assets/blog_arch_installation_thumbnail.png
alternative: Thumbnail for the Arch Linux Installtion Blog
date: 2026/09/25
slug: Arch-Linux-installation
---

For a while I'd been thinking about installing Arch Linux, but every Google search made me question the opposite: whether I could handle it, and what it would bring to the table. But for me, someone who wants to build a greater understanding of computers and how they work, I thought, let's just give it a try and see what happens.

And here I am writing on my newly installed Arch Linux Operating System.

## Getting the prerequisites

After using Linux Ubuntu for a year, I had dialed in the basics of the command line and thought that it was time to switch to Arch so that I had a full do-it-yourself operating system. 

After reading through the [Arch Linux Installation Guide](https://wiki.archlinux.org/title/Installation_guide) I created a bootable flash drive with the newest **Arch Linux x86_64 .iso** file on it. 

When I had the bootable flash drive, I made sure that my old Linux Ubuntu system was backed up. This ensured that my old files couldn't get lost and could later be moved onto my new operating system.

## Booting Arch for the first time as root

When you install Arch Linux for the first time on your PC, you get launched into the terminal as root. This is because, with root access, you have a broad set of privileges that allow you to perform system-level operations such as partitioning the disk, mounting filesystems, and installing the system.

Then, once you've been connected to the internet, you can access the installation guide. When you follow the installation guide, you'll see that you need to be able to, for example, allocate certain parts of your disk (SSD or HDD) to separate blocks.

Which is where root access comes in handy.

## Setting up the system so it can boot

When I set up Arch for the first time, I needed to create three separate partitions on my disk, which are logical regions of a block device: **1) for the EFI system partition, 2) for the Linux swap partition, and 3) for the Linux x86_64 root partition**.

The **EFI System Partition** stores boot-related files that the UEFI firmware can access during startup. I allocated 1GiB on my disk for the EFI System Partition.

The **Linux Swap Partition** is a disk space the kernel can use as part of its virtual-memory management. Memory pages can be moved from RAM to swap. I allocated 4 GiB on my disk for the Linux Swap Partition.

And **then the Linux x86_64 Root Partition** is where I created the main filesystem, which is mounted at **/** and contains most of the installed system. It requires at least 32GiB, but depending on the amount of disk space remaining, it's best to use that space for your filesystem.

Once the disk has been partitioned and the system installed and mounted under /mnt, it's time to enter the new system through arch-chroot /mnt. Once you've accessed the new system, the guide gives you a few action steps to follow. For example, set up a user account and password, time and location, and set up the most important packages such as a network manager.

Once you have finished the system setup, you can launch into the new, fresh Arch system.

## What it taught me

Installing Arch Linux taught me the abstraction that default operating systems such as macOS, Windows, and Linux Ubuntu take away by creating a pre-developed package for us. 

As described above, you need to do everything yourself: install a boot system, partition the disk, install a network manager, and install all necessary packages to improve the system.

It also gave me insight into where virtual memory is used (The Linux Swap Partition).

Well, this is it for now. I know it's only the start, and the future will bring me challenges and frustrations that will lead to a deeper understanding of Linux and Arch, so if you'd like to see some updates on my journey using Linux, Arch, and building out parts, stick around.

If you see some major improvements, have questions, or give me some useful tips, feel free to open an [issue](https://github.com/Lmpkessels/blog/issues/new) or reach me at my [email](mailto:l@lmpkessels.com).