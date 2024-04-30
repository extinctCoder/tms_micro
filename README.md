# TMS_MICRO

[![Publish container images to GHCR](https://github.com/extinctCoder/tms_micro/actions/workflows/build_image.yml/badge.svg)](https://github.com/extinctCoder/tms_micro/actions/workflows/build_image.yml)

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

<!-- https://www.youtube.com/watch?v=DfmxNzbGPzY -->
<!-- https://www.youtube.com/watch?v=s_o8dwzRlu4 -->

```sh
docker buildx build --no-cache --file Dockerfile.main --tag main_service:latest .
docker buildx build --no-cache --file Dockerfile.auth --tag auth_service:latest .
docker buildx build --no-cache --file Dockerfile.user --tag user_service:latest .
```

Semantic release

```sh
semantic-release generate-config -f json
semantic-release generate-config -f toml > pyproject.toml
semantic-release --noop version --print
```

ok raifat vai upgrading to version 2 try again again
