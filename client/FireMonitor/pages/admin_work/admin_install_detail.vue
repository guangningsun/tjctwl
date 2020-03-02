<template>
	<view>
		<cu-custom bgColor="bg-gradual-dark-purple" :isBack="true">
			<block slot="content">安装详情</block>
		</cu-custom>

		<view class="cu-card">
			<view class="cu-item">
				<view class="bg-white">
					<view class="flex justify-center margin-top margin-bottom">
						<image class="margin-left-xl" :src="this.construction_image" style="width: 150upx; height: 150upx;"></image>
					</view>
				</view>

				<view class="flex cu-form-group">
					<view class="title">设备编码</view>
					<view>{{this.device_sn}}</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">设备名称</view>
					<view>{{this.device_name}}</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">业主姓名</view>
					<view>{{this.owner_str}}</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">业主电话</view>
					<view>{{this.owner_tel_str}}</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">地址</view>
					<view>{{this.device_address}}</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">安装位置</view>
					<view>{{this.install_location}}</view>
				</view>
				<view class="cu-form-group">
					<view class="padding-bottom-sm">
						<view class="title margin-top-sm">地图位置</view>
						<map :latitude="latitude" :longitude="longitude" :markers="covers"></map>
					</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">安装时间</view>
					<view>{{this.construction_createtime}}</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				latitude: 39.909,
				longitude: 116.39742,

				id: "",
				construction_createtime: "",
				deviceStatus: "",
				construction_image: "",
				device_sn: "",
				device_name: "",
				construction_worker: "",
				install_location: "",
				device_address: "",
				owner_info_list: [],

				owner_str: '',
				owner_tel_str: '',
			}
		},
		onLoad: function(option) {
			if(option.installDeviceInfo !== undefined){
				let info = JSON.parse(option.installDeviceInfo);
				this.id = info.id;
				this.construction_createtime = info.construction_createtime;
				this.deviceStatus = info.deviceStatus;
				this.construction_image = info.construction_image;
				this.device_sn = info.device_sn;
				this.device_name = info.device_name;
				this.construction_worker = info.construction_worker;
				this.install_location = info.install_location;
				this.device_address = info.device_address;
				this.owner_info_list = info.owner_info_list;
				// this.owner_info_list = [{
				// 	"owner_name": "zysun",
				// 	"owner_tel": "1521918621"
				// }, {
				// 	"owner_name": "ssdun",
				// 	"owner_tel": "151918621"
				// }, {
				// 	"owner_name": "sun",
				// 	"owner_tel": "158621"
				// }];
				this.owner_str = this.owner_info_list.map(item => item.owner_name).toString();
				this.owner_tel_str = this.owner_info_list.map(item => item.owner_tel).toString();
			}
		},
		methods: {

		}
	}
</script>

<style>

</style>
