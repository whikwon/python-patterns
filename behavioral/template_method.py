"""
- http://ima.udg.edu/~sellares/EINF-ES1/TemplateMethodToni.pdf
- https://github.com/open-mmlab/mmdetection/blob/master/mmdet/models/detectors/base.py
"""

from abc import ABC, abstractmethod


class BaseDetector(ABC):

    @abstractmethod
    def forward(self, x):
        pass

    @abstractmethod
    def extract_feat(self):
        pass

    @property
    def with_neck(self):
        """Hook"""
        return hasattr(self, "neck") and self.neck is not None


class OneStageDetector(BaseDetector):
    def __init__(self, neck=None):
        self.neck = neck

    def forward(self, x):
        x = self.extract_feat(x)
        if self.with_neck:
            x = self.neck(x)
        x += 1
        return x

    def extract_feat(self, x):
        return x // 2


class TwoStageDetector(BaseDetector):
    def __init__(self, neck=None):
        self.neck = neck

    def forward(self, x):
        x = self.extract_feat(x)
        if self.with_neck:
            x = self.neck(x)
        x -= 1
        return x

    def extract_feat(self, x):
        return x // 4


class Neck(object):
    def __call__(self, x):
        return x * 2


def main():
    neck = Neck()
    one_stage = OneStageDetector(neck)
    two_stage = TwoStageDetector()

    x = 10
    assert one_stage.forward(x) == 11
    assert two_stage.forward(x) == 1


if __name__ == "__main__":
    main()
