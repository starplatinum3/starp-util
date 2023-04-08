@PostMapping(value = "/#doName#")
    public Object #doName#(@RequestBody QuestionPageRequestVM model) {
        List<Map<String, String>> list =
                commonRepository.#doName#("list", null);
        logger.info("list {}", list);
        return RestResponse.ok(list);

    }