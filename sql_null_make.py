
"""
select url,url_biz,url_mid,url_sn,url_idx from ck_dpi_sch.e_spd_wechat_article_result_local where url=""
 or url_biz="" or url_mid="" or url_sn="" or url_idx="" limit 1000"""
#  url_biz=''
# 要单引号 
where_sql=''
for file in ['url_biz','url_mid']:
    where_sql+=f"file = '' or "
    # sel_em='sel count(*) where url_mid=""'
    sel_em=f'sel count(*) where {file}=""'
    sel_em=f'sel count(*) where {file}="";'

    # sql 判断 有哪些字段是空的 

# sel count(*) where url_mid="";

"""
 sel 'url_biz' as filedNmae, count(*) where url_mid="";
  sel count(*) where url_mid="";
  
   sel count(*) where url_mid="";
    sel count(*) where url_mid="";
    """