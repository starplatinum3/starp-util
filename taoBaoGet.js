

function downloadTxt(filename, text) {
    var pom = document.createElement('a');
    pom.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    pom.setAttribute('download', filename);
    if (document.createEvent) {
        var event = document.createEvent('MouseEvents');
        event.initEvent('click', true, true);
        pom.dispatchEvent(event);
    } else {
        pom.click();
    }
}


function downloadPage() {
    let itemNames= document.getElementsByClassName("pc-items-item-title pc-items-item-title-row2")

    console.log(itemNames);
    
    // let  searchWord= document.getElementsByClassName("text-wrap")[0].textContent
    // console.log(searchWord);
    
    // let  searchWord= document.getElementById("J_searchForm").textContent
    // console.log(searchWord);
    let  J_searchForm= document.getElementById("J_searchForm")
    console.log(J_searchForm);
    
    // let  searchWord= J_searchForm.innerText
    // let  searchWord= J_searchForm.value 
    // console.log(searchWord);
    let  inputs=  J_searchForm.getElementsByTagName("input")
    // console.log(inputs);
    // let input0=  inputs[0]
    // console.log("input0");
    // console.log(input0);
    let  submitBtn=  document.getElementsByClassName("submit")[0]
    // .click()
    // submit
    // let submitBtn= inputs[0].getElementsByTagName("input")[0]
    console.log("submitBtn");
    console.log(submitBtn);
    
    submitBtn.click()
    
    // 热卖PC搜索
    // https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&keyword=java&clk1=f0c0948220ecee34d8e48fcb4b69b80b&upsId=f0c0948220ecee34d8e48fcb4b69b80b&spm=a2e0b.20350158.search.1&pid=mm_26632258_3504122_32538762&union_lens=recoveryid%3A201_33.42.156.233_16319860_1667716432848%3Bprepvid%3A201_33.8.41.104_12221870_1667717148444
    let searchWordInput = J_searchForm.getElementsByTagName("input")[0]
    
    let  searchWord= searchWordInput.value
    console.log(searchWord);
    
    searchWordInput.value="java"
    
    let afterCouponList= document.getElementsByClassName("coupon-price-afterCoupon")
    console.log(afterCouponList);
    
    let  res=[]
    
    if(itemNames.length!=afterCouponList.length){
      console.log("长度不同" );
      alert("长度不同" );
    }else{
        // console.log("长度相同" );
        // alert("长度相同" );
    }
    
    
    for(let i=0;i<itemNames.length;i++){
        // itemNames[i]
        res.push({
            itemName:itemNames[i].innerText,
            afterCoupon:afterCouponList[i].innerText,
            date:new Date()
        })
        // console.log(itemNames[i].innerText,afterCouponList[i].innerText)
    }
    
    let answerListStr = JSON.stringify(res)
    let txtName = `taobao_${searchWord}.json`
    
    // downloadTxt(txtName, answerListStr)

}


let downloadPageInterval = setInterval(() => {
    downloadPage()
}, 4000)