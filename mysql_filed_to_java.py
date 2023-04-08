# mysql_filed_to_java
mysql_filed="tenant_id"

import strUtil.strUtil as strUtil

# strUtil.to 

# strUtil.toCamel
java_filed=strUtil.toCamel(mysql_filed)
# strUtil.toCamel(mysql_filed)

print(java_filed)
print(f'String {java_filed} ;')

f'<result column="{mysql_filed}" jdbcType="VARCHAR" property="{java_filed}" />'