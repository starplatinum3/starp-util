postList = {
    list: query => post(`/api/admin/education/subject/list`),
    pageList: query => post('/api/admin/education/subject/page', query),
    edit: query => post('/api/admin/education/subject/edit', query),
    save: query => post(`${apiPreffix}/save`, query),
    saveAll: query => post(`${apiPreffix}/saveAll`, query),
    deleteBy: query => post(`${apiPreffix}/deleteBy`, query),
    selectPageEqual: (query, data) => postWithQuery(`${apiPreffix}/selectPage/equal`, query, data),
    selectByExample: (query, data) => postWithQuery(`${apiPreffix}/selectByExample`, query, data),
    // selectPageEqual: query => post(`${apiPreffix}/selectPage/equal`, query),
    selectByExample: query => post(`${apiPreffix}/selectByExample`, query),
    selectPage: query => post(`${apiPreffix}/selectPage`, query),
    removeByIds: query => post(`${apiPreffix}/removeByIds`, query),
    selectPlusPage: query => post(`${apiPreffix}/selectPlusPage`, query),
    select: id => post('/api/admin/education/subject/select/' + id),
    deleteSubject: id => post('/api/admin/education/subject/delete/' + id)
}


// for (let o of  postList){
//     console.log(o);
// }

function fun_name(num) {
    var tmp = arguments.callee.toString();
    var re = /function\s*(\w*)/i;
    var matches = re.exec(tmp);
    // alert(matches[1]);
    console.log(matches);
    // console.log(matches[1]);
}

for (let i in postList) {
    let one = postList[i]
    console.log(one);
    let funcStr = one.toString()
    console.log(funcStr);
    // one.
    // js 获取 函数的名字 
    // fun_name(one);

    //     [Function: selectPlusPage]
    // query => post(`${apiPreffix}/selectPlusPage`, query)
    // [Function: select]
    // id => post('/api/admin/education/subject/select/' + id)
    // [Function: deleteSubject]
    // id => post('/api/admin/education/subject/delete/' + id)
}

postNamesList = ['save', 'saveAll', 'deleteBy', 'selectPageEqual', 'selectByExample',
    'selectPage', 'removeByIds', 'selectPlusPage', 'select', 'deleteSubject'
]


// let strNew = str.replace(/World/g,"Bro");
function replaceAll(oldStr, from, to) {
    return oldStr.replace(/`${from}`/g, to);
    // js repalce all 
    // tmplate.replace("")
}

// function replaceAll(s1, s2) {
//     return this.replace(new RegExp(s1, "gm"), s2);
// };

//我同学dearning，从网上搜来的函数
String.prototype.replaceAll = function (s1, s2) {
    return this.replace(new RegExp(s1, "gm"), s2);
};

function makePostList(tmplate, postName) {

    // js repalce all 
    // tmplate.replace("")
    let code = tmplate
        .replaceAll("#postName#", postName)
    return code;
    //    let code= replaceAll("#postName#",postName)
}
// 1、导入fs模块，来操作文件
const fs = require('fs')
// 2、调用fs.readFile()方法读取文件
fs.readFile('postWithQueryOne.js', 'utf8', function (err, dataStr) {
    // 打印失败的结果
    // 如果读取成功，则err的值为null
    // 如果读取失败，则返回错误对象，dataStr的值为undefined
    console.log(err)
    console.log('-------')
    // 打印成功的结果
    console.log(dataStr)

    let  allPost=[]


    for (let postName of postNamesList) {
        let postOne = makePostList(dataStr, postName)
        allPost.push(postOne)
    }

  let   allPostStr=  allPost.join("\n")
    // console.log(allPost);
    console.log(allPostStr);
})




// node js 读取 文件 
// for (let postName of postNamesList){
//     let url="`${apiPreffix}/selectPage/equal`"
// `
// selectPageEqual: (query, data) => postWithQuery(`${apiPreffix}/selectPage/equal`, query, data),
// `
// }

// ————————————————
// 版权声明：本文为CSDN博主「普通网友」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
// 原文链接：https://blog.csdn.net/m0_66314752/article/details/122426207

// console.log("loglog");
// from="222"
// console.log(/`${from}`/g,);
// console.log(/`${from}`/g,);