<template>
	<view>
		<cu-custom bgColor="bg-gradual-dark-purple" :isBack="true">
			<block slot="content">隐患上报</block>
		</cu-custom>

		<view class="cu-card">
			<view class="cu-item">
				<view class="flex cu-form-group">
					<view class="title">上报人</view>
					<view>{{reporter}}</view>
				</view>

				<!-- <view class="cu-form-group">
					<view class="title">隐患等级</view>
					<picker @change="classPickerChange" :value="class_picker_index" :range="class_picker">
						<view class="picker text-gray">
							{{class_picker_index>-1 ? class_picker[class_picker_index]:'选择隐患等级'}}
						</view>
					</picker>
				</view>

				<view class="cu-form-group">
					<view class="title">隐患类型</view>
					<picker @change="typePickerChange" :value="type_picker_index" :range="type_picker">
						<view class="picker text-gray">
							{{type_picker_index>-1 ? type_picker[type_picker_index]:'选择隐患类型'}}
						</view>
					</picker>
				</view> -->

				<!-- <view class="cu-form-group">
					<view class="title">隐患楼层</view>
					<picker @change="floorPickerChange" :value="floor_picker_index" :range="floor_picker">
						<view class="picker text-gray">
							{{floor_picker_index>-1 ? floor_picker[floor_picker_index]:'选择隐患楼层'}}
						</view>
					</picker>
				</view> -->

				<view class="cu-form-group">
					<view class="title">隐患楼层</view>
					<input class="text-right" placeholder="请输入隐患楼层" name="input" v-model="floor"></input>
				</view>

				<view class="cu-form-group">
					<view class="title">具体位置</view>
					<input class="text-right" placeholder="请输入具体位置" name="input" v-model="address"></input>
				</view>

				<view class="cu-form-group align-start">
					<view class="title">隐患描述</view>
					<textarea class="text-right" maxlength="-1" :disabled="modalName!=null" @input="textareaDangerDescInput" v-model="desc"
					 placeholder="请输入隐患描述"></textarea>
				</view>

				<view class="cu-bar bg-white margin-top solid-top">
					<view class="action">
						图片上传
					</view>
					<view class="action">
						{{imgList.length}}/1
					</view>
				</view>
				<view class="cu-form-group margin-bottom-sm">
					<view class="grid col-4 grid-square flex-sub">
						<view class="bg-img" v-for="(item,index) in imgList" :key="index" @tap="ViewImage" :data-url="imgList[index]">
							<image :src="imgList[index]" mode="aspectFill"></image>
							<view class="cu-tag bg-red" @tap.stop="DelImg" :data-index="index">
								<text class='cuIcon-close'></text>
							</view>
						</view>
						<view class="solids" @tap="ChooseImage" v-if="imgList.length<4">
							<text class='cuIcon-cameraadd'></text>
						</view>
					</view>
				</view>

			</view>


			<view class="justify-between bottom-box">
				<view class="padding flex flex-direction">
					<button class="cu-btn bg-dark-purple lg" @click="onAddDanger">提交</button>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				class_picker_index: -1,
				class_picker: ["11", "22", "33"],
				type_picker_index: -1,
				type_picker: ["tt", "tt2", "tt3"],
				floor_picker_index: -1,
				floor_picker: ["ff", "ff2", "ff3"],
				textareaDangerDescValue: "",
				imgList: [],
				reporter: '',
				floor: '',
				address: '',
				desc: '',
				modalName: null,
			}
		},
		onLoad() {
			this.reporter = uni.getStorageSync('key_user_name');
		},
		methods: {
			classPickerChange(e) {
				if (this.class_picker_index === -1) {
					this.class_picker_index = 0;
				} else {
					this.class_picker_index = e.detail.value;
				}
				this.checkBtnEnable();
			},
			typePickerChange(e) {
				if (this.type_picker_index === -1) {
					this.type_picker_index = 0;
				} else {
					this.type_picker_index = e.detail.value;
				}
				this.checkBtnEnable();
			},
			textareaDangerDescInput(e) {
				this.textareaDangerDescValue = e.detail.value
			},
			floorPickerChange(e) {
				if (this.floor_picker_index === -1) {
					this.floor_picker_index = 0;
				} else {
					this.floor_picker_index = e.detail.value;
				}
				this.checkBtnEnable();
			},
			checkBtnEnable() {
				if (this.date == '' ||
					this.class_picker[this.class_picker_index] == '' ||
					this.class_picker[this.class_picker_index] == undefined ||
					this.type_picker[this.type_picker_index] == '' ||
					this.type_picker[this.type_picker_index] == undefined ||
					this.floor_picker[this.floor_picker_index] == '' ||
					this.floor_picker[this.floor_picker_index] == undefined
				) {
					this.btn_disabled = true;
				} else {
					this.btn_disabled = false;
				}
			},
			DelImg(e) {
				uni.showModal({
					title: '删除照片',
					content: '确定要删除这张照片吗？',
					cancelText: '否',
					confirmText: '是',
					success: res => {
						if (res.confirm) {
							this.imgList.splice(e.currentTarget.dataset.index, 1)
						}
					}
				})
			},
			ChooseImage() {
				uni.chooseImage({
					count: 1, //默认9
					sizeType: ['original', 'compressed'], //可以指定是原图还是压缩图，默认二者都有
					sourceType: ['album', 'camera'],
					success: (res) => {
						if (this.imgList.length != 0) {
							this.imgList = this.imgList.concat(res.tempFilePaths)
						} else {
							this.imgList = res.tempFilePaths
						}
					}
				});
			},
			successCallback(rsp) {
				if (rsp.data.error === 0) {
					uni.hideLoading();
					setTimeout(function() {
						uni.navigateBack({
							delta: 1
						});
					}, 1500);
				}
			},
			failCallback(err) {
				uni.hideLoading();
				console.log('api_add_danger failed', err);
			},
			completeCallback(rsp) {},
			onAddDanger() {
				uni.showLoading({
					title: '上报中...'
				});
				if (this.isEmpty(this.floor) ||
					this.isEmpty(this.address) ||
					this.isEmpty(this.desc)
					// || this.imgList.length === 0
				) {
					this.showToast('请正确填写信息');
				} else {
					var timestamp = Date.parse(new Date()) / 1000;
					let params = {
						danger_create_user: this.reporter,
						danger_floor_level: this.floor,
						danger_address_detail: this.address,
						danger_desc: this.desc,
						// danger_image: this.,
						danger_create_time: timestamp,
					};
					this.requestWithMethod(
						getApp().globalData.api_danger,
						"POST",
						params,
						this.successCallback,
						this.failCallback,
						this.completeCallback);
			}
		}
	}
	}
</script>

<style>

</style>
