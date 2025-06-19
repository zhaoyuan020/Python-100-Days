import cv2
import os  # 要提取视频的文件名，隐藏后缀


# 机智的刘同学-副本.mp4

sourceFileName = '机智的刘同学-副本'  # 在这里把后缀接上
# video_path = os.path.join('E:/百度云下载/遗留物', sourceFileName + '.mpg')
video_path = r"D:\迅雷下载\机智的刘同学-副本.mp4"
times = 0
frameFrequency = 1  # 提取视频的频率，每50帧提取一个
outPutDirName = 'D:/迅雷下载/' + sourceFileName + '/'  # 输出图片到当前目录vedio文件夹下
if not os.path.exists(outPutDirName):  # 如果文件目录不存在则创建目录
    os.makedirs(outPutDirName)
camera = cv2.VideoCapture(video_path)
while True:
    times += 1
    res, image = camera.read()
    if type(image) == type(None):
        print(res)
        print(type(image))
        print(type(None))
        break
    print(res)
    if not res:
        print('not res , not image')

        break
    if times % frameFrequency == 0:
        # cv2.imwrite("./20220830153140_20220830154000/" + str(times) + '.jpg', image)
        # cv2.imwrite(outPutDirName + str(times) + '.jpg', image)
        # cv2.imwrite('D:\\迅雷下载\\机智的刘同学-副本\\' + str(times) + '.jpg', image)
        # cv2.imwrite('D://迅雷下载//机智的刘同学-副本//' + str(times) + '.jpg', image)
        # cv2.imwrite('D:/迅雷下载/机智的刘同学-副本/' + str(times) + '.jpg', image)
        # cv2.imwrite('./机智的刘同学-副本/' + str(times) + '.jpg', image)
        cv2.imwrite('./' + str(times) + '.jpg', image)
        # 原来是因为路径里有汉字，fuck！
        print(outPutDirName + str(times) + '.jpg')

        # + '\\'
print('图片提取结束')
camera.release()