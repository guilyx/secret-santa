# Secret Santa Generator

## Run

For better use, write a shell script in the scripts/ folder as followed :

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

## Contribute

To setup the project on your local machine:

1. Click on `Fork`.
2. Go to your fork and `clone` the project to your local machine.
3. `git clone https://github.com/Guilyx/secret-santa.git`

To contribute to the project:

1. Choose any open issue from [here](https://github.com/Guilyx/secret-santa/issues). 
2. Comment on the issue: `Can I work on this?` and get assigned.
3. Make changes to your fork and send a PR.

To create a PR:

Follow the given link to make a successful and valid PR: https://help.github.com/articles/creating-a-pull-request/

To send a PR, follow these rules carefully, **otherwise your PR will be closed**:

1. Make PR title in this format: `Fixes #IssueNo : Name of Issue`

For any doubts related to the issues, i.e., to understand the issue better etc, comment down your queries on the respective issue.
