# %%
import time
import os
import json

# %% 读取配置文件和种子列表
try:
    with open("config.json", "r") as f:
        config = json.load(f)
except FileNotFoundError:
    print("请先配置 config.json 文件")
    exit(1)

with open("torrents.json", "r") as f:
    torrents = json.load(f)

# %% 生成下载脚本
sh = ""
count = 0
total_vol = 0
for torrent in torrents:
    if (
        torrent["vol_unit"] == "T"
        or torrent["vol_unit"] == "G"
        or torrent["vol_unit"] == "K"
    ):
        continue
    if config["min_size"] < torrent["vol_val"] <= config["max_size"]:
        count += 1
        total_vol += torrent["vol_val"]
        if config["ipv6"]:
            sh += (
                config["url_open_cmd"]
                + ' "https://kp.m-team.cc/download.php?id=%s&passkey=%s&https=1&ipv6=1"\n'
            ) % (torrent["id"], config["passkey"])
        else:
            sh += (
                config["url_open_cmd"]
                + ' "https://kp.m-team.cc/download.php?id=%s&passkey=%s&https=1"\n'
            ) % (torrent["id"], config["passkey"])
print("满足条件的种子数量为：%d 个" % (count))
print("满足条件的种子总大小为：%.2f GB" % (total_vol / 1024))

# %% 执行下载脚本
if config["if_download"]:
    for line in sh.split("\n"):
        os.system(line)
        time.sleep(0.5)
