
*************************************

pip uninstall opencv-python
pip uninstall opencv-contrib-python
******************************************

pip install opencv-contrib-python
pip install imutils

******************************************
python super_res_image.py --model LapSRN_x8.pb --image zebra.png
python super_res_image.py --model EDSR_x4.pb --image zebra.png
python super_res_image.py --model LapSRN_x8.pb --image adrian.png
python super_res_image.py --model EDSR_x4.pb --image adrian.png
python super_res_image.py --model LapSRN_x8.pb --image KG0621.jpg
python super_res_image.py --model EDSR_x4.pb --image KG0621.jpg

****************************************************************
python super_res_video.py --model ESPCN_x4.pb



