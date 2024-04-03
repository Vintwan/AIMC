from scenedetect import open_video, SceneManager, split_video_ffmpeg
from scenedetect.detectors import ContentDetector
from scenedetect.video_splitter import split_video_ffmpeg
from scenedetect.scene_manager import save_images

video_path = "video.mp4"
video_clips_dir = "sence_list/"
video_clips_images_dir = "sence_images_list/"

# 生成场景图片
def find_scenes(video_path, threshold=27.0, output="",num_images = 3):
    # Open our video, create a scene manager, and add a detector.
    video = open_video(video_path)
    scene_manager = SceneManager()
    scene_manager.add_detector(
        ContentDetector(threshold=threshold))
    # Detect all scenes in video from current position to end.
    scene_manager.detect_scenes(video, show_progress=True)
    # `get_scene_list` returns a list of start/end timecode pairs
    scene_list = scene_manager.get_scene_list()
    # save each scene that was found.
    save_images(scene_list,video,show_progress=True,num_images = num_images,output_dir=output)
    return 

# 分割场景视频
def split_video_into_scenes(video_path, threshold=27.0, output=""):
    # Open our video, create a scene manager, and add a detector.
    video = open_video(video_path)
    scene_manager = SceneManager()
    scene_manager.add_detector(
        ContentDetector(threshold=threshold))
    scene_manager.detect_scenes(video, show_progress=True)
    scene_list = scene_manager.get_scene_list()
    split_video_ffmpeg(video_path, scene_list, show_progress=True,output_dir=output)
    return

# 生成场景图片
find_scenes(
    video_path= video_path,
    num_images = 1, #每个场景保留几张图片
    output= video_clips_images_dir
)

# 分割场景视频
# split_video_into_scenes(
#     video_path= video_path,
#     output= video_clips_dir
# )



# --------------- 以下为临时参考 -----------------

# import os
# import cv2

# def VLink(video_path,images_path,interval=10):
#     # video_path = 'D:/Resource/MaxFish.mp4'  # 视频地址
#     # images_path = 'D:/Resource/images/'  # 图片输出文件夹
#     # interval = 10  # 每间隔10帧取一张图片
#     num = 1
#     vid = cv2.VideoCapture(video_path)#打开这个视频
#     while vid.isOpened():
#         is_read, frame = vid.read()  #按帧读取视频  frame是读取图像  is_read是布尔值。文件读取到结尾返回FALSE
#         if is_read:
#             file_name =  num
#             cv2.imwrite(images_path + str(file_name) + '.jpg', frame)
#             cv2.waitKey(1)  
#             num += 1
#         else:
#             break

# def tailor_video():
#     # 要提取视频的文件名，隐藏后缀
#     sourceFileName = 'material'
#     # 在这里把后缀接上
#     video_path = os.path.join("G:/material/", sourceFileName + '.mp4')
#     times = 0
#     # 提取视频的频率，每10帧提取一个
#     frameFrequency = 10
#     # 输出图片到当前目录video文件夹下
#     outPutDirName = 'G:/material/video/' + sourceFileName + '/'
#     if not os.path.exists(outPutDirName):
#         # 如果文件目录不存在则创建目录
#         os.makedirs(outPutDirName)
#     camera = cv2.VideoCapture(video_path)
#     while camera.isOpened():
#         res, image = camera.read()
#         if not res:
#             print('not res , not image')
#             break
#         times += 1
#         if times % frameFrequency == 0:
#             cv2.imwrite(outPutDirName + str(times) + '.jpg', image)  #文件目录下将输出的图片名字命名为10.jpg这种形式
#             cv2.waitKey(1)
#             print(outPutDirName + str(times) + '.jpg')
#     print('图片提取结束')


# # 截取字幕区域
# def tailor(path1,path2,begin,end,step_size):  #截取字幕
#     for i in range(begin,end,step_size):
#         fname1=path1 % str(i)
#         print(fname1)
#         img = cv2.imread(fname1)
#         print(img.shape)
#         cropped = img[500:600, 100:750]  # 裁剪坐标为[y0:y1, x0:x1]
#         imgray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
#         thresh = 200
#         ret, binary = cv2.threshold(imgray, thresh, 255, cv2.THRESH_BINARY)  # 输入灰度图，输出二值图
#         binary1 = cv2.bitwise_not(binary)  # 取反
#         cv2.imwrite(path2 % str(i), binary1)


def text_create(name, msg):
    desktop_path = "G:/material/"  # 新创建的txt文件的存放路径
    full_path = desktop_path + name + '.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w')
    file.write(msg)
    file.close()

# 定义一个函数，用来判断是否是中文，是中文的话就返回True代表要提取中文字幕
def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False
