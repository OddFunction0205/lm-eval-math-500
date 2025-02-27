# 介绍

本仓库基于https://github.com/EleutherAI/lm-evaluation-harness 框架，完成了math 500数据集的评测。主要是实现了lm_eval/tasks/math500文件夹中math500.yaml和utils.py文件的实现。

该框架同时还提供了通过Open API测评GPT类模型的命令。

该框架同时还提供了clash for linux，方便没有在服务器上 装梯子的用户使用，以便从huggingface上下载MATH 500数据和预训练模型

# 使用说明

## 1.搭梯子（如果有需要）

首先打开clash文件夹，把补充好config.yaml。导入配置教程参考：https://www.bilibili.com/video/BV1mJ1sYKEoK/?spm_id_from=333.337.searchcard.all.click&vd_source=0cf0e7a265a93dd5f6a617cc12842466

开启代理的步骤：
```
cd clash
chmod +x clash
./clash -d .
```
出现类似的信息，说明梯子启动正常：

```
(base) root@autodl-container-e3534a912f-635cb8ff:/lm-evaluation-harness/clash# ./clash -d .
INFO[0000] Start initial compatible provider 故障转移
INFO[0000] Start initial compatible provider 自动选择
INFO[0000] Start initial compatible provider SDK DNS
INFO[0000] RESTful API listening at: 127.0.0.1:9090
INFO[0000] Mixed(http+socks) proxy listening at: [::]:7890
```

然后保持这个终端不要关闭，再开一个新的终端，执行以下命令：
```
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
```

于是网络连接的问题就被顺利解决了。

## 进行测评

在终端中运行下列命令，即可进行测评

```
export OPENAI_API_KEY=（换成自己的API）
lm_eval --model openai-completions \
--model_args model=gpt-4o-mini-2024-07-18 \
--tasks math500
```

这样，就可以测评gpt-4o-mini-2024-07-18模型在MATH 500数据集上的表现了。如果需要替换测试模型，可以将gpt-4o-mini-2024-07-18换乘其他的。具体模型名称可以参考：https://platform.openai.com/docs/models
