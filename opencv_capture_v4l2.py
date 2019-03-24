import numpy as np
import cv2
import os
import v4l2capture
import select
import v4l2


if __name__ == '__main__':

    #cap = cv2.VideoCapture(0)
    #cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1920)      # <-- this doesn't work. OpenCV tries to set VIDIO_S_CROP instead of the frame format
    #cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 1080)

    width_height_Cmd = 'sudo v4l2-ctl -d /dev/video1 --set-fmt-video=width=640,height=480,pixelformat=1'
    os.system(width_height_Cmd)


    # python-v4l2capture

    # min=0 max=255 step=1 default=128 value=128
    brightness_Cmd = 'sudo v4l2-ctl -d /dev/video1 --set-ctrl brightness=128'
    os.system(brightness_Cmd)

    # min=0 max=255 step=1 default=32 value=32
    contrast_Cmd = 'sudo v4l2-ctl -d /dev/video1 --set-ctrl contrast=32'
    os.system(contrast_Cmd)

    # min=0 max=255 step=1 default=32 value=32
    saturation_Cmd = 'sudo v4l2-ctl -d /dev/video1 --set-ctrl saturation=32'
    os.system(saturation_Cmd)

    # default=1 value=1
    white_balance_temperature_auto_Cmd = 'sudo v4l2-ctl -d /dev/video1 --set-ctrl white_balance_temperature_auto=1'
    os.system(white_balance_temperature_auto_Cmd)

    # min=0 max=255 step=1 default=64 value=131
    gain_Cmd = 'sudo v4l2-ctl -d /dev/video1 --set-ctrl gain=64'
    os.system(gain_Cmd)

    # min=0 max=255 step=1 default=64 value=131
    gain_Cmd = 'sudo v4l2-ctl -d /dev/video1 -L'
    os.system(gain_Cmd)




    # min=0 max=2 default=2 value=2 (0: Disabled, 1: 50 Hz, 2: 60 Hz)
    power_line_frequency_Cmd = 'sudo v4l2-ctl -d /dev/video1 --set-ctrl power_line_frequency=2'
    os.system(power_line_frequency_Cmd)

    # min=0 max=10000 step=10 default=4000 value=1070 flags=inactive
    white_balance_temperature_Cmd = 'sudo v4l2-ctl -d /dev/video1 --set-ctrl white_balance_temperature=0'
    os.system(white_balance_temperature_Cmd)

    # min=0 max=255 step=1 default=24 value=24
    sharpness_Cmd = 'sudo v4l2-ctl -d /dev/video1 --set-ctrl sharpness=24'
    os.system(sharpness_Cmd)

    # min=0 max=1 step=1 default=0 value=0
    backlight_compensation_Cmd = 'sudo v4l2-ctl -d /dev/video1 --set-ctrl backlight_compensation=0'
    os.system(backlight_compensation_Cmd)

    # min=0 max=3 default=3 value=1 (1: Manual Mode, 3: Aperture Priority Mode)
    exposure_auto_Cmd = 'sudo v4l2-ctl -d /dev/video1 --set-ctrl exposure_auto=1'
    os.system(exposure_auto_Cmd)

































    # min=1 max=10000 step=1 default=166 value=667
    exposure_absolute_Cmd = 'sudo v4l2-ctl -d /dev/video1 --set-ctrl exposure_absolute_Cmd=150'
    os.system(exposure_absolute_Cmd)

    # default=0 value=1
    exposure_auto_priority_Cmd = 'sudo v4l2-ctl -d /dev/video1 --set-ctrl exposure_auto_priority=0'
    os.system(exposure_auto_priority_Cmd)

    # Open the video device.
    video = v4l2capture.Video_device("/dev/video1")

    #video.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
    #video = video.set_exposure_auto(0)
    #subprocess.call('v4l2-ctl --device=/dev/video0 --set-ctrl exposure_absolute=20', shell=True).

    # Suggest an image size to the device. The device may choose and
    # return another size if it doesn't support the suggested one.

    #v4l2 - ctl - d / dev / video1 - c exposure_auto = 1


    #size_x, size_y = video.set_format(640, 480) #720p #1920, 1080,
    # print ("device chose {0}x{1} res".format(size_x, size_y))

    # Create a buffer to store image data in. This must be done before
    # calling 'start' if v4l2capture is compiled with libv4l2. Otherwise
    # raises IOError.
    video.create_buffers(30)

    # Send the buffer to the device. Some devices require this to be done
    # before calling 'start'.
    video.queue_all_buffers()

    # Start the device. This lights the LED if it's a camera that has one.
    print("start capture")
    video.start()
    i=0
    while(True):
        i=i+1
        select.select((video,), (), ())
        image_data = video.read_and_queue()
        #print("decode")
        #i=0
        if i%10==0:
            os.system(gain_Cmd)
        frame = cv2.imdecode(np.frombuffer(image_data, dtype=np.uint8), cv2.IMREAD_COLOR)
        cv2.imshow('frame', frame)
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break
    video.close()
    cv2.destroyAllWindows()


