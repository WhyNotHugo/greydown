Greydown
========

This python script monitors the battery status, and starts decreasing
the screen colour when the battery is under 10%. It only works if compiz
is your WM, and is somewhat hackinsh, since compiz's d-bus plugin is
broken atm.

The effect is a very gradual greyscaling of the screen when running our
of battery.

Normal battery monitors inform the user in two ways:

* A popup that doesn't go away until clicked: this is rather obstrusive.
* A popup that goes away on it's own: this can easily go unnoticed AND
can be obstrusive.
* A tray icons or something alike: It's unlikely I'd ever notice this
before my battery runs out.

Gradually greyscaling the screen means that it's extremel unlikely that
you fail to notice the warning. But it'll be several minutes before it
even interferes with you actual work/gaming/wharever.

Copyright (c) 2014, Hugo Osvaldo Barrera &lt;hugo@barrera.io&gt;
