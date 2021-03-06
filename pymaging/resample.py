# -*- coding: utf-8 -*-
# Copyright (c) 2012, Jonas Obrist
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Jonas Obrist nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL JONAS OBRIST BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from pymaging.utils import fdiv
import array


def nearest(source, width, height, pixelsize):
    assert pixelsize == 1, "yea... gotta implement this generically"
    pixels = []
    pixelappend = pixels.append # cache for cpython
    x_ratio = fdiv(source.width, width) # get the x-axis ratio
    y_ratio = fdiv(source.height, height) # get the y-axis ratio
    y_range = range(height) # an iterator over the indices of all lines (y-axis)
    x_range = range(width) # an iterator over the indices of all rows (x-axis)
    for y in y_range:
        source_y = int(round(y * y_ratio)) # get the source line
        line = array.array('B') # initialize a new line
        lineappend = line.append # cache for cypthon
        for x in x_range:
            source_x = int(round(x * x_ratio)) # get the source row
            lineappend(source.pixels[source_y][source_x])
        pixelappend(line)
    return pixels
