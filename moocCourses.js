// course-card-wrapper

let  courseCards=
Array.from(document.getElementsByClassName('course-card-wrapper'))
// document.getElementsByClassName('course-card-wrapper')
// [0].style.display = 'none'

let hrefs=courseCards.map(courseCard=>courseCard.getElementsByTagName('a')[0].href)

let  title=
document.getElementsByClassName('common-info-wrapper common-info-wrapper-fix-height')[0].textContent

// let  

let  score=
document.getElementsByClassName('score ')[0].textContent.trim().replace('\n','')

let  courseStatus=
document.getElementsByClassName('course-status')[0].textContent
`<!DOCTYPE html>\n<html>\n  \n<head>\n    <title>\n        How to get the name of a\n        file using JavaScript\n    </title>\n      \n    <style>\n        body {\n            text-align: center;\n        }\n        h1 {\n            color: green;\n        }\n        #geeks {\n            font-size: 26px; \n            font-weight: bold; \n            color: green;\n        }\n    </style>\n</head>\n  \n<body>\n    <h1>GeeksforGeeks</h1>\n      \n    <p>\n        Click on the button to get\n        the name of the file.\n    </p>\n      \n    <button onclick="GFG_Fun();">\n        click here\n    </button>\n      \n    <p id="geeks"></p>\n      \n    \x3Cscript>\n        var down = document.getElementById('geeks');\n  \n        function GFG_Fun() {\n            var path = window.location.pathname;\n            down.innerHTML = path.split("/").pop();\n        }\n    \x3C/script>\n</body>\n  \n</html>\n`

// for(let courseCard of  courseCards){
//     // o.style.display = 'none'
//     let  href=
//     courseCard.getElementsByTagName('a')[0].href

//     console.log(href);
// }

let resHrefs=[
    "https://www.icourse163.org/learn/HIT-154005?tid=1463162470",
    "https://www.icourse163.org/learn/HIT-154005?tid=1465409451",
    "https://www.icourse163.org/learn/XMU-1002335004?tid=1464929448",
    "https://www.icourse163.org/learn/XMU-1002335004?tid=1467032457",
    "https://www.icourse163.org/learn/XMU-1002335004?tid=1468187449",
    "https://www.icourse163.org/learn/HIT-1002123007?tid=1467039443",
    "https://www.icourse163.org/learn/RUC-1001655006?tid=1465315447",
    "https://www.icourse163.org/learn/ZJU-232005?tid=1465158453"
]


// D:\proj\python\my_util_py_pub\moocCourses.js
let moocCoursesObjList=[
    {
        "href": "https://www.icourse163.org/learn/HIT-154005?tid=1463162470",
        "title": {},
        "score": {},
        "courseStatus": {}
    },
    {
        "href": "https://www.icourse163.org/learn/HIT-154005?tid=1465409451",
        "title": {},
        "score": {},
        "courseStatus": {}
    },
    {
        "href": "https://www.icourse163.org/learn/XMU-1002335004?tid=1464929448",
        "title": {},
        "score": {},
        "courseStatus": {}
    },
    {
        "href": "https://www.icourse163.org/learn/XMU-1002335004?tid=1467032457",
        "title": {},
        "score": {},
        "courseStatus": {}
    },
    {
        "href": "https://www.icourse163.org/learn/XMU-1002335004?tid=1468187449",
        "title": {},
        "score": {},
        "courseStatus": {}
    },
    {
        "href": "https://www.icourse163.org/learn/HIT-1002123007?tid=1467039443",
        "title": {},
        "score": {},
        "courseStatus": {}
    },
    {
        "href": "https://www.icourse163.org/learn/RUC-1001655006?tid=1465315447",
        "title": {},
        "score": {},
        "courseStatus": {}
    },
    {
        "href": "https://www.icourse163.org/learn/ZJU-232005?tid=1465158453",
        "title": {},
        "score": {},
        "courseStatus": {}
    }
]

let moocCoursesObjListTrue=
[
    {
        "href": "https://www.icourse163.org/learn/HIT-154005?tid=1463162470",
        "title": "\n\n\n\n\n\n\n\n\n\n\n\n\n计算机网络\n\n\n\n哈尔滨工业大学\n\n",
        "score": "96.29分",
        "courseStatus": "2021年7月25日已结束"
    },
    {
        "href": "https://www.icourse163.org/learn/HIT-154005?tid=1465409451",
        "title": "\n\n\n\n\n\n\n\n\n\n\n\n\n计算机网络\n\n\n\n哈尔滨工业大学\n\n",
        "score": "0.00分",
        "courseStatus": "2022年1月9日已结束"
    },
    {
        "href": "https://www.icourse163.org/learn/XMU-1002335004?tid=1464929448",
        "title": "\n\n\n\n\n\n\n\n\n\n\n\n\n大数据技术原理与应用\n\n\n\n厦门大学\n\n",
        "score": "0.00分",
        "courseStatus": "2021年12月31日已结束"
    },
    {
        "href": "https://www.icourse163.org/learn/XMU-1002335004?tid=1467032457",
        "title": "\n\n\n\n\n\n\n\n\n\n\n\n\n大数据技术原理与应用\n\n\n\n厦门大学\n\n",
        "score": "0.00分",
        "courseStatus": "2022年6月11日已结束"
    },
    {
        "href": "https://www.icourse163.org/learn/XMU-1002335004?tid=1468187449",
        "title": "\n\n\n\n\n\n\n\n\n\n\n\n\n大数据技术原理与应用\n\n\n\n厦门大学\n\n",
        "score": "0.00分",
        "courseStatus": "2022年12月31日已结束"
    },
    {
        "href": "https://www.icourse163.org/learn/HIT-1002123007?tid=1467039443",
        "title": "\n\n\n\n\n\n\n\n\n\n\n\n\n编译原理\n\n\n\n哈尔滨工业大学\n\n",
        "score": "0.00分",
        "courseStatus": "2022年7月31日已结束"
    },
    {
        "href": "https://www.icourse163.org/learn/RUC-1001655006?tid=1465315447",
        "title": "\n\n\n\n\n\n\n\n\n\n\n\n\n数据库系统概论（高级篇）\n\n\n\n中国人民大学\n\n",
        "score": "62.83分",
        "courseStatus": "2022年1月15日已结束"
    },
    {
        "href": "https://www.icourse163.org/learn/ZJU-232005?tid=1465158453",
        "title": "\n\n\n\n\n\n\n\n\n\n\n\n\n概率论与数理统计\n\n\n\n浙江大学\n\n",
        "score": "60.00分",
        "courseStatus": "2022年1月3日已结束"
    }
]