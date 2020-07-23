<!-- HTMLを記述 -->
<template>
  <div>
    <div class="imgContent">
      <div class="imagePreview">
        <img :src="uploadedImage" style="width:100%;" />
      </div>
      <input type="file" class="file_input" name="photo" @change="onFileChange"  accept="image/*" />
      <button @click='onUploadImage'>画像判定してクレメンス・・・</button>
    </div>
  </div>
</template>

<!-- JavaScriptを記述 -->
<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:5000'
export default {
  data () {
    return {
      randomNum: 0,
      uploadedImage: ''
    }
  },
  methods: {
    getRandom () {
      this.randomNum = this.getRandomNum()
    },
    getRandomNum () {
      return axios.get(API_URL)
    },
    onFileChange (e) {
      let files = e.target.files || e.dataTransfer.files
      this.createImage(files[0])
    },
    // アップロードした画像を表示
    createImage (file) {
      let reader = new FileReader()
      reader.onload = (e) => {
        this.uploadedImage = e.target.result
      }
      reader.readAsDataURL(file)
    },
    removeImage (e) {
      this.uploadedImage = ''
    },
    onUploadImage () {
      var params = new FormData()
      params.append('image', this.uploadedImage)
      axios.post(`${API_URL}/rand`, params).then(function (response) {
        console.log(response.data)
      })
    },
    created () {
      this.getRandom()
    }
  }
}

</script>

<style scoped>
.imgContent {
  width: 90%;
  max-width: 50%;
  margin:auto;
  margin-bottom:40px;
}
.imagePreview {
  height:80vh;
  background: rgb(240, 240, 240);
  overflow:hidden;
  border-radius: 10px;
  background-position: center center;
  background-size: cover;
  margin-bottom:30px;
  position: relative;
  }
 .fileUpload {
  text-align: center;
  position: absolute;
  height: 25px;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  margin: auto;
  color:rgb(134, 134, 134);
  padding: 20px;
}
</style>
