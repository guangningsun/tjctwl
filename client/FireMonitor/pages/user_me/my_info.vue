<template>
	<view>
		<cu-custom bgColor="bg-gradual-dark-purple" :isBack="true">
			<block slot="content">帐户管理</block>
		</cu-custom>

		<view class="cu-item">
			<view class="cu-form-group margin-top">
				<view class="flex align-center">
					<text class="text-lg">头像</text>
				</view>
				<view class="margin cu-avatar lg round" style="background-image:url(../../static/me/head3.png);"></view>
			</view>
		</view>

		<view class="cu-list menu margin-top">
			<view class="cu-item" :class="menuArrow?'arrow':''" @tap="showModal" data-target="ModifyNicknameModal">
				<view class="content">
					<text class="text-lg">昵称</text>
				</view>
				<view class="action">
					<text class="text-grey text-lg margin-right-sm">昵称XX</text>
					<text class="cuIcon-right text-gray"></text>
				</view>
			</view>
			<view class="cu-item" :class="menuArrow?'arrow':''" @tap="showModal" data-target="ModifyTelModal">
				<view class="content">
					<text class="text-lg">手机</text>
				</view>
				<view class="action">
					<text class="text-grey text-lg margin-right-sm">17499939339</text>
					<text class="cuIcon-right text-gray"></text>
				</view>
			</view>
			<view class="cu-item" :class="menuArrow?'arrow':''" @tap="gotoModifyPass">
				<view class="content">
					<text class="text-lg">密码</text>
				</view>
				<view class="action">
					<text class="cuIcon-right text-gray"></text>
				</view>
			</view>
		</view>

		<!-- 修改telmodal -->
		<view class="cu-modal" :class="modalName=='ModifyTelModal'?'show':''">
			<view class="cu-dialog">
				<view class="cu-bar bg-white justify-end">
					<view class="content">修改电话</view>
					<view class="action" @tap="hideModal">
						<text class="cuIcon-close text-light-purple"></text>
					</view>
				</view>

				<form>
					<view class="cu-form-group">
						<view class="title">手机号码</view>
						<input class="text-left" placeholder="输入新手机号" name="input"></input>
					</view>

					<view class="cu-form-group">
						<view class="title">验 证 码 </view>
						<input class="text-left" placeholder="请输入验证码" name="input"></input>
						<view class="cu-btn bg-purple light" @click="veryfiying" v-if="state===false">获取验证码</view>
						<view class="cu-btn bg-grey" v-if="state===true">倒计时{{ currentTime }}s</view>
					</view>
				</form>

				<view class="cu-bar bg-white justify-end">
					<view class="action">
						<button class="cu-btn line-green text-purple" @tap="hideModal">取消</button>
						<button class="cu-btn bg-gradual-dark-purple margin-left" @tap="onConfirmModify">修改</button>
					</view>
				</view>
			</view>
		</view>

		<!-- 修改昵称modal -->
		<view class="cu-modal" :class="modalName=='ModifyNicknameModal'?'show':''">
			<view class="cu-dialog">
				<view class="cu-bar bg-white justify-end">
					<view class="content">修改昵称</view>
					<view class="action" @tap="hideModal">
						<text class="cuIcon-close text-light-purple"></text>
					</view>
				</view>

				<form>
					<view class="cu-form-group">
						<view class="title">昵称</view>
						<input class="text-left" placeholder="输入新昵称" name="input"></input>
					</view>
				</form>

				<view class="cu-bar bg-white justify-end">
					<view class="action">
						<button class="cu-btn line-green text-purple" @tap="hideModal">取消</button>
						<button class="cu-btn bg-gradual-dark-purple margin-left" @tap="onConfirmModify">修改</button>
					</view>
				</view>
			</view>
		</view>

	</view>
</template>

<script>
	export default {
		data() {
			return {
				state: false, //是否开启倒计时
				totalTime: 60, //总时间，单位秒
				recordingTime: 0, //记录时间变量
				currentTime: 0, //显示时间变量
				modalName: null,
			}
		},
		methods: {
			showModal(e) {
				this.modalName = e.currentTarget.dataset.target
			},
			hideModal(e) {
				this.modalName = null
			},
			gotoModifyPass() {
				uni.navigateTo({
					url: './modify_pass'
				})
			},
			veryfiying() {
				//把显示时间设为总时间
				this.currentTime = this.totalTime;
				//开始倒计时
				this.state = true;
				//执行倒计时
				this.veryfiyingTime();
			},
			veryfiyingTime() {
				let that = this;
				//判断是否开启
				if (this.state) {
					//判断显示时间是否已到0，判断记录时间是否已到总时间
					if (this.currentTime > 0 && this.recordingTime <= this.totalTime) {
						//记录时间增加 1
						this.recordingTime = this.recordingTime + 1;
						//显示时间，用总时间 - 记录时间
						this.currentTime = this.totalTime - this.recordingTime;
						//1秒钟后，再次执行本方法
						setTimeout(() => {
							//定时器内，this指向外部，找不到vue的方法，所以，需要用that变量。
							that.veryfiyingTime();
						}, 1000)
					} else {
						//时间已完成，还原相关变量
						this.state = false; //关闭倒计时
						this.recordingTime = 0; //记录时间为0
						this.currentTime = this.totalTime; //显示时间为总时间
					}
				} else {
					//倒计时未开启，初始化默认变量
					this.state = false;
					this.recordingTime = 0;
					this.currentTime = this.totalTime;
				}
			},
		}
	}
</script>

<style>

</style>
