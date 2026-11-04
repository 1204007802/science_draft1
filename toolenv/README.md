# toolenv —— 远程执行环境

这个目录是**工具库在仓库里的投影**。工作流启动时从 `toolenv/requirements.txt` 安装，
让远程环境和本地 `envs/py-sci` 用同一套钉死版本。

- `requirements.txt` —— 由 `Science/tools/src/py-sci/requirements.txt` 同步，不要手改
- `selfcheck.py` —— 验证环境；跑一次看到 `TOOLENV_OK` 即正常

研究员**不需要**自己装依赖，也不需要提交这个目录。
