Use tmux for terminal multiplexer (optional).

Put your script on the server:

```
sftp clarkf@poisson.ucdavis.edu
put file1.py
put file2.py
exit
```

Then ssh into the server.

```
ssh clarkf@poisson.ucdavis.edu
python file1.py
```


Run in debug mode:
```
python -m pdb myscript
```

Then press `c` for continue.
