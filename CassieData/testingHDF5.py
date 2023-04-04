import numpy as np 
import h5py 

cass_jumping = np.loadtxt(open("C:/Users/Cassie G/Documents/390FinalProject-1/jumping_cg.csv"), delimiter=",", skiprows=1)
cass_walking = np.loadtxt(open("C:/Users/Cassie G/Documents/390FinalProject-1/walking_cg.csv"), delimiter=",", skiprows=1)

#writing to hdf5
with h5py.File('./hdf5_data.h5' , 'w') as hdf:
    #defining the individual groups on the LHS for Cassie Greidanus
    #Jump and Walk are stored separate under Cassie Greidanus folder
    CG_dataj = hdf.create_group('CassieGreidanus/Jump')
    CG_dataw = hdf.create_group('CassieGreidanus/walk')

    CG_dataj.create_dataset('cassJump', data=cass_jumping)
    CG_dataw.create_dataset('cassWalk', data=cass_walking)

    #defining the individual groups on the LHS for Leo
    #Jump and Walk are stored separate under Leo's folder


    #defining the individual groups on the LHS for Henry
    #Jump and Walk are stored separate under Henry's folder


#reading to hdf5
'''
with h5py.File('.hdf5_data.h5', 'r') as hdf:
    ls = list(hdf.keys())
    print(ls)
    cassJump = hdf.get('cassJump')
    print(type(cassJump))
    cJump_array = np.array(cassJump)
    print(type(cJump_array))
'''