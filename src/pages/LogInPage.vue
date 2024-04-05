<template>
  <q-layout>
    <q-page-container>
      <q-page class="flex flex-center">
        <q-card class="my-card">
          <q-card-section>
            <div class="text-h5 text-center q-my-md">请选择登录类型</div>
          </q-card-section>

          <q-card-section class="q-pt-none">
            <div class="row justify-around q-gutter-md">
              <div
                :class="accountType === 'business' ? 'selected' : ''"
                class="account-type"
                @click="setAccountType('business')"
              >
                <q-img
                  square
                  src="../assets/R-C.jpg"
                  style="width: 100px; height: 100px"
                  class="rounded-full"
                  contain
                />
                <div>企业用户</div>
              </div>
              <div
                :class="accountType === 'bank' ? 'selected' : ''"
                class="account-type"
                @click="setAccountType('bank')"
              >
                <q-img
                  square
                  src="../assets/bank.png"
                  style="width: 100px; height: 100px"
                  class="rounded-full"
                  contain
                />
                <div>银行用户</div>
              </div>
            </div>
          </q-card-section>

          <q-form @submit="onLogin" class="q-gutter-md">
            <q-card-section>
              <q-input
                outlined
                v-model="loginCredentials.username"
                label="手机号/邮箱"
                lazy-rules
                :rules="[
                  (val) => (val && val.length > 0) || '请输入手机号或邮箱',
                ]"
              />
              <q-input
                outlined
                v-model="loginCredentials.password"
                type="password"
                label="密码"
                lazy-rules
                :rules="[(val) => (val && val.length > 0) || '请输入密码']"
              />
            </q-card-section>

            <q-card-section class="text-right">
              <q-btn flat label="去注册" color="primary" @click="signUp" />
              <q-btn type="submit" label="登录" color="primary" />
            </q-card-section>
          </q-form>
        </q-card>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref, reactive } from "vue";
import { useRouter } from "vue-router";
import {
  QPage,
  QCard,
  QCardSection,
  QForm,
  QInput,
  QBtn,
  Loading,
  Notify,
} from "quasar";
import { useQuasar } from "quasar";
import axios from "axios";
import { computed } from "vue";
import { useStore } from "vuex";

const store = useStore();
const router = useRouter();
// Action to save token

const $q = useQuasar();

// 创建响应式的引用
const accountType = ref(null);
const loginCredentials = reactive({
  username: "",
  password: "",
});

// 定义方法
const setAccountType = (type) => {
  accountType.value = type;
};
function signUp() {
  router.push("/signup");
}
const onLogin = () => {
  Loading.show();
  console.log("im here");
  axios
    .post("http://47.122.24.142:7766/api/token/", loginCredentials)
    .then((response) => {
      Loading.hide();

      const token = response.data.access;
      console.log(token);
      store.dispatch("saveToken", token);

      Notify.create({
        color: "green-4",
        textColor: "white",
        icon: "cloud_done",
        message: "登录成功",
      });
      if (response.data.is_Enterprise === true) {
        localStorage.setItem("userToken", token);
        localStorage.setItem("userName", loginCredentials.username);
        router.push("/personal");
      } else {
        localStorage.setItem("bankToken", token);
        router.push("/search");
      }
    })
    .catch((error) => {
      console.log("failed!");
      Loading.hide();
      console.error("Registration error:", error);
      Notify.create({
        color: "red-5",
        textColor: "white",
        icon: "error",
        message: "登录失败",
      });
    });
};
</script>

<style>
.my-card {
  width: 400px;
  max-width: 90%;
}

.account-type {
  cursor: pointer;
  text-align: center;
}

.account-type > div {
  margin-top: 8px;
}

.selected {
  border: 2px solid #027be3;
  border-radius: 8px;
}

.rounded-full {
  border-radius: 50%; /* 产生圆形效果 */
}
</style>
