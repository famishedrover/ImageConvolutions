import numpy as np

def hadamard_prod(mat_01 , mat_02 ) :
    m , n = mat_01.shape
    p , q = mat_02.shape
    
    if (m!=p) or (n!=q) :
        return 0
    return mat_01*mat_02
    
    
def convolution2D(image , kernel) :
    m , n = image.shape
    p , q = kernel.shape
    out = np.zeros((m-p+1,n-q+1))
    
    for ix in range(out.shape[0] ) :
        for iy in range(out.shape[1]) :
            
            im_patch = image[ix:ix+p , iy:iy +q]
            im_patch = hadamard_prod(im_patch , kernel)
#             s = im_patch.mean()
            s = im_patch.sum()
            if s<0 :
                s = 0.0
            elif s>255.0 :
                s = 255.0
            out[ix,iy] = s
            #convolve here
            
    return out


