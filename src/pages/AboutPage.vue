<template>
  <div class="homepage-banner">
    <q-img
      src="../assets/qianshan.jpg"
      alt="Banner Image"
      class="banner-image"
    />
    <div class="banner-text">
      <p>基于数字化的企业碳足迹管理体系创新</p>
      <p>——助力“中国刷业之都”绿色低碳发展</p>
    </div>
    <div class="normal-text">
      <p>
        碳足迹管理第三方认证平台——“碳析TanX”，专为有“中国刷业之都”之称的安徽省潜山市源潭镇9000多家制刷企业和个体户及其上下游企业和金融机构设计。平台通过数字化技术实现碳排放数据的透明、可靠记录与核查，提供一键生成碳排放报告功能，助力企业展示节能减排成效。同时，平台为金融机构提供精准的碳减排信息，支持绿色金融决策，推动刷业产业集群数字化转型和低碳化发展，实现经济与环境效益的双赢。
      </p>
    </div>
  </div>
</template>

<script></script>

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
  top: 30%; /* 将标题文本定位到图片的上方中央 */
  left: 50%;
  transform: translate(-50%, -50%); /* 确保准确居中 */
  color: white; /* 白色文字 */
  font-size: 42px; /* 增大标题文字大小 */
  text-align: center; /* 标题文本居中 */
  /* 可以添加更多样式来调整字体、间距等 */
}

.normal-text {
  position: absolute;
  top: 60%; /* 将内容文本定位到图片的下方中央 */
  left: 50%;
  transform: translate(-50%, -50%); /* 确保准确居中 */
  color: white; /* 白色文字 */
  font-size: 24px; /* 缩小内容文字大小 */
  text-align: center; /* 内容文本居中 */
  width: 80%; /* 控制文本宽度 */
  /* 可以添加更多样式来调整字体、间距等 */
}
</style>
