// D:\zhihuAnss
// 
// js  读取 json  

// 导入
const fs = require('fs')
const path = require('path')
// D:\zhihuAnss
//1.读取data.json文件
fs.readFile(path.join(__dirname, 'data.json'), 'utf8', (err, data) => {
  if (err) {
    console.log(err)
    return
  }
  console.log(data);
})