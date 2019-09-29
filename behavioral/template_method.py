"""
- http://ima.udg.edu/~sellares/EINF-ES1/TemplateMethodToni.pdf
- https://github.com/open-mmlab/mmdetection/blob/master/mmdet/models/detectors/base.py
"""

from abc import ABC, abstractmethod


class BaseDetector(ABC):

    @abstractmethod
    def forward(self):
        pass

    @abstractmethod
    def extract_feat(self, img):
        pass

    @property
    def with_neck(self):
        """Hook"""
        return hasattr(self, "neck") and self.neck is not None


class OneStageDetector(BaseDetector):
    def __init__(self, neck):
        self.neck = neck

    def forward(self):
        pass

    def extract_feat(self):
        pass


class TwoStageDetector(BaseDetector):
    def __init__(self, neck):
        self.neck = neck

    def forward(self):
        pass

    def extract_feat(self):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
