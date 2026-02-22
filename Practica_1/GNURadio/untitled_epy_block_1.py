import numpy as np
from gnuradio import gr

class blk(gr.sync_block):  
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='e_Acum',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        
        self.acum = 0.0

    def work(self, input_items, output_items):
        x = input_items[0]
        y0 = output_items[0]

        # quitar DC (media del bloque)
        x_mean = np.mean(x)

        for i in range(len(x)):
            self.acum += (x[i] - x_mean)
            y0[i] = self.acum

        return len(y0)


