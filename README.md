# Phigros：剧情电子书与匿名全 AP 存档

**4.0.1（157）｜第九章第二部分｜非官方资源整理**

本仓库分享一份有逐段游戏内出处的剧情导读、一份匿名全 AP 修改存档。电子书无需 Root；存档仅适用于安卓、已解锁 BL 且已获取 Root 的设备。

> **存档中的 AP 来自修改，并非实际游玩成绩。仅供离线体验与资料查看，请勿用于排名、成绩认证或冒充个人成绩。** 存档经过静态校验，尚未完成真机运行及云登录测试。

## 下载

| 内容 | GitHub 下载 | 网盘备用 |
| --- | --- | --- |
| 电子书 EPUB | [下载 EPUB](https://github.com/yskzctx/phigros-story-and-save/releases/download/v4.0.1-157/Phigros-story-guide-4.0.1.epub) | [蓝奏云](https://wwaxo.lanzn.com/i9vzB4apst3a)，提取码 **dvn7** |
| 匿名全 AP 安卓 Root 存档 XML | [下载存档](https://github.com/yskzctx/phigros-story-and-save/releases/download/v4.0.1-157/com.PigeonGames.Phigros.v2.playerprefs.xml) | [蓝奏云](https://wwaxo.lanzn.com/ilDe24apst4b)，**无需密码** |

[查看全部发布文件](https://github.com/yskzctx/phigros-story-and-save/releases) · [哔哩哔哩介绍视频](https://www.bilibili.com/video/BV1QFHh6FEVA/)

Releases 仅提供电子书 EPUB 本体和可直接替换的加密存档 XML；主分支保留源码、文档和核对记录。

## 剧情电子书

- 覆盖 15 个章节组、503 条客户端收藏品记录，包含第九章第二部分新增的 20 条资料。
- 梳理世界设定、人物、主线与支线、时间线及解谜线索。
- 每个故事段落标明“收藏品 → 章节 → 条目名称”，点击出处可跳转到对应附录条目。
- 采用重新撰写的归纳与解读，区分明确叙述、角色说法和综合解释。**含结局剧透。**

这是非官方导读。503 条覆盖指本版收藏品数据库，不能等同于已穷尽所有演出、对话和悬案。详见 [阅读说明](docs/book-guide.md)，或直接查看 [Markdown 正文](book/story-guide.md)。

## 匿名全 AP 修改存档

| 内容 | 本版范围 |
| --- | --- |
| 歌曲与常规谱面 | 327 首歌曲、1037 张常规谱面全部 1000000 分、100% 准确率，并带有全连标记 |
| 收藏品 | 503 条，获得及已读状态已写入 |
| 头像 | 109 个头像获得标记 |
| 第九章第二部分 | 曲目解锁、剧情通关及结局完成字段已写入 |
| 特别挑战 | 5 档生命值选项开放 |
| 资料 | 统一昵称 Player，简介为空，原个人标识已移除 |

AP 指满分，FC 指全连。SP 演出谱面不计入上述常规成绩数量；Rks 不强制指定为 17。文件不包含原始私人备份或普通保留成绩版存档。

### 使用条件和替换位置

**安卓手机 + BL（Bootloader）已解锁 + 已获取 Root，三项均需满足。** 仅解锁 BL、没有 Root 的设备，以及 iOS 设备，不适用本存档。

先强制停止游戏，另行备份原存档，再用下载的同名加密 XML 替换：

```text
/data/data/com.PigeonGames.Phigros/shared_prefs/com.PigeonGames.Phigros.v2.playerprefs.xml
```

保留文件原有所有者、用户组和权限。发行版提供的是可直接替换的加密 XML。建议断网首次启动；异常时停止游戏并恢复备份。

**替换会覆盖原成绩与设置；云存档下载可能覆盖本地修改。** 本存档按 4.0.1（157）制作，其他版本兼容性未经验证。完整步骤见 [存档使用说明](docs/save-guide.md)。

## 检查与版本记录

- 存档：加密往返、常规谱面全 AP、503 条收藏品覆盖和个人标识清理检查通过；**尚未真机测试**。
- 电子书：EPUBCheck 检查无错误、无警告；1,229 个内部链接核对无断链。
- 源文件完整性：[SHA256SUMS](SHA256SUMS)。校验命令：`python scripts/verify_release.py`。
- 成品文件哈希：[发行附件清单](verification/release-assets.json)。下载成品后可运行 `python scripts/verify_release.py --artifacts-dir 下载目录`。

[核对说明](docs/verification.md) · [更新记录](CHANGELOG.md) · [反馈方法](CONTRIBUTING.md) · [权利与来源说明](RIGHTS.md)

## 仓库目录

```text
book/           电子书 Markdown 正文与样式源码
media/          投稿文案与口播分镜源码
data/           503 条收藏品的标题和游戏位置索引
docs/           阅读、使用和核对说明
verification/   已完成的检查记录与客户端来源信息
scripts/        本地文件完整性校验脚本
```

本仓库不包含游戏安装包、完整资源包或整套剧情原文，不代表鸽游官方。
