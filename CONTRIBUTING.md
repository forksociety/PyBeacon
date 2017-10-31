# Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

## Get Started!

Ready to contribute? Here's how to set up `PyBeacon` for local development.
You can contribute in many ways:

1. Fork the `PyBeacon` repo on GitHub.
2. Clone your fork locally:

  ```shell
  $ git clone git@github.com:your_name_here/PyBeacon.git
  ```

3. Install your local copy into a virtualenv. Assuming you have virtualenv installed, this is how you set up your fork for local development:

  ```shell
  $ cd PyBeacon/
  $ virtualenv env
  $ source env/bin/activate
  $ python setup.py develop
  $ pip install coveralls pytest pytest-cov
  ```

4. Create a branch for local development:

  ```shell
  $ git checkout -b name-of-your-bugfix-or-feature
  ```
   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass the test:

  ```shell
  $ py.test
  ```

6. Commit your changes and push your branch to GitHub::

  ```shell
  $ git add .
  $ git commit -m "Your detailed description of your changes."
  $ git push origin name-of-your-bugfix-or-feature
  ```

7. Submit a pull request through the [GitHub website](https://github.com/nirmankarta/PyBeacon).

## How to contribute?
* Follow the Getting Started guidelines to get a headstart.
* Create an issue first and then get it approved before creating a PR to allow for better management.
* Make sure to make PRs against the `dev` branch.
* No trivial edits, ie. simply rearranging topics will not be accepted.

## Types of Contributions

You can contribute in many ways:

### Report Bugs

Report bugs at https://github.com/nirmankarta/PyBeacon/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the [GitHub issues](https://github.com/nirmankarta/PyBeacon/issues) for bugs. Anything tagged with "bug"
and "help wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

PyBeacon could always use more documentation, whether as part of the
official PyBeacon docs, in docstrings, or even on the web in blog posts,
articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at https://github.com/nirmankarta/PyBeacon/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.md.
3. The pull request should work for Python 2.7+ and 3.3+ and later. Check
   https://travis-ci.org/PyBeacon/PyBeacon/pull_requests
   and make sure that the tests pass for all supported Python versions.
