
// export 
const userColumns = [{
    label: "age",
    key: "age"
  },
  {
    label: "birthDay",
    key: "birthDay"
  },
  {
    label: "createTime",
    key: "createTime"
  },
  {
    label: "是否删除",
    key: "deleted"
  },
  {
    label: "id",
    key: "id"
  },
  {
    label: "头像地址",
    key: "imagePath"
  },
  {
    label: "lastActiveTime",
    key: "lastActiveTime"
  },
  {
    label: "modifyTime",
    key: "modifyTime"
  },
  {
    label: "password",
    key: "password"
  },
  {
    label: "phone",
    key: "phone"
  },
  {
    label: "真实姓名",
    key: "realName"
  },
  {
    label: "1.学生 2.老师 3.管理员",
    key: "role"
  },
  {
    label: "1.男 2女",
    key: "sex"
  },
  {
    label: "1.启用 2禁用",
    key: "status"
  },
  {
    label: "tenantId",
    key: "tenantId"
  },
  {
    label: "学生年级(1-12)",
    key: "userLevel"
  },
  {
    label: "用户名",
    key: "userName"
  },
  {
    label: "userUuid",
    key: "userUuid"
  },
  {
    label: "微信openId",
    key: "wxOpenId"
  },
]

// for(let userColumn of userColumns){
//   userColumn.label
// }

let userColumnsLabels=userColumns.map(o=>o.label)
console.log(userColumnsLabels);
// node js 写 出文件
userColumnsLabelsStr=
userColumnsLabels.join(',')
console.log("userColumnsLabelsStr");
console.log(userColumnsLabelsStr);
// let outStr=userColumnsLabelsStr

function mockRow(userColumns){
  let rowVals=[]
  for(let userColumn of userColumns){
    // userColumn.key
    rowVals.push("1")
    // outStr+="1,"
  }
return  rowVals.join(',')
}

let outStr=userColumnsLabelsStr+"\n"+mockRow(userColumns)

const fs = require('fs')
// const content = ' 雷猴雷猴\n'
let  content = outStr
content="\uFEFF"+content
const opt = {
  encoding: 'utf8',
  // flag: 'a', // a：追加写入；w：覆盖写入
  flag: 'w',
}

let filepath='userColumnsLabels.csv'
console.log("filepath");
console.log(filepath);
// fs.writeFile utf-8 
fs.writeFile('userColumnsLabels.csv', content, opt, (err) => {
  if (err) {
    console.error(err)
  }
})

function writeFile(filepath,content){
  let  endContent = "\uFEFF"+content
  const opt = {
    encoding: 'utf8',
    // flag: 'a', // a：追加写入；w：覆盖写入
    flag: 'w',
  }
  
  fs.writeFile(filepath, endContent, opt, (err) => {
    if (err) {
      console.error(err)
    }
  })
  
  // let filepath='userColumnsLabels.csv'
  // console.log("filepath");
  // console.log(filepath
}