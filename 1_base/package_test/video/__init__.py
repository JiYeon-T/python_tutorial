# 在模块 __init__.py 文件中定义 __all__ 列表的作用:
# 当外部直接使用 from video import * 时, 会自动导入这 __all__ 中定义的模块
__all__ = ["mp4", "wav"]