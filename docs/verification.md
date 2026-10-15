# 核对范围

本版目标为 Phigros 4.0.1（157）。2026-10-03 整理公开分享版本。

## 客户端来源

通过公开 APKCombo 下载包读取客户端清单、收藏品数据库和章节配置，确认包名、版本 4.0.1、构建号 157。来源及资源 SHA-256 记录见 [`client-source.json`](../verification/client-source.json)。

该来源是 Google Play 公开分发镜像，不是对 TapTap 安装包逐字节一致性的验证，也不代表官方审校。仓库不提供游戏安装包或完整资源包。

## 存档

详细结果见 [`save.json`](../verification/save.json)。

- 327 首歌曲、1037 张常规谱面的满分、准确率及全连字段已核对。
- 全部 503 条收藏品的获得及已读状态、109 个头像获得标记已覆盖。
- 第九章二阶段通关字段、有效推进枚举、结局完成标记与客户端结束流程核对；中途续播字段已清除。
- 加密后再解密的回读检查通过；公开版本已清理原个人标识。
- **没有真机运行、联网登录或云同步稳定性测试。** 写入字段不能等同于已实测全部手机上的显示和行为。

## 电子书

详见 [`book.json`](../verification/book.json) 与 [`epubcheck.json`](../verification/epubcheck.json)。

- 503 条收藏品定位，20 条新增资料均在正文中引用。
- 131 处正文出处块，1,229 个内部链接检查，未发现断链。
- EPUBCheck 5.4.0 检查：无致命错误、错误或警告。

## 视频

详见 [`video.json`](../verification/video.json)。

1920×1080、30 fps、H.264 视频与 48 kHz AAC 音频，约 106 秒。字幕文本与口播核对、整段视频解码检查通过。视频展示来自电子书与说明页面，未提供真机游戏运行录像；配音是合成语音。

## 仓库文件

在仓库根目录执行：

```sh
python scripts/verify_release.py
```

默认核对主分支源文件哈希、503 条索引及核对记录。成品放在 Releases，下载后可另行核对：

```sh
python scripts/verify_release.py --artifacts-dir /path/to/downloaded-assets
```

此模式检查下载目录中已存在的已登记 EPUB 和 XML 文件的大小与哈希，不要求下载所有附件。这不替代真机测试。
