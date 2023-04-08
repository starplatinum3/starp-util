def like(word='大纲'):
    doc_name_regex = f'.*{word}.*'
    return {'$regex': doc_name_regex}