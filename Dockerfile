FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04

WORKDIR /

ENV NV_NCCL_VERSION=2.15.1-1+cuda11.8

RUN apt-get update && apt-get install -y wget apt-utils

RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.0-1_all.deb && \
    dpkg -i cuda-keyring_1.0-1_all.deb && apt-get update && apt-get install -y libnccl2=${NV_NCCL_VERSION} libnccl-dev=${NV_NCCL_VERSION}

RUN apt-get update && apt-get -y install nano python3-dev python3-pip python3-virtualenv

RUN pip install --upgrade pip && pip install "jax[cuda11_cudnn82]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html && \
    pip install flax dm-haiku rlax optax chex

CMD ["bash"]