# !/usr/bin/python
# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# from PIL import Image
# #import Image
# import select
# import v4l2capture
# import time
# # Open the video device.
# video = v4l2capture.Video_device("/dev/video0")
# # Suggest an image size to the device. The device may choose and
# # return another size if it doesn't support the suggested one.
# #size_x, size_y = video.set_format(1280, 1024, fourcc='MJPG')
# # Create a buffer to store image data in. This must be done before
# # calling 'start' if v4l2capture is compiled with libv4l2. Otherwise
# # raises IOError.
# video.create_buffers(30)
# # Send the buffer to the device. Some devices require this to be done
# # before calling 'start'.
# video.queue_all_buffers()
# # Start the device. This lights the LED if it's a camera that has one.
# video.start()
# stop_time = time.time() + 10.0
# with open('/home/maria/Desktop/video.mp4', 'wb') as f:
#     while stop_time >= time.time():
#         # Wait for the device to fill the buffer.
#         select.select((video,), (), ())
#         # The rest is easy :-)
#         image_data = video.read_and_queue()
#         f.write(image_data)
# video.close()
#print("Saved video.mjpg (Size: " + str(size_x) + " x " + str(size_y) + ")")
#
# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# # !/usr/bin/env python
# import numpy as np
# import cv2
# import os
# import v4l2capture
# import select
# if __name__ == '__main__':
#     # cap = cv2.VideoCapture(0)
#     # cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1920)      # <-- this doesn't work. OpenCV tries to set VIDIO_S_CROP instead of the frame format
#     # cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 1080)
#     # The following is from: https://github.com/gebart/python-v4l2capture
#     # Open the video device.
#     video = v4l2capture.Video_device("/dev/video1")
#     # Suggest an image size to the device. The device may choose and
#     # return another size if it doesn't support the suggested one.
#     #size_x, size_y = video.set_format(1920, 1080, fourcc='MJPG')
#     #print("device chose {0}x{1} res".format(size_x, size_y))
#     # Create a buffer to store image data in. This must be done before
#     # calling 'start' if v4l2capture is compiled with libv4l2. Otherwise
#     # raises IOError.
#     video.create_buffers(30)
#     # Send the buffer to the device. Some devices require this to be done
#     # before calling 'start'.
#     video.queue_all_buffers()
#     # Start the device. This lights the LED if it's a camera that has one.
#     print("start capture")
#     video.start()
#     while (True):
#         # We used to do the following, but it doesn't work :(
#         # ret, frame = cap.read()
#         # Instead...
#         # Wait for the device to fill the buffer.
#         select.select((video,), (), ())
#         # The rest is easy :-)
#         image_data = video.read_and_queue()
#         print("decode")
#         frame = cv2.imdecode(np.frombuffer(image_data, dtype=np.uint8), cv2.cv.CV_LOAD_IMAGE_COLOR)
#         cv2.imshow('frame', frame)
#         key = cv2.waitKey(1)
#         if key & 0xFF == ord('q'):
#             break
#     # cap.release()
#     video.close()
#     cv2.destroyAllWindows()