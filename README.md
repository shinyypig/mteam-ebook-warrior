# M-Team 电子书战士

本项目保存了截至 2023 年 4 月 25 日 M-Team 所有电子书的种子信息，共计 4,233 个。可以利用本项目下的`get_torrents.py`脚本下载所需要的种子文件。

## 使用方法

在项目根目录下创建一个`config.json`文件，具体示例可参照`config.example.json`。

各参数项说明如下：

```json
{
    // 为 M-Team 的用户 passkey，可在已下载的种子中，或者从tracker中找到
    "passkey": "xxx",
    // 要下载的电子书大小的最小值，单位为 MB
    "min_size": 1,
    // 要下载的电子书大小的最大值，单位为 MB
    "max_size": 20,
    // 是否使用 IPv6 地址
    "ipv6": false
    // 打开 url 的命令，macOS 下为 open，其余系统请自行修改
    "url_open_cmd": "open"
    // 是否下载种子文件，如果为 false，则输出对应的统计结果
    "if_download": false
}
```

需要注意的是，代码只在 macOS 下测试过，使用`open`命令来打开种子文件对应的 url（wget 会被拦截，不清楚为什么）。如果是其他系统，自行查找对应的指令。
