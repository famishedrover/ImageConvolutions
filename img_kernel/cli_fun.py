import numpy as np
import cv2
from constants import *
import os


def report_cli_err () :
  print 'CLI parameter error, use python imageTransform --doc for documentation'
  exit()


def get_img_path(argv) :
  try:
    return argv[1]
  except :
    report_cli_err()


def choose_kernel(argv) :
  kernel = np.asarray(blur_kernel)  #initialization
  if '-o' in argv:
    kernel = np.asarray(outline_kernel)
    print 'Outline kernel selected'
  elif '-d' in argv:
  	kernel = np.asarray(identity_kernel) 
  	print 'Identity kernel selected'
  elif '-b' in argv:
  	kernel = np.asarray(blur_kernel)
  	print 'Blur kernel selected'
  elif '-p' in argv:
    kernel = np.asarray(custom1_blur_kernel)
    print 'Custom1 blur kernel selected'
  elif '-q' in argv:
    kernel = np.asarray(custom2_blur_kernel)
    print 'Custom2 blur kernel selected'
  else :
    kernel = np.asarray(identity_kernel)
    print 'Default Identity kernel.'

  return kernel

def choose_kernel_img_plot (argv , c) :
  try : 
    if '--chk' in argv :
      import matplotlib.pyplot as plt
      plt.figure(0)
      plt.imshow(c,cmap = 'gray')
      plt.axis('off')
      plt.show()
  except :
    print 'ERR plotting image , check your installation of matplotlib '

def get_img_dir(path) :
  p = path.split('/')
  z = p[-1].split('.')
  z = z[0] + '_'
  p = '/'.join(p[:-1])
  p += '/'
  return p , z

def choose_nsave (argv , im_b , c , path) :
  if '--nsave' in argv :
    pass
  else :
    p , z = get_img_dir(path)
    print p
    n = '0'
    save_name = p + z +'bw'+n+'.png'
    save_name_kernel = p + z +'bw_kernel'+n+'.png'

    while os.path.isfile(save_name) or os.path.isfile(save_name_kernel) :
      n = str(int(n) + 1)
      save_name = p + z +'bw'+n+'.png'
      save_name_kernel = p + z +'bw_kernel'+n+'.png'
    print 'Saving as'
    print save_name 
    print save_name_kernel
    cv2.imwrite(save_name , im_b)
    cv2.imwrite(save_name_kernel , c)


def choose_kernel_intensity (argv) :
  r = 1
  for txt in argv :
    if '-i' in txt :
        t = txt
        txt = txt.replace('-i' , '')
        try :
            r = int(txt)
        except :
            print '%s is not supported , -i must be followed by an integer less than 5'%t
            r = -1
  if r < 0 :
    r = -1
  return r

def rundoc(argv) :
  try :
    if argv[1] == '--doc' :
      with open('doc.txt' , 'r') as f :
        x = f.read()
      print x
      return 1 
    else :
      pass
      return 0
  except :
    return 0
    report_cli_err()






