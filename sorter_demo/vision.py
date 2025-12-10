import time

from .models import Detection, Pose


class VisionService:
    """Mock vision service that returns deterministic detections for testing."""

    def __init__(self):
        self.frame_id = "cam"
        self.counter = 0

    def capture(self):
        self.counter += 1
        return {"frame_id": self.frame_id, "seq": self.counter}

    def detect(self, frame) -> list[Detection]:
        stamp = time.time()
        detections = [
            Detection(
                bbox=(100, 120, 200, 220),
                cls="red_box",
                score=0.95,
                pose_cam=Pose(
                    position=[0.4, 0.1, 0.2],
                    quat=[0.0, 0.0, 0.0, 1.0],
                    frame_id=self.frame_id,
                    stamp=stamp,
                ),
                size=[0.25, 0.18, 0.12],
            ),
            Detection(
                bbox=(220, 130, 320, 230),
                cls="blue_box",
                score=0.88,
                pose_cam=Pose(
                    position=[0.38, -0.05, 0.22],
                    quat=[0.0, 0.0, 0.0, 1.0],
                    frame_id=self.frame_id,
                    stamp=stamp,
                ),
                size=[0.22, 0.16, 0.1],
            ),
        ]
        return detections

