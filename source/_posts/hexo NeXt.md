---
title: hexo NeXt的設置(持續更新)
date: 2022-02-12 22:00:16
tags: blog
categories: blog
comments: false
---



# [hexo 網誌框架 + github Page](https://hexo.io/zh-cn/)
## install hexo
```shell=
npm install hexo-cli -g
hexo init blog
cd blog
npm install
hexo server # 啟動
```

## [Choose theme](https://hexo.io/themes/)
- 很多人使用[NeXt](https://theme-next.iissnan.com/getting-started.html)

```shell=
git clone https://github.com/iissnan/hexo-theme-next themes/next
```
也可以下載穩定版本zip，解壓縮後重新命名成next，放到blog/themes 底下，自己新增themes資料夾。
我自己也使用NeXt

- 我遇到的問題
    - [可能會無法正常啟動](https://github.com/iissnan/hexo-theme-next/issues/2253)，原因是hexo在5.0之後把swig刪除，需要自己安裝`npm i hexo-renderer-swig`
    - [cannot GET /20%/](https://www.zhihu.com/question/353097489/answer/888107103)

[參考配置](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/676805/)
[參考配置2](https://maoao530.github.io/2017/01/25/hexo-blog-seo/)
[參考配置3](https://ed521.github.io/2020/05/hexo-next-upgrade/)

### 我的配置
- 去_config.yml(./_config.yml)
```yaml=
theme: next # landscape
language: zh-tw
url: https://a920604a.github.io
root: /blog/

```
```shell=
hexo server # 啟動
```



### 我的 themes下的配置文件(.theme/next/_config.yml)
```yaml=

menu:
  home: /home/|| home
  目錄: /archives/|| archive
  分類: /categories/|| th
  標籤: /tags/|| tags
  關於我: /about/|| user
# /|| 中間不能有空格

scheme: Mist


canvas_nest: true # 文章摘要

social:
  GitHub: https://github.com/a920604a || github
  E-Mail: mailto:a920604a@gmail.com || envelope
  FB Page: https://www.facebook.com/yu.an.1800 || facebook
  Instagram: https://instagram.com/yuan3509 || instagram
  
avatar: /images/animal3.jpg


auto_excerpt:
  enable: true
  
highlight_theme: night eighties 

# 拜訪流量計算
busuanzi_count:
  # count values only if the other configs are false
  enable: true
  # custom uv span for the whole site
  site_uv: true
  site_uv_header: <i class="fa fa-user"></i>訪問人數
  site_uv_footer: 次
  # custom pv span for the whole site
  site_pv: true
  site_pv_header: <i class="fa fa-eye"></i>總訪問量
  site_pv_footer: 次
  # custom pv span for one page only
  page_pv: true
  page_pv_header: <i class="fa fa-file-o"></i>瀏覽
  page_pv_footer: 次



# 搜尋功能 必須安裝 npm install hexo-generator-searchdb --save
local_search:
  enable: true
  # if auto, trigger search by changing input
  # if manual, trigger search by pressing enter key or search button
  trigger: auto
  # show top n results per article, show all results by setting to -1
  top_n_per_article: 1
  # Unescape html strings to the readable one.
  unescape: false
  # Preload the search data when the page loads.
  preload: false


# npm install --save hexo-symbols-count-time 
字數統計以及閱讀時間
```


## 新增 pags, categories, about資料夾

`hexo g`會編譯並產生public目錄，底下為之後要部署的網誌

- 新增 pags, categories, about資料夾
用命令方式新增，會自動在source 目錄底下新增該目錄並在目錄底下新增`index.md`，如下。
```bash=

hexo new page "home"
hexo new page "archives"
hexo new page "categories"
hexo new page "tags"
hexo new page "about"
# INFO  Validating config
# INFO  Created: ~/Desktop/project/blog/source/categories/index.md

# hexo new [layout] <title>
# 佈局	路徑
# post	source/_posts
# page	source
# draft	source/_drafts
```
在手動至
```yaml=
/source/categories/index.md
+ type: "categories"
/source/tags/index.md
+ type: "tags"
```

#### 做了哪些事
- 搜尋功能 `npm install hexo-generator-searchdb --save`
- 上傳github  `npm install hexo-deployer-git --save`
- 加載進度條
`$ git clone https://github.com/theme-next/theme-next-pace themes/next/source/lib/pace`
修改 next/_config.yml
`pace = true`
- 網站運行時間
修改 next/_config.yml
```
footer:
  # Specify the date when the site was setup.
  # If not defined, current year will be used.
  since: 2022
```
- [sidebar 近期文章](https://www.chingow.cn/posts/c7372a12.html)
- 顯示當前瀏覽進度
修改 next/_config.yml

```
back2top:
  enable: true
  sidebar: false
  scrollpercent: true  #  瀏覽頁面時，顯示當前瀏覽紀錄
```
- 側邊欄移至左邊
Muse 和 Mist 則需要深度修改source code才能實現改變側邊欄位置
修改themes/next/source/css/_custom/custom.styl
```
.sidebar-toggle {
  left: 30px;
}

.sidebar {
  left: 0px;
}

```
修改themes/next/source/js/src/motion.js
```
-     {paddingRight: SIDEBAR_WIDTH},
+     {paddingLeft: SIDEBAR_WIDTH},

-   NexT.utils.isDesktop() && $('body').velocity('stop').velocity({paddingRight: 0});
+   NexT.utils.isDesktop() && $('body').velocity('stop').velocity({paddingLeft: 0});
```



#### TODO
- [更改背景顏色](https://maoao530.github.io/2017/01/25/hexo-blog-seo/)
- 更改blog背景
- [人數統計](https://teddybearfp.github.io/2019/03/29/Hexo-Next-%E4%BA%BA%E6%95%B8%E7%B5%B1%E8%A8%88-Busuanzi-LeanCloud/)
- [評論系統](https://yashuning.github.io/2018/06/29/hexo-Next-%E4%B8%BB%E9%A2%98%E6%B7%BB%E5%8A%A0%E8%AF%84%E8%AE%BA%E5%8A%9F%E8%83%BD/)`npm install --save gitment`





- 網站地圖 `npm install hexo-generator-sitemap --save`
- 點擊愛心功能
- 鑲嵌音樂
- 請我喝一杯咖啡XD
- 下拉式選單
- 整理layout



## 佈署至GitHub Pages
安裝git套件
`npm install hexo-deployer-git --save`
至github新增repo

至_config.yaml
```yaml=
deploy:
  type: "git"
  repo:
    github: https://github.com/a920604a/a920604a.github.io.git
  branch: main
```
`hexo g`生成網誌至public目錄
上傳至github `hexo d`
public in 
`https://a920604a.github.io/a920604a.github.io`
