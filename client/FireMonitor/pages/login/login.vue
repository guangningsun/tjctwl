<template>
	<view class="content">
		<view class="zai-box">
			<image src="../../static/login.png" mode='aspectFit' class="zai-logo"></image>
			<view class="zai-title">天津城投物联</view>
		
			<view class="flex padding align-center">
				<form>
					<view class="cu-form-group">
						<view class="title">用户名</view>
						<input placeholder="请输入用户名" name="input"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">密&nbsp &nbsp码</view>
						<input placeholder="请输入密码" name="input"></input>
					</view>
				</form>
		
			</view>
		</view>
		<view class="justify-between bottom-box">
			<view class="zai-label">忘记密码？</view>
			<button class="zai-btn">登录</button>
		</view>
	</view>
</template>

<script>
</script>

<style>
	.zai-box {
		padding: 100upx 100upx;
		position: relative;
		background-color: #FFFFFF;
	}
	
	.content {
		background-color: #FFFFFF;
		min-height:100vh;
	}
	
	.bottom-box {
		padding: 20upx 20upx;
		position: relative;
		background-color: #FFFFFF;
	}

	.zai-logo {
		width: 100%;
		width: 100%;
		height: 310upx;
	}

	.zai-title {
		position: absolute;
		top: 0;
		line-height: 500upx;
		font-size: 56upx;
		color: #fff;
		text-align: center;
		width: 100%;
		margin-left: -100upx;
	}

	.zai-form {
		margin-top: 100upx;
	}

	.zai-input {
		background: #e2f5fc;
		margin-top: 30upx;
		border-radius: 100upx;
		padding: 20upx 40upx;
		font-size: 36upx;
	}

	.input-placeholder,
	.zai-input {
		color: #94afce;
	}

	.zai-label {
		padding: 60upx 0;
		text-align: center;
		font-size: 30upx;
		color: #a7b6d0;
	}

	.zai-btn {
		background: #201B4F;
		color: #fff;
		border: 0;
		border-radius: 10upx;
		font-size: 36upx;
	}

	.zai-btn:after {
		border: 0;
	}

	/*按钮点击效果*/
	.zai-btn.button-hover {
		transform: translate(1upx, 1upx);
	}
</style>
