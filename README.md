# fin-doc-rag

金融合规文档 RAG：北交所监管规则的知识库问答与要点检索（个人项目，面向 AI 应用工程师求职）。

## 项目定位

基于公开学术数据集 Compliance-to-Code（361 部北交所金融监管规则、1,159 条合规单元），构建"监管文本 → 切分 → 向量化 → 检索 → 引用溯源 → 生成"的问答系统。合规问答对引用准确性、跨条款检索的要求很高——这是展示 RAG 工程能力（而非框架套壳）的强场景。

## 完成定义（验收标准）

- 能对着架构图讲 10 分钟，被追问不慌
- 20 条问答评测集 + 改进前后数据对比
- 至少 3 个 bad case 及对应调优记录
- Docker 部署，提供可公开访问的 URL

## 数据来源与许可

- 数据集：Compliance-to-Code（[GitHub](https://github.com/AlexJJJChen/Compliance-to-Code) / HuggingFace GPS-Lab/Compliance-to-Code），论文 [arXiv:2505.19804](https://arxiv.org/abs/2505.19804)
- 底层文档：北交所公开发布的金融监管规则
- 许可：CC BY-NC 4.0（非商用）。本项目为个人学习与求职演示用途；数据集**不提交进仓库**，运行 `scripts/download_data.py` 拉取，使用与引用时注明来源

## 任务跟踪

任务以 GitHub Issues 跟踪（约定见 `docs/agents/issue-tracker.md`）。
