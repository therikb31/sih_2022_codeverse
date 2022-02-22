import cv2
import numpy as np

#manual input
length = 1920
d = 400
# width = 480
# fps = 30
# height = length
infile = "Hologram/test_in.mp4"
outfile = "Hologram/test_out.mp4"
padding = 0
screen_below_pyramid = False
'''Transform infile video to a hologram video with no audio track and save to outfile'''
capture = cv2.VideoCapture(infile)
capture.open(infile)
if capture.isOpened():
    width  = capture.get(cv2.CAP_PROP_FRAME_WIDTH)   # float `width`
    height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float `height`
    fps = capture.get(cv2.CAP_PROP_FPS)

# length = request.form['length']
# d = request.form['d']
# padding = request.form['padding'] or 0
assert 0 < int(length) <= 5000, 'Length is not in (0, 5000].'
assert 0 < int(d) < int(length) / 2, 'd is not in (0, length/2).'
assert 0 <= 2 * int(padding) < min(2 * int(d), int(length) / 2 - int(d)), 'Padding is too large.'
length, d, padding = map(int, [length, d, padding])
if length % 2:
    length += 1 # Keep length even for convenience
cap = cv2.VideoCapture(infile)
bgd = np.zeros((length, length, 3), np.uint8) # Create a black background
new_wid = 2 * d - 2 * padding
new_hgt = int(float(new_wid) / width * height)
if new_hgt + d + 2 * padding > length / 2:
    new_hgt = length / 2 - d - 2 * padding
    new_wid = int(float(new_hgt) / height * width)
if new_wid % 2:
    new_wid -= 1
if new_hgt % 2:
    new_hgt -= 1

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter(outfile, fourcc, fps, (length,length))

while(1):
    ret, frame = cap.read()
    if not ret:
        break
    resized_frame = cv2.resize(frame, (new_wid, new_hgt))
    if screen_below_pyramid:
        resized_frame = cv2.flip(resized_frame, 0)
    bgd[length // 2 + d + padding:length // 2 + d + new_hgt + padding, length // 2 - new_wid // 2:length // 2 + new_wid // 2] =\
        resized_frame
    bgd[length // 2 - d - padding - new_hgt:length // 2 - d - padding, length // 2 - new_wid // 2:length // 2 + new_wid // 2] =\
        cv2.flip(resized_frame, -1)
    bgd[length // 2 - new_wid // 2:length // 2 + new_wid // 2, length // 2 + d + padding:length // 2 + d + new_hgt + padding] =\
        cv2.flip(cv2.transpose(resized_frame), 0)
    bgd[length // 2 - new_wid // 2:length // 2 + new_wid // 2, length // 2 - d - padding - new_hgt:length // 2 - d - padding] =\
        cv2.flip(cv2.transpose(resized_frame), 1)
    out.write(bgd)

cap.release()
out.release()
print("done")