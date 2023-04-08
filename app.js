 
new Vue({
	el:"#vueapp",
	mounted(){
		this._initVueApp();
		this.btnTakePhotoClicked();
	},
	
	methods:{
		async _initVueApp(){
			this.$refs.video.srcObject= await navigator.mediaDevices.getUserMedia({video:true,audio:false});			
			this._context2d=this.$refs.canvas.getContext("2d");
			this.canvas=this.$refs.canvas;
		},
		
		btnTakePhotoClicked(){
			this._context2d.drawImage(this.$refs.video,0,0,400,300)
			var img = document.createElement("img"); // 创建img元素
			img.src =this.canvas.toDataURL("image/png"); // 截取视频第一帧
			var svaeHref = document.getElementById("save_herf");
			console.log(img.src)
			
			var sd=document.getElementById("save_img");
			svaeHref.href = img.src;
			sd.src=img.src
			
		},
	}
});