from scipy.stats import mode
import numpy as np
import cv2

def ann_rgb2cls(data_path):
    nocls = np.array([0, 0, 0])
    cls1 = np.array([26, 0, 255]) #도복
    cls2 = np.array([204, 0, 250]) #결주
    cls3 = np.array([245, 39, 8]) #정상
    cls4 = np.array([245, 299, 0])#도열병
    cls5 = np.array([0, 123, 245]) #부진
    class_list = [nocls, cls1, cls2, cls3, cls4, cls5]

    dx = [0, 0, -1, 1, -2, 2, 0, 0]
    dy = [1, -1, 0, 0, 0, 0, 2, -2]

    def remove_blur(mask, cls_img):
        w, h = cls_img.shape[:2]
        for x in range(512):
            for y in range(512):
                if not mask[x, y]:
                    temp = []
                    for d in range(8):
                        nx, ny = x+dx[d], y+dy[d]
                        if 0<= nx< w and 0<= ny <h:
                            temp.append(cls_img[nx][ny])
                    cls_img[x][y] = mode(temp)[0][0]

        return cls_img



    def mapping_without_blur(ann_dir):
        img = cv2.imread(ann_dir)
        img = np.array(img)
        dist = []
        for c in class_list: #각 클래스와의 거리 구하기
            dist.append(np.sum((img - c)*(img - c), axis=2))
        dist = np.array(dist)   
        min_dist = np.min(dist, axis= 0)
        mask = np.where(min_dist == 0, True, False)
        mapped_img = np.argmin(dist, axis= 0) #가장 가까운 거리의 인덱스 할당
        result = remove_blur(mask, mapped_img)  
        return result


###########################################
# 사용 예시
if __name__ == "__main__":
    mapping_img = ann_rgb2cls(file_path)