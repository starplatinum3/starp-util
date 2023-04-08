// job

// Array.to 

let  jobs=document.getElementsByClassName('job')
let  names=document.getElementsByClassName('name')

let  jobsArray=Array.from(jobs)
// Array.from(jobs)
let  resList=[]
for(let i=0;i<names.length;i++){
    let  name =  names[i].textContent.trim()
    let  job =  jobsArray[i].innerHTML.trim()
    resList.push({
        name,
        job
    })
    // console.log(names[i].innerHTML)
}

// resList
// for(let job of jobsArray){
    
//     console.log(job.innerHTML);
// }