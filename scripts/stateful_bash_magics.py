from .bash_kernel_wrapper import BashKernel

from __future__ import print_function
from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic)

@magics_class
class StatefulBashMagics(Magics):
    "Magics that hold additional state"

    # Singleton bash kernel for all cell and line magics in notebook
    bash_kernel = BashKernel(get_ipython().kernel)
    
    def __init__(self, shell):
        # You must call the parent constructor
        super(StatefulBashMagics, self).__init__(shell)        
    
    @line_magic
    def plbash(self, line):
        self.bash_kernel.do_execute(line, False)

    @cell_magic
    def pcbash(self, line, cell):
        self.bash_kernel.do_execute(cell, False)

    @line_cell_magic
    def pbash(self, line, cell=None):
        "Magic that works both as %pblmagic and as %%pbccmagic"
        if cell is None:
            self.bash_kernel.do_execute(line, False)
            return line
        else:
            self.bash_kernel.do_execute(cell, False)

ip = get_ipython()
magics = StatefulBashMagics(ip)
ip.register_magics(magics)
