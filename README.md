# Secret Santa

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

Launch the shell script from root :

```sh scripts/scriptname.sh```
