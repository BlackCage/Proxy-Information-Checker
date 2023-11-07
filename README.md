# Proxy Information Checker

[![PyPI](https://img.shields.io/pypi/v/proxy_information)](https://pypi.org/project/proxy_information/)
[![Python Version](https://img.shields.io/pypi/pyversions/proxy_information)](https://pypi.org/project/proxy_information/)
[![GitHub License](https://img.shields.io/github/license/BlackCage/Proxy-Information-Checker)](https://github.com/BlackCage/Proxy-Information-Checker/blob/main/LICENSE)

`proxy_information` is a Python package for verifying and collecting information about proxy servers. With this package, you can easily check the status, response time, anonymity level, and geolocation of a given proxy server.

## Features

- Check the status of a proxy server.
- Measure the response time of a proxy server.
- Determine the anonymity level (Transparent, Elite, or Anonymous) of a proxy server.
- Retrieve the country and country code of a proxy server's location.

## Installation

You can install `proxy_information` using pip:

```bash
pip install proxy_information
```

## Usage

```python
from proxy_information import ProxyInformation

# Initialize a ProxyInformation instance
checker = ProxyInformation()

# Verify a proxy server and get its information
proxy_info = checker.check_proxy("103.88.35.200:1080")

# Print the results
print(proxy_info)
```

## Contributing

We welcome contributions from the community to help us improve and grow this project. If you would like to contribute, please follow these guidelines:

- Check if there are any open issues you would like to work on, or if you have a new idea or feature to suggest, create a new issue on the [GitHub repository](https://github.com/BlackCage/Proxy-Information-Checker/issues).
- Fork the repository and create a new branch for your contributions.
- Make your changes, ensuring that your code follows the project's coding style and conventions.
- Write clear, concise, and well-documented code and commit messages.
- Test your changes to ensure they work as expected.
- Submit a pull request to the main repository, explaining the purpose of your changes and referencing the related issue.

We appreciate your contributions and look forward to working together to make this project even better.

## License

This project is licensed under the MIT License. By contributing to this project, you agree to adhere to the terms and conditions outlined in the [LICENSE](https://github.com/BlackCage/Proxy-Information-Checker/blob/main/LICENSE) file. The MIT License is a permissive open-source license that allows you to use, modify, distribute, and even sell the software, provided you give appropriate credit and include the original license when redistributing the code. For more details, please refer to the [LICENSE](https://github.com/BlackCage/Proxy-Information-Checker/blob/main/LICENSE) file.

## Author

This project is authored by a dedicated developer who strives to create innovative software solutions. To explore more projects and get in touch, visit the following:

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BlackCage) [![Twitter](https://img.shields.io/badge/Twitter-000000?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/BlackByte_) [![ProtonMail](https://img.shields.io/badge/ProtonMail-8B89CC?style=for-the-badge&logo=protonmail&logoColor=white)](mailto:blackcage_faq@proton.me)

Your feedback and collaboration are greatly appreciated. Thank you for your interest in this project.
