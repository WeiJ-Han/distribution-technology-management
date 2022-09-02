pip install -r requirements.txt
pip install -r requirements2.txt
pip install dlib-19.8.1-cp36-cp36m-win_amd64.whl
pip install imutils
pip install opencv-contrib-python
pip install cmake
pip install dlib
python people_counter.py --prototxt MobileNetSSD_deploy.prototxt --model MobileNetSSD_deploy.caffemodel --input example_01.mp4 --output output1_01.avi
python people_counter.py --prototxt MobileNetSSD_deploy.prototxt --model MobileNetSSD_deploy.caffemodel --input people.mp4 --output people_out.avi