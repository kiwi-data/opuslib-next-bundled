#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
#

"""Opus library loading and common ctypes aliases."""

import ctypes

from opuslib_next._loader import load_libopus

__author__ = "kalicyh <kalicyh@qq.com>"
__copyright__ = "Copyright (c) 2025, Kalicyh"
__license__ = "BSD 3-Clause License"


libopus = load_libopus()

c_int_pointer = ctypes.POINTER(ctypes.c_int)
c_int16_pointer = ctypes.POINTER(ctypes.c_int16)
c_float_pointer = ctypes.POINTER(ctypes.c_float)
c_ubyte_pointer = ctypes.POINTER(ctypes.c_ubyte)
