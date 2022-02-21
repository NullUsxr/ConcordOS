# Copyright (c) 2022 ConcordOS, All Rights Reserved
project('ConcordOS', 'cpp', version: '0.1.0')

cppflags = ['-fno-PIC', '-fstrength-reduce', '-fomit-frame-pointer', '-fno-builtin', '-nostdlib', '-ffreestanding', '-std=gnu++11']

link_file = meson.source_root() + '/arch/' + get_option('arch') + '/kernel.ld'
link_am = ['-Wl,-T', '-Wl,' + link_file, '-nostdlib',  
    '-fno-PIC', '-no-pie', '-Wl,--build-id=none']
clang_target = ''

kernel_src = files(
  'src/kernel/main.cc',
)

kernel_inc = include_directories('include')

if get_option('arch') == 'x86-64'
  cflags += ['-m64', '-march=x86-64', '-mcmodel=kernel']
  clang_target = 'x86_64-unknown-none-elf'
  link_am += ['-mcmodel=kernel', '-Wl,-z,max-page-size=0x1000,-n']
endif

# Clang support cross-compiling by default
# No cross-compiler required

if meson.get_compiler('cpp').get_id() == 'clang'
  cppflags += ['--target=' + clang_target]
endif

executable('cnkrnl', kernel_src, include_directories: kernel_inc, link_depends: link_file, cpp_args: cppflags, link_args: link_am)
