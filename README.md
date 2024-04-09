# deploy

## setup kubernetes cluster

make a file called `kind-config`

```sh
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
- role: worker
- role: worker
```

## create cluster

crete cluster using this command

```sh
kind create cluster --name=multinode-cluster --config=kind-config
```

```sh
kubectl cluster-info --context kind-multinode-cluster
```

```sh
kubectl get nodes
kind get clusters
```

https://www.youtube.com/watch?v=DfmxNzbGPzY
