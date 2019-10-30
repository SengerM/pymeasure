#
# This file is part of the PyMeasure package.
#
# Copyright (c) 2013-2019 PyMeasure Developers
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

from pymeasure.instruments import Instrument
from pymeasure.instruments.validators import strict_range

class APSIN12G(Instrument):
    """ Represents the Anapico APSIN12G Signal Generator with option 9K,
    HP and GPIB.
    """
    FREQ_LIMIT = [9e3, 12e9]
    POW_LIMIT = [-30, 27]

    power = Instrument.control(
        "SOUR:POW:LEV:IMM:AMPL?;", "SOUR:POW:LEV:IMM:AMPL %gdBm;",
        """ A floating point property that represents the output power
        in dBm. This property can be set. """,
        validator=strict_range,
        values=POW_LIMIT
    )
    frequency = Instrument.control(
        ":FREQ:CW?;", ":FREQ:CW %eHz;",
        """ A floating point property that represents the output frequency
        in Hz. This property can be set. """,
        validator=strict_range,
        values=FREQ_LIMIT
    )

    def __init__(self, resourceName, **kwargs):
        super(APSIN12G, self).__init__(
            resourceName,
            "Anapico APSIN12G Signal Generator",
            **kwargs
        )

    def enableRF(self):
        """ Enables the RF output.
        """
        self.write("OUTP:STAT 1")

    def disableRF(self):
        """ Disables the RF output.
        """
        self.write("OUTP:STAT 0")

