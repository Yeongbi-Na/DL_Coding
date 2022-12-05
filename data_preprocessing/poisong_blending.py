import scipy.sparse
from collections import deque
from scipy.sparse.linalg import spsolve
from os import path
import cv2
import numpy as np
import matplotlib.pyplot as plt

def poissong_blending(scr_dir, tgt_dir, ann_dir, cls_dir, my_class):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    source = cv2.imread(scr_dir) 
    target = cv2.imread(tgt_dir)
    ann = cv2.imread(ann_dir)
    offset = (0, 0) 
    def visualize_imgs():
        print('Source image size:', source.shape[:-1])
        plt.imshow(source[:,:,::-1]) # this is a trick to display the image in here 
        plt.show()
        print('Target image size:', target.shape[:-1])
        plt.imshow(target[:,:,::-1])
        plt.show()
        print('Mask size:', mask.shape)
        plt.imshow(mask, cmap='gray')
        plt.show()
        print('ann size:', ann.shape)
        plt.imshow(ann, cmap='gray')
        plt.show()
        return
        
    def find_mask(ann_path, my_class):
        ann = cv2.imread(ann_path, cv2.IMREAD_GRAYSCALE)
        ann = cv2.resize(ann, dsize=(64, 64), interpolation = cv2.INTER_CUBIC)
        x_idx, y_idx = np.where(ann == my_class)
        check_num = 10
        box = []
        mask = np.zeros(ann.shape)
        
        def make_big_mask(x, y, resize_shape):
            offs = 3
            #ann[max(0, min(x)-offs):min(resize_shape[0], max(x)+offs), max(0, min(y)-offs):min(resize_shape[1], max(y)+offs)] = 255 #그냥 흰, 검으로 만들려고
            mask[max(0, min(x)-offs):min(resize_shape[0], max(x)+offs), max(0, min(y)-offs):min(resize_shape[1], max(y)+offs)] = 255
            return
        def bfs(i, j):
            q = deque()
            q.append([i, j])

            while q:
                x, y = q.popleft()
                for d in range(4):
                    for ex in range(1, 3):
                        nx, ny = x+dx[d]*ex, y+dy[d]*ex
                        if 0<=nx< ann.shape[0] and 0<=ny< ann.shape[1]:
                            if ann[nx,ny] == my_class:
                                q.append([nx, ny])
                                ann[nx, ny] = check_num
            return

        for i in range(len(x_idx)):
            x, y = x_idx[i], y_idx[i]
            if ann[x,y] == my_class:
                bfs(x, y)
                ann[x, y] = check_num
                #min max  구하기
                box.append(np.where(ann == check_num))
                check_num += 1
           
        for i in range(len(box)):
            make_big_mask(box[i][0], box[i][1], (64, 64))
            
        mask = cv2.resize(mask, dsize=(512, 512), interpolation = cv2.INTER_CUBIC)
        return mask
    
    def do_poissong_blending(source, mask, target): 
        def laplacian_matrix(n, m):   
            mat_D = scipy.sparse.lil_matrix((m, m))
            mat_D.setdiag(-1, -1)
            mat_D.setdiag(4)
            mat_D.setdiag(-1, 1)
                
            mat_A = scipy.sparse.block_diag([mat_D] * n).tolil()
            
            mat_A.setdiag(-1, 1*m)
            mat_A.setdiag(-1, -1*m)
            
            return mat_A
            
        y_max, x_max = target.shape[:-1]
        y_min, x_min = 0, 0
        x_range = x_max - x_min
        y_range = y_max - y_min

        M = np.float32([[1, 0, offset[0]], [0, 1, offset[1]]])
        source = cv2.warpAffine(source, M, (x_range, y_range))
        mask = cv2.warpAffine(mask, M, (x_range, y_range))
        mask = mask[y_min:y_max, x_min:x_max]
        mask[mask != 0] = 1
        mat_A = laplacian_matrix(y_range, x_range)
        laplacian = mat_A.tocsc()
                
        for y in range(1, y_range - 1):
            for x in range(1, x_range - 1):
                if mask[y, x] == 0:
                    k = x + y * x_range
                    mat_A[k, k] = 1
                    mat_A[k, k + 1] = 0
                    mat_A[k, k - 1] = 0
                    mat_A[k, k + x_range] = 0
                    mat_A[k, k - x_range] = 0
        mat_A = mat_A.tocsc()
            
        mask_flat = mask.flatten()    
        for channel in range(source.shape[2]):
            source_flat = source[y_min:y_max, x_min:x_max, channel].flatten()
            target_flat = target[y_min:y_max, x_min:x_max, channel].flatten()        
            # inside the mask:
            # \Delta f = div v = \Delta g       
            alpha = 1
            mat_b = laplacian.dot(source_flat)*alpha
            # outside the mask:
            # f = t
            mat_b[mask_flat == 0] = target_flat[mask_flat == 0]
            x = spsolve(mat_A, mat_b)    
            x = x.reshape((y_range, x_range))
            x[x > 255] = 255
            x[x < 0] = 0
            x = x.astype('uint8')
            target[y_min:y_max, x_min:x_max, channel] = x
        return target

    mask = find_mask(cls_dir, my_class)
    
    
    visualize_imgs()
    result = do_poissong_blending(source, mask, target)
    plt.imshow(result[::-1])
    plt.show()
    return result
