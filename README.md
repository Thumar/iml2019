# IML 2019 Tutorials

## Four ways to start the notebook

#### 1. SWAN

[![SWAN](http://swanserver.web.cern.ch/swanserver/images/badge_swan_white_150.png)](https://cern.ch/swanserver/cgi-bin/go?projurl=https://github.com/3pia/iml2019.git)


#### 2. Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/3pia/iml2019/master)


#### 3. Docker with a local checkout

```shell
git clone https://github.com/3pia/iml2019
cd iml2019
./docker/run.sh
```


#### 4. Standalone docker image from the docker hub

```
docker run -ti -u $(id -u):$(id -g) -p 8888:8888 3pia/iml2019
```
