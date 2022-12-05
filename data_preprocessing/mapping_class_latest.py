def ann_rgb2cls(data_path, num_workers=8, replace=False):
    print("Converting annotation images to class images...")
    nocls = np.array([0, 0, 0])
    cls1 = np.array([245, 39, 8])  # 정상
    cls2 = np.array([245, 299, 0])  # 도열병
    cls3 = np.array([26, 0, 255])  # 도복
    cls4 = np.array([204, 0, 250])  # 결주
    cls5 = np.array([0, 123, 245])  # 부진
    class_list = [nocls, cls1, cls2, cls3, cls4, cls5]
    dx = [0, 0, -1, 1, -1, -1, 1, 1]
    dy = [1, -1, 0, 0, -1, 1, -1, 1]

    def remove_blur(mask, cls_img):
        w, h = cls_img.shape[:2]
        for x in range(w):
            for y in range(h):
                if not mask[x, y]:
                    valid = []
                    for d in range(8):
                        nx, ny = x+dx[d], y+dy[d]
                        if 0 <= nx < w and 0 <= ny < h:
                            valid.append(cls_img[nx][ny])
                    cls_img[x][y] = np.argmax(np.bincount(valid))
        return cls_img

    def mapping_without_blur(file_path):
        img = cv2.imread(file_path)
        img = np.array(img)
        dist = []
        for c in class_list:  # 각 클래스와의 거리 구하기
            dist.append(np.sum((img - c)*(img - c), axis=2))
        dist = np.array(dist)
        min_dist = np.min(dist, axis=0)
        mask = np.where(min_dist == 0, True, False)
        mapped_img = np.argmin(dist, axis=0)  # 가장 가까운 거리의 인덱스 할당
        result = remove_blur(mask, mapped_img)
        return result

    rgb_ann_dir = os.path.join(data_path, "rgb_ann")
    cls_ann_dir = os.path.join(data_path, "cls_ann")

    if not replace and os.path.exists(cls_ann_dir):
        print(
            f"using existing class annotation files: {os.path.abspath(cls_ann_dir)}")
        return

    os.makedirs(cls_ann_dir, exist_ok=True)
    file_list = os.listdir(rgb_ann_dir)
    try:
        file_list.remove('.ipynb_checkpoints')
    except:
        pass
    
    def worker(file_list):
        for file in tqdm.tqdm(file_list):
            result = mapping_without_blur(os.path.join(rgb_ann_dir, file))
            cv2.imwrite(os.path.join(cls_ann_dir, file), result)

    file_list = np.array_split(file_list, num_workers)
    proc_list = []
    for i in range(num_workers):
        proc_list.append(Process(target=worker, args=(file_list[i],)))
    for proc in proc_list:
        proc.start()
    for proc in proc_list:
        proc.join()

    print("Converting annotation images to class images is done!")
