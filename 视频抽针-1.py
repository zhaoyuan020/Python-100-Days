import cv2
import os


def video_to_frames(video_path, outPutDirName):
    times = 0

    # 提取视频的频率，每1帧提取一个
    frame_frequency = 1

    # 如果文件目录不存在则创建目录
    if not os.path.exists(outPutDirName):
        os.makedirs(outPutDirName)

    # 读取视频帧
    camera = cv2.VideoCapture(video_path)

    while True:
        times = times + 1
        res, image = camera.read()
        if not res:
            print('not res , not image')
            print(res)
            break
        # 按照设置间隔存储视频帧
        if times % frame_frequency == 0:
            # cv2.imwrite(outPutDirName + '\\' + str(times) + '.jpg', image)
            cv2.imwrite(outPutDirName + str(times) + '.jpg', image)
            print(outPutDirName + str(times) + '.jpg')

    print('图片提取结束')
    # 释放摄像头设备
    camera.release()


video_path = r"D:/古之欲-新/2.JK女儿侍奉内射爽到爆 - Trim.mp4"
# ourceFileName = '广东夫妇'
outPutDirName = 'D:/shipinchouzhen/'

video_to_frames(video_path, outPutDirName)