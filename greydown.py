#!/usr/bin/env python

# Copyright (c) 2014, Hugo Osvaldo Barrera <hugo@barrera.io>

# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.

# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from xdg import BaseDirectory

import os
import time

compiz_config = os.path.join(BaseDirectory.xdg_config_home,
                             "compiz-1/compizconfig/Default.ini")
battery_base_dir = "/sys/class/power_supply/BAT0"

config_in = open(compiz_config)
lines = config_in.readlines()
config_in.close()


def set_colour(lines, percentage):
    target_lines = []

    for line in lines:
        if line.startswith("s0_saturation_values"):
            target_lines.append("s0_saturation_values = {};"
                                .format(percentage))
        else:
            target_lines.append(line)

    config_out = open(compiz_config, "w")
    config_out.writelines(target_lines)
    config_out.close()

    print("Colour set to {}%".format(percentage))

while (True):
    battery_full_file = open(os.path.join(battery_base_dir, "energy_full"))
    battery_full = float(battery_full_file.read())
    battery_full_file.close()

    battery_now_file = open(os.path.join(battery_base_dir, "energy_now"))
    battery_now = float(battery_now_file.read())
    battery_now_file.close()

    battery_percent = battery_now/battery_full * 100
    print("Battery at {} %".format(battery_percent))

    if battery_percent < 10:
        # 10% battery -> 100% colour
        #  9% battery ->  90% colour
        colour = int(battery_percent * 10)
        set_colour(lines, colour)
    else:
        set_colour(lines, 100)

    time.sleep(2)
