from string import Template

readme_query_template = Template(
    """{
        repository(owner: "$owner", name: "$name") {
            description 
            homepageUrl
        }
    }"""
)