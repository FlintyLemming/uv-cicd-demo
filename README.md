# CI/CD 演示素材

演示如何在持续集成流水线中使用 uv 来加速 Python 项目的依赖安装和测试。

## 项目结构

```
ci-demo/
├── .github/workflows/
│   └── uv-ci.yml          # GitHub Actions 配置
├── src/
│   └── calculator.py      # 示例 Python 模块
├── tests/
│   └── test_calculator.py # pytest 测试文件
└── requirements.txt       # 项目依赖
```

## 运行测试

在本地运行测试：

```bash
# 使用 uv 安装依赖并运行测试
uv pip install -r requirements.txt
uv run --with pytest python -m pytest

# 或者直接使用 uv run（推荐用于 CI）
uv run --with pytest python -m pytest
```

## CI/CD 流程

- 使用 GitHub Actions 作为示例
- 通过 `astral-sh/setup-uv@v1` 快速安装 uv
- 利用 uv 缓存加速依赖解析和安装
- 在隔离环境中运行测试

## 优势展示

1. **速度提升**：相比传统 `pip install`，uv 可减少 50-80% 的依赖安装时间
2. **依赖锁定**：确保 CI 环境与开发环境的一致性
3. **缓存利用**：uv 的全局缓存机制在 CI 中也能发挥作用