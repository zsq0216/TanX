<template>
  <q-page class="row justify-center">
    <q-card class="col-5 row justify-center my-custom-margin">
      <q-form
        class="q-gutter-md q-py-xl col-9"
        @submit="onSubmit"
        @reset="onReset"
      >
        <q-input
          v-model="registerForm.Tel"
          label="手机号"
          :rules="[(val) => (val && val.length > 0) || '请输入手机号']"
        />

        <q-input
          v-model="registerForm.EnterpriseName"
          label="企业名称"
          :rules="[(val) => (val && val.length > 0) || '请输入企业名称']"
        />
        <q-input
          v-model="registerForm.mail"
          label="邮箱"
          :rules="[
            (val) => (val && val.match(emailPattern)) || '请输入有效的邮箱地址',
          ]"
        />
        <q-input
          v-model="registerForm.pwd"
          :type="showPassword ? 'text' : 'password'"
          label="密码"
          :rules="[(val) => (val && val.length > 0) || '请输入密码']"
        >
          <template v-slot:append>
            <q-icon
              :name="showPassword ? 'visibility_off' : 'visibility'"
              class="cursor-pointer"
              @click="showPassword = !showPassword"
            />
          </template>
        </q-input>
        <q-input
          v-model="registerForm.confirmPassword"
          label="确认密码"
          :type="showComfirtPassword ? 'text' : 'password'"
          :rules="[(val) => (val && val === registerForm.pwd) || '密码不匹配']"
        >
          <template v-slot:append>
            <q-icon
              :name="showComfirtPassword ? 'visibility_off' : 'visibility'"
              class="cursor-pointer"
              @click="showComfirtPassword = !showComfirtPassword"
            />
          </template>
        </q-input>
        <div>
          <q-btn label="注册" type="submit" color="primary" />
          <q-btn
            label="重置"
            type="reset"
            color="primary"
            flat
            class="q-ml-sm"
          />
          <q-btn flat label="去登录" color="primary" @click="onLogin" />
        </div>
      </q-form>
    </q-card>
  </q-page>
</template>

<script setup>
import { reactive, ref } from "vue";
import { useQuasar, Loading, Notify} from "quasar";
import { useRouter } from 'vue-router';
import axios from "axios";
const $q = useQuasar();
// 获取 router 实例
const router = useRouter();

const registerForm = reactive({
  Tel: "",
  pwd: "",
  EnterpriseName: "",
  mail: "",
  confirmPassword: "",
});

const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
function onLogin() {
  router.push("/login");
}

const onSubmit = () => {
  const formData = new FormData();
  Object.keys(registerForm).forEach((key) => {
    formData.append(key, registerForm[key]);
  });
  Loading.show();
  console.log("im here");
  axios
    .post("http://47.122.24.142:7766/api/register", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    })
    .then((response) => {
      Loading.hide();
      if (response.status === 201) {
        console.log("success!");
        Notify.create({
          color: "green-4",
          textColor: "white",
          icon: "cloud_done",
          message: "注册成功",
        });
        router.push("/login");
      } else if (response.status === 202) {
        console.log("用户已存在");
        Notify.create({
          color: "orange-5",
          textColor: "white",
          icon: "warning",
          message: "用户已存在",
        });
      } else {
        // 处理其他响应状态码
        console.log("其他情况");
      }
    })
    .catch((error) => {
      console.log(registerForm);
      console.log("failed!");
      Loading.hide();
      console.error("Registration error:", error);
      Notify.create({
        color: "red-5",
        textColor: "white",
        icon: "error",
        message: "注册失败",
      });
    });
};
const showPassword = ref(false);
const showComfirtPassword = ref(false);
const onReset = () => {
  Object.assign(registerForm, {
    Tel: "",
    pwd: "",
    EnterpriseName: "",
    mail: "",
    confirmPassword: "",
  });
};
</script>

<style>
.my-custom-margin {
  margin-top: 130px;
  margin-bottom: 130px;
}
</style>
