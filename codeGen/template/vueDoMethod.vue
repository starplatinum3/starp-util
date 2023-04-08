

<el-button type="" @click="#doThing#_do">#doThing#_do</el-button>

#this_list#
<div @click="changeTableName(item)"
  :key="item" v-for="item in #this_list#">
   {{item}}
 </div>

 #doThing#_do(){
   
    allApi.  #doThing#({
        "tableName": this.TableName,
    }).then(res=>{
        console.log("res #doThing#");
        console.log(res);
        this.#this_list# = res. response
    
     })
  },

 
  #doThing#_do () {
    axios.
    get( Common.drawUrl+'draw/#doThing#').then(res => {
      console.log("res");
      console.log(res);
      let content= res.data.content|| res.data.data.content
      console.log("content");
      console.log(content);
      
    })
  },

  // save 
  #doThing#_do  () {

    var content = JSON.stringify(this.draw)
    // var params = new URLSearchParams()
    // params.append('content', content)
    let params={
      content
    }
    axios.post(Common.drawUrl+'draw/#doThing#', params).then(res => {
      if (res.data.code === 1) {
        this.$message({
          message: '画布保存成功',
          type: 'success'
        })
      } else {
        this.$message.error('画布保存失败')
      }
    })
  },

  #doThing#: (data) => post('/api/all/#doThing#',data),


  @PostMapping(value = "/#doThing#")
    public Object #doThing#(@RequestBody QuestionPageRequestVM model) {
        List<Map<String, String>> list =
                commonRepository.#doThing#("list", null);
        logger.info("list {}", list);
        return RestResponse.ok(list);

    }