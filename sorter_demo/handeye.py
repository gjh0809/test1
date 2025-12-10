from .models import Pose


def _mat_vec_mul(mat4, vec4):
    return [sum(mat4[i][j] * vec4[j] for j in range(4)) for i in range(4)]


class HandEye:
    """Convert poses from camera frame to robot base frame using fixed extrinsic."""

    def __init__(self, T_cam_base: list[list[float]]):
        if len(T_cam_base) != 4 or any(len(row) != 4 for row in T_cam_base):
            raise ValueError("T_cam_base must be 4x4 homogeneous matrix")
        self.T = T_cam_base

    def to_base(self, pose_cam: Pose) -> Pose:
        p = pose_cam.position + [1.0]
        p_base = _mat_vec_mul(self.T, p)
        # 为简化演示，假设相机与基坐标系无相对旋转，直接复用四元数。
        quat_base = pose_cam.quat
        return Pose(
            position=p_base[:3],
            quat=quat_base,
            frame_id="base",
            stamp=pose_cam.stamp,
        )

