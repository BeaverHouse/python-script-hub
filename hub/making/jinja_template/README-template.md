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
    {%- if react %}
    <a href="https://react.dev/">
      <img src="https://img.shields.io/badge/React-61DAFB.svg?style=flat&logo=React&logoColor=black" alt="React">
    </a>
    {%- endif %}
    {%- if typescript %}
    <a href="https://www.typescriptlang.org/">
      <img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=flat&logo=TypeScript&logoColor=white" alt="TypeScript">
    </a>
    {%- endif %}
    {%- if eslint %}
    <a href="https://eslint.org/">
      <img src="https://img.shields.io/badge/ESLint-4B32C3?logo=eslint&logoColor=fff&style=flat" alt="ESLint">
    </a>
    {%- endif %}
    {%- if yarn %}
    <a href="https://yarnpkg.com/">
      <img src="https://img.shields.io/badge/Yarn-2C8EBB?logo=yarn&logoColor=fff&style=flat" alt="Yarn">
    </a>
    {%- endif %}
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
    {%- if pandas %}
    <a href="https://pandas.pydata.org/">
      <img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
    </a>
    {%- endif %}
    {%- if pytest %}
    <a href="https://docs.pytest.org/en/8.0.x/">
      <img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white" alt="Pytest">
    </a>
    {%- endif %}
    {%- if golang %}
    <a href="https://go.dev/">
      <img src="https://img.shields.io/badge/Go-00ADD8?logo=go&logoColor=fff&style=flat" alt="Go">
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
