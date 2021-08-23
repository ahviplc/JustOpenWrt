#
ZZZ="package/lean/default-settings/files/zzz-default-settings"

sed -i 's/192.168.1.1/192.168.1.100/g' package/base-files/files/bin/config_generate              # 修改默认IP地址为192.168.1.100,此为管理页面访问ip

# sed -i 's/luci-theme-bootstrap/luci-theme-argon/g' feeds/luci/collections/luci/Makefile        # 选择argon为默认主题
sed -i "s/OpenWrt /LC compiled in $(TZ=UTC-8 date "+%Y.%m.%d") @ OpenWrt /g" $ZZZ                # 增加个性名字 LC
sed -i '/CYXluq4wUazHjmCDBCqXF/d' $ZZZ                                                           # 设置密码为空
