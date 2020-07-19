<!-- HTMLを記述 -->
<template>
  <div>
    <p>Home</p>
    <button @click="getRandom">その画像、判定してやんよ</button>
    <label>
      画像を選択
      <input  type='file' placeholder='判定画像を入力してください'/>
    </label>
    <p>Random number from backend: {{ randomNum }}</p>
    <h1 v-if="randomNum%4==0">Awesome!!!</h1>
    <h2 v-if="randomNum%4==1">Good</h2>
    <h2 v-if="randomNum%4==2">Bad...</h2>
    <h1 v-if="randomNum%4==3">S〇〇ks!!!</h1>
  </div>
</template>

<!-- JavaScriptを記述 -->
<script>
import axios from 'axios'

export default {
  data () {
    return {
      randomNum: 0,
      productForm: {
        image: {
          photo: null
        }
      },
      photoURL: ''
    }
  },
  methods: {
    getRandom () {
      this.randomNum = this.getRandomNum()
    },
    getRandomNum () {
      const path = 'http://localhost:5000/rand'
      axios.get(path)
        .then(response => {
          this.randomNum = response.data.randomNum
        })
        .catch(error => {
          console.log(error)
        })
    },
    onFileChange (e) {
      const file = e.target.files[0]
      this.productForm.image.photo = file
      this.photoURL = URL.createObjectURL(file)
    }
  },
  created () {
    this.getRandom()
  }
}
</script>
<!--一行空行を入れてください-->
