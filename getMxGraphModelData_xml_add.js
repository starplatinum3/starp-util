// let  textareaList=document.getElementsByTagName('textarea')

// console.log(textareaList);

// // let  mxGraphModelData=
// // textareaList[0].innerHTML
// let mxGraphModelDom=  textareaList[0]
// console.log(mxGraphModelDom);
// // let mxGraphModelData=
// // mxGraphModelDom.innerText

// let mxGraphModelData=
// mxGraphModelDom.value

// console.log(mxGraphModelData);

let geBtns =
    document.getElementsByClassName('geBtn')

console.log(geBtns);

let cacelBtn =
    geBtns[0]
// geBtns[0]
// js  在一个dom 前面 添加一个按钮

let btnsDom =
    cacelBtn.parentElement

console.log(btnsDom);

function getMxGraphModelData() {
    let textareaList = document.getElementsByTagName('textarea')

    console.log(textareaList);

    // let  mxGraphModelData=
    // textareaList[0].innerHTML
    let mxGraphModelDom = textareaList[0]
    console.log(mxGraphModelDom);
    // let mxGraphModelData=
    // mxGraphModelDom.innerText

    let mxGraphModelData =
        mxGraphModelDom.value

    console.log(mxGraphModelData);
    return mxGraphModelData
}

// var oBtn = document.createElement("input");
var oBtn = document.createElement("button");

oBtn.id = "btn";
oBtn.type = "button";
oBtn.value = "按钮"
oBtn.innerText = "getMxGraphModelData"
oBtn.onclick = function () {
    // console.log("object");
    let MxGraphModelData =
        getMxGraphModelData()

    console.log("MxGraphModelData");
    console.log(MxGraphModelData);
}
btnsDom.appendChild(oBtn)
// document.body.appendChild(oBtn);

// ————————————————
// 版权声明：本文为CSDN博主「我是星星bling」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
// 原文链接：https://blog.csdn.net/qq_45099319/article/details/126970874

let mxPopupMenuItems=
document.getElementsByClassName('mxPopupMenuItem')

let  editDrawBtn=
mxPopupMenuItems[mxPopupMenuItems.length-2]

// let  editDrawBtn=
// mxPopupMenuItems[mxPopupMenuItems.length-1]
console.log(editDrawBtn);

editDrawBtn.click()

editDrawBtn.onclick=function(){
    console.log('onclick');
}

// editDrawBtn. 
// console.log(editDrawBtn.click);
