import matplotlib.pyplot as plt
import numpy as np
working_path = "/Users/chris/sublime/CT/output/"
imgs = np.load(working_path+'images_0000_0003.npy')
lungmask = np.load(working_path+'lungmask_0000_0003.npy')
for i in range(len(imgs)):
    print ("image %d" % i)
    fig,ax = plt.subplots(2,2,figsize=[8,8])
    ax[0,0].imshow(imgs[i],cmap='gray')
    ax[0,1].imshow(lungmask[i],cmap='gray')
    ax[1,0].imshow(imgs[i]*lungmask[i],cmap='gray')
    plt.show()
    #raw_input("hit enter to cont : ")