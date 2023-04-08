viewPath='Vue3LoginDo'
router_template="""
 {
      path: '/{viewPath}',
      name: '{viewPath}',
      component: () => import('../views/{viewPath}.vue'),
      meta: {
          index: 1,
      },
  },"""

router=router_template.replace('{viewPath}',viewPath)
# router=f""" {
#       path: '/{viewPath}',
#       name: '{viewPath}',
#       component: () => import('../views/${viewPath}.vue'),
#       meta: {
#           index: 1,
#       },
#   },

# """

# // JS截取字符串反斜杠_寂寞沙洲冷1号选手的博客-CSDN博客_js字符串截取反斜杠
# // https://blog.csdn.net/weixin_40283749/article/details/127496612

# console.log(`router`);
# // js  raw  反斜杠 
# console.log(router);
router_link=f"""
<div>
<router-link to="/{viewPath}">{viewPath}</router-link>
</div>

"""


print(router)
print(fr'D:\proj\vue\vue3-book-demo-login\src\router\index.ts:179')

print(router_link)
print(fr'D:\proj\vue\vue3-book-demo-login\src\views\HomeView.vue:40')
print(fr'D:\proj\vue\vue3-book-demo-login\viewPathMake.py:43')
# 43行 10列 不知道怎么去
# console.log(String.raw`D:\proj\vue\vue3-book-demo-login\src\router\index.ts`);
    

# console.log(String.raw`D:\proj\vue\vue3-book-demo-login\src\views\HomeView.vue`);