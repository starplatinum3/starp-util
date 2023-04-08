packagecom.w.test;importjava.io.File;importjava.io.FileInputStream;importjava.io.InputStream;importjava.util.ArrayList;importjava.util.List;importjava.util.regex.Matcher;importjava.util.regex.Pattern;importorg.apache.poi.POIXMLDocument;importorg.apache.poi.POIXMLTextExtractor;importorg.apache.poi.hwpf.HWPFDocument;importorg.apache.poi.hwpf.extractor.WordExtractor;importorg.apache.poi.hwpf.usermodel.CharacterRun;importorg.apache.poi.hwpf.usermodel.Paragraph;importorg.apache.poi.hwpf.usermodel.Range;importorg.apache.poi.openxml4j.opc.OPCPackage;importorg.apache.poi.poifs.filesystem.POIFSFileSystem;importorg.apache.poi.xwpf.extractor.XWPFWordExtractor;importorg.apache.poi.xwpf.usermodel.XWPFDocument;importorg.apache.poi.xwpf.usermodel.XWPFParagraph;importorg.apache.poi.xwpf.usermodel.XWPFRun;importcom.example.model.Policy_content;public classGetWord {public static voidmain(String[] args) {//TODO Auto-generated method stub

    try{
    
    List list = new ArrayList<>();
    
    InputStream is= new FileInputStream(new File("文件路径")); //需要将文件路更改为word文档所在路径。
    
    POIFSFileSystem fs= newPOIFSFileSystem(is);
    
    HWPFDocument document= newHWPFDocument(fs);
    
    Range range=document.getRange();
    
    CharacterRun run1= null;//用来存储第一行内容的属性
    
    CharacterRun run2 = null;//用来存储第二行内容的属性
    
    int q=1;for (int i = 0; i < range.numParagraphs()-1; i++) {
    
    Paragraph para1= range.getParagraph(i);//获取第i段
    
    Paragraph para2 = range.getParagraph(i+1);//获取第i段
    
    int t=i; //记录当前分析的段落数
    
    String paratext1= para1.text().trim().replaceAll("\r\n", ""); //当前段落和下一段
    
    String paratext2 = para2.text().trim().replaceAll("\r\n", "");
    
    run1=para1.getCharacterRun(0);
    
    run2=para2.getCharacterRun(0);if (paratext1.length() > 0&¶text2.length() > 0) {//这个if语句为的是去除大标题，连续三个段落字体大小递减就跳过
    
    if(run1.getFontSize()>run2.getFontSize()&&run2.getFontSize()>range.getParagraph(i+2).getCharacterRun(0).getFontSize()) {continue;
    
    }//连续两段字体格式不同
    
    if(run1.getFontSize()>run2.getFontSize()) {
    
    String content=paratext2;
    
    run1=run2; //从新定位run1 run2
    
    run2=range.getParagraph(t+2).getCharacterRun(0);
    
    t=t+1;while(run1.getFontSize()==run2.getFontSize()) {//连续的相同
    
    content+=range.getParagraph(t+1).text().trim().replaceAll("\r\n", "");
    
    run1=run2;
    
    run2=range.getParagraph(t+2).getCharacterRun(0);
    
    t++;
    
    }if(paratext1.indexOf("HYPERLINK")==-1&&content.indexOf("HYPERLINK")==-1) {
    
    System.out.println(q+"标题"+paratext1+"\t内容"+content);
    
    i=t;
    
    q++;
    
    }
    
    }
    
    }
    
    }
    
    }catch(Exception e) {
    
    e.printStackTrace();
    
    }
    
    }
    
    }
    // ————————————————
    // 版权声明：本文为CSDN博主「weixin_39783915」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
    // 原文链接：https://blog.csdn.net/weixin_39783915/article/details/114121250