

let  inputs=
document.getElementsByClassName('sd-Input-input-1DdWs sd-Input-common-input-VNsWe')

let inputShows=
document.getElementsByClassName('sd-Input-display-value-3ojbk sd-Input-display-value-spacing-Rc6iN')
// console.log(inputs);

for( let i=0;i<inputShows.length;i++){
    // inputs[i].value='test'
    let   input= inputShows[i]
   let  placeholder=  input.getAttribute('placeholder')
//    console.log(placeholder);
//    if("紧急联系人"==placeholder){
//        input.value='test'
//    }
let  inputVal=inputVals[placeholder]
if(!inputVal){
    continue
}
// input.value 设置了 鼠标移动上去 就没了
input.setAttribute('value',inputVal)
// input.value=inputVal
//    input.value= inputVals[placeholder]
}

// $0.__reactEventHandlers$kousg41c7og.onChange
console.log(object);
$0.__reactEventHandlers$kousg41c7og.onChange= function (e){
    
}
// placeholder

let  inputVals={
    "紧急联系人":"缪奇栋",
    "紧急联系人电话":"15258508503",
    "由何处得知招聘信息":"内部推荐",
    "所在院系":"计算机与计算科学",
    "学习方式":"全日制",
    "学习成绩":"",
}

for( let i=0;i<inputs.length;i++){
    // inputs[i].value='test'
    let   input= inputs[i]
   let  placeholder=  input.getAttribute('placeholder')
//    console.log(placeholder);
//    if("紧急联系人"==placeholder){
//        input.value='test'
//    }
let  inputVal=inputVals[placeholder]
if(!inputVal){
    continue
}
// input.value 设置了 鼠标移动上去 就没了
input.setAttribute('value',inputVal)
// input.value=inputVal
//    input.value= inputVals[placeholder]
}