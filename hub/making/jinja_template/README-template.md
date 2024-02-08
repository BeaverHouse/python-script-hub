<p align="center">
  <a href="https://github.com/{{ repo }}">
    <img src="logo.png" alt="Logo">
  </a>

  <p align="center">
    {{ description }}
    <br>
    <br>
    {%- if homepage %}
    <a href="{{ homepage }}"><strong>View the website »</strong></a>
    <br>
    <br>
    {%- endif %}
    <a href="https://github.com/{{ repo }}/issues">Bug Report</a>
    |
    <a href="https://github.com/{{ repo }}/issues">Request to HU-Lee</a>
  </p>

  <p align="center">
    {%- if markdown %}
    <a href="https://daringfireball.net/projects/markdown/">
      <img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
    </a>
    {%- endif %}
    {%- if yaml %}
    <a href="https://yaml.org/">
      <img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
    </a>
    {%- endif %}
    {%- if python %}
    <a href="https://www.python.org/">
      <img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
    </a>
    {%- endif %}
    {%- if poetry %}
    <a href="https://python-poetry.org/">
      <img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat&logo=Poetry&logoColor=white" alt="Poetry">
    </a>
    {%- endif %}
    {%- if pytest %}
    <a href="https://docs.pytest.org/en/8.0.x/">
      <img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white" alt="Pytest">
    </a>
    {%- endif %}
    <a href="./LICENSE">
      <img src="https://img.shields.io/github/license/{{ repo }}" alt="License">
    </a>
  </p>
</p>

<!-- Content -->

<br>

## Contributing

See the [CONTRIBUTING.md][contributing].

[contributing]: ./CONTRIBUTING.md
