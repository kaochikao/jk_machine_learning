
list environements
```sh
conda env list
```

switching active env
```sh
source activate python3
```

switch back to base
```sh
source activate
```

environment locations
not under /home/ec2-user/SageMaker, not persisted in EBS volume
```sh
/home/ec2-user/anaconda3/envs/*
```

list packages of current env
```sh
conda list
conda list -n myenv
conda list -n myenv pandas
```

create env
```sh
conda create -n myenv
```

```sh
conda install -n myenv pandas
```



---------------------------------------------------------------------
```sh
(python3) sh-4.2$ conda list -n python3 pyarrow
# packages in environment at /home/ec2-user/anaconda3/envs/python3:
#
# Name                    Version                   Build  Channel
pyarrow                   0.16.0                    <pip>
pyarrow                   0.11.1           py36he6710b0_0
```

```sh
(python3) sh-4.2$ python -m ipykernel install --user --name myenv --display-name "foo (bar)"
Installed kernelspec myenv in /home/ec2-user/.local/share/jupyter/kernels/myenv
```
-m mod : run library module as a script

