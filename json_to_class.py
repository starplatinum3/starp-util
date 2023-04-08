# {className=com.starp.exam.controller.TenantController, classURL=/api/tenant, methodName=delete, methodURL=/api/tenant/tenant/delete/{id}, requestType=POST}
json={"className":"springfox.documentation.swagger.web.ApiResourceController","classURL":"/swagger-resources","methodName":"securityConfiguration","methodURL":"/swagger-resources/configuration/security"}

for key in json.keys():
    # print(key)
    # print(json[key])
    field_line=f'String {key} ;'
    print(field_line)

