# Security Related Pre-commit hooks

## Summary
pre-commit git hooks that will run the following security checkers on the source code:
- [safety](https://github.com/pyupio/safety) - Safety checks installed python dependencies for known security vulnerabilities.
- [bandit](https://pypi.python.org/pypi/bandit/) - Bandit checks for common security issues in Python code.

This setup is based on the delegating script writtten by [Carlos Jenkins](https://gist.github.com/carlos-jenkins/89da9dcf9e0d528ac978311938aade43) that allows multiple hooks in a git repository.