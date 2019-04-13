# IML 2019 Tutorials

The tutorials run in environments with **either** TensorFlow *v1* or *v2*:

- **Introduction tutorial**: TensorFlow *v1*
- **Feature engineering tutorial**: TensorFlow *v2*
- **GAN tutorial**: TensorFlow *v1*

Be aware of slight differences in their setup as explained in the following.

In general, there are four ways to start the notebooks.

### 1. SWAN

Click on the following link:

[![SWAN](http://swanserver.web.cern.ch/swanserver/images/badge_swan_white_150.png)](https://cern.ch/swanserver/cgi-bin/go?projurl=https://github.com/3pia/iml2019.git)

You will be asked to configure the environment in a small dialog.

- For TensorFlow *v1*, just press on the "Start my Session" button at the 
bottom.
- For TensorFlow *v2*, enter the following environment script path and then press the "Start my Session" button:

```
/eos/user/m/mrieger/public/iml2019/lbn/setup.sh
```


### 2. Binder

For TensorFlow *v1*:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/3pia/iml2019/master)

For TensorFlow *v2*:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/3pia/iml2019/tf2)


### 3. Docker with a local checkout

```shell
git clone https://github.com/3pia/iml2019
cd iml2019

# for TensorFlow v1 (introduction and GAN tutorials)
./docker/tf1/run.sh

# for TensorFlow v2 (feature engineering tutorial)
./docker/tf2/run.sh
```


### 4. Standalone docker image from the docker hub

```
# for TensorFlow v1 (introduction and GAN tutorials)
docker run -ti -u $(id -u):$(id -g) -p 8888:8888 3pia/iml2019:tf1

# for TensorFlow v2 (feature engineering tutorial)
docker run -ti -u $(id -u):$(id -g) -p 8888:8888 3pia/iml2019:tf2
```
