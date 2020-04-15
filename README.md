![github-ci](https://github.com/master-coro/artin-pathfinding/workflows/github-ci/badge.svg)
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<p align="center">
    <img src="https://raw.githubusercontent.com/Guilyx/guilyx.github.io/master/images/projects/secret_santa.gif" alt="Logo" width="550" height="400">                           
</a>

## Setup

To setup the project on your local machine:

1. Click on `Fork`.
2. Go to your fork and `clone` the project to your local machine.
3. `git clone https://github.com/Guilyx/secret-santa.git`
4. `pip3 install -r requirements.txt`

## Run

To run the project for your personal use, write a shell script in the scripts/ folder as followed :

```
python3 main.py mail=sender-email@example.com pw=sender-password<< EOF
4 # number of participants
John # names of the participants (more or less than 4 inputs not supported yet)
Doe
Foo
Bar
email1@example.com
email2@example.com
email3@example.com
email4@example.com
EOF
```

Launch the shell script from the project's root :

```sh scripts/scriptname.sh```

Another way to do it is to use the command line interface by simply running :

```python3 main.py mail=sender-email@example.com pw=sender-password```

Then let the interface guide you. ( It's still more conveniant with the first option. ) Feel free to contribute by starting a GUI, the idea is in the books but time lacks.

## Contribute

To contribute to the project:

1. Choose any open issue from [here](https://github.com/Guilyx/secret-santa/issues). 
2. Comment on the issue: `Can I work on this?` and get assigned.
3. Make changes to your fork and send a PR.

To create a PR:

Follow the given link to make a successful and valid PR: https://help.github.com/articles/creating-a-pull-request/

To send a PR, follow these rules carefully, **otherwise your PR will be closed**:

1. Make PR title in this formats: 
```
Fixes #IssueNo : Name of Issue
``` 
```
Feature #IssueNo : Name of Issue
```
```
Enhancement #IssueNo : Name of Issue
```

According to what type of issue you believe it is.

For any doubts related to the issues, i.e., to understand the issue better etc, comment down your queries on the respective issue.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Erwin Lejeune - [@spida_rwin](https://twitter.com/spida_rwin) - erwin.lejeune15@gmail.com

## Contributors

Everyone part of the original team or that assisted throughout the development.

- [Erwin Lejeune](https://github.com/Guilyx)

[contributors-shield]: https://img.shields.io/github/contributors/guilyx/secret-santa.svg?style=flat-square
[contributors-url]: https://github.com/guilyx/secret-santa/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/guilyx/secret-santa.svg?style=flat-square
[forks-url]: https://github.com/guilyx/secret-santa/network/members
[stars-shield]: https://img.shields.io/github/stars/guilyx/secret-santa.svg?style=flat-square
[stars-url]: https://github.com/guilyx/secret-santa/stargazers
[issues-shield]: https://img.shields.io/github/issues/guilyx/secret-santa.svg?style=flat-square
[issues-url]: https://github.com/guilyx/secret-santa/issues
[license-shield]: https://img.shields.io/github/license/guilyx/secret-santa.svg?style=flat-square
[license-url]: https://github.com/guilyx/secret-santa/blob/master/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/erwinlejeune-lkn
