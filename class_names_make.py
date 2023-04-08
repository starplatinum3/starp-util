# """
#   "id": "V5KkBoUBVS8PTbGok-ft",
#         "quesContent": "demoData",
#         "questionType": 1,
#         "subjectId": 1,
#         "score": 1,
#         "gradeLevel": 1,
#         "difficult": 1,
#         "correct": "demoDataHaoHUozhi",
#         "infoTextContentId": 1,
#         "createUser": 1,
#         "videoLink": "demoData",
#         "status": 1,
#         "deleted": true,
#         "analyze": "demoData",
#         "title": "demoData""""


jsonData={
        "id": "V5KkBoUBVS8PTbGok-ft",
        "quesContent": "demoData",
        "questionType": 1,
        "subjectId": 1,
        "score": 1,
        "gradeLevel": 1,
        "difficult": 1,
        "correct": "demoDataHaoHUozhi",
        "infoTextContentId": 1,
        "createUser": 1,
        "videoLink": "demoData",
        "status": 1,
        "deleted": "true",
        "analyze": "demoData",
        "title": "demoData"
      }

for key in jsonData.keys():
    print(f'   public  static String  {key}="{key}";')