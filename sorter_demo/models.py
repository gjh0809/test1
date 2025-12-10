from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Pose:
    position: List[float]  # [x, y, z]
    quat: List[float]  # [x, y, z, w]
    frame_id: str
    stamp: float


@dataclass
class Detection:
    bbox: Tuple[int, int, int, int]  # (x1, y1, x2, y2)
    cls: str
    score: float
    pose_cam: Pose
    size: List[float]  # [l, w, h]


@dataclass
class GraspCandidate:
    pose_base: Pose
    score: float
    target_lane: str

