let icon_quotes = document.getElementsByClassName('icon-quote')



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

function
downloadJsonObj(filename, jsonObj) {
    let all_articles_str = JSON.stringify(jsonObj)
    downloadTxt(filename, all_articles_str)
}

let
    txt_search =
    document.getElementById('txt_search').textContent



function getNowTimeStr() {
    var current = new Date(); //实例化Date对象
    var nowYear = current.getFullYear(); //获取当前的年份
    var nowMonth = current.getMonth() + 1; //默认显示的是0-11月，比我们正常的月份少一个月，所以要+1
    var nowdates = current.getDate(); //获取日期
    // ————————————————
    // 版权声明：本文为CSDN博主「樱花树下的空白」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
    // 原文链接：https://blog.csdn.net/qq_45382872/article/details/124325266
    var nowHours = current.getHours(); //获取小时
    var nowMinutes = current.getMinutes(); //获取分钟
    var nowSeconds = current.getSeconds(); //获取秒
    // var nowTime = nowYear + "-" + nowMonth + "-" + nowdates + " " + nowHours + ":" + nowMinutes + ":" + nowSeconds;
    // console.log(nowTime);
    var nowTime = nowYear + "_" + nowMonth + "_" + nowdates + "_" + nowHours + "_" + nowMinutes + "_" + nowSeconds;
    return nowTime
}

function downloadFile() {
    let res = {
        location_href: location.href,
        all_articles: all_articles
    }

    let NowTimeStr = getNowTimeStr()
    // let all_articles_str = JSON.stringify(all_articles)
    // downloadTxt('all_articles.json', all_articles_str)
    downloadJsonObj(`all_articles_${txt_search}_${NowTimeStr}.json`, res)
}


function click_and_get(icon_quote) {


    if (!icon_quote) {
        downloadFile()
        return
    }
    icon_quote.click()
    setTimeout(() => {
        let All_quote_r = getAll_quote_r_one_click()


        let layui_layer_close = document.getElementsByClassName('layui-layer-ico layui-layer-close layui-layer-close1')[0]

        if (!layui_layer_close) {

            downloadFile()
            return
        }
        layui_layer_close.click()


        function dataPush() {

            all_articles.push({
                All_quote_r: All_quote_r
            })



            let end = all_articles.length >= icon_quotes.length
            if (end) {

                console.log(all_articles);
                let res = {
                    location_href: location.href,
                    all_articles: all_articles
                }

                let NowTimeStr = getNowTimeStr()
                // let all_articles_str = JSON.stringify(all_articles)
                // downloadTxt('all_articles.json', all_articles_str)
                downloadJsonObj(`all_articles_${txt_search}_${NowTimeStr}.json`, res)
            }
        }

        dataPush()
        // setTimeout(() => {

        //     dataPush()
        // }, 2000)




    }, 1000)
}
let all_articles = []

for (let i = 0; i < icon_quotes.length; i++) {
    let icon_quote = icon_quotes[i]

    console.log(icon_quote);

    setTimeout(() => {
        click_and_get(icon_quote)
    }, (i + 1) * 2000)


}

// icon_quotes[0].click()


function getAll_quote_r(quote_r) {
    let All_quote_r = []
    for (let i = 0; i < quote_r.length; i++) {
        let quote_r_one = quote_r[i]
        All_quote_r.push({
            quote_r_one: quote_r_one.textContent
        })

        // console.log(icon_quote);

    }

    return All_quote_r
}


function getAll_quote_r_one_click() {

    let quote_r = document.getElementsByClassName('quote-r')
    // let  quote_r= document.getElementsByClassName('quote-r')[0].textContent
    let All_quote_r =
        getAll_quote_r(quote_r)

    return All_quote_r


    // All_quote_r. 
}