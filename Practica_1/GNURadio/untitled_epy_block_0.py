"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name="Diferenciador",
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.prev = 0.0

    def work(self, input_items, output_items):
        x = input_items[0]
        y = output_items[0]

        y[0] = x[0] - self.prev
        y[1:] = x[1:] - x[:-1]

        self.prev = x[-1]

        return len(y)
