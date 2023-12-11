# enviroment-managment
This is a simple system to define properties per environment

To use this in any python project import only the config.py file.

```
from enviroment-management import config
```

To define environment variables edit the following files

```
dev.py -> for developer enviroment variables
prod.py -> for production variables
env.py -> for os enviroment variables 
```

## Set working environment
To set the current working environment (dev or prod) add the variable PYTHON_ENV to your os variables and the appropriate value 

## Set variables

### Development
Edit the config dict in the dev.py file

### Production
Edit the config dict in the prod.py file

### Environment
Edit the config dict in the env.py file and add the corresponding variable names to your os system variables

Eg. if you want to define a port name as an environment variable your config file should look like this:

```
config = {
    ...
    'port': get_env('PORT')
    ...
}
```

And you should register the PORT env variable 
## Variable Priority

If you assign the same variables for the varius config files they will be assigned to the final config file with the following priority:
1) dev/prod
2) env
3) default
## Resources used: 

https://softwareengineering.stackexchange.com/questions/342788/best-way-to-handle-dev-test-prod-variables-in-python/396762#396762