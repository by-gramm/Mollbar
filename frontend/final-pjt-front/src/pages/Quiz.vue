<template>
  <div class="d-flex justify-content-center" id="cardBox">
    <!-- <div v-if="showScore">
        <b-card
        title="Results"
        style="max-width: 20rem;"
        >
        You Scored {{score}} of {{questions.length}}
        </b-card>
    </div> -->
    <div v-if="showScore">
        <b-card
            v-if="scoreHigh"
            title="점수"
            style="max-width: 20rem;"  
        >
            <h5>{{score * 10}} / {{questions.length * 10}}</h5>
            <p>영잘알이시군요!</p>
        </b-card>
        <b-card
            v-else
            title="점수"
            style="max-width: 20rem;" 
        >
            <h5>{{score * 10}} / {{questions.length * 10}}</h5>
            <p>몰봐와 함께 한국영화를 더 알아가요.</p>
        </b-card>
    </div>
    <div class="card-q" v-else>
    <span v-if="!startQuiz">
      <b-card
        img-src="https://imgtoolkit.culturebase.org/?color=FFFFFF&quality=8&ar_ratio=1.3&format=jpg&file=http%3A%2F%2Fdata.heimat.de%2Fpics%2F5%2Fe%2F0%2Fa%2Fd%2Fpic_1387803322_5e0ad29c4026d5f9a038cfc4c13840dc.jpeg&do=cropOut&width=1200&height=450"
        img-alt="Image"
        img-top
        title="영잘알 테스트 - 한국영화 편"
        style="max-width: 20rem;"
        class="mb-2 overflow-hidden"
      >
      <b-card-text class="mt-5 mb-5">
        <p>2000년 이후 개봉한 한국영화 포스터의 일부분과 4개의 보기가 주어집니다.</p>
        <p>포스터에 맞는 영화 제목을 골라주세요.</p>
        <p>총 10개의 문제가 주어지며, 각 문제당 15초의 제한 시간이 있습니다.</p>
      </b-card-text>
      <b-button @click="startQuizFunc()">Start Quiz</b-button>
    </b-card>
    </span>

    <span v-else>
    <b-card 
        title="영잘알 테스트 - 한국영화 편"
        style="max-width: 20rem; position: relative;"
        class="mb-2 overflow-hidden"
        :questions="questions"
    >
    <!-- <b-card-img
      id="poster-image"
      v-model="questions"
      :src="'https://image.tmdb.org/t/p/w500' + questions[currentQuestion].poster_path"
      bottom
    >
    </b-card-img> -->
    <div 
      id="poster-image"
      :style="{backgroundImage: `url(https://image.tmdb.org/t/p/w500${questions[currentQuestion].poster_path})`}"
    >
    </div>
    <b-card-text id="question">
      Question No.{{currentQuestion + 1}} of {{questions.length}}
    </b-card-text>
    <br>
    <b-progress
        variant="warning"
        :max="15"
        :value="countDown"
        height="4px"
      ></b-progress>
  
    <b-card-text>
      <span style="font-size: 40px;"><strong>{{countDown}} </strong></span>
    </b-card-text>

    <!-- <b-card-image>
      {{questions[currentQuestion].poster_path}}
    </b-card-image> -->
    <!-- <b-card-text>
      {{questions[currentQuestion].questionText}}
    </b-card-text> -->
    <div class="answer-section">
      <b-button :key="index" v-for="(option, index) in questions[currentQuestion].options" @click="handleAnswerClick(option.isCorrect)" class="ans-option-btn" variant="primary">{{option.title}}</b-button>
    </div>
  </b-card>
    </span>
  </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            currentQuestion: 0,
            showScore: false,
            score:0,
            countDown : 15,
            timer:null,
            startQuiz: false,
            scoreHigh: false,

            questions : [],
        }
    },

    methods:{
        startQuizFunc(){
            this.startQuiz = true
            this.countDownTimer()
        },
        handleAnswerClick(isCorrect) {
            clearTimeout(this.timer);
            let nextQuestion = this.currentQuestion + 1;
            if(isCorrect) {
                this.score = this.score + 1;
            }
            if(nextQuestion < this.questions.length){
            this.currentQuestion = nextQuestion;

            this.countDown = 15;
            this.countDownTimer();
            }
            else {
                if (this.score > 7) {
                  this.scoreHigh = true;
                }
                this.showScore = true;
            }
        },
        countDownTimer() {
            if (this.countDown > 0) {
                this.timer = setTimeout(() => {
                    this.countDown -= 1
                    this.countDownTimer()
                }, 1000)
            }
            else {
                this.handleAnswerClick(false)
            }
        }
    },
    created() {
        // quiz set을 가져온다.
        axios({
            method: 'get',
            url: `http://127.0.0.1:8000/api/v1/community/kmovie_quiz/`,
            headers: {
                Authorization: `Bearer ${localStorage.getItem('jwt')}`
            }
        })
        .then(res => {
            this.questions = res.data
        })
        .catch(err => console.log(err))
    }
    
}
</script>

<style scoped>
@import url(//fonts.googleapis.com/earlyaccess/notosanskr.css);

p, h5 {
  font-family: 'Noto Sans KR', sans-serif;
}

h5 {
  color: tomato;
  margin-top: 20px;
}

.card {
    min-width: 100%;
    border-radius: 15px;
    border: none;
    /* padding: 20px; */
    box-shadow: 10px 10px 42px 0px rgba(0, 0, 0, 0.75);
}
.card-q{
    min-width: 60%;
}
.ans-option-btn{
    min-width: 50%;
    font-size: 16px;
    color: #ffffff;
    align-items: center;
    cursor: pointer;
    margin-bottom: 5px;


}
.answer-section {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.timer-text {
  background: rgb(230, 153, 12);
  padding: 15px;
  margin-top: 20px;
  margin-right: 20px;
  border: 5px solid rgb(255, 189, 67);
  border-radius: 15px;
  text-align: center;
}

.card-img, .card-img-top {
    border-top-left-radius: calc(0.25rem - 1px);
    border-top-right-radius: calc(0.25rem - 1px);
    height: 350px;
}

#poster-image {
  /* position: absolute; */
  height: 40px;
  width: 100%;
  background: no-repeat center center fixed;
  margin-top: 50px;
  background-position-y: 10%;
  overflow: hidden;
}

#question {
  margin-top: 100px;
}

#cardBox {
  margin-top: 50px;
}

</style>
