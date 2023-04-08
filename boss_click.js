
let cpc_job_list_chat_4s=
document.getElementsByClassName('cpc_job_list_chat_4')

let  chatBtns=
document.getElementsByClassName('start-chat-btn')
// chatBtns[0].click()

for(let i=0;i<chatBtns.length;i++){
    // chatBtns[i].click()
    // console.log(`click ${i}`)
    // chatBtns[i].href='https://www.google.com'
    chatBtns[i].setAttribute('target','_blank')
}