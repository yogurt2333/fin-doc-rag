# fin-doc-rag

金融文档 RAG：中文金融合规文本 + 英文 SEC 10-K 年报的问答与检索（个人项目，面向 AI 应用工程师求职）。

## 项目定位

一个统一的问答系统，覆盖两个金融垂直场景：

1. **中文合规（监管科技）**：基于 Compliance-to-Code（361 部北交所金融监管规则、1,159 条合规单元），重点处理条款交叉引用与引用溯源。
2. **英文投研（年报问答）**：基于 Multi-Doc-2025（2,327 条 QA，179 份标普 500 公司 SEC 10-K 年报），覆盖跨公司、跨年度与文本-表格混合推理。

管线：文档解析 → 切分 → 向量化 → 检索 → Rerank → 引用溯源 → 生成。合规问答与年报问答对引用准确性、跨文档检索要求都很高——这是展示 RAG 工程能力（而非框架套壳）的强场景。

## 完成定义（验收标准）

- 能对着架构图讲 10 分钟，被追问不慌
- 在 Multi-Doc-2025 官方测试集上跑出可报的数字（检索命中率 / 端到端准确率，按难度分层）+ 合规场景评测集
- 至少 3 个 bad case 及对应调优记录
- Docker 部署，提供可公开访问的 URL

## 数据来源与许可

- **Compliance-to-Code**（中文合规）：[GitHub](https://github.com/AlexJJJChen/Compliance-to-Code) / HuggingFace GPS-Lab/Compliance-to-Code，论文 [arXiv:2505.19804](https://arxiv.org/abs/2505.19804)；底层为北交所公开发布的监管规则；**CC BY-NC 4.0（非商用）**
- **Multi-Doc-2025**（英文年报）：[HuggingFace](https://huggingface.co/datasets/Anonymous-Team-HC-RAG/Multi-Doc-2025)，论文 HC-RAG（evidence-centric RAG over heterogeneous financial filings）；底层为 SEC EDGAR 公开的 10-K 年报；**CC BY 4.0**
- 两个数据集**都不提交进仓库**，由下载脚本拉取，使用与引用时注明来源（本项目为个人学习与求职演示用途）

## 任务跟踪

任务以 GitHub Issues 跟踪（约定见 `docs/agents/issue-tracker.md`）。
