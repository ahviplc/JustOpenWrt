**English** | [使用 GitHub Actions 云编译 OpenWrt - 图文 - 中文](https://p3terx.com/archives/build-openwrt-with-github-actions.html)

# Slogan

> JustOpenWrt,你的专属❤软路由❤.

# Actions-OpenWrt

> https://github.com/P3TERX/Actions-OpenWrt

# Copy That By LC

```markdown
云编译OpenWrt，添加梦寐以求的插件，一次成功！_哔哩哔哩_bilibili
https://www.bilibili.com/video/BV1SL411n7xG

openWrt云编译进阶教程_哔哩哔哩_bilibili
https://www.bilibili.com/video/BV1J44y1y7iE

GitHub - fw876/helloworld -【ssr-plus】
https://github.com/fw876/helloworld

GitHub - vernesong/OpenClash: A Clash Client For OpenWrt
https://github.com/vernesong/OpenClash

openwrt云编译教程 – Doctor's Secret
http://www.dsecret.com/0069.html

Index of /lede/x86_64/ -【https://github.com/bleach1991/lede】
https://imgs.mpdn.fun:8443/lede/x86_64/

GitHub - bleach1991/lede
https://github.com/bleach1991/lede

OpenWRT 软件包中文对照说明 - 资源分享 - 网吧软件
http://www.wbini.com/id-12.html

DDNSTO 内网穿透
https://www.ddnsto.com/

GitHub - linkease/docker_ddnsto: docker for ddnsto
https://github.com/linkease/docker_ddnsto

Index of /binary/ddnsto/synology/ - KoolShare 固件下载服务器
https://firmware.koolshare.cn/binary/ddnsto/synology/

GitHub - tsl0922/ttyd: Share your terminal over the web
https://github.com/tsl0922/ttyd

GitHub - lisaac/luci-app-dockerman: Docker Manager interface for LuCI
https://github.com/lisaac/luci-app-dockerman
```

> https://github.com/facerleo/openwrt-owner

> https://github.com/ahviplc/JustOpenWrt

```markdown
To connect to this session copy and paste the following into a terminal or browser:
CLI: ssh at6ACtVJN8vwsVku7dawQRAYk@nyc1.tmate.io
URL: https://tmate.io/t/at6ACtVJN8vwsVku7dawQRAYk
TIPS: Run 'touch /tmp/continue' to continue to the next step.

# 命令

cd openwrt

make menuconfig

进行下面一些列配置之后
no1. Target Images 
-> 选中 Build GRUB images(*) Build LiveCD images(ISO) Build VMware images files(VMDK)
-> Kernet partition szie (iN MB) 16 改为 100  和 Root filesystem partition szie (iN MB) 160 改为 260

no2. Global build settings
Enable ipv6 support in packages 保持默认即可

no3. LuCI > application
选中你喜欢的插件
推荐必选
docker | ssr-plus | ddns | clash | commands | ttyd | adblock | ***

no4. LuCI > Themes
推荐选中的主题
argon_new
或其他你喜欢的
atmaterial | ifit | material | netgear | opentomato | opentomcat | opentopd

执行退出命令
logout
```

[![LICENSE](https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square&label=LICENSE)](https://github.com/P3TERX/Actions-OpenWrt/blob/master/LICENSE)
![GitHub Stars](https://img.shields.io/github/stars/P3TERX/Actions-OpenWrt.svg?style=flat-square&label=Stars&logo=github)
![GitHub Forks](https://img.shields.io/github/forks/P3TERX/Actions-OpenWrt.svg?style=flat-square&label=Forks&logo=github)

A template for building OpenWrt with GitHub Actions

## Usage

- Click the [Use this template](https://github.com/P3TERX/Actions-OpenWrt/generate) button to create a new repository.
- Generate `.config` files using [Lean's OpenWrt](https://github.com/coolsnowwolf/lede) source code. ( You can change it through environment variables in the workflow file. )
- Push `.config` file to the GitHub repository.
- Select `Build OpenWrt` on the Actions page.
- Click the `Run workflow` button.
- When the build is complete, click the `Artifacts` button in the upper right corner of the Actions page to download the binaries.

## Tips

- It may take a long time to create a `.config` file and build the OpenWrt firmware. Thus, before create repository to build your own firmware, you may check out if others have already built it which meet your needs by simply [search `Actions-Openwrt` in GitHub](https://github.com/search?q=Actions-openwrt).
- Add some meta info of your built firmware (such as firmware architecture and installed packages) to your repository introduction, this will save others' time.

## Credits

- [Microsoft Azure](https://azure.microsoft.com)
- [GitHub Actions](https://github.com/features/actions)
- [OpenWrt](https://github.com/openwrt/openwrt)
- [Lean's OpenWrt](https://github.com/coolsnowwolf/lede)
- [tmate](https://github.com/tmate-io/tmate)
- [mxschmitt/action-tmate](https://github.com/mxschmitt/action-tmate)
- [csexton/debugger-action](https://github.com/csexton/debugger-action)
- [Cowtransfer](https://cowtransfer.com)
- [WeTransfer](https://wetransfer.com/)
- [Mikubill/transfer](https://github.com/Mikubill/transfer)
- [softprops/action-gh-release](https://github.com/softprops/action-gh-release)
- [ActionsRML/delete-workflow-runs](https://github.com/ActionsRML/delete-workflow-runs)
- [dev-drprasad/delete-older-releases](https://github.com/dev-drprasad/delete-older-releases)
- [peter-evans/repository-dispatch](https://github.com/peter-evans/repository-dispatch)

## License

[MIT](https://github.com/P3TERX/Actions-OpenWrt/blob/main/LICENSE) © [**P3TERX**](https://p3terx.com)
