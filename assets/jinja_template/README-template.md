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
    {%- for stack in stacks %}
    <a href="{{ stack['href'] }}">
      <img src="{{ stack['src'] }}" alt="{{ stack['name'] }}">
    </a>
    {%- endfor %}
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
