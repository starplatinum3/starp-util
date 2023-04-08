
function

    // 对象转query字符串的方法
    queryObjToPathStr(obj) {
		// 首先判断obj是否为真，为真则进行处理，不然直接return
		if (obj) {
			// 定义变量接收query字符串
			let query = ""
			// 循环遍历对象
			for (let i in obj) {
				// 定义变量接收对象的value值
				let value = obj[i]
				// 若对象的value值为数组，则进行join打断
				if (Array.isArray(value)) {
					value = value.join(",")
				}
				// 进行字符串拼接
				query += `&${i}=${value}`
			}
			// replace返回一个新的字符串，要用query重新接受一下，并把第一个&替换为?
			query = query.replace('&', '?')
			// 返回生成的query字符串
			return query
		}
		return ""
	}


    
  let obj = {
    username: '我叫胡八一',
    password: 1627889159
}
console.log(queryObjToPathStr(obj)) //?username=我叫胡八一&password=1627889159