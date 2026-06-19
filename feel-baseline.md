# 手感基准（锁定于 2026-06-15）

参考游戏：微信跳一跳
核心操作：按住蓄力 → 松手跳跃
禁止感觉：穿模/边缘误判、输入延迟、节奏太慢

## 手感参数
```
CHARGE_SPEED:     0.9       → 约 1.1 秒蓄满
MIN_JUMP_DIST:    20        → 最短跳
MAX_JUMP_DIST:    320       → 最远跳
JUMP_DURATION:    0.55s     → 跳跃时长
PLATFORM_DIST:    120~280   → 平台间距
PLATFORM_SIZE:    50~100    → 平台宽/深
PLATFORM_H:       30        → 平台高度
LANDING_MARGIN:   8         → 落地宽容边距
PERFECT:          >85%      → 完美判定
NICE:             >60%      → 不错判定
CAMERA_LERP:      4.0       → 镜头跟随
ANGLE_VARIATION:  ±0.35rad  → 方向变化
```

## 投影公式
```
sx = (rx - rz) * cos30 + w/2
sy = -(rx + rz) * sin30 - wy + h*0.62
平台方向: -Z = 屏幕右上
```

## 关键修复
- 玩家站在平台顶部 (PLATFORM_H)，非地面
- 跳跃起点用玩家实际位置，非平台中心
- 跳跃弧线偏移 PLATFORM_H
