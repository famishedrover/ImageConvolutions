import cv2 
from sys import argv
import numpy as np
from convolution import convolution2D
from cli_fun import choose_kernel , choose_kernel_img_plot ,choose_nsave , choose_kernel_intensity , report_cli_err , get_img_path,rundoc

#rundoc should always be before any other call.
resp = rundoc(argv)
if resp == 1 :
  exit()

  
path = get_img_path(argv)

im = cv2.imread(path)
if im is None :
  report_cli_err()
print 'Given Shape :',im.shape
x = im.shape[0] # height
y = im.shape[1] # length

# if x > y:
# 	y = x
# else :
# 	x = y
# print 'converted to shape',x,',',y

im_b = cv2.cvtColor(im , cv2.COLOR_RGB2GRAY)
print 'Dim of black/white img ',im_b.shape


kernel = choose_kernel(argv)


print 'Please Wait ...'

i = choose_kernel_intensity (argv)

if i == -1 :
  report_cli_err()
else :
  print 'Kernel Intensity ',i
  if i == 1 :
    c = convolution2D(im_b , kernel)
  else :
    if i > 4 :
      report_cli_err()
    c = convolution2D(im_b , kernel)
    for ix in range(i-1) :
      c = convolution2D(c,kernel)

print 'bkg image', c.shape

#whether or not to plot the kernelised img
choose_kernel_img_plot(argv , c)

#whether or not to save kernelised img , default is to save the image.
choose_nsave(argv , im_b , c , path)




