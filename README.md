# 分拣系统示例（Cursor 开发）

本仓库包含一个简化的分拣系统示例，演示视觉检测、手眼变换、抓取规划、运动执行与状态机的基本流程。代码为纯 Python，可在本地快速运行。

## 主要内容
- `sorter_demo/`：核心模块（数据模型、手眼标定转换、抓取规划、视觉与运动仿真、流水线与状态机）。
- `app.py`：运行单次分拣流程的示例入口。
- `tests/`：基于 unittest 的基础用例。

## 快速开始（单次或循环）
```bash
# 单次运行（默认 5 次循环，含间隔）
python app.py

# 指定循环次数与间隔
python app.py --iterations 10 --sleep 0.1

# 无限循环（Ctrl+C 终止）
python app.py --iterations 0
```

运行后将输出每次分拣/拆垛的结果与累计成功次数。

## 测试
```bash
python -m unittest discover tests
```
