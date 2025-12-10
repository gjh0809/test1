from .models import Detection, GraspCandidate
from .handeye import HandEye


def map_lane(det: Detection) -> str:
    cls_lane = {
        "red_box": "lane_A",
        "blue_box": "lane_B",
        "green_box": "lane_C",
    }
    return cls_lane.get(det.cls, "lane_misc")


class GraspPlanner:
    """Generate grasp candidates from detection results."""

    def __init__(self, handeye: HandEye, safe_offset: float = 0.02):
        self.handeye = handeye
        self.safe_offset = safe_offset

    def generate(self, det: Detection) -> list[GraspCandidate]:
        pose_base = self.handeye.to_base(det.pose_cam)
        offset = [0.0, 0.0, det.size[2] / 2 + self.safe_offset]
        pose_base.position = [
            pose_base.position[0] + offset[0],
            pose_base.position[1] + offset[1],
            pose_base.position[2] + offset[2],
        ]
        # Keep vertical orientation for top suction
        pose_base.quat = [0.0, 0.0, 0.0, 1.0]
        score = det.score
        return [GraspCandidate(pose_base=pose_base, score=score, target_lane=map_lane(det))]

