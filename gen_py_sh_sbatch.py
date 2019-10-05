import numpy as np
import os,sys
import shutil
import subprocess

def generate_batch_file(X):
    tmpl = open('runsrw.sh.template', 'r').read()
    fname = 'runsrw_%(slit_size_um)dum.sh' % X
    print ('Generate the batch bash file: ',fname)
    guninpt = open(fname, 'w')
    guninpt.write(tmpl % X)
    guninpt.close()

def generate_srwpy_file(X):
    fname_template = X['fn_srw_template']
    tmpl = open(fname_template, 'r').read()
    
    fname_srwpy = fname_template[:-12] + '_%(slit_size_um)dum.py'%X
    print ('Generate the SRW example python file: ',fname_srwpy)
    guninpt = open(fname_srwpy, 'w')
    guninpt.write(tmpl % X)
    guninpt.close()
    X['fn_srw_py'] = fname_srwpy
    return X

def main(v):
    X = {'fn_srw_template': 'SRWLIB_Example.py.template',
         'N_node': 5,
         'n_processor': 51,
         'c_thread': 1,
         'hour':00,
         'min':30,
         'QOS': "debug", #"premium",
         'tasks_per_node': 5,
         'job_name': "{}um".format(v),
         'nMacroElec': 10000,
         'nMacroElecAvgOneProc': 5,
         'SavingPeriod': 100,
         'slit_size_um': v,
         'slit_size_m': v*1e-6,
        }
    X = generate_srwpy_file(X)
    generate_batch_file(X)

if __name__ == "__main__":
    for i in [20, 30, 40, 50, 60]:
        main(i)
        #subprocess.call("sbatch runsrw_{}um.sh".format(i), shell = True)
