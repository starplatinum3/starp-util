function GFG_Fun() {
    var path = window.location.pathname;
    // down.innerHTML = path.split("/").pop();
 let  urlFileName= path.split("/").pop();
 console.log("urlFileName");
 console.log(urlFileName);

}


function getUrlFileName() {
    var path = window.location.pathname;
    console.log("path");
    console.log(path);
//     path
// VM2533:5 /home.htm

    // down.innerHTML = path.split("/").pop();
 let  urlFileName= path.split("/").pop();
 console.log("urlFileName");
 console.log(urlFileName);

 return urlFileName
}


let  funcRes=`
GFG_Fun()
VM2529:5 urlFileName
VM2529:6 home.htm
`
// GFG_Fun()

getUrlFileName()