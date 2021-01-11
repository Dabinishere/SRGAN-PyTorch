# Copyright 2020 Dakewe Biotech Corporation. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""File for accessing GAN via PyTorch Hub https://pytorch.org/hub/
Usage:
    import torch
    model = torch.hub.load("Lornatang/SRGAN-PyTorch", upscale_factor=4, num_residual_block=16)
"""
import torch
from torch.hub import load_state_dict_from_url

from srgan_pytorch import Generator

model_urls = {
    "srgan_2x2_16": "https://github.com/Lornatang/SRGAN-PyTorch/releases/download/0.1.0/GAN_srgan_2x2_16.pth",
    "srgan_4x4_16": "https://github.com/Lornatang/SRGAN-PyTorch/releases/download/0.1.0/GAN_srgan_2x2_23.pth",
    "srgan_2x2_23": "https://github.com/Lornatang/SRGAN-PyTorch/releases/download/0.1.0/GAN_srgan_4x4_16.pth",
    "srgan_4x4_23": "https://github.com/Lornatang/SRGAN-PyTorch/releases/download/0.1.0/GAN_srgan_4x4_23.pth"
}

dependencies = ["torch"]


def create(arch, upscale_factor, num_residual_block, pretrained, progress):
    """ Creates a specified GAN model

    Args:
        arch (str): Arch name of model.
        upscale_factor (int): Image magnification factor.
        num_residual_block (int): How many residual blocks are combined.
        pretrained (bool): Load pretrained weights into the model.
        progress (bool): Show progress bar when downloading weights.

    Returns:
        PyTorch model.
    """
    model = Generator(upscale_factor, num_residual_block)
    if pretrained:
        state_dict = load_state_dict_from_url(model_urls[arch], progress=progress, map_location=torch.device("cpu"))
        model.load_state_dict(state_dict)
    return model


def srgan_2x2_16(pretrained: bool = False, progress: bool = True) -> Generator:
    r"""GAN model architecture from the
    `"One weird trick..." <https://arxiv.org/abs/1609.04802>`_ paper.

    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
        progress (bool): If True, displays a progress bar of the download to stderr
    """
    return create("srgan_2x2_16", 2, 16, pretrained, progress)


def srgan_3x3_16(pretrained: bool = False, progress: bool = True) -> Generator:
    r"""GAN model architecture from the
    `"One weird trick..." <https://arxiv.org/abs/1609.04802>`_ paper.

    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
        progress (bool): If True, displays a progress bar of the download to stderr
    """
    return create("srgan_3x3_16", 3, 16, pretrained, progress)


def srgan_4x4_16(pretrained: bool = False, progress: bool = True) -> Generator:
    r"""GAN model architecture from the
    `"One weird trick..." <https://arxiv.org/abs/1609.04802>`_ paper.

    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
        progress (bool): If True, displays a progress bar of the download to stderr
    """
    return create("srgan_4x4_16", 4, 16, pretrained, progress)


def srgan_2x2_23(pretrained: bool = False, progress: bool = True) -> Generator:
    r"""GAN model architecture from the
    `"One weird trick..." <https://arxiv.org/abs/1609.04802>`_ paper.

    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
        progress (bool): If True, displays a progress bar of the download to stderr
    """
    return create("srgan_2x2_23", 2, 23, pretrained, progress)


def srgan_3x3_23(pretrained: bool = False, progress: bool = True) -> Generator:
    r"""GAN model architecture from the
    `"One weird trick..." <https://arxiv.org/abs/1609.04802>`_ paper.

    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
        progress (bool): If True, displays a progress bar of the download to stderr
    """
    return create("srgan_3x3_23", 3, 23, pretrained, progress)


def srgan_4x4_23(pretrained: bool = False, progress: bool = True) -> Generator:
    r"""GAN model architecture from the
    `"One weird trick..." <https://arxiv.org/abs/1609.04802>`_ paper.

    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
        progress (bool): If True, displays a progress bar of the download to stderr
    """
    return create("srgan_4x4_23", 4, 23, pretrained, progress)
