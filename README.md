[![Build Status](https://circleci.com/gh/cloudify-examples/wagon-factory-blueprint.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/cloudify-examples/wagon-factory-blueprint)

##  Wagon Factory Blueprint

This blueprint brings up a VM to build a wagon.

## prerequisites

You will need a *Cloudify Manager* running in either AWS, Azure, or Openstack.

If you have not already, set up the [example Cloudify environment](https://github.com/cloudify-examples/cloudify-environment-setup). Installing that blueprint and following all of the configuration instructions will ensure you have all of the prerequisites, including keys, plugins, and secrets.


*This has only been tested on Centos VMs in AWS, Azure, and Openstack. Some modifications should be made for other platforms.*


### Step 1: Install the Wagon Deployment

Next you provide those inputs to the blueprint and execute install:


#### For AWS run:

```shell
$ cfy install \
    https://github.com/cloudify-examples/wagon-factory-blueprint/archive/4.0.1.zip \
    -b wagon \
    -n aws-blueprint.yaml \
    -i plugin_zip=[URL_OF_PLUGIN_ZIP_ARCHIVE]
```


#### For Azure run:

```shell
$ cfy install \
    https://github.com/cloudify-examples/wagon-factory-blueprint/archive/4.0.1.zip \
    -b wagon \
    -n azure-blueprint.yaml \
    -i plugin_zip=[URL_OF_PLUGIN_ZIP_ARCHIVE]
```


#### For Openstack run:

```shell
$ cfy install \
    https://github.com/cloudify-examples/wagon-factory-blueprint/archive/4.0.1.zip \
    -b wagon \
    -n openstack-blueprint.yaml \
    -i plugin_zip=[URL_OF_PLUGIN_ZIP_ARCHIVE]
```


### Step 2: Show Deployments Outputs

```shell
$ cfy deployments outputs wagon
Retrieving outputs for deployment wagon...
 - "download":
     Description:
     Value: http://**.**.**.**:8080
```


### Step 3: Upload Wagon

Open that URL in a browser and you will see the directory listing with the wagon file. Copy the wagon url and upload it to your manager:

```shell
$ cfy plugins upload http://**.**.**.**:8080/wagon.wgn
```
