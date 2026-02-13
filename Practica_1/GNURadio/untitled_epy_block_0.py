import numpy as np
from gnuradio import gr

class blk(gr.sync_block):  
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='e_Acum',
            in_sig=[np.float32],   # Ajusta tipo si es complejo
            out_sig=[np.float32]
        )
        
        self.acum = 0.0  # Variable de estado (memoria)

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        for i in range(len(in0)):
            self.acum += in0[i]
            out[i] = self.acum

        return len(out)
