// a

let aList = document.getElementsByTagName('a')
// let d=
let supported_version_list_str = `
cp36-cp36m-manylinux1_x86_64
cp36-cp36m-linux_x86_64
cp36-abi3-manylinux1_x86_64
cp36-abi3-linux_x86_64
cp36-none-manylinux1_x86_64
cp36-none-linux_x86_64
cp35-abi3-manylinux1_x86_64
cp35-abi3-linux_x86_64
cp34-abi3-manylinux1_x86_64
cp34-abi3-linux_x86_64
cp33-abi3-manylinux1_x86_64
cp33-abi3-linux_x86_64
cp32-abi3-manylinux1_x86_64
cp32-abi3-linux_x86_64
py3-none-manylinux1_x86_64
py3-none-linux_x86_64
cp36-none-any
cp3-none-any
py36-none-any
py3-none-any
py35-none-any
py34-none-any
py33-none-any
py32-none-any
py31-none-any
py30-none-any`
supported_version_list_str =
    supported_version_list_str.trim()
supported_version_list =
    supported_version_list_str.split('\n')

// String对象的方法
// 方法一: indexOf() (推荐)
// var str = "123";
// console.log(str.indexOf("3") != -1 );  // true

function strIsIn(wantStr, baseStr) {
    return baseStr.indexOf(wantStr) != -1
}



function for_supported_version_list(aTextContent) {
    for (let i = 0; i < supported_version_list.length; i++) {
        let supported_version = supported_version_list[i]
        //   console .log(supported_version)
        // aTextContent 完整 
        if(strIsIn(supported_version, aTextContent)){
            return true
        }
        //   for ( let  j= 0 ;j<aList.length;j++){
        //      let  a=aList[j]
        //      let  href=a.href
    }
    return false
}
// fun 
// js 判断字符串 在字符串
let  outHtml=''
for (let i = 0; i < aList.length; i++) {
    // aList[i].addEventListener('click',function(e){
    //     e.preventDefault()
    //     console.log('click')
    // })

    let a = aList[i]
    // a.href
    let aTextContent = a.textContent
    // if(!for_supported_version_list(aTextContent)){
    //     // a.style.color = 'red'
    //     a.style.display='none'
      
    // }
    if(for_supported_version_list(aTextContent)){
        outHtml+=a.outerHTML+"<br>\n"
    }
   

}
// D:\proj\python\my_util_py_pub\pip_links.js
console.log(outHtml);