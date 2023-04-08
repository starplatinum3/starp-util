def list_all(collection):
    collection_find=collection.find()
    collection_find=list(collection_find)
    # print("collection_find")
    # print(collection_find)
    return collection_find
