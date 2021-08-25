
FROM pytorch/pytorch:1.8.1-cuda11.1-cudnn8-devel

RUN python3 -m pip install --no-cache-dir \
        opencv-python==4.5.1.48 \   
        pillow \
        matplotlib \
        numpy \
        PyYAML \
        tqdm \
        tensorboard \
        scipy \ 
        torchvision==0.9.1  

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

CUDA_HOME="/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

ADD /stanford_drone_dataset/images/ /home/emmanouil/Desktop/ProjectCV/PyTorch_YOLOv4/stanford_drone_dataset/images/
ADD /stanford_drone_dataset/labels/ /home/emmanouil/Desktop/ProjectCV/PyTorch_YOLOv4/stanford_drone_dataset/labels/

COPY . .

ENTRYPOINT ["python3"]
