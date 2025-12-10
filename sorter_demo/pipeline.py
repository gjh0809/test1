from typing import Iterable

from .models import Detection
from .planner import GraspPlanner
from .motion import MotionService
from .vision import VisionService
from .state_machine import StateMachine


class SorterPipeline:
    """Simple sequential pipeline that processes detections and triggers motions."""

    def __init__(
        self,
        vision: VisionService,
        planner: GraspPlanner,
        motion: MotionService,
        sm: StateMachine,
    ):
        self.vision = vision
        self.planner = planner
        self.motion = motion
        self.sm = sm

    def run_once(self) -> bool:
        frame = self.vision.capture()
        detections: Iterable[Detection] = self.vision.detect(frame)
        if not detections:
            self.sm.handle("detect_empty")
            return False

        # Prioritize higher-score targets first
        for det in sorted(detections, key=lambda d: -d.score):
            grasps = self.planner.generate(det)
            grasps = sorted(grasps, key=lambda g: -g.score)
            for g in grasps:
                if not self.motion.plan(g.pose_base, g.target_lane):
                    self.sm.handle("plan_fail")
                    continue
                if not self.motion.execute():
                    self.sm.handle("exec_fail")
                    continue
                self.sm.handle("success")
                return True

        self.sm.handle("no_success")
        return False

