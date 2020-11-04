import numpy as np
np.set_printoptions(threshold=np.inf)
from PIL import Image

def main():
    data_im = Image.open("/Users/wangbing/Downloads/compare_pic/382_12_45.png")
    ade_im  = Image.open("/Users/wangbing/Downloads/compare_pic/ade.png")
    data_im = np.array(data_im)
    ade_im = np.array(ade_im)
    max_data_im = np.max(data_im)
    max_ade_im = np.max(ade_im)
    print("max of data = ", max_data_im)
    print("max of ade = ", max_ade_im)
    print(data_im.shape)
    #print(ade_im)

if __name__ == '__main__':
    main()
