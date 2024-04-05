<template>
    <div class="homepage-banner">
    <q-img  src="../assets/qianshan.jpg" alt="Banner Image" class="banner-image"/>
    <div class="banner-text">
      <p>基于数字化的企业碳足迹管理体系创新</p>
      <p>——助力“中国刷业之都”绿色低碳发展</p></div>
  </div>
  </template>

  <script>

  </script>

<style scoped>
.homepage-banner {
  position: relative;
  text-align: center; /* 确保文本居中 */
}

.banner-image {
  width: 100%; /* 或根据需要调整 */
  height: auto; /* 保持图片比例 */
}

.banner-text {
  position: absolute;
  top: 50%; /* 将文本定位到图片的中央 */
  left: 50%;
  transform: translate(-50%, -50%); /* 确保准确居中 */
  color: white; /* 白色文字 */
  font-size: 36px; /* 文字大小，可调整 */
  /* 可以添加更多样式来调整字体、间距等 */
}
</style>
