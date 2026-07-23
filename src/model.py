import torch.nn as nn
from torchvision import models
from torchvision.models import MobileNet_V3_Small_Weights


class MultiClassClassificationModel(nn.Module):
    def __init__(self, num_classes=4):
        super(MultiClassClassificationModel, self).__init__()
        self.mobilenet = models.mobilenet_v3_small(weights=MobileNet_V3_Small_Weights.DEFAULT)

        # Modify the classifier to output num_classes instead of 1
        self.mobilenet.classifier[3] = nn.Linear(self.mobilenet.classifier[3].in_features, num_classes)

    def forward(self, x):
        return self.mobilenet(x)