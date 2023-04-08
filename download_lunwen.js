let  downloadlinks=document.getElementsByClassName('downloadlink icon-download')

for(let i=0;i<downloadlinks.length;i++){
    let  downloadlink=downloadlinks[i]

    // setTimeout(()=>{
    //     downloadlink.click()
    // },(i+1)*10000)

    setTimeout(()=>{
        downloadlink.click()
    },(i)*10000)

    // downloadlink.click()
}

// console.log(downloadlinks);
// error_obj={}
// cosole.log('log error')
// cosole.log(error_obj)

// cosole.log('log error '+JSON.stringify(error_obj))